# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_query.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='grpc_query.proto',
  package='cb_grpc.msg.Main',
  syntax='proto3',
  serialized_options=_b('\n\032org.querc.cb_grpc.msg.grpcB\016QueryCouchbaseP\001'),
  serialized_pb=_b('\n\x10grpc_query.proto\x12\x10\x63\x62_grpc.msg.Main\x1a\x19google/protobuf/any.proto\"\x1a\n\x05Query\x12\x11\n\tN1QlQuery\x18\x01 \x01(\t\".\n\rQueryResponse\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\"A\n\x05\x44ocID\x12)\n\x06\x62ucket\x18\x01 \x01(\x0e\x32\x19.cb_grpc.msg.Main.Buckets\x12\r\n\x05\x64ocID\x18\x02 \x01(\t\"T\n\x06JsonID\x12)\n\x06\x62ucket\x18\x01 \x01(\x0e\x32\x19.cb_grpc.msg.Main.Buckets\x12\r\n\x05\x64ocID\x18\x02 \x01(\t\x12\x10\n\x08\x64ocument\x18\x03 \x01(\t\"h\n\x05\x41nyID\x12)\n\x06\x62ucket\x18\x01 \x01(\x0e\x32\x19.cb_grpc.msg.Main.Buckets\x12\r\n\x05\x64ocID\x18\x02 \x01(\t\x12%\n\x07\x64\x65tails\x18\x03 \x03(\x0b\x32\x14.google.protobuf.Any*%\n\x07\x42uckets\x12\x08\n\x04main\x10\x00\x12\x07\n\x03txn\x10\x01\x12\x07\n\x03hxn\x10\x02\x32\xbd\x03\n\x0cQueryService\x12G\n\tn1qlQuery\x12\x17.cb_grpc.msg.Main.Query\x1a\x1f.cb_grpc.msg.Main.QueryResponse\"\x00\x12\x43\n\x05kvGet\x12\x17.cb_grpc.msg.Main.DocID\x1a\x1f.cb_grpc.msg.Main.QueryResponse\"\x00\x12\x46\n\x08kvDelete\x12\x17.cb_grpc.msg.Main.DocID\x1a\x1f.cb_grpc.msg.Main.QueryResponse\"\x00\x12\x44\n\x05kvPut\x12\x18.cb_grpc.msg.Main.JsonID\x1a\x1f.cb_grpc.msg.Main.QueryResponse\"\x00\x12G\n\x08kvUpsert\x12\x18.cb_grpc.msg.Main.JsonID\x1a\x1f.cb_grpc.msg.Main.QueryResponse\"\x00\x12H\n\nanyService\x12\x17.cb_grpc.msg.Main.AnyID\x1a\x1f.cb_grpc.msg.Main.QueryResponse\"\x00\x42.\n\x1aorg.querc.cb_grpc.msg.grpcB\x0eQueryCouchbaseP\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])

_BUCKETS = _descriptor.EnumDescriptor(
  name='Buckets',
  full_name='cb_grpc.msg.Main.Buckets',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='main', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='txn', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='hxn', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=400,
  serialized_end=437,
)
_sym_db.RegisterEnumDescriptor(_BUCKETS)

Buckets = enum_type_wrapper.EnumTypeWrapper(_BUCKETS)
main = 0
txn = 1
hxn = 2



_QUERY = _descriptor.Descriptor(
  name='Query',
  full_name='cb_grpc.msg.Main.Query',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='N1QlQuery', full_name='cb_grpc.msg.Main.Query.N1QlQuery', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=65,
  serialized_end=91,
)


_QUERYRESPONSE = _descriptor.Descriptor(
  name='QueryResponse',
  full_name='cb_grpc.msg.Main.QueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='cb_grpc.msg.Main.QueryResponse.content', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='cb_grpc.msg.Main.QueryResponse.code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=93,
  serialized_end=139,
)


_DOCID = _descriptor.Descriptor(
  name='DocID',
  full_name='cb_grpc.msg.Main.DocID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bucket', full_name='cb_grpc.msg.Main.DocID.bucket', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='docID', full_name='cb_grpc.msg.Main.DocID.docID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=141,
  serialized_end=206,
)


_JSONID = _descriptor.Descriptor(
  name='JsonID',
  full_name='cb_grpc.msg.Main.JsonID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bucket', full_name='cb_grpc.msg.Main.JsonID.bucket', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='docID', full_name='cb_grpc.msg.Main.JsonID.docID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='document', full_name='cb_grpc.msg.Main.JsonID.document', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=208,
  serialized_end=292,
)


_ANYID = _descriptor.Descriptor(
  name='AnyID',
  full_name='cb_grpc.msg.Main.AnyID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bucket', full_name='cb_grpc.msg.Main.AnyID.bucket', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='docID', full_name='cb_grpc.msg.Main.AnyID.docID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='details', full_name='cb_grpc.msg.Main.AnyID.details', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=294,
  serialized_end=398,
)

_DOCID.fields_by_name['bucket'].enum_type = _BUCKETS
_JSONID.fields_by_name['bucket'].enum_type = _BUCKETS
_ANYID.fields_by_name['bucket'].enum_type = _BUCKETS
_ANYID.fields_by_name['details'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['Query'] = _QUERY
DESCRIPTOR.message_types_by_name['QueryResponse'] = _QUERYRESPONSE
DESCRIPTOR.message_types_by_name['DocID'] = _DOCID
DESCRIPTOR.message_types_by_name['JsonID'] = _JSONID
DESCRIPTOR.message_types_by_name['AnyID'] = _ANYID
DESCRIPTOR.enum_types_by_name['Buckets'] = _BUCKETS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Query = _reflection.GeneratedProtocolMessageType('Query', (_message.Message,), dict(
  DESCRIPTOR = _QUERY,
  __module__ = 'grpc_query_pb2'
  # @@protoc_insertion_point(class_scope:cb_grpc.msg.Main.Query)
  ))
_sym_db.RegisterMessage(Query)

QueryResponse = _reflection.GeneratedProtocolMessageType('QueryResponse', (_message.Message,), dict(
  DESCRIPTOR = _QUERYRESPONSE,
  __module__ = 'grpc_query_pb2'
  # @@protoc_insertion_point(class_scope:cb_grpc.msg.Main.QueryResponse)
  ))
_sym_db.RegisterMessage(QueryResponse)

DocID = _reflection.GeneratedProtocolMessageType('DocID', (_message.Message,), dict(
  DESCRIPTOR = _DOCID,
  __module__ = 'grpc_query_pb2'
  # @@protoc_insertion_point(class_scope:cb_grpc.msg.Main.DocID)
  ))
_sym_db.RegisterMessage(DocID)

JsonID = _reflection.GeneratedProtocolMessageType('JsonID', (_message.Message,), dict(
  DESCRIPTOR = _JSONID,
  __module__ = 'grpc_query_pb2'
  # @@protoc_insertion_point(class_scope:cb_grpc.msg.Main.JsonID)
  ))
_sym_db.RegisterMessage(JsonID)

AnyID = _reflection.GeneratedProtocolMessageType('AnyID', (_message.Message,), dict(
  DESCRIPTOR = _ANYID,
  __module__ = 'grpc_query_pb2'
  # @@protoc_insertion_point(class_scope:cb_grpc.msg.Main.AnyID)
  ))
_sym_db.RegisterMessage(AnyID)


DESCRIPTOR._options = None

_QUERYSERVICE = _descriptor.ServiceDescriptor(
  name='QueryService',
  full_name='cb_grpc.msg.Main.QueryService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=440,
  serialized_end=885,
  methods=[
  _descriptor.MethodDescriptor(
    name='n1qlQuery',
    full_name='cb_grpc.msg.Main.QueryService.n1qlQuery',
    index=0,
    containing_service=None,
    input_type=_QUERY,
    output_type=_QUERYRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='kvGet',
    full_name='cb_grpc.msg.Main.QueryService.kvGet',
    index=1,
    containing_service=None,
    input_type=_DOCID,
    output_type=_QUERYRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='kvDelete',
    full_name='cb_grpc.msg.Main.QueryService.kvDelete',
    index=2,
    containing_service=None,
    input_type=_DOCID,
    output_type=_QUERYRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='kvPut',
    full_name='cb_grpc.msg.Main.QueryService.kvPut',
    index=3,
    containing_service=None,
    input_type=_JSONID,
    output_type=_QUERYRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='kvUpsert',
    full_name='cb_grpc.msg.Main.QueryService.kvUpsert',
    index=4,
    containing_service=None,
    input_type=_JSONID,
    output_type=_QUERYRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='anyService',
    full_name='cb_grpc.msg.Main.QueryService.anyService',
    index=5,
    containing_service=None,
    input_type=_ANYID,
    output_type=_QUERYRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_QUERYSERVICE)

DESCRIPTOR.services_by_name['QueryService'] = _QUERYSERVICE

# @@protoc_insertion_point(module_scope)
