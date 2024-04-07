from concurrent import futures
from message_publisher import publish_location

import grpc
import location_pb2
import location_pb2_grpc

class LocationIngestionServicer(location_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):
        request_value  = {
            "person_id": int(request.person_id),
            "latitude": request.latitude,
            "longitude": request.longitude
        }

        print(f"request_value :{ request_value } ")
        publish_location(request_value)

        return location_pb2.LocationMessage(**request_value )


server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_LocationServiceServicer_to_server(LocationIngestionServicer(), server)


print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()

server.wait_for_termination()
