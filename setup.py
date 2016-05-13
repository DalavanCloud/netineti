""" Setup tools information"""
from setuptools import setup

def readme():
    """Prepares README.rst for long description"""
    with open('README.rst') as f:
        return f.read()

setup(name='netineti',
      version='0.3.0',
      description='Finder of scientific names in texts',
      long_description=readme(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Text Processing :: Linguistic',
      ],
      keywords='scientific names taxonomy biology nomenclature biodiversity',
      url='https://github.com/mbl-cli/netineti',
      author='Lakshmi Manohar Akella, Chack Ha, Dmitry Mozzherin',
      author_email='dmozzherin@gmail.com',
      license='MIT',
      packages=['netineti'],
      install_requires=[
          'tornado>=4.3',
          'nltk>=3.1',
          'scikit-learn>=0.17'
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['funniest-joke=funniest.command_line:main'],
      },
      include_package_data=True
     )
