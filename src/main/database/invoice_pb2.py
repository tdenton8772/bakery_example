# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: database/invoice.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='database/invoice.proto',
  package='org.querc.cb_grpc.msg.Invoice',
  syntax='proto3',
  serialized_options=_b('\n\025org.querc.cb_grpc.msgB\007Invoice'),
  serialized_pb=_b('\n\x16\x64\x61tabase/invoice.proto\x12\x1dorg.querc.cb_grpc.msg.Invoice\"\x9e\t\n\nnewInvoice\x12\x10\n\x08jsonType\x18\x01 \x01(\t\x12\r\n\x05\x64ocID\x18\x02 \x01(\t\x12\x0f\n\x07\x63omment\x18\x03 \x01(\t\x12\x10\n\x08\x64\x61te_due\x18\x04 \x01(\t\x12\x13\n\x0b\x63reate_date\x18\x05 \x01(\t\x12\x17\n\x0fpartner_bank_id\x18\x06 \x01(\t\x12\x0e\n\x06number\x18\x07 \x01(\t\x12\x12\n\njournal_id\x18\x08 \x01(\r\x12#\n\x1b\x61mount_total_company_signed\x18\t \x01(\x02\x12\x10\n\x08residual\x18\n \x01(\x02\x12\x12\n\npartner_id\x18\x0b \x01(\r\x12\x12\n\ncreate_uid\x18\x0c \x01(\t\x12\x16\n\x0e\x61mount_untaxed\x18\r \x01(\x02\x12\x11\n\treference\x18\x0e \x01(\t\x12\x1f\n\x17residual_company_signed\x18\x0f \x01(\x02\x12\x1b\n\x13\x61mount_total_signed\x18\x10 \x01(\x02\x12\x19\n\x11message_last_post\x18\x11 \x01(\t\x12\x12\n\ncompany_id\x18\x12 \x01(\r\x12\x12\n\namount_tax\x18\x13 \x01(\x02\x12\x0f\n\x07move_id\x18\x14 \x01(\t\x12\x0c\n\x04sent\x18\x15 \x01(\x08\x12\x12\n\naccount_id\x18\x16 \x01(\r\x12\x12\n\nreconciled\x18\x17 \x01(\x08\x12\x0e\n\x06origin\x18\x18 \x01(\t\x12\x11\n\tmove_name\x18\x19 \x01(\t\x12\x16\n\x0ereference_type\x18\x1a \x01(\r\x12\x14\n\x0c\x64\x61te_invoice\x18\x1b \x01(\t\x12\x17\n\x0fpayment_term_id\x18\x1c \x01(\r\x12\x12\n\nwrite_date\x18\x1d \x01(\t\x12\x17\n\x0fresidual_signed\x18\x1e \x01(\x02\x12\x0c\n\x04\x64\x61te\x18\x1f \x01(\t\x12\x0f\n\x07user_id\x18  \x01(\r\x12\x11\n\twrite_uid\x18! \x01(\r\x12\x1a\n\x12\x66iscal_position_id\x18\" \x01(\r\x12\x14\n\x0c\x61mount_total\x18# \x01(\x02\x12\x1d\n\x15\x61mount_untaxed_signed\x18$ \x01(\x02\x12\x13\n\x0b\x63urrency_id\x18% \x01(\r\x12\x19\n\x11refund_invoice_id\x18& \x01(\r\x12\x0c\n\x04name\x18\' \x01(\t\x12\x1d\n\x15\x63ommercial_partner_id\x18( \x01(\r\x12\x1b\n\x13partner_shipping_id\x18) \x01(\r\x12\x0f\n\x07team_id\x18* \x01(\r\x12\x13\n\x0b\x63\x61mpaign_id\x18+ \x01(\t\x12\x14\n\x0cincoterms_id\x18, \x01(\r\x12\x13\n\x0bpurchase_id\x18- \x01(\t\x12\x19\n\x11x_sales_territory\x18. \x01(\t\x12\x17\n\x0f\x61uto_invoice_id\x18/ \x01(\x08\x12\x16\n\x0e\x61uto_generated\x18\x30 \x01(\x08\"#\n\x05state\x12\x10\n\x0c\x64\x65\x66\x61ultValue\x10\x00\x12\x08\n\x04paid\x10\x01\"(\n\x06Medium\x12\x11\n\rdefaultMedium\x10\x00\x12\x0b\n\x07medium1\x10\x01\"(\n\x06Source\x12\x11\n\rdefaultSource\x10\x00\x12\x0b\n\x07source1\x10\x01\x42 \n\x15org.querc.cb_grpc.msgB\x07Invoiceb\x06proto3')
)



