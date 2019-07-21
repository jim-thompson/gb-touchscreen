import time
import serial
import serial.tools.list_ports
from g_serial import * 
from g_client import *
from g_data import * 
import sys
import threading
 
host = "192.168.1.169" 
port = 63200
baudrate = 250000

class mainhandler():
	def __init__(self, clientconn, serialconn, data_o):
		self.clientconn = clientconn
		self.serialconn = serialconn
		self.data = data_o
		self.senderthread = SenderThread(self.clientconn, self.data)
		self.senderthread.start()
	
	def ex_wrap(self, function):
		try:
			function()
		except error, exc:
			self.clientconn.is_conn = False
			print "Server Disconnected!"
		except IOError:
			self.serialconn.is_open = False
			self.data.changestatus("OF")
			print "Serial Disconnected!\n"

	# def attempt_transfer_header(self):
	# 	if self.clientconn.is_conn and self.serialconn.is_open:
	# 		self.clientconn.senddata(self.serialconn.header)

#	Main loop for the Gigabotnode to read/ send data
	def loop(self):
#		Conditional statement if one or both of the Server and Serial is disconnected.
		if(not (self.clientconn.is_conn and self.serialconn.is_open) ):
#		If either one is disconnected, attempt to connect.
			if not self.clientconn.is_conn: self.clientconn.attemptconnect(host,port)
			if not self.serialconn.is_open: self.serialconn.attemptconnection(self.data)
#		The instant both become connected, send the header to the server.
			if(self.clientconn.is_conn and self.serialconn.is_open):
				self.data.buffer.clear()
				self.data.addtobuffer("HD",self.data.header)
				self.data.addtobuffer("SS",self.data.stats)
				self.senderthread.counter = 5

		# if self.clientconn.is_conn and not self.serialconn.is_open:
		# 	#Set status of the printer to OFF
		# 	self.data.changestatus("OF")

		if not self.clientconn.is_conn and self.serialconn.is_open:
			d = self.serialconn.readdata()

		elif self.clientconn.is_conn and self.serialconn.is_open:
			d = self.serialconn.readdata()
			#self.clientconn.senddata(d)

class SenderThread(threading.Thread):
	_stop = False
	def __init__(self, clientconn, data_obj):
		super(SenderThread,self).__init__()
		self.clientconn = clientconn
		self.data_obj = data_obj
		self.counter = 0
	def stop(self):
		self._stop = True
	def run(self):
		while self._stop == False:
			self.counter += 1
			time.sleep(1)
			if self.counter >= 5:
				msg = self.data_obj.buffer
				print "MSG: ",msg
				try:
					if self.clientconn.is_conn: self.clientconn.senddata(msg)
				except error, exc:
					self.clientconn.is_conn = False
					print "Server Disconnected!"
				#clear the buffer after data is sent
				self.data_obj.buffer.clear()
				self.counter = 0

if __name__ == "__main__":
#	Attempt to Initialize the Client Connection, Data Object, and Serial Connection.
	client_conn= g_client(host,port)
	data_obj = g_data()
	serial_conn = g_serial(data_obj)

#	Create mainhandler object
	mainhand = mainhandler(client_conn, serial_conn, data_obj)

	while True:
		time.sleep(1)
		mainhand.ex_wrap(mainhand.loop)

	print "program ended"

	# conn.close()
