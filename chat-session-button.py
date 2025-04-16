import sys
from llama_cpp import Llama
import subprocess
import shlex
import re
import time
import os
import pyautogui
from gpiozero import Button


button = Button(2)

# Function to remove square brackets
def remove_square_brackets(text):
  return re.sub(r"\[[^\]]*\]", "", text)

# Function for recording and transcribing audio (assuming 'whisper' binary)
def record_and_transcribe():
    print("The device is listening you can ask your question now")
    whisper_binary = "/home/pi/whisper.cpp/models/ggml-base.en.bin"
    stream_command = ["stream", "-m", whisper_binary, "--step", "4000", "--length", "8000", "-c", "0", "-t", "2", "-ac", "512"]

    stream_process = subprocess.Popen(stream_command, stdout=subprocess.PIPE)

    transcript = ""

    try:
        while True:
            line = stream_process.stdout.readline().decode("utf-8").strip()
            transcript += line + "\n"
            print(transcript, end="")
            if button:
                pyautogui.hotkey('ctrl', 'c')

    except KeyboardInterrupt:
        print("\nStopping model...")

    finally:
        if stream_process.poll() is None:
            stream_process.terminate()
        transcript = remove_square_brackets(transcript)
        transcript = transcript.strip()
    return transcript

# Load the LLM model
print("Loading LLM")
llm = Llama(model_path="/home/pi/llama/tinyllama-bnb-4bitodel-unsloth.Q4_K_M.gguf", verbose=False)
# llm = Llama(model_path="/home/pi/majorproject/new_tinyllama.gguf", verbose=False)


# Define the prompt
prompt = """You are a child assistant, you are helping children of age group 6 to 10 years to grow. So answer the following question in simple words so that the child of age group 6 to 10 years can understand it easily. The Answer should be in friendly way and the maximum number of words in the respone should be less than 50.

### Question:
{}

### Answer:
{}
"""

# Function to process the question and get the response
def process_and_respond(user_message):
    # transcript = remove_square_brackets(user_message)
    # transcript = transcript.strip()
    print("Question goes to LLM")

    start_time = time.time()
    output = llm(user_message, max_tokens=40)
    end_time = time.time()
    elapsed_time = end_time - start_time

    response = output['choices'][0]["text"]
    print(response)
    print(elapsed_time)

    # Speech synthesis
    if (response != "") or (response != " "):
        response = remove_quotes(response)
        command = "echo " + str(response) + " | \
        piper --model /home/pi/en_US-lessac-medium.onnx --output-raw | \
        aplay -r 22050 -f S16_LE -t raw -"
        subprocess.run(command, capture_output=False, shell=True)
        # return response
    else:
        response = "Sorry! I couldnot understand that, could you please repeat it once again"
        command = "echo " + str(response) + " | \
        piper --model /home/pi/en_US-lessac-medium.onnx --output-raw | \
        aplay -r 22050 -f S16_LE -t raw -"
        subprocess.run(command, capture_output=False, shell=True)
        # return ""

def remove_quotes(input_str):
    # Replace single quotes with an empty string
    result = input_str.replace("'", "")

    # Replace double quotes with an empty string
    result = result.replace('"', "")

    return result

while True:
    user_input = record_and_transcribe()
    time.sleep(2.5)
    input_ = prompt.format(user_input,"")
    print(input_)
    process_and_respond(input_)
