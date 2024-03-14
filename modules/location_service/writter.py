import grpc
import location_pb2
import location_pb2_grpc

def main():
    # Create a gRPC channel to communicate with the server
    channel = grpc.insecure_channel("localhost:5005")

    # Create a stub for the LocationService
    stub = location_pb2_grpc.LocationServiceStub(channel)

    # Create a LocationRequest instance and set the location_id field
    request = location_pb2.LocationRequest(location_id="123")  # Adjust the location_id as needed

    # Call the GetLocation method
    response = stub.GetLocation(request)

    # Print the response
    print("Response:", response)

if __name__ == "__main__":
    main()
