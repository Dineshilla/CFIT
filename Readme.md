# 🧒 Child-Friendly Interactive Tool

This project is a child-friendly interactive Q&A assistant powered by **TinyLlama**, designed to respond to children's questions in a simple and engaging manner. It features speech-to-text (STT), text-to-speech (TTS), and a fine-tuned LLM running on a **Raspberry Pi 4**.

---

## 🚀 Project Objective

To build an offline-capable, voice-based AI assistant tailored for children aged 6–10, using a lightweight LLM (TinyLlama) fine-tuned on a custom dataset and deployed on Raspberry Pi 4.

---

## 🛠️ Technologies Used

- 🧠 **LLM**: [TinyLlama](https://huggingface.co/unsloth) fine-tuned using [Unsloth](https://huggingface.co/datasets/unsloth/notebooks/blob/main/Alpaca_%2B_Llama_7b_full_example.ipynb)
- 🎤 **Speech-to-Text**: [Whisper](https://github.com/ggerganov/whisper.cpp)
- 🔊 **Text-to-Speech**: [Piper](https://github.com/rhasspy/piper)
- 🐍 Python, Regex, Shell scripting
- 🥧 Deployed on: Raspberry Pi 4
- 📈 Evaluation Metrics: ROUGE & BLEU

---

## 📚 Dataset

- Created using **Gemini 4** for realistic child-style Q&A pairs.
- Covers **36 domains** with over **1000+ Q&A samples**.
- Focused on ensuring answers are simple, non-technical, and easy to understand for children.

---

## 💡 Features

- Fully **offline** and real-time.
- Captures speech input from children.
- Transcribes questions using Whisper.
- Generates simplified responses using TinyLlama.
- Converts answers into speech using Piper.
- Evaluated using **ROUGE** and **BLEU** metrics for quality.

---

## 🧪 Model Training

We used the [Unsloth notebook](https://huggingface.co/datasets/unsloth/notebooks/blob/main/Alpaca_%2B_Llama_7b_full_example.ipynb) to fine-tune the TinyLlama model on our custom dataset. Other models like **Phi-3** and **LLaMA 2** were tested for comparative performance.

---

## 🧩 MVP Code Structure

Key file: `mvp.py` (Running on Raspberry Pi)
Main features include:

- Audio input handling and transcription (`record_and_transcribe`)
- Prompt generation for child-friendly LLM response
- TTS conversion using Piper
- Output playback using `aplay` (avaiable only on Linux, if you are using windows to run, use playback option from Piper)

---

## 🧠 Model Selector

Explore and pick the best model from [HuggingFace - Unsloth](https://huggingface.co/unsloth) based on your use case and device capability.
For our use case: TinyLlama 

---


## 👥 Contributors

- **Illa Dinesh Kumar** - [idineshkumar12321@gmail.com](mailto:idineshkumar12321@gmail.com)
- **Onteddu Chaitanya Reddy** - [chaitanyareddy0702@gmail.com](mailto:chaitanyareddy0702@gmail.com)
- **Anirudh Edpugnati** - [aniedpuganti@gmail.com](mailto:aniedpuganti@gmail.com)
- **Guttula Pavan** - [pavanguttula123@gmail.com](mailto:pavanguttula123@gmail.com)  

---

### For Dataset or any doubts contact us
