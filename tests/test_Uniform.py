import unittest
import numpy as np
from prob_distrs import Uniform

class TestUniformClass(unittest.TestCase):
    def setUp(self):
      self.uniform = Uniform(1, 6)
      self.uniform_file = Uniform()
      self.uniform_file.read_data_file('tests/data/data_uniform.txt')

    def test_initialization(self): 
      self.assertEqual(self.uniform.a, 1, 'incorrect lower bound')
      self.assertEqual(self.uniform.b, 6, 'incorrect upper bound')

    def test_read_data_file(self):
      self.assertEqual(self.uniform_file.data,\
       [3,2,5,2,3,2,4,2,5,4,3,5,4,1,2,3,3,2,5,6,5,4,6,6,1,3,5,1,4],\
        'data not read in correctly')
         
    def test_mean_calculation(self):
      self.assertAlmostEqual(self.uniform_file.calculate_mean(),\
         sum(self.uniform_file.data) / float(len(self.uniform_file.data)), None,'calculated mean not as expected', .5)

    def test_stdev_calculation(self):
      self.assertAlmostEqual(round(self.uniform_file.calculate_stdev(), 5), 1.52272, None,'standard deviation incorrect', .1)

    def test_pdf(self):
      self.assertEqual(self.uniform.pdf(1.8), 0.2,\
        'pdf function does not give expected result')

    def test_cdf(self):
		  self.assertEqual(self.uniform.cdf(1.8), 0.16,\
		 'cdf function does not give expected result')
    
if __name__ == '__main__':
    unittest.main()
