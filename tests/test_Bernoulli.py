import unittest

from prob_distrs import Bernoulli
from prob_distrs import Binomial

class TestBernoulliClass(unittest.TestCase):
    def setUp(self):
        self.bernoulli = Bernoulli(0.4)

    def test_initialization(self):
        self.assertEqual(self.bernoulli.p, 0.4, 'p value incorrect')
        self.assertEqual(self.bernoulli.n, 1, 'n value incorrect')
    
    def test_calculate_mean(self):
        mean = self.bernoulli.calculate_mean()
        self.assertEqual(mean, .4)
    
    def test_calculate_stdev(self):
        stdev = self.bernoulli.calculate_stdev()
        self.assertEqual(round(stdev,2), .49)
        
    def test_pmf(self):
        self.assertEqual(round(self.bernoulli.pmf(0), 5), .6)
        self.assertEqual(round(self.bernoulli.pmf(1), 5), .4)

    def test_pmf_assertion_error(self):
        with self.assertRaises(AssertionError):
            self.bernoulli.pmf(2)

    def test_add(self):
        bernoulli_one = Bernoulli(.4)
        bernoulli_two = Bernoulli(.4)
        bernoulli_sum = bernoulli_one + bernoulli_two
        
        self.assertEqual(bernoulli_sum.p, .4)
        self.assertEqual(bernoulli_sum.n, 2)

    def test_add_with_binomial(self):
        bernoulli = Bernoulli(.4)
        binomial = Binomial(.4, 5)
        bernoulli_sum = bernoulli + binomial
        
        self.assertEqual(bernoulli_sum.p, .4)
        self.assertEqual(bernoulli_sum.n, 6)

    def test_add_assertion_error(self):
    	bernoulli_one = Bernoulli(.5)
        bernoulli_two = Bernoulli(.4)
        
        with self.assertRaises(AssertionError):
            bernoulli_sum = bernoulli_one + bernoulli_two
    
if __name__ == '__main__':
    unittest.main()
