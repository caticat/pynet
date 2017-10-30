# -*- coding: utf-8 -*-

"msg manager"

import threading
from data import *

class DataManager(object):
	
	"""data management"""

	def __init__(self, queueRecv, queueSend):
		self.__queueRecv = queueRecv
		self.__queueSend = queueSend
		self.__protocol = dict()

		# thread
		self.__threadRecv = threading.Thread(target=self.__recv)

	def start(self):
		self.__loop = True
		self.__threadRecv.start()

	def stop(self):
		self.__loop = False
		self.__queueRecv.put(AddrData(ptl = PTL_EXIT))

	def join(self):
		self.__threadRecv.join()

	def regist(self, ptl, fun):
		self.__protocol[ptl]=fun

	def __recv(self):
		print("begin recving msg loop")
		while self.__loop:
			protocolData = self.__queueRecv.get()
			if protocolData.ptl in self.__protocol:
				self.__protocol[protocolData.ptl](protocolData.data)
			elif protocolData.ptl == PTL_EXIT:
				pass
			else:
				print("[ERROR]no ptl[%s]" % protocolData.ptl)
		print("finish recving msg loop")

	def send(self, ptl, data):
		self.__queueSend.put(ProtocolData(ptl, data))
