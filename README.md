Accelerating BLIP-2 with TensorRT-LLM on Windows
This project demonstrates how to accelerate BLIP-2, a vision-language model, using NVIDIA's TensorRT-LLM on Windows. It includes steps for generating ONNX models, building TensorRT engines, and converting to TRT-LLM checkpoint format for both ViT and Qformer architectures. The project leverages FP16 as the default pipeline, with support for INT8/INT4 weight-only quantization for reduced latency.

# Prerequisites:
Python 3.10
CUDA 12.2
cuDNN 9
NVIDIA RTX 4090 GPU
Windows 11
Ensure your system meets the above specifications for optimal performance.

# Installation
Clone this repository to your local machine.

Install the required Python packages using the provided requirements.txt:

bash
Copy code
pip install -r requirements.txt

# Build TensorRT-LLM from source
https://github.com/NVIDIA/TensorRT-LLM

Windows: https://github.com/NVIDIA/TensorRT-LLM/tree/main/windows#building-from-source

# Serve using the Flask API and start the Gradio client.