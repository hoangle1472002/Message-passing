import grpc
import location_pb2
import location_pb2_grpc
from concurrent import futures

# Define your LocationServiceServicer implementation
class LocationServiceServicer(location_pb2_grpc.LocationServiceServicer):
    def GetLocation(self, request, context):
        location_id = request.location_id
        location_data = retrieve_location(location_id)
        return location_pb2.LocationResponse(id=location_data.id)

    def CreateLocation(self, request, context):
        new_location_data = create_location(request)
        return location_pb2.LocationResponse(id=new_location_data.id)

# Function to create a gRPC server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServiceServicer(), server)
    print("Server starting on port 5005")
    server.add_insecure_port('[::]:5005')
    server.start()
    server.wait_for_termination()

# Example function to retrieve location data from some source
def retrieve_location(location_id):
    location_data = location_pb2.LocationRequest(location_id=location_id)
    return location_data

# Example function to create a new location
def create_location(request):
    print(request)
    new_location_data = location_pb2.LocationRequest(location_id="123")
    return new_location_data

if __name__ == '__main__':
    serve()
