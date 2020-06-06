from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
	name='prob_distrs',
    version='0.2.1',
    description='Some popular probability distributions',
    long_description = readme,
    packages=find_packages(exclude = ('tests', 'docs', 'dists')),
    author="Aditya Vadlamani",
    author_email = 'aditya.t.vadlamani@gmail.com',
    url = 'https://github.com/AdityaVadlamani/prob-distrs',
    license = license,
    zip_safe=False
)
