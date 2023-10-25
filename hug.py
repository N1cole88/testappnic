from huggingface_hub import InferenceClient
client = InferenceClient(model= "Salesforce/blip-image-captioning-large")
text = client.image_to_text("astronaut.png")
#image = client.text_to_image("An astronaut riding a horse on the moon.")
#image.save("astronaut.png")
print("Text:", text)
