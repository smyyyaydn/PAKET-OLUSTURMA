
from setuptools import setup, find_packages

setup(
    name='python-package-example',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An example python package',
    long_description=open('README.txt').read(),
    install_requires=['numpy'],
    url='https://https://github.com/smyyyaydn/paket-olu-turma-',
    author='Bill Mills',
    author_email='myemail@example.com'
)
