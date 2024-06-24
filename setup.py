from setuptools import setup, find_packages

def read_requirements():
    with open('requirements.txt') as req:
        return req.read().splitlines()

setup(
    name='Youtube_data_analysis',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=read_requirements(),
    author='Immanuel',  # Replace with your name
    author_email='immanuel2504@gmail.com',
)
