from fastapi import FastAPI
import socket

app = FastAPI()

@app.get('/instance-id')
async def get_instance_id():
    instance_id = socket.gethostname()
    return {'instance_id': instance_id}

