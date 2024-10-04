import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setup(self):
       """Setup the SimpleCalculator instance before each test."""
       self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2,3), 5)             #Standard case
        self.assertEqual(self.calc.add(-1, 1), 0)           #Adding -ve and +ve
        self.assertEqual(self.calc.add(0, 0), 0)            #Adding zero
        self.assertEqual(self.calc.add(-6, -6), 12)         #Adding two -ves
        self.assertEqual(self.calc.add(2.3, 2.3), 4.6)      #Adding floats

    def test_subtraction(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(10,5), 5)              #Standard case
        self.assertEqual(self.calc.subtract(-1, -1), 0)            #Subtacting two -ves
        self.assertEqual(self.calc.subtract(0, 0), 0)              #Subtracting zeros
        self.assertEqual(self.calc.subtract(-6, 6), -12)           #Subtracting -ve and +ve
        self.assertEqual(self.calc.subtract(2.3, 2.3), 0)          #Subtracting floats


    def test_multiply(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(2,3), 6)               #Standard case
        self.assertEqual(self.calc.multiply(-1, 1), -1)            #Multiplying -ve and +ve
        self.assertEqual(self.calc.multiply(0, 0), 0)              #Multiplying zero
        self.assertEqual(self.calc.multiply(-6, -6), 36)           #Multiplying two -ves
        self.assertEqual(self.calc.multiply(2.3, 2.3), 5.29)       #Multiplying floats

    def test_division(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(10,2), 5)            #Standard case
        self.assertEqual(self.calc.divide(-5, 1), -5)          #Dividing -ve and +ve
        self.assertEqual(self.calc.divide(-36, -6), 6)         #Dividing two -ves
        self.assertEqual(self.calc.divide(1.0, 2.0), 0.5)      #Dividing floats

        self.assertEqual(self.calc.divide(36, 0), "Expected None when dividing by zero")        
        self.assertEqual(self.calc.divide(0, 0), "Expected None when dividing zero by zero")     

    def test_zero_division(self):
        """Test edge case with zero as denominator or numerator."""
        self.assertEqual(self.calc.divide(0, 10), 0)         
        self.assertEqual(self.calc.divide(10, 0), 0)     

if __name__ == "__main__":
    unittest.main()

                         
