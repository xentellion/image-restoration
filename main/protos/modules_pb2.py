# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/modules.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14protos/modules.proto\x12\x06module\"1\n\rModuleRequest\x12\x12\n\nisMultiple\x18\x01 \x01(\x08\x12\x0c\n\x04text\x18\x02 \x01(\t\"\x1e\n\x0bModuleReply\x12\x0f\n\x07message\x18\x01 \x01(\t2\xfc\x01\n\x06Module\x12<\n\x0cSimSwapImage\x12\x15.module.ModuleRequest\x1a\x13.module.ModuleReply\"\x00\x12<\n\x0cSimSwapVideo\x12\x15.module.ModuleRequest\x1a\x13.module.ModuleReply\"\x00\x12:\n\nGhostImage\x12\x15.module.ModuleRequest\x1a\x13.module.ModuleReply\"\x00\x12:\n\nGhostVideo\x12\x15.module.ModuleRequest\x1a\x13.module.ModuleReply\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.modules_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MODULEREQUEST._serialized_start=32
  _MODULEREQUEST._serialized_end=81
  _MODULEREPLY._serialized_start=83
  _MODULEREPLY._serialized_end=113
  _MODULE._serialized_start=116
  _MODULE._serialized_end=368
# @@protoc_insertion_point(module_scope)
