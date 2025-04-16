###########################################################################################################################
import subprocess
import shlex
import time
import os
import re


def remove_square_brackets(text):
  """
  Removes all text enclosed in square brackets from the given string.

  Args:
      text: The string to process.

  Returns:
      A new string with all bracketed text removed.
  """
  return re.sub(r"\[[^\]]*\]", "", text)  # Regular expression for bracketed text

# Assuming the Whisper binary is named 'whisper'
whisper_binary = "/home/pi/whisper.cpp/models/ggml-tiny.en.bin"

def record_and_transcribe():
    global start_time
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
        start_time = time.time()
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
