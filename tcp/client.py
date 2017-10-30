# -*- coding: utf-8 -*-

"a network framework by tcp(client)"

#还是用这个吧,多线程模型肯定不行
#pip install Twisted

import socket
import threading
from data import *
from const import *


class TCPC(object):
	
	"""TCP Client"""

	def __init__(self, addr, queueRecv, queueSend):
		# param
		self.__addr = addr
		self.__queueRecv = queueRecv
		self.__queueSend = queueSend

		# net
		self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		# thread
		self.__threadRecv = threading.Thread(target=self.__recv)
		self.__threadSend = threading.Thread(target=self.__send)

	def start(self):
		self.__loop = True
		self.__socket.connect(self.__addr)
		self.__threadRecv.start()
		self.__threadSend.start()

	def stop(self):
		self.__loop = False
		self.__socket.sendto(AddrData(ptl = PTL_EXIT).toBytes(), tuple(self.__addrBind))
		self.__queueSend.put(AddrData(ptl = PTL_EXIT))

	def join(self):
		self.__threadRecv.join()
		self.__threadSend.join()

	def __recv(self): 
		print("begin revcing msg")
		head = b""
		body = b""
		bodyLen = 0
		readLen = 0
		while self.__loop:
			# 拆包
			if len(head) < MSG_DATA_LEN:
				head += self.__socket.recv(MSG_DATA_LEN)
				if len(head) == MSG_DATA_LEN:
					bodyLen = int_from_bytes(head)
					if bodyLen >= MSG_MAX_LEN:
						print("[ERROR]invalid data length")
						head = b""
						body = b""
						bodyLen = 0
						readLen = 0
			if len(head) == MSG_DATA_LEN:
				body += self.__socket.recv(bodyLen - readLen)
				readLen = len(body)
				if readLen == bodyLen:
					protocolData = ProtocolData()
					protocolData.toData(body)
					if protocolData.ptl == PTL_EXIT:
						break
					self.__queueRecv.put(protocolData)
					head = b""
					body = b""
					bodyLen = 0
					readLen = 0
		print("finish revcing msg")

	def __send(self):
		print("begin sending msg")
		while self.__loop:
			protocolData = self.__queueSend.get()
			if protocolData.ptl == PTL_EXIT:
				break
			self.__socket.send(protocolData.toBytesWithLen())
			# print("send:", protocolData)
		print("finish sending msg")
