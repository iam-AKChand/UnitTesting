import unittest
class TestCase2(unittest.TestCase):
	def setUp(self):
		print('TestCase2:setUp executed..')
	def test3(self):
		print('TestCase2:test3 executed..')
	def tearDown(self):
		print('TestCase2:tearDown executed..')