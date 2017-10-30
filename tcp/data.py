# -*- coding: utf-8 -*-

"tcp data"

from const import *

def int_to_bytes(x):
    return x.to_bytes((x.bit_length() + 7) // 8, 'big', signed=True)

def int_from_bytes(xbytes):
    return int.from_bytes(xbytes, 'big', signed=True)

# 增加长度参数
def int_to_bytes_len(x, lenth):
    return x.to_bytes(lenth, 'big', signed=True)

class ProtocolData(object):
	def __init__(self, ptl = 0, data = b""):
		self.ptl = ptl
		self.data = data

	# 数据转化协议字符串
	def toBytesWithLen(self):
		bPtl = int_to_bytes_len(self.ptl, MSG_PROTOCOL_LEN)
		bData = bPtl + self.data
		bLen = int_to_bytes_len(len(bData), MSG_DATA_LEN)
		return bLen + bData

	# bytes转化为结构体数据
	def toData(self, bData):
		if (len(bData) < MSG_PROTOCOL_LEN):
			return
		bPtl = bData[:MSG_PROTOCOL_LEN]
		self.ptl = int_from_bytes(bPtl)
		self.data = bData[MSG_PROTOCOL_LEN:]
