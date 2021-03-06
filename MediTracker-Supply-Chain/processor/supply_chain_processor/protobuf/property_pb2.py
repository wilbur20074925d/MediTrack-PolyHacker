# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: supply_chain_processor/protobuf/property.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='supply_chain_processor/protobuf/property.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n.supply_chain_processor/protobuf/property.proto\"\xe9\x01\n\x08Property\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\trecord_id\x18\x02 \x01(\t\x12+\n\tdata_type\x18\x03 \x01(\x0e\x32\x18.PropertySchema.DataType\x12%\n\treporters\x18\x04 \x03(\x0b\x32\x12.Property.Reporter\x12\x14\n\x0c\x63urrent_page\x18\x05 \x01(\r\x12\x0f\n\x07wrapped\x18\x06 \x01(\x08\x1a\x41\n\x08Reporter\x12\x12\n\npublic_key\x18\x01 \x01(\t\x12\x12\n\nauthorized\x18\x02 \x01(\x08\x12\r\n\x05index\x18\x03 \x01(\r\"/\n\x11PropertyContainer\x12\x1a\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\t.Property\"\xa2\x01\n\x0ePropertySchema\x12\x0c\n\x04name\x18\x01 \x01(\t\x12+\n\tdata_type\x18\x02 \x01(\x0e\x32\x18.PropertySchema.DataType\x12\x10\n\x08required\x18\x03 \x01(\x08\"C\n\x08\x44\x61taType\x12\t\n\x05\x42YTES\x10\x00\x12\n\n\x06STRING\x10\x01\x12\x07\n\x03INT\x10\x02\x12\t\n\x05\x46LOAT\x10\x03\x12\x0c\n\x08LOCATION\x10\x04\"\xc0\x01\n\rPropertyValue\x12\x0c\n\x04name\x18\x01 \x01(\t\x12+\n\tdata_type\x18\x02 \x01(\x0e\x32\x18.PropertySchema.DataType\x12\x13\n\x0b\x62ytes_value\x18\x0b \x01(\x0c\x12\x14\n\x0cstring_value\x18\x0c \x01(\t\x12\x11\n\tint_value\x18\r \x01(\x12\x12\x13\n\x0b\x66loat_value\x18\x0e \x01(\x02\x12!\n\x0elocation_value\x18\x0f \x01(\x0b\x32\t.Location\"\x98\x02\n\x0cPropertyPage\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\trecord_id\x18\x02 \x01(\t\x12\x34\n\x0freported_values\x18\x03 \x03(\x0b\x32\x1b.PropertyPage.ReportedValue\x1a\xb0\x01\n\rReportedValue\x12\x16\n\x0ereporter_index\x18\x01 \x01(\r\x12\x11\n\ttimestamp\x18\x02 \x01(\x04\x12\x13\n\x0b\x62ytes_value\x18\x0b \x01(\x0c\x12\x14\n\x0cstring_value\x18\x0c \x01(\t\x12\x11\n\tint_value\x18\r \x01(\x12\x12\x13\n\x0b\x66loat_value\x18\x0e \x01(\x02\x12!\n\x0elocation_value\x18\x0f \x01(\x0b\x32\t.Location\"7\n\x15PropertyPageContainer\x12\x1e\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\r.PropertyPage\"/\n\x08Location\x12\x10\n\x08latitude\x18\x01 \x01(\x12\x12\x11\n\tlongitude\x18\x02 \x01(\x12\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PROPERTYSCHEMA_DATATYPE = _descriptor.EnumDescriptor(
  name='DataType',
  full_name='PropertySchema.DataType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BYTES', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCATION', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=431,
  serialized_end=498,
)
_sym_db.RegisterEnumDescriptor(_PROPERTYSCHEMA_DATATYPE)


_PROPERTY_REPORTER = _descriptor.Descriptor(
  name='Reporter',
  full_name='Property.Reporter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='public_key', full_name='Property.Reporter.public_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='authorized', full_name='Property.Reporter.authorized', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='index', full_name='Property.Reporter.index', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=219,
  serialized_end=284,
)

