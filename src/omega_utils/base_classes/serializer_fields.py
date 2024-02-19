from rest_framework import serializers
import uuid
import json
from typing import Union
from django.utils import timezone
from pypsst import Utils


class BinarySerializationField(serializers.Field):
    """
    Serializer field for binary data.

    This converts a django.db.models.BinaryField to a hexadecimal string
    and vice versa. This way binary data can be sent over the API.
    """

    def to_representation(self, obj: bytes) -> str:
        """Convert the binary data to a string."""
        if isinstance(obj, str):
            return obj
        if not isinstance(obj, bytes):
            raise TypeError(f"Expected bytes, got {type(obj)}")
        return obj.hex()

    def to_internal_value(self, data: str) -> bytes:
        """Convert the string to binary data."""
        if isinstance(data, bytes):
            return data
        if not isinstance(data, str):
            raise TypeError(f"Expected str, got {type(data)}")
        return bytes.fromhex(data)


class UuidField(serializers.Field):
    """
    Serializer field for a uuid4 class
    
    This converts a uuid.uuid4() instance to a hexadecimal string and
    vice versa. This way uuid4's can be serialized using the restframework
    serialization class
    """

    def to_representation(self, value: uuid.UUID):
        """Converts the uuid to a string."""
        if isinstance(value, str):
            return value
        return value.hex
    
    def to_internal_value(self, data: str) -> uuid.UUID:
        """Converts the string to a uuid."""
        if isinstance(data, uuid.UUID):
            return data
        return uuid.UUID(hex=data, version=4)


class JsonSerializationField(serializers.Field):
    """Serializer field for json data."""

    def to_representation(self, obj: Union[str, dict]) -> str:
        """Convert the json data to a string."""
        if isinstance(obj, str):
            return obj
        return json.dumps(obj)

    def to_internal_value(self, data: str) -> Union[str, dict]:
        """Convert the string to dict data."""
        if isinstance(data, bytes):
            return data
        return json.loads(data)
        

class DateTimeSerializerField(serializers.Field):
    """Serializer field for datetime data with timezone."""

    def to_representation(self, obj: timezone.datetime) -> str:
        """Convert the datetime data to a string."""
        if isinstance(obj, str):
            return obj
        return obj.strftime(format=Utils.DATETIME_FORMAT)

    def to_internal_value(self, data: str) -> timezone.datetime:
        """Convert the string to datetime data."""
        if isinstance(data, timezone.datetime):
            return data
        return timezone.datetime.strptime(data, Utils.DATETIME_FORMAT)