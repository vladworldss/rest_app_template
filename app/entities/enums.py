from enum import Enum


class HTTPMethod(str, Enum):
    POST = 'POST'
    GET = 'GET'
    DELETE = 'DELETE'
    PUT = 'PUT'


class Direction(str, Enum):
    INCOMING = 'incoming'
    OUTGOING = 'outgoing'


class EmailStatus(int, Enum):
    DRAFT = 0
    SEND = 1
    ERROR = 2
