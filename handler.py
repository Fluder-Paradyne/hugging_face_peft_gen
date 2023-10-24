import runpod
import os
import time
from generation import inference
from models import InputPayload
import json


def handler(event):
    input_payload = InputPayload(**event)
    output = inference(input_payload)
    print(output, "output")
    return output


runpod.serverless.start({"handler": handler})
