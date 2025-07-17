import grpc

from hello_world_pb2_grpc import GreeterStub
from hello_world_pb2 import HelloRequest, HelloResponse

import os
from dotenv import load_dotenv
load_dotenv()

SERVER_URL = os.getenv("SERVER_URL", "localhost:50051")

with grpc.insecure_channel(SERVER_URL) as channel:
    stub = GreeterStub(channel)
    request = HelloRequest(name="David")
    response: HelloResponse = stub.SayHello(request)
    print("Response:", response.message)