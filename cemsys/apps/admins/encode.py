from decimal import Decimal
from datetime import datetime
from functools import singledispatch
import json


@singledispatch
def convert(obj):
    raise TypeError("不能转换数据类型")


@convert.register(datetime)
def _(obj):
    return obj.strftime("%Y-%m-%d %H:%M:%S")


@convert.register(Decimal)
def _(obj):
    return float(obj)


class DecimalEncoder(json.JSONEncoder):
    """处理Object of type 'Decimal' is not JSON serializable"""
    def default(self, obj):
        try:
            return convert(obj)
        except TypeError:
            return super(DecimalEncoder, self).default(obj)
