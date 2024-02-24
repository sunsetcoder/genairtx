# RTX Image2Caption - Accelerating BLIP-2 with TensorRT-LLM on Windows PC with NVIDIA RTX 🎉 

This project demonstrates how to accelerate BLIP-2, a vision-language model, accelerated to near real-time inference using NVIDIA's TensorRT-LLM on Windows.
It includes steps for generating ONNX models, building TensorRT engines, and converting to TRT-LLM checkpoint format for both ViT and Qformer architectures. 
The project currently leverages FP16 as the default pipeline. INT8/INT4 weight-only quantization will offer reduced latency.

# Model
  * BLIP-2<br>Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models <br>
  [Paper](https://arxiv.org/abs/2301.12597)

# Prerequisites:
Python 3.10

CUDA 12.2

cuDNN 9

NVIDIA RTX 4090 GPU

Windows 11

Ensure your system meets the above specifications for optimal performance. Requires NVIDIA RTX GPU.

# Installation
Clone this repository to your local machine.

Install the required Python packages using the provided requirements.txt:

```bash
pip install -r requirements.txt
```

# Build TensorRT-LLM from source
https://github.com/NVIDIA/TensorRT-LLM

Windows: https://github.com/NVIDIA/TensorRT-LLM/tree/main/windows#building-from-source

# Serve model using the Flask API endpoint and start the Gradio client.