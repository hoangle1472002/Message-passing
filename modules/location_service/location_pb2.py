# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: location.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0elocation.proto\x12\x10location_service\"&\n\x0fLocationRequest\x12\x13\n\x0blocation_id\x18\x01 \x01(\t\"\x1e\n\x10LocationResponse\x12\n\n\x02id\x18\x01 \x01(\t2\xc0\x01\n\x0fLocationService\x12T\n\x0bGetLocation\x12!.location_service.LocationRequest\x1a\".location_service.LocationResponse\x12W\n\x0e\x43reateLocation\x12!.location_service.LocationRequest\x1a\".location_service.LocationResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'location_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_LOCATIONREQUEST']._serialized_start=36
  _globals['_LOCATIONREQUEST']._serialized_end=74
  _globals['_LOCATIONRESPONSE']._serialized_start=76
  _globals['_LOCATIONRESPONSE']._serialized_end=106
  _globals['_LOCATIONSERVICE']._serialized_start=109
  _globals['_LOCATIONSERVICE']._serialized_end=301
# @@protoc_insertion_point(module_scope)