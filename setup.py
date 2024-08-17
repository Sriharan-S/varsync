from setuptools import setup, find_packages

setup(
    name='varsync',
    version='0.1',
    description='A Simple Library used to save your variables in cloud.',
    author='Sriharan',
    author_email='sriharan2544@gmail.com',
    packages=find_packages(),
    install_requires=[
        'mysql-connector-python',
        'json'        
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
