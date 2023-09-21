import runpod
import os
import time
from generation import inference
from models import InputPayload
import json


## load your model(s) into vram here



def handler(event):
    # print(event,'event')
    # event = json.loads(event)
    print(event["input"],'input')
    model_input = event["input"]

    # print(model_input.inputs, "model_input")
    # model_input = json.loads(event["input"])
    # print(model_input, "model_input")
    input_payload = InputPayload(**model_input)
    output = inference(input_payload)
    print(output,'output')
    return "hello world"

runpod.serverless.start({
    "handler": handler
})