_PROPERTY = _descriptor.Descriptor(
  name='Property',
  full_name='Property',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Property.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='record_id', full_name='Property.record_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data_type', full_name='Property.data_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reporters', full_name='Property.reporters', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_page', full_name='Property.current_page', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wrapped', full_name='Property.wrapped', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PROPERTY_REPORTER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=284,
)


_PROPERTYCONTAINER = _descriptor.Descriptor(
  name='PropertyContainer',
  full_name='PropertyContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entries', full_name='PropertyContainer.entries', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=286,
  serialized_end=333,
)


_PROPERTYSCHEMA = _descriptor.Descriptor(
  name='PropertySchema',
  full_name='PropertySchema',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='PropertySchema.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data_type', full_name='PropertySchema.data_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='required', full_name='PropertySchema.required', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PROPERTYSCHEMA_DATATYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=336,
  serialized_end=498,
)


_PROPERTYVALUE = _descriptor.Descriptor(
  name='PropertyValue',
  full_name='PropertyValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='PropertyValue.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data_type', full_name='PropertyValue.data_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bytes_value', full_name='PropertyValue.bytes_value', index=2,
      number=11, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='PropertyValue.string_value', index=3,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='int_value', full_name='PropertyValue.int_value', index=4,
      number=13, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='float_value', full_name='PropertyValue.float_value', index=5,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location_value', full_name='PropertyValue.location_value', index=6,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=501,
  serialized_end=693,
)


_PROPERTYPAGE_REPORTEDVALUE = _descriptor.Descriptor(
  name='ReportedValue',
  full_name='PropertyPage.ReportedValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reporter_index', full_name='PropertyPage.ReportedValue.reporter_index', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='PropertyPage.ReportedValue.timestamp', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bytes_value', full_name='PropertyPage.ReportedValue.bytes_value', index=2,
      number=11, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='PropertyPage.ReportedValue.string_value', index=3,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='int_value', full_name='PropertyPage.ReportedValue.int_value', index=4,
      number=13, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='float_value', full_name='PropertyPage.ReportedValue.float_value', index=5,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location_value', full_name='PropertyPage.ReportedValue.location_value', index=6,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=800,
  serialized_end=976,
)

_PROPERTYPAGE = _descriptor.Descriptor(
  name='PropertyPage',
  full_name='PropertyPage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='PropertyPage.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='record_id', full_name='PropertyPage.record_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reported_values', full_name='PropertyPage.reported_values', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PROPERTYPAGE_REPORTEDVALUE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=696,
  serialized_end=976,
)


_PROPERTYPAGECONTAINER = _descriptor.Descriptor(
  name='PropertyPageContainer',
  full_name='PropertyPageContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entries', full_name='PropertyPageContainer.entries', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=978,
  serialized_end=1033,
)


_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='Location.latitude', index=0,
      number=1, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='Location.longitude', index=1,
      number=2, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1035,
  serialized_end=1082,
)

_PROPERTY_REPORTER.containing_type = _PROPERTY
_PROPERTY.fields_by_name['data_type'].enum_type = _PROPERTYSCHEMA_DATATYPE
_PROPERTY.fields_by_name['reporters'].message_type = _PROPERTY_REPORTER
_PROPERTYCONTAINER.fields_by_name['entries'].message_type = _PROPERTY
_PROPERTYSCHEMA.fields_by_name['data_type'].enum_type = _PROPERTYSCHEMA_DATATYPE
_PROPERTYSCHEMA_DATATYPE.containing_type = _PROPERTYSCHEMA
_PROPERTYVALUE.fields_by_name['data_type'].enum_type = _PROPERTYSCHEMA_DATATYPE
_PROPERTYVALUE.fields_by_name['location_value'].message_type = _LOCATION
_PROPERTYPAGE_REPORTEDVALUE.fields_by_name['location_value'].message_type = _LOCATION
_PROPERTYPAGE_REPORTEDVALUE.containing_type = _PROPERTYPAGE
_PROPERTYPAGE.fields_by_name['reported_values'].message_type = _PROPERTYPAGE_REPORTEDVALUE
_PROPERTYPAGECONTAINER.fields_by_name['entries'].message_type = _PROPERTYPAGE
DESCRIPTOR.message_types_by_name['Property'] = _PROPERTY
DESCRIPTOR.message_types_by_name['PropertyContainer'] = _PROPERTYCONTAINER
DESCRIPTOR.message_types_by_name['PropertySchema'] = _PROPERTYSCHEMA
DESCRIPTOR.message_types_by_name['PropertyValue'] = _PROPERTYVALUE
DESCRIPTOR.message_types_by_name['PropertyPage'] = _PROPERTYPAGE
DESCRIPTOR.message_types_by_name['PropertyPageContainer'] = _PROPERTYPAGECONTAINER
DESCRIPTOR.message_types_by_name['Location'] = _LOCATION

