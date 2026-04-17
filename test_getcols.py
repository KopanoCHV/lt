import unittest

from getbest import getCols

class TestGetCols(unittest.TestCase):
	
	def setUp(self): #sets up testing
		self.line ="Course,Student Number,Mark,Comment"

	def tearDown(self): #cleans after the test
		del self.line
		del num
		del mark
	
	def test_get_cols_function_for_student_Number(self): #checks if the function gets the right index for student number
		num,mark = getCols(self.line)
		self.assertEqual(num,1)
		

	def test_get_cols_function_for_Mark(self): #checks if the function gets the right index for Mark
		num,mark = getCols(self.line)
		self.assertEqual(mark,2)

if __name__ == '__main__':
	unittest.main()
