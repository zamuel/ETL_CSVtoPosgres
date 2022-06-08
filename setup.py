# Import required functions
from setuptools import setup, find_packages

# Call setup function
setup(
    author="Samuel Aguilar",
    description='Extract a .csv files for a zip and clean the data for storage on a postgres data base',
    name="ETL",
    packages=find_packages(include=["ETL", "ETL.*"]),
    version="1.0",
    install_requires=['os', 'csv', 'ZipFile', 'datetime', 'request', 'sqlalchemy']
)
