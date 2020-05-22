from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
      long_description = f.read()

setup(name='threephasescim',
      version='0.9.5',

      packages=find_packages(where='threephasescim'),
      package_dir={'': 'threephasescim'},
      package_data={'threephasescim/threephasescim/lookupTables' : ['*.xlsx']},
      
      description='An obnoxious attempt to design three phase induction motors using Python 3',
      url='https://github.com/pranabendra/three-phase-scim',
      author='Pranabendra Prasad Chandra',
      author_email='pranabendrachandra@gmail.com',
      license='MIT',
      include_package_data=True,
      long_description=long_description,
      long_description_content_type='text/markdown',
      install_requires=['pandas', 'numpy', 'scipy', 'xlrd', 'openpyxl',],
      zip_safe=False)
