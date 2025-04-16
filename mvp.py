import sys
from llama_cpp import Llama
import subprocess
import shlex
import re
import time
import os


print("Loading LLM")
# llm = Llama(model_path="/home/pi/llama/tinyllama-bnb-4bitodel-unsloth.Q4_K_M.gguf", verbose=False)
llm = Llama(model_path="/home/pi/majorproject/new_tinyllama.gguf", verbose=False)
prompt = """You are a child assistant, you are helping children of age group 6 to 10 years to grow. So answer the following question in simple words so that the child of age group 6 to 10 years can understand it easily. The Answer should be in friendly way and the maximum number of words in the respone should be less than 50.

### Question:
{}

### Answer:
"""

##########################################################################################################################

def remove_square_brackets(text):
  """
  Removes all text enclosed in square brackets from the given string.

  Args:
      text: The string to process.

  Returns:
      A new string with all bracketed text removed.
  """
  return re.sub(r"\[[^\]]*\]", "", text)  # Regular expression for bracketed text

# Example usage
text_with_brackets = "[This is a sentence] with bracketed text [and another example]."
cleaned_text = remove_square_brackets(text_with_brackets)


###########################################################################################################################

# Assuming the Whisper binary is named 'whisper'
whisper_binary = "/home/pi/whisper.cpp/models/ggml-tiny.en.bin"

def record_and_transcribe():
    # Replace 'whisper' with the actual command if needed
    stream_command = ["stream", "-m", whisper_binary, "--step", "4000", "--length", "8000", "-c", "0", "-t", "4", "-ac", "512"]

    stream_process = subprocess.Popen(stream_command, stdout=subprocess.PIPE)

    transcript = ""  # Initialize transcript as an empty string

    try:
        while True:
            line = stream_process.stdout.readline().decode("utf-8").strip()

            # Append transcribed text to transcript
            transcript += line + "\n"

            # Print transcript for monitoring (optional)
            print(transcript, end="")

    except KeyboardInterrupt:
        print("\nStopping model...")

    finally:
        # Terminate stream process if running
        if stream_process.poll() is None:
            stream_process.terminate()

    return transcript

# Print announcement before listening
print("Speak:")

# Call the function to record and transcribe
transcript = record_and_transcribe()

# Process the transcript as needed (e.g., save to file)
transcript = remove_square_brackets(transcript)
transcript = transcript.strip()
print("Full transcript:\n", transcript)


#####################################################################################################
time.sleep(3)
print("Question goes to LLM")
start_time = time.time()
input_ = prompt.format(transcript)
output = llm(input_, max_tokens=40)
end_time = time.time()
elapsed_time = end_time - start_time
print(output['choices'][0]["text"])

#####################################################################################################

print(elapsed_time)

command = "echo " + output['choices'][0]["text"] + " | \
  piper --model /home/pi/en_US-lessac-medium.onnx --output-raw | \
  aplay -r 22050 -f S16_LE -t raw -"
subprocess.run(command, capture_output=False, shell=True)