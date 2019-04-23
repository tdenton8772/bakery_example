# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: database.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='database.proto',
  package='org.querc.cb_grpc.msg.database',
  syntax='proto3',
  serialized_options=_b('\n\025org.querc.cb_grpc.msgB\010database'),
  serialized_pb=_b('\n\x0e\x64\x61tabase.proto\x12\x1eorg.querc.cb_grpc.msg.database\"\x0b\n\tConnected\")\n\x06TxnLog\x12\x0e\n\x06\x64oc_id\x18\x01 \x01(\t\x12\x0f\n\x07\x63hanges\x18\x02 \x03(\tB!\n\x15org.querc.cb_grpc.msgB\x08\x64\x61tabaseb\x06proto3')
)




_CONNECTED = _descriptor.Descriptor(
  name='Connected',
  full_name='org.querc.cb_grpc.msg.database.Connected',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=61,
)


_TXNLOG = _descriptor.Descriptor(
  name='TxnLog',
  full_name='org.querc.cb_grpc.msg.database.TxnLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='doc_id', full_name='org.querc.cb_grpc.msg.database.TxnLog.doc_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='changes', full_name='org.querc.cb_grpc.msg.database.TxnLog.changes', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=104,
)

DESCRIPTOR.message_types_by_name['Connected'] = _CONNECTED
DESCRIPTOR.message_types_by_name['TxnLog'] = _TXNLOG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Connected = _reflection.GeneratedProtocolMessageType('Connected', (_message.Message,), dict(
  DESCRIPTOR = _CONNECTED,
  __module__ = 'database_pb2'
  # @@protoc_insertion_point(class_scope:org.querc.cb_grpc.msg.database.Connected)
  ))
_sym_db.RegisterMessage(Connected)

TxnLog = _reflection.GeneratedProtocolMessageType('TxnLog', (_message.Message,), dict(
  DESCRIPTOR = _TXNLOG,
  __module__ = 'database_pb2'
  # @@protoc_insertion_point(class_scope:org.querc.cb_grpc.msg.database.TxnLog)
  ))
_sym_db.RegisterMessage(TxnLog)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)