_NEWINVOICE_STATE = _descriptor.EnumDescriptor(
  name='state',
  full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.state',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='defaultValue', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='paid', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1121,
  serialized_end=1156,
)
_sym_db.RegisterEnumDescriptor(_NEWINVOICE_STATE)

_NEWINVOICE_MEDIUM = _descriptor.EnumDescriptor(
  name='Medium',
  full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.Medium',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='defaultMedium', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='medium1', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1158,
  serialized_end=1198,
)
_sym_db.RegisterEnumDescriptor(_NEWINVOICE_MEDIUM)

_NEWINVOICE_SOURCE = _descriptor.EnumDescriptor(
  name='Source',
  full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.Source',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='defaultSource', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='source1', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1200,
  serialized_end=1240,
)
_sym_db.RegisterEnumDescriptor(_NEWINVOICE_SOURCE)


_NEWINVOICE = _descriptor.Descriptor(
  name='newInvoice',
  full_name='org.querc.cb_grpc.msg.Invoice.newInvoice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jsonType', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.jsonType', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='docID', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.docID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comment', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.comment', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date_due', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.date_due', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_date', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.create_date', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partner_bank_id', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.partner_bank_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='number', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.number', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='journal_id', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.journal_id', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount_total_company_signed', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.amount_total_company_signed', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='residual', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.residual', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partner_id', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.partner_id', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_uid', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.create_uid', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount_untaxed', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.amount_untaxed', index=12,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reference', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.reference', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='residual_company_signed', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.residual_company_signed', index=14,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount_total_signed', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.amount_total_signed', index=15,
      number=16, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message_last_post', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.message_last_post', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='company_id', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.company_id', index=17,
      number=18, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount_tax', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.amount_tax', index=18,
      number=19, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='move_id', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.move_id', index=19,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sent', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.sent', index=20,
      number=21, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account_id', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.account_id', index=21,
      number=22, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reconciled', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.reconciled', index=22,
      number=23, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='origin', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.origin', index=23,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='move_name', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.move_name', index=24,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reference_type', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.reference_type', index=25,
      number=26, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date_invoice', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.date_invoice', index=26,
      number=27, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payment_term_id', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.payment_term_id', index=27,
      number=28, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='write_date', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.write_date', index=28,
      number=29, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='residual_signed', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.residual_signed', index=29,
      number=30, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.date', index=30,
      number=31, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.user_id', index=31,
      number=32, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='write_uid', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.write_uid', index=32,
      number=33, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fiscal_position_id', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.fiscal_position_id', index=33,
      number=34, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount_total', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.amount_total', index=34,
      number=35, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount_untaxed_signed', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.amount_untaxed_signed', index=35,
      number=36, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currency_id', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.currency_id', index=36,
      number=37, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='refund_invoice_id', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.refund_invoice_id', index=37,
      number=38, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.name', index=38,
      number=39, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commercial_partner_id', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.commercial_partner_id', index=39,
      number=40, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partner_shipping_id', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.partner_shipping_id', index=40,
      number=41, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='team_id', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.team_id', index=41,
      number=42, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='campaign_id', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.campaign_id', index=42,
      number=43, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='incoterms_id', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.incoterms_id', index=43,
      number=44, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='purchase_id', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.purchase_id', index=44,
      number=45, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='x_sales_territory', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.x_sales_territory', index=45,
      number=46, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auto_invoice_id', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.auto_invoice_id', index=46,
      number=47, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auto_generated', full_name='org.querc.cb_grpc.msg.Invoice.newInvoice.auto_generated', index=47,
      number=48, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _NEWINVOICE_STATE,
    _NEWINVOICE_MEDIUM,
    _NEWINVOICE_SOURCE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=1240,
)

_NEWINVOICE_STATE.containing_type = _NEWINVOICE
_NEWINVOICE_MEDIUM.containing_type = _NEWINVOICE
_NEWINVOICE_SOURCE.containing_type = _NEWINVOICE
DESCRIPTOR.message_types_by_name['newInvoice'] = _NEWINVOICE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

newInvoice = _reflection.GeneratedProtocolMessageType('newInvoice', (_message.Message,), dict(
  DESCRIPTOR = _NEWINVOICE,
  __module__ = 'database.invoice_pb2'
  # @@protoc_insertion_point(class_scope:org.querc.cb_grpc.msg.Invoice.newInvoice)
  ))
_sym_db.RegisterMessage(newInvoice)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)