from setuptools import setup, find_packages
import os


def _get_requirements(file_name="requirements.txt"):
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, file_name)) as f:
        requirements = f.read().splitlines()
        if not requirements:
            raise RuntimeError(f"Unable to read requirements from the {file_name} file.")
    return requirements


setup(name='chemdesc',
      version='0.2.1',
      description='Parallel descriptors computation for molecular chemistry',
      url='https://github.com/jules-leguy/ChemDesc',
      author='Jules Leguy',
      author_email='leguy.jules@gmail.com',
      install_requires=_get_requirements(),
      license='LGPL',
      packages=find_packages(),
      zip_safe=False)
