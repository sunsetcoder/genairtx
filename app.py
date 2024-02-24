import os
import gradio as gr
import requests

def send_image_to_flask(image):
    # Save PIL image to a temporary file
    temp_image_path = "temp_image.png"  # It's more efficient to define the path once and use it for both saving and opening the file
    with open(temp_image_path, "wb") as f:
        image.save(f, format="PNG")
    
    # Open the image file again to send as a file object
    with open(temp_image_path, "rb") as f:
        response = requests.post("http://127.0.0.1:5001/caption", files={"image": f})
        if response.status_code == 200:
            caption = response.json().get("caption", "No caption found.")
        else:
            caption = "Error from server: " + response.json().get("error", "Unknown error")

    os.remove(temp_image_path)  # Clean up by removing the temporary file after use
    return caption

demo = gr.Interface(fn=send_image_to_flask,
                    inputs=[gr.Image(label="Upload image", type="pil")],
                    outputs=[gr.Label(value="Caption")],
                    title="RTX Image2Caption",
                    description="Caption any image",
                    examples=[
                        os.path.join(os.path.dirname(__file__), "examples/1.jpg"),
                        os.path.join(os.path.dirname(__file__), "examples/2.png"),
                        os.path.join(os.path.dirname(__file__), "examples/3.png"),
                        os.path.join(os.path.dirname(__file__), "examples/4.jpg"),
                        os.path.join(os.path.dirname(__file__), "examples/5.jpg"),
                        os.path.join(os.path.dirname(__file__), "examples/7.png"),
                        os.path.join(os.path.dirname(__file__), "examples/8.png"),
                        os.path.join(os.path.dirname(__file__), "examples/9.png"),
                        os.path.join(os.path.dirname(__file__), "examples/10.png"),
                        os.path.join(os.path.dirname(__file__), "examples/11.png"),
                        os.path.join(os.path.dirname(__file__), "examples/12.png"),
                        os.path.join(os.path.dirname(__file__), "examples/13.png"),
                        os.path.join(os.path.dirname(__file__), "examples/14.png"),
                        os.path.join(os.path.dirname(__file__), "examples/15.png"),
                        os.path.join(os.path.dirname(__file__), "examples/16.png"),
                        os.path.join(os.path.dirname(__file__), "examples/17.png"),
                        os.path.join(os.path.dirname(__file__), "examples/18.png"),
                    ],
                    )

demo.launch()