Property = _reflection.GeneratedProtocolMessageType('Property', (_message.Message,), dict(

  Reporter = _reflection.GeneratedProtocolMessageType('Reporter', (_message.Message,), dict(
    DESCRIPTOR = _PROPERTY_REPORTER,
    __module__ = 'supply_chain_processor.protobuf.property_pb2'
    # @@protoc_insertion_point(class_scope:Property.Reporter)
    ))
  ,
  DESCRIPTOR = _PROPERTY,
  __module__ = 'supply_chain_processor.protobuf.property_pb2'
  # @@protoc_insertion_point(class_scope:Property)
  ))
_sym_db.RegisterMessage(Property)
_sym_db.RegisterMessage(Property.Reporter)

PropertyContainer = _reflection.GeneratedProtocolMessageType('PropertyContainer', (_message.Message,), dict(
  DESCRIPTOR = _PROPERTYCONTAINER,
  __module__ = 'supply_chain_processor.protobuf.property_pb2'
  # @@protoc_insertion_point(class_scope:PropertyContainer)
  ))
_sym_db.RegisterMessage(PropertyContainer)

PropertySchema = _reflection.GeneratedProtocolMessageType('PropertySchema', (_message.Message,), dict(
  DESCRIPTOR = _PROPERTYSCHEMA,
  __module__ = 'supply_chain_processor.protobuf.property_pb2'
  # @@protoc_insertion_point(class_scope:PropertySchema)
  ))
_sym_db.RegisterMessage(PropertySchema)

PropertyValue = _reflection.GeneratedProtocolMessageType('PropertyValue', (_message.Message,), dict(
  DESCRIPTOR = _PROPERTYVALUE,
  __module__ = 'supply_chain_processor.protobuf.property_pb2'
  # @@protoc_insertion_point(class_scope:PropertyValue)
  ))
_sym_db.RegisterMessage(PropertyValue)

PropertyPage = _reflection.GeneratedProtocolMessageType('PropertyPage', (_message.Message,), dict(

  ReportedValue = _reflection.GeneratedProtocolMessageType('ReportedValue', (_message.Message,), dict(
    DESCRIPTOR = _PROPERTYPAGE_REPORTEDVALUE,
    __module__ = 'supply_chain_processor.protobuf.property_pb2'
    # @@protoc_insertion_point(class_scope:PropertyPage.ReportedValue)
    ))
  ,
  DESCRIPTOR = _PROPERTYPAGE,
  __module__ = 'supply_chain_processor.protobuf.property_pb2'
  # @@protoc_insertion_point(class_scope:PropertyPage)
  ))
_sym_db.RegisterMessage(PropertyPage)
_sym_db.RegisterMessage(PropertyPage.ReportedValue)

PropertyPageContainer = _reflection.GeneratedProtocolMessageType('PropertyPageContainer', (_message.Message,), dict(
  DESCRIPTOR = _PROPERTYPAGECONTAINER,
  __module__ = 'supply_chain_processor.protobuf.property_pb2'
  # @@protoc_insertion_point(class_scope:PropertyPageContainer)
  ))
_sym_db.RegisterMessage(PropertyPageContainer)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), dict(
  DESCRIPTOR = _LOCATION,
  __module__ = 'supply_chain_processor.protobuf.property_pb2'
  # @@protoc_insertion_point(class_scope:Location)
  ))
_sym_db.RegisterMessage(Location)


# @@protoc_insertion_point(module_scope)
