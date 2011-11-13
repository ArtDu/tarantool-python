# -*- coding: utf-8 -*-
# pylint: disable=C0301,W0105,W0401,W0614

import struct


# pylint: disable=C0103
struct_BL = struct.Struct("<BL")
struct_LB = struct.Struct("<LB")
struct_L = struct.Struct("<L")
struct_LL = struct.Struct("<LL")
struct_LLL = struct.Struct("<LLL")
struct_LLLL = struct.Struct("<LLLL")
struct_LLLLL = struct.Struct("<LLLLL")


REQUEST_TYPE_CALL = 22
REQUEST_TYPE_DELETE = 21
REQUEST_TYPE_INSERT = 13
REQUEST_TYPE_SELECT = 17
REQUEST_TYPE_UPDATE = 19


UPDATE_OPERATION_CODE = {'=': 0, '+': 1, '&': 2, '^': 3, '|': 4, 'splice': 5}