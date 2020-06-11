import unittest

from prob_distrs import Poisson

class TestPoissonClass(unittest.TestCase):
    def setUp(self):
        self.poisson = Poisson(5)
        self.poisson_file = Poisson()
        self.poisson_file.read_data_file('tests/data/data_poisson.txt')

    def test_initialization(self): 
        self.assertEqual(self.poisson.lam, 5, 'incorrect lamda')

    def test_read_data_file(self):
        self.assertEqual(self.poisson_file.data,\
         [39,85,44,87,3,56,80,7,74,18,80,55,42,47,73,79,3,54,41,73,83,53,73,93,69],\
          'data not read in correctly')
         
    def test_mean_calculation(self):
        self.assertEqual(self.poisson_file.calculate_mean(),\
         sum(self.poisson_file.data) / float(len(self.poisson_file.data)), 'calculated mean not as expected')

    def test_stdev_calculation(self):
        self.assertEqual(round(self.poisson_file.calculate_stdev(), 2), 7.51, 'standard deviation incorrect')

    def test_pmf(self):
        self.assertEqual(round(self.poisson.pmf(5), 5), .17547,\
         'pmf function does not give expected result')

	def test_cdf(self):
		self.assertEqual(round(self.poisson.cdf(5), 5), .61596,\
		 'cdf function does not give expected result')

    def test_pmf_assertion_error(self):
        with self.assertRaises(AssertionError):
            self.poisson.pmf(3.1415927)    

    def test_add(self):
        poisson_one = Poisson(5)
        poisson_two = Poisson(3)
        poisson_sum = poisson_one + poisson_two
        
        self.assertEqual(poisson_sum.lam, 8)
    
if __name__ == '__main__':
    unittest.main()
