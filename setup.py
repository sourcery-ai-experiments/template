from setuptools import setup, find_packages

setup(
    name='template',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy',
        'pandas',
        'scipy',
        'matplotlib',
        'jupyter',
        'ruff',
        'sphinx',
        'python-dotenv',
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'template=src.main:main',
        ],
    },
)
