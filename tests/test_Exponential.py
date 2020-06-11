import unittest

from prob_distrs import Exponential

class TestExponentialClass(unittest.TestCase):
    def setUp(self):
        self.exponential = Exponential(5)
        self.exponential_file = Exponential()
        self.exponential_file.read_data_file('tests/data/data_exponential.txt')

    def test_initialization(self): 
        self.assertEqual(self.exponential.rate, 5, 'incorrect rate parameter')

    def test_read_data_file(self):
        self.assertEqual(self.exponential_file.data,\
         [0.17749903, 0.02573502, 0.39472495, 0.27610555, 0.05389677, 0.14517014, 0.09735444, 0.1733805, 0.47561218, 0.04255559, 0.13629608, 0.18274326, \
         0.20526775, 0.28807018, 0.04894014, 0.53181988, 0.25468589, 0.04165556, 0.2953461, 0.14876471],\
          'data not read in correctly')
         
    def test_mean_calculation(self):
        self.assertEqual(round(self.exponential_file.calculate_mean(), 5),\
         round(sum(self.exponential_file.data) / float(len(self.exponential_file.data)),5), 'calculated mean not as expected')

    def test_stdev_calculation(self):
        self.assertAlmostEqual(self.exponential_file.calculate_stdev(), .25, None,'standard deviation incorrect', 5)

    def test_pdf(self):
        self.assertEqual(round(self.exponential.pdf(.45), 5), 0.5270,\
         'pdf function does not give expected result')

	def test_cdf(self):
		self.assertEqual(round(self.exponential.cdf(.45), 5), 0.8946,\
		 'cdf function does not give expected result')
    
if __name__ == '__main__':
    unittest.main()
