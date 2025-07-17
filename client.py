import grpc

from hello_world_pb2_grpc import GreeterStub
from hello_world_pb2 import HelloRequest, HelloResponse


with grpc.insecure_channel("localhost:50051") as channel:
    stub = GreeterStub(channel)
    request = HelloRequest(name="David")
    response: HelloResponse = stub.SayHello(request)
    print("Response:", response.message)