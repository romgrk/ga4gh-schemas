# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ga4gh/schemas/ga4gh/bio_metadata.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from ga4gh.schemas.ga4gh import metadata_pb2 as ga4gh_dot_schemas_dot_ga4gh_dot_metadata__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ga4gh/schemas/ga4gh/bio_metadata.proto',
  package='ga4gh.schemas.ga4gh',
  syntax='proto3',
  serialized_pb=_b('\n&ga4gh/schemas/ga4gh/bio_metadata.proto\x12\x13ga4gh.schemas.ga4gh\x1a\x1cgoogle/protobuf/struct.proto\x1a\"ga4gh/schemas/ga4gh/metadata.proto\"\xd7\x02\n\nIndividual\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ndataset_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x0f\n\x07\x63reated\x18\x05 \x01(\t\x12\x0f\n\x07updated\x18\x06 \x01(\t\x12\x32\n\x07species\x18\x07 \x01(\x0b\x32!.ga4gh.schemas.ga4gh.OntologyTerm\x12.\n\x03sex\x18\x08 \x01(\x0b\x32!.ga4gh.schemas.ga4gh.OntologyTerm\x12\x37\n\x04info\x18\t \x03(\x0b\x32).ga4gh.schemas.ga4gh.Individual.InfoEntry\x1aG\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.ListValue:\x02\x38\x01\"\xbc\x02\n\tBiosample\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ndataset_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x32\n\x07\x64isease\x18\x05 \x01(\x0b\x32!.ga4gh.schemas.ga4gh.OntologyTerm\x12\x0f\n\x07\x63reated\x18\x06 \x01(\t\x12\x0f\n\x07updated\x18\x07 \x01(\t\x12\x15\n\rindividual_id\x18\x08 \x01(\t\x12\x36\n\x04info\x18\t \x03(\x0b\x32(.ga4gh.schemas.ga4gh.Biosample.InfoEntry\x1aG\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.ListValue:\x02\x38\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,ga4gh_dot_schemas_dot_ga4gh_dot_metadata__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_INDIVIDUAL_INFOENTRY = _descriptor.Descriptor(
  name='InfoEntry',
  full_name='ga4gh.schemas.ga4gh.Individual.InfoEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ga4gh.schemas.ga4gh.Individual.InfoEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='ga4gh.schemas.ga4gh.Individual.InfoEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=402,
  serialized_end=473,
)

_INDIVIDUAL = _descriptor.Descriptor(
  name='Individual',
  full_name='ga4gh.schemas.ga4gh.Individual',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ga4gh.schemas.ga4gh.Individual.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='ga4gh.schemas.ga4gh.Individual.dataset_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='ga4gh.schemas.ga4gh.Individual.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='ga4gh.schemas.ga4gh.Individual.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='created', full_name='ga4gh.schemas.ga4gh.Individual.created', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='updated', full_name='ga4gh.schemas.ga4gh.Individual.updated', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='species', full_name='ga4gh.schemas.ga4gh.Individual.species', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sex', full_name='ga4gh.schemas.ga4gh.Individual.sex', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='info', full_name='ga4gh.schemas.ga4gh.Individual.info', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_INDIVIDUAL_INFOENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=473,
)


_BIOSAMPLE_INFOENTRY = _descriptor.Descriptor(
  name='InfoEntry',
  full_name='ga4gh.schemas.ga4gh.Biosample.InfoEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ga4gh.schemas.ga4gh.Biosample.InfoEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='ga4gh.schemas.ga4gh.Biosample.InfoEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=402,
  serialized_end=473,
)

_BIOSAMPLE = _descriptor.Descriptor(
  name='Biosample',
  full_name='ga4gh.schemas.ga4gh.Biosample',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ga4gh.schemas.ga4gh.Biosample.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='ga4gh.schemas.ga4gh.Biosample.dataset_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='ga4gh.schemas.ga4gh.Biosample.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='ga4gh.schemas.ga4gh.Biosample.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='disease', full_name='ga4gh.schemas.ga4gh.Biosample.disease', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='created', full_name='ga4gh.schemas.ga4gh.Biosample.created', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='updated', full_name='ga4gh.schemas.ga4gh.Biosample.updated', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='individual_id', full_name='ga4gh.schemas.ga4gh.Biosample.individual_id', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='info', full_name='ga4gh.schemas.ga4gh.Biosample.info', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_BIOSAMPLE_INFOENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=476,
  serialized_end=792,
)

_INDIVIDUAL_INFOENTRY.fields_by_name['value'].message_type = google_dot_protobuf_dot_struct__pb2._LISTVALUE
_INDIVIDUAL_INFOENTRY.containing_type = _INDIVIDUAL
_INDIVIDUAL.fields_by_name['species'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_metadata__pb2._ONTOLOGYTERM
_INDIVIDUAL.fields_by_name['sex'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_metadata__pb2._ONTOLOGYTERM
_INDIVIDUAL.fields_by_name['info'].message_type = _INDIVIDUAL_INFOENTRY
_BIOSAMPLE_INFOENTRY.fields_by_name['value'].message_type = google_dot_protobuf_dot_struct__pb2._LISTVALUE
_BIOSAMPLE_INFOENTRY.containing_type = _BIOSAMPLE
_BIOSAMPLE.fields_by_name['disease'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_metadata__pb2._ONTOLOGYTERM
_BIOSAMPLE.fields_by_name['info'].message_type = _BIOSAMPLE_INFOENTRY
DESCRIPTOR.message_types_by_name['Individual'] = _INDIVIDUAL
DESCRIPTOR.message_types_by_name['Biosample'] = _BIOSAMPLE

Individual = _reflection.GeneratedProtocolMessageType('Individual', (_message.Message,), dict(

  InfoEntry = _reflection.GeneratedProtocolMessageType('InfoEntry', (_message.Message,), dict(
    DESCRIPTOR = _INDIVIDUAL_INFOENTRY,
    __module__ = 'ga4gh.schemas.ga4gh.bio_metadata_pb2'
    # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.Individual.InfoEntry)
    ))
  ,
  DESCRIPTOR = _INDIVIDUAL,
  __module__ = 'ga4gh.schemas.ga4gh.bio_metadata_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.Individual)
  ))
_sym_db.RegisterMessage(Individual)
_sym_db.RegisterMessage(Individual.InfoEntry)

Biosample = _reflection.GeneratedProtocolMessageType('Biosample', (_message.Message,), dict(

  InfoEntry = _reflection.GeneratedProtocolMessageType('InfoEntry', (_message.Message,), dict(
    DESCRIPTOR = _BIOSAMPLE_INFOENTRY,
    __module__ = 'ga4gh.schemas.ga4gh.bio_metadata_pb2'
    # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.Biosample.InfoEntry)
    ))
  ,
  DESCRIPTOR = _BIOSAMPLE,
  __module__ = 'ga4gh.schemas.ga4gh.bio_metadata_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.Biosample)
  ))
_sym_db.RegisterMessage(Biosample)
_sym_db.RegisterMessage(Biosample.InfoEntry)


_INDIVIDUAL_INFOENTRY.has_options = True
_INDIVIDUAL_INFOENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_BIOSAMPLE_INFOENTRY.has_options = True
_BIOSAMPLE_INFOENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)