import unittest

from prob_distrs import Binomial
        
class TestBinomialClass(unittest.TestCase):
    def setUp(self):
        self.binomial = Binomial(0.4, 20)
        self.binomial_file = Binomial()
        self.binomial_file.read_data_file('tests/data/data_binomial.txt')

    def test_initialization(self):
        self.assertEqual(self.binomial.p, 0.4, 'p value incorrect')
        self.assertEqual(self.binomial.n, 20, 'n value incorrect')

    def test_read_data_file(self):
        self.assertEqual(self.binomial_file.data,\
         [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,1,0,0,1,0,0,1,1,0,0], 'data not read in correctly')
    
    def test_calculate_mean(self):
        mean = self.binomial.calculate_mean()
        self.assertEqual(mean, 8)

        mean = self.binomial_file.calculate_mean()
        self.assertEqual(mean, 9)
    
    def test_calculate_stdev(self):
        stdev = self.binomial.calculate_stdev()
        self.assertEqual(round(stdev,2), 2.19)

        stdev = self.binomial_file.calculate_stdev()
        self.assertEqual(round(stdev,2), 2.40)
        
    def test_pmf(self):
        self.assertEqual(round(self.binomial.pmf(5), 5), 0.07465)
        self.assertEqual(round(self.binomial.pmf(3), 5), 0.01235)
    
        self.assertEqual(round(self.binomial_file.pmf(5), 5), 0.04270)
        self.assertEqual(round(self.binomial_file.pmf(3), 5), 0.00584)

	def test_cdf(self):
		self.assertEqual(round(self.binomial.cdf(5), 5), 0.12560)
		self.assertEqual(round(self.binomial.cdf(3), 5), 0.01596)

    def test_pmf_assertion_error(self):
        with self.assertRaises(AssertionError):
            self.binomial.pmf(5.5)

    def test_add(self):
        binomial_one = Binomial(.4, 20)
        binomial_two = Binomial(.4, 60)
        binomial_sum = binomial_one + binomial_two
        
        self.assertEqual(binomial_sum.p, .4)
        self.assertEqual(binomial_sum.n, 80)

    def test_add_assertion_error(self):
    	binomial_one = Binomial(.5, 20)
        binomial_two = Binomial(.4, 60)
        
        with self.assertRaises(AssertionError):
            binomial_sum = binomial_one + binomial_two
    
if __name__ == '__main__':
    unittest.main()
