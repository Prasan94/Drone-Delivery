"""Module for Drone delivery project

This module demonstrates a simple object oriented drone delivery project,
Currently it is assumed that there is only one drone, command centre and delivery point.
Developer documentation is available using sphinx

Usage :
------------

	This module can be executed by using below command:

		$ pyhton DroneDelivery.py

Attributes :
------------

    There is no module level variable
	
Tasks :
-------

	*Get the delivery order from command centre
	*Deliver the item to the delivery address
	*Unload the item and get back to the warehouse.
	*Communicate the status in each stage with the command centre

"""
import math
from operator import attrgetter
import random
import time

class WareHosue(object):
	"""This class contains information about warehouse

	You can add all warehouse relates parameter and operations in this class

	Parameters ( received by __init__ ) :

	There is no variable passed.But it has following instance variables
	*warehouse: (tuple) warehouse coordinates
	*deliveryLimit: (tuple) maximun coordinates that a delivery address can have 

	Attributes ( class variables ) :

	There is no class variable

	"""
	def __init__(self):
		self.warehouse = (0, 0)
		self.deliveryLimit = (50, 50)

class NoOptionException(Exception):
	"""
	"""
	pass

class Drone(object):
	"""This class contains information and operations related to drone.

	You can add parameters and operations related to drone activity. 

	Parameters ( received by __init__ ) :

	There is no variable passed.But it has following instance parameters
	*wharehouseObj: (object) object of warehouse class
	*speed: (int) average speed of the drone
	*engaged: (boolean) whether the drone is engaged with ongoing delivery or not

	Attributes ( class variables ) :

	There is no class variable

	"""
	def __init__(self):
		self.warehouseObj = WareHosue()
		self.speed = 1 #km/min
		self.__engaged = False

	def __can_it_be_delivered_to_destination(self):
		"""Decides if item can be delivered mentioned destination by comparing destination coordinates with permissible coordinates
		
		:return: True
		:rtype: Boolean

		:raises Exception: raises exception with proper message if destination coordinate is greater than permissible coordinates

		"""
		if sum(self.__destination) > sum(self.warehouseObj.deliveryLimit):
			raise Exception("Item can't be delivered to this address\n")
		return True

	def __take_off(self):
		"""Responsible for the drone to fly if it is not enagaged.

		:raises Exception: raises exception with proper message if drone is already engaged
		"""
		if self.__engaged:
			raise Exception("Drone is currently engaged")
		self.__engaged = True
		print("Drone is taking off\n")
		return True

	def __calculate_distance(self):
		"""Calculates distance between destination and warehouse

		:return: distance
		:rtype: float

		"""
		distance = math.sqrt((self.__destination[0] - self.warehouseObj.warehouse[0]) ** 2 + (self.__destination[1] - self.warehouseObj.warehouse[1]) ** 2)
		return distance

	def __calculate_time(self, distance):
		"""Calculates time required to cover the given distance

		:param1: (float) distance to be covered

		:return: time in minutes
		:rtype: int

		"""
		time = int(math.ceil(distance/self.speed))
		print("Time required to reach the destination: %s minutes\n" % time)
		return time

	@staticmethod
	def __destination_reached(timeToReachDestination):
		"""Indicates the drone has reached the destination after waiting for the drone to reach the destination.

		:param1: (int) time required to reach destination

		"""
		time.sleep(timeToReachDestination)
		print("Drone has reached the destination\n")

	@staticmethod
	def __item_unloaded():
		"""Waits for the drone to unload item and then indicates thet the item has been unloaded.
		"""
		unloadingTime = random.randint(1,5)
		time.sleep(unloadingTime)
		print("Item has been unloaded\n")

	def __returned_to_warehouse(self, timeToReachwarehouse):
		"""After waiting for the drone to return to warehouse it indicates that drone has returned and is free to take the next delivery
		"""
		time.sleep(timeToReachwarehouse)
		print("Drone has returned to warehouse and ready for the next delivery\n")
		self.__engaged = False

	def pickup(self, destination):
		"""This method trgeers all the operations of the drone in a proper flow

		:param1: (tuple) destination

		:raises Exception: raises exception with proper message if anything goes wrong in any of the stages

		"""
		self.__destination = destination
		try:
			self.__can_it_be_delivered_to_destination()
			self.__take_off()
			distance = self.__calculate_distance()
			timeToReach = self.__calculate_time(distance)
			self.__destination_reached(timeToReach)
			self.__item_unloaded()
			self.__returned_to_warehouse(timeToReach)
		except Exception as err:
			print(err)

def command_centre():
	"""This is responsible for the Drone class object creation.
	:raises Exception: raises with proper message if entered destination is not a tuple with two positive values
	
	"""
	try:
		destination = input("Enter the destination coordinates (in a tuple)\n")
	except SyntaxError: 
		raise Exception("Please Enter Destination\n")
	if not (isinstance(destination, tuple) and len(destination) == 2 and destination[0] * destination[1] > 0):
		raise Exception("Please enter the destination in a tuple with two positive values\n")
	
	drone = Drone()
	drone.pickup(destination)

proceed = True
while proceed:
	try:
		command_centre()
		proceed = raw_input("You want to assign one more delivery? press Y for YES any other key for NO\n")
		proceed = False if not proceed.upper() == "Y" else proceed
	except NoOptionException as err:
		print err
		proceed = raw_input("You want to assign one more delivery? press Y for YES any other key for NO\n")
	except Exception as err:
		print(err)



	
