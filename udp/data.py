# -*- coding: utf-8 -*-

"udp data"

from net.udp.const import *

def int_to_bytes(x):
    return x.to_bytes((x.bit_length() + 7) // 8, 'big', signed=True)

def int_from_bytes(xbytes):
    return int.from_bytes(xbytes, 'big', signed=True)

# 增加长度参数
def int_to_bytes_len(x, lenth):
    return x.to_bytes((lenth + 7) // 8, 'big', signed=True)

class AddrData(object):
	def __init__(self, addr = (), ptl = 0, data = ""):
		self.addr = addr
		self.ptl = ptl
		self.data = data

	# 数据转化协议字符串
	def toBytes(self):
		bPtl = int_to_bytes_len(self.ptl, MSG_PROTOCOL_LEN)
		return bPtl + self.data.encode("utf-8")

	# bytes转化为结构体数据
	def toData(self, bData):
		lPtl = MSG_PROTOCOL_LEN // 8
		if (len(bData) < lPtl):
			return
		bPtl = bData[:lPtl]
		self.ptl = int_from_bytes(bPtl)
		self.data = bData[lPtl:].decode("utf-8")
