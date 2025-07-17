from concurrent import futures
import grpc
import hello_world_pb2
import hello_world_pb2_grpc

class Greeter(hello_world_pb2_grpc.GreeterServicer):
    def SayHello(self, request: hello_world_pb2.HelloRequest, context):
        return hello_world_pb2.HelloResponse(
            message=f"Hello, {request.name}!"
        )

port = 50051
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
hello_world_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
server.add_insecure_port(f"[::]:{port}")
server.start()
print("Server started, listening on", port)
server.wait_for_termination()