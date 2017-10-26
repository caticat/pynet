# -*- coding: utf-8 -*-

"a network framework by udp(server)"

import time
import socket
import threading
from net.udp.data import *

class UDPS(object):
	
	"""UDP Server"""
	
	def __init__(self, port, queueRecv, queueSend, recvBuffLen=MSG_MAX_LEN):
		# param
		self.__port = port
		self.__queueRecv = queueRecv
		self.__queueSend = queueSend
		self.__recvBuffLen = recvBuffLen

		# net
		self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

		# thread
		self.__threadRecv = threading.Thread(target=self.__recv)
		self.__threadSend = threading.Thread(target=self.__send)

	def start(self):
		self.__loop = True
		self.__socket.bind(("localhost", self.__port))
		self.__threadRecv.start()
		self.__threadSend.start()

	def stop(self):
		self.__loop = False
		self.__socket.sendto(AddrData(ptl = PTL_EXIT).toBytes(), ("localhost", self.__port))
		self.__queueSend.put(AddrData(ptl = PTL_EXIT))

	def join(self):
		self.__threadRecv.join()
		self.__threadSend.join()

	def __recv(self):
		print("begin revcing msg")
		while self.__loop:
			data, addr = self.__socket.recvfrom(self.__recvBuffLen) # UDP没有粘包问题
			addrData = AddrData(addr)
			addrData.toData(data)
			if addrData.ptl == PTL_EXIT:
				break
			# print("[recv][%s:%s][%s]%s" % (*addr, addrData.ptl, addrData.data))
			self.__queueRecv.put(addrData)
		print("finish revcing msg")

	def __send(self):
		print("begin sending msg")
		while self.__loop:
			addrData = self.__queueSend.get()
			if addrData.ptl == PTL_EXIT:
				break
			# print("[send][%s:%s][%s]%s" % (*addrData.addr, addrData.ptl, addrData.data))
			self.__socket.sendto(addrData.toBytes(), addrData.addr)
		time.sleep(0.1)
		print("finish sending msg")

