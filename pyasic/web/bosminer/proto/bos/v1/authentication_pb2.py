# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bos/v1/authentication.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1b\x62os/v1/authentication.proto\x12\x0e\x62raiins.bos.v1"2\n\x0cLoginRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t"\x0f\n\rLoginResponse"8\n\x12SetPasswordRequest\x12\x15\n\x08password\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x0b\n\t_password"\x15\n\x13SetPasswordResponse2\xb5\x01\n\x15\x41uthenticationService\x12\x44\n\x05Login\x12\x1c.braiins.bos.v1.LoginRequest\x1a\x1d.braiins.bos.v1.LoginResponse\x12V\n\x0bSetPassword\x12".braiins.bos.v1.SetPasswordRequest\x1a#.braiins.bos.v1.SetPasswordResponseb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "bos.v1.authentication_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_LOGINREQUEST"]._serialized_start = 47
    _globals["_LOGINREQUEST"]._serialized_end = 97
    _globals["_LOGINRESPONSE"]._serialized_start = 99
    _globals["_LOGINRESPONSE"]._serialized_end = 114
    _globals["_SETPASSWORDREQUEST"]._serialized_start = 116
    _globals["_SETPASSWORDREQUEST"]._serialized_end = 172
    _globals["_SETPASSWORDRESPONSE"]._serialized_start = 174
    _globals["_SETPASSWORDRESPONSE"]._serialized_end = 195
    _globals["_AUTHENTICATIONSERVICE"]._serialized_start = 198
    _globals["_AUTHENTICATIONSERVICE"]._serialized_end = 379
# @@protoc_insertion_point(module_scope)
