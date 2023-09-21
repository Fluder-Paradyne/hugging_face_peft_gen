import runpod
import os
import time
from generation import inference


## load your model(s) into vram here

def handler(event):
    print(event,'event')
    output = inference(event.input)

runpod.serverless.start({
    "handler": handler
})