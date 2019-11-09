import unittest
import DroneDelivery
import math

class Drone(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(Drone, self).__init__(*args, **kwargs)
		self.droneObject = DroneDelivery.Drone()
		self.droneObject._Drone__destination = (5, 5)

	def test___can_it_be_delivered_to_destination_Success(self):
		self.assertTrue(self.droneObject._Drone__can_it_be_delivered_to_destination())
		

	def test___can_it_be_delivered_to_destination_Failure(self):
		self.droneObject = DroneDelivery.Drone()
		self.droneObject._Drone__destination = (500, 50)
		with self.assertRaises(Exception):
			self.droneObject._Drone__can_it_be_delivered_to_destination()

	def test___take_off_Success(self):
		self.assertTrue(self.droneObject._Drone__take_off())
	
	def test___take_off_Failure(self):
		self.droneObject = DroneDelivery.Drone()
		self.droneObject._Drone__engaged = True
		with self.assertRaises(Exception):	
			self.droneObject._Drone__take_off()

	def test___calculate_distance(self):
		self.assertEqual(math.floor(self.droneObject._Drone__calculate_distance()), 7 )

	def test___calculate_time(self):
		self.assertEqual(self.droneObject._Drone__calculate_time((7.07106781187)), 8)

if __name__ == "__main__":
	unittest.main(verbosity=2)

		