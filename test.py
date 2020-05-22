
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

    def test_sub1(self):
		#case 1, A is n integer B is an integer
		solution = self.app.get('/sub?A=6&B=2')
		self.assertEqual(b'4.0', solution.data)

	def test_sub2(self):

		#case 2, A is rational number and B is rational number p/q form
		solution = self.app.get('/sub?A=3/2&B=1/2')
		self.assertEqual(b'1.0', solution.data)

	def test_sub3(self):

		#case 3, A is a float and B is a float
		solution = self.app.get('/sub?A=10.2&B=1.002')
		self.assertEqual(b'9.198', solution.data)

	def test_sub4(self):

		#case 4, when A is float and B is integer
		solution = self.app.get('/sub?A=22.222&B=2')
		self.assertEqual(b'20.222', solution.data)

	def test_sub5(self):

		#case 5, when A is integer and B is float
		solution = self.app.get('/sub?A=12&B=1.111')
		self.assertEqual(b'10.889', solution.data)

	def test_sub6(self):

		#case 6, when A is fraction p/q and B is an integer
		solution = self.app.get('/sub?A=1/2&B=12')
		self.assertEqual(b'-11.5', solution.data)

	def test_sub7(self):

		#case 7, when A is an integer and B is a fraction p/q
		solution = self.app.get('/sub?A=3&B=2/10')
		self.assertEqual(b'2.8', solution.data)

	def test_sub8(self):

		#case 8, when A input is an alphabet(non integer) and B is integer
		solution = self.app.get('/sub?A=satya&B=10')
		self.assertEqual(b'-10.0', solution.data)#non integer type considered as not valid , in this case which is zero

	def test_sub9(self):

		#case 9, when A input is an integer and B input is an alphabet
		solution = self.app.get('/sub?A=22&B=prakash')
		self.assertEqual(b'22.0', solution.data)
		#when one input is alphabet and other input be any number, whether rational , integer, fraction ultimately the result will be the input which was an integer

	def test_sub10(self):

		#case 10, when A input is of the form p/q where q=0 and B input be any number
		solution = self.app.get('sub?A=1/0&B=2')
		self.assertEqual(b"None", solution.data)
		#according to the script if q=0 in p/q form then it should display an error

	def test_sub11(self):

		#case 11, when A input is any number and B=p/q form where q=0
		solution = self.app.get('sub?A=12&B=2/0')
		self.assertEqual(b"None", solution.data)

	def test_mul1(self):
		#case 1, A is n integer B is an integer
		solution = self.app.get('/mul?A=20&B=2')
		self.assertEqual(b'40.0', solution.data)

	def test_mul2(self):

		#case 2, A is rational number and B is rational number p/q form
		solution = self.app.get('/mul?A=3/2&B=22/4')
		self.assertEqual(b'8.25', solution.data)

	def test_mul3(self):

		#case 3, A is a float and B is a float
		solution = self.app.get('/mul?A=0.00089&B=100000.00')
		self.assertEqual(b'89.0', solution.data)

	def test_mul4(self):

		#case 4, when A is float and B is integer
		solution = self.app.get('/mul?A=22.222&B=98')
		self.assertEqual(b'2177.756', solution.data)

	def test_mul5(self):

		#case 5, when A is integer and B is float
		solution = self.app.get('/mul?A=1000&B=9.99')
		self.assertEqual(b'9990.0', solution.data)

	def test_mul6(self):

		#case 6, when A is fraction p/q and B is an integer
		solution = self.app.get('/mul?A=11&B=99')
		self.assertEqual(b'1089.0', solution.data)

	def test_mul7(self):

		#case 7, when A is an integer and B is a fraction p/q
		solution = self.app.get('/mul?A=23&B=9/13')
		self.assertEqual(b'15.9230769231', solution.data)

	def test_mul8(self):

		#case 8, when A input is an alphabet(non integer) and B is integer
		solution = self.app.get('/mul?A=satya&B=22')
		self.assertEqual(b'0.0', solution.data)#non integer type considered as not valid , in this case which is zero

	def test_mul9(self):

		#case 9, when A input is an integer and B input is an alphabet
		solution = self.app.get('/mul?A=22&B=reddy')
		self.assertEqual(b'0.0', solution.data)
		#when one input is alphabet and other input be any number, whether rational , integer, fraction ultimately the result will be the input which was an integer

	def test_mul10(self):

		#case 10, when A input is of the form p/q where q=0 and B input be any number
		solution = self.app.get('mul?A=1/0&B=2')
		self.assertEqual(b"None", solution.data)
		#according to the script if q=0 in p/q form then it should display an error but it is resolved using zerodivision module

	def test_mul11(self):

		#case 11, when A input is any number and B=p/q form where q=0
		solution = self.app.get('mul?A=12&B=2/0')
		self.assertEqual(b"None", solution.data)

	def test_div1(self):
		#case 1, A is n integer B is an integer
		solution = self.app.get('/div?A=20&B=2')
		self.assertEqual(b'10.0', solution.data)

	def test_div2(self):

		#case 2, A is rational number and B is rational number p/q form
		solution = self.app.get('/div?A=3/2&B=22/4')
		self.assertEqual(b'0.272727272727', solution.data)

	def test_div3(self):

		#case 3, A is a float and B is a float
		solution = self.app.get('/div?A=0.089&B=102.22')
		self.assertEqual(b'0.000870671101546', solution.data)

	def test_div4(self):

		#case 4, when A is float and B is integer
		solution = self.app.get('/div?A=22.222&B=98')
		self.assertEqual(b'0.226755102041', solution.data)

	def test_div5(self):

		#case 5, when A is integer and B is float
		solution = self.app.get('/div?A=10&B=2.2')
		self.assertEqual(b'4.54545454545', solution.data)

	def test_div6(self):

		#case 6, when A is fraction p/q and B is an integer
		solution = self.app.get('/div?A=12&B=100')
		self.assertEqual(b'0.12', solution.data)

	def test_div7(self):

		#case 7, when A is an integer and B is a fraction p/q
		solution = self.app.get('/div?A=12&B=2/3')
		self.assertEqual(b'18.0', solution.data)

	def test_div8(self):

		#case 8, when A input is an alphabet(non integer) and B is integer
		solution = self.app.get('/div?A=reddy&B=12')
		self.assertEqual(b'0.0', solution.data)#non integer type considered as not valid , in this case which is zero

	def test_div9(self):

		#case 9, when A input is an integer and B input is an alphabet
		solution = self.app.get('/div?A=22&B=prakash')
		self.assertEqual(b'None', solution.data)
		#when one input is alphabet and other input be any number, whether rational , integer, fraction ultimately the result will be the input which was an integer

	def test_div10(self):

		#case 10, when A input is of the form p/q where q=0 and B input be any number
		solution = self.app.get('div?A=1/0&B=2')
		self.assertEqual(b'None', solution.data)
		#according to the script if q=0 in p/q form then it should display an error

	def test_div11(self):

		#case 11, when A input is any number and B=p/q form where q=0
		solution = self.app.get('div?A=12&B=2/0')
		self.assertEqual(b'None', solution.data)


if __name__ == '__main__':
	unittest.main()