
import unittest
import main


class TestCalculator(unittest.TestCase):#unittest module provides a set of tools for constructing and running scripts, we will test features of online calculator in this case
	
	def setUp(self):#setUp , when unittest module is used and it enables application to test
		main.app.testing = True
		self.app = main.app.test_client()

	def test_add1(self):
		#case 1, A is n integer B is an integer
		solution = self.app.get('/add?A=20&B=2')
		self.assertEqual(b'22.0', solution.data)

	def test_add2(self):

		#case 2, A is rational number and B is rational number p/q form
		solution = self.app.get('/add?A=3/2&B=1/2')
		self.assertEqual(b'2.0', solution.data)

	def test_add3(self):

		#case 3, A is a float and B is a float
		solution = self.app.get('/add?A=122.22&B=1.002')
		self.assertEqual(b'123.222', solution.data)

	def test_add4(self):

		#case 4, when A is float and B is integer
		solution = self.app.get('/add?A=22.222&B=98')
		self.assertEqual(b'120.222', solution.data)

	def test_add5(self):

		#case 5, when A is integer and B is float
		solution = self.app.get('/add?A=100&B=98.9')
		self.assertEqual(b'198.9', solution.data)

	def test_add6(self):

		#case 6, when A is fraction p/q and B is an integer
		solution = self.app.get('/add?A=1/2&B=99')
		self.assertEqual(b'99.5', solution.data)

	def test_add7(self):

		#case 7, when A is an integer and B is a fraction p/q
		solution = self.app.get('/add?A=30&B=2/10')
		self.assertEqual(b'30.2', solution.data)

	def test_add8(self):

		#case 8, when A input is an alphabet(non integer) and B is integer
		solution = self.app.get('/add?A=prakash&B=22')
		self.assertEqual(b'22.0', solution.data)#non integer type considered as not valid , in this case which is zero

	def test_add9(self):

		#case 9, when A input is an integer and B input is an alphabet
		solution = self.app.get('/add?A=22&B=satya')
		self.assertEqual(b'22.0', solution.data)
		#when one input is alphabet and other input be any number, whether rational , integer, fraction ultimately the result will be the input which was an integer

	def test_add10(self):

		#case 10, when A input is of the form p/q where q=0 and B input be any number
		solution = self.app.get('add?A=1/0&B=2')
		self.assertEqual(b"None", solution.data)
		#according to the script if q=0 in p/q form then it should display an error but it is resolved using zerodivision module 

	def test_add11(self):

		#case 11, when A input is any number and B=p/q form where q=0
		solution = self.app.get('add?A=12&B=2/0')
		self.assertEqual(b"None", solution.data)


if __name__ == '__main__':
	unittest.main()