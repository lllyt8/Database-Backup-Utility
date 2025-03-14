from setuptools import setup

setup(
    name="dbbackup",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click>=7.0",
        "PyYAML>=5.1",
        "mysqlclient>=1.4.6",
        "psycopg2-binary>=2.8.0",
        "pymongo>=3.10.0",
    ],
    entry_points={
        "console_scripts": [
            "dbbackup = dbbackup.cli:main",
        ],
    },
    python_requires=">=3.6",
)
