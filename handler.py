import runpod
from text_generation import Client

client = Client("http://0.0.0.0:8080")


def handler(event):
    output = client.generate("What is Deep Learning?", max_new_tokens=20).generated_text
    return output


runpod.serverless.start({
    "handler": handler
})
