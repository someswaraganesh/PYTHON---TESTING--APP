import unittest
from multiply import multiplication
class multiplytestcase(unittest.Testcase):
  def test_1(self):
    result=multiplication(3,4)
    self.assertEqual(result,12)
    
     
