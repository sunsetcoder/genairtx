from flask import Flask, request, jsonify
from PIL import Image
from transformers import AutoProcessor, Blip2ForConditionalGeneration
import torch
from io import BytesIO

app = Flask(__name__)

MAX_NEW_TOKENS = 20

@app.route('/caption', methods=['POST'])
def caption_image():
    if 'image' not in request.files:
        return jsonify({"error": "Image file is missing"}), 400
    
    image_file = request.files['image']
    image = Image.open(BytesIO(image_file.read())).convert('RGB')

    inputs = processor(image, return_tensors="pt").to(device, torch.float16)
    generated_ids = model.generate(**inputs, max_new_tokens=MAX_NEW_TOKENS)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0].strip()

    return jsonify({"caption": generated_text})

if __name__ == '__main__':
    processor = AutoProcessor.from_pretrained("Salesforce/blip2-opt-2.7b")
    model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-opt-2.7b", torch_dtype=torch.float16)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)
    app.run(debug=False, port=5001, host='0.0.0.0')