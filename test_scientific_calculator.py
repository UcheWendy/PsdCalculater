import unittest
from scientific_calculator import sin, cos, tan, sqrt, log, exp
class TestScientificCalculator(unittest.TestCase):
    #tests for sin function
    def testSinPositive(self):
        result = sin(90)
        self.assertEqual(result, 1.0)
        
    def testSinNegative(self):
        result = sin(-90)
        self.assertEqual(result, -1.0)
        
    def testSinZero(self):
        result = sin(0)
        self.assertEqual(result, 0.0)
        
    def testSinNonNumeric(self):
        with self.assertRaises(ValueError):
            sin("ninety")
            
     #tests for cos function     
    def testCosPositive(self):
        result = cos(45)
        self.assertAlmostEqual(result, 0.7071, places=4)
        
    def testCosNegative(self):
        result = cos(-180)
        self.assertEqual(result, -1.0)
        
    def testCosZero(self):
        result = cos(0)
        self.assertEqual(result, 1.0)
    def testCosNonNumeric(self):
        with self.assertRaises(ValueError):
            cos([45])
 
     
     #tests for tan function
     
    def testTanPositive(self):
        result = tan(45)
        self.assertAlmostEqual(result, 1.0)
        
    def testTanNegative(self):
        result = tan(-45)
        self.assertAlmostEqual(result, -1.0)
        
    def testTanZero(self):
        result = tan(0)
        self.assertEqual(result, 0.0)
    def testTanNonNumeric(self):
        with self.assertRaises(ValueError):
            tan({"angle": 45})
        
    #tests for square root
        
    def testSqrtPositive(self):
        result = sqrt(25)
        self.assertEqual(result,5)
        
    def testSqrtNegative(self):
        with self.assertRaises(ValueError):
            sqrt(-15)
        
    def testSqrtZero(self):
        result = sqrt(0)
        self.assertEqual(result, 0)
        
    def testSqrtNonNumeric(self):
        with self.assertRaises(ValueError):
            sqrt("ten")
        
    #tests for log function
    def testLogPositive(self):
        result = log(16,2)
        self.assertEqual(result, 4)
        
    def testLogNegative(self):
        with self.assertRaises(ValueError):
            log(-14,2)
        
    def testLogZero(self):
       with self.assertRaises(ValueError):
            log(0, 2)
            
    def testLogNonNumeric(self):
        with self.assertRaises(ValueError):
            log(100,"10")
    def testLogInvalidInput(self):
        with self.assertRaises(ValueError):
            log(-1)
            
            
    #tests for exponential function
        
    def testExpPositive(self):
        result = exp(3)
        self.assertAlmostEqual(result, 20.0855, places=4)
        
    def testExpNegative(self):
        result = exp(-3)
        self.assertAlmostEqual(result, 0.04979, places=5)
        
    def testExpZero(self):
        result = exp(0)
        self.assertEqual(result, 1)
    
    def testExpInvalidInput(self):
        with self.assertRaises(ValueError):
            exp("3")
                
if __name__ == '__main__':
    unittest.main()
        