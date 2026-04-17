import unittest

from getbest import findTop

class TestGetCols(unittest.TestCase):
	
	def setUp(self): #sets up testing
		self.line ="ELEN3020,2717070,80,Good"
		
	def tearDown(self): #cleans after the test
		del self.line
		del index
		del mark
		
	def test_index_and_Mark(self): #Tests if the right index and mark are returned
		index,mark = findTop(self.line,1,2)
		self.assertEqual(index,0)
		self.assertEqual(mark,80)
	
if __name__ == '__main__':
	unittest.main()
