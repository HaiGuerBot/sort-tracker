from setuptools import setup, find_packages
import os


build_number = os.getenv('BUILD_NUMBER', 0)
VERSION = '0.0.{}'.format(build_number)

setup(
    name='sort',
    version=VERSION,
    description='Sort tracker',
    url='https://github.deere.com/JDES-Machine-Learning/sort-tracker',
    author='Abram Haich',
    author_email='haichabramp@johndeere.com',
    license='GPL',
    packages=["sort"],
    install_requires = [
                    'filterpy==1.4.5',
                    'scikit-image==0.17.2',
                    'lap==0.4.0'
                   ],
    zip_safe=False,
    python_requires='>=3.7.3',
)