from setuptools import setup, find_packages

setup(name='threephasescim',
      version='0.9.1',

      packages=find_packages(where='threephasescim'),
      package_dir={'': 'threephasescim'},
      package_data={'threephasescim/lookupTables' : ['*.xlsx']},
      
      description='An obnoxious attempt to design three phase induction motors using Python 3',
      url='https://github.com/pranabendra/three-phase-scim',
      author='Pranabendra Prasad Chandra',
      author_email='pranabendrachandra@gmail.com',
      license='MIT',
      install_requires=['pandas', 'numpy', 'scipy', 'xlrd', 'openpyxl',],
      zip_safe=False)
