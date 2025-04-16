from llama_cpp import Llama
import sys

print("Loading LLM")
llm = Llama(model_path="/home/pi/llama/tinyllama-bnb-4bitodel-unsloth.Q4_K_M.gguf", verbose=False)
prompt = """You are a child assistant, you are helping children of age group 6 to 10 years to grow. So answer the following question in simple words so that the child of age group 6 to 10 years can understand it easily. The Answer should be in friendly way and the maximum number of words in the respone should be less than 50.

### Question:
{}

### Answer:
"""

transcript = sys.argv[1].strip()
output = llm(prompt.format(transcript), max_tokens=40)
print(output['choices'][0]["text"])