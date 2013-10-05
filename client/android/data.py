#!/usr/bin/env python2.7
#-*- coding:utf-8 -*-

from types import BooleanType, IntType, UnicodeType, NoneType

class Data(object):
    # row is (DataType, DefaultValue,) 
    struct = {'id': (IntType, None,),
            'title': (UnicodeType, '',),
            'description': (UnicodeType, '',),
            'deadline': (UnicodeType, '',),
            'create_date': (UnicodeType, None,),
            'done': (BooleanType, False,)}
    data = []
    current = -1

    #--- data ---#
    @staticmethod
    def add_data(data):
        if data:
            Data.data.append(data)
        return True

    @staticmethod
    def set_data(list_data):
        if list_data:
            Data.data = list_data
        return True

    @staticmethod
    def clear_data():
        Data.data = []

    @staticmethod
    def get_data(data_id=None):
        data_id = Data.current if data_id is None else data_id
        res = [row for row in Data.data if row.has_key('id') and row['id'] == data_id]
        res = res[0] if len(res) > 0 else {}
        return res

    @staticmethod
    def get_value(key, data_id=None):
        res = None
        data = Data.get_data(data_id)
        if data and data.has_key(key):
            res = data[key]
        return res if res else ''

    @staticmethod
    def set_value(key, value, data_id=None):
        data = Data.get_data(data_id)
        data[key] = value

    #--- structure ---#
    @staticmethod
    def get_defaults():
        res = {}
        for key in Data.data:
            res[key] = Data.get_default_value(key)
        return res

    @staticmethod
    def get_structure():
        res = {}
        for key in Data.struct:
            res[key] = Data.get_type(key)
        return res

    @staticmethod
    def get_type(key):
        row = Data._get_row(key) 
        return row[0]

    @staticmethod
    def get_default_value(key):
        row = Data._get_row(key) 
        return row[1]

    @staticmethod
    def _get_row(key):
        res = (NoneType, None,)
        res = [Data.struct[row_key] for row_key in Data.struct if Data.struct.has_key(row_key) and row_key == key][0]
        return res