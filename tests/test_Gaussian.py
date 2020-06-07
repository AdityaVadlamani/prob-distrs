import unittest

from prob_distrs import Gaussian

class TestGaussianClass(unittest.TestCase):
    def setUp(self):
        self.gaussian = Gaussian(25, 2)
        self.gaussian_file = Gaussian()
        self.gaussian_file.read_data_file('tests/data/data_gaussian.txt')

    def test_initialization(self): 
        self.assertEqual(self.gaussian.mean, 25, 'incorrect mean')
        self.assertEqual(self.gaussian.stdev, 2, 'incorrect standard deviation')

    def test_read_data_file(self):
        self.assertEqual(self.gaussian_file.data,\
         [39,85,44,87,3,56,80,7,74,18,80,55,42,47,73,79,3,54,41,73,83,53,73,93,69],\
          'data not read in correctly')
         
    def test_mean_calculation(self):
        self.assertEqual(self.gaussian.calculate_mean(),\
         sum(self.gaussian.data) / float(len(self.gaussian.data)), 'calculated mean not as expected')

    def test_stdev_calculation(self):
        self.assertEqual(round(self.gaussian_file.calculate_stdev(), 2), 26.89, 'sample standard deviation incorrect')
        self.assertEqual(round(self.gaussian_file.calculate_stdev(0), 2), 26.34, 'population standard deviation incorrect')

    def test_pdf(self):
        self.assertEqual(round(self.gaussian.pdf(25), 5), 0.19947,\
         'pdf function does not give expected result')     

    def test_cdf(self):
        self.assertEqual(round(self.gaussian.cdf(26), 4), 0.6915,\
         'cdf function does not give expected result')   

    def test_add(self):
        gaussian_one = Gaussian(25, 3)
        gaussian_two = Gaussian(30, 4)
        gaussian_sum = gaussian_one + gaussian_two
        
        self.assertEqual(gaussian_sum.mean, 55)
        self.assertEqual(gaussian_sum.stdev, 5)
    
if __name__ == '__main__':
    unittest.main()
