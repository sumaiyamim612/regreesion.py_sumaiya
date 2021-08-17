from setuptools import find_namespace_packages, setup
setup(
    name='regresspy',

    # Define the author of the repository.
    author='Sumaiya islam mim',

    # Define the Author's email
    author_email='sumaiya35-2322@diu.edu.bd',

    # Define the version of this library.
    version='1.0.0',

    # Here are the name of regression py.
    keywords='gradient descent, regression, loss, SGDRegressor',

    # here are the packages that extend internly
    packages=find_namespace_packages(include=['regresspy', 'regresspy.*']),

    # These are the dependencies the library needs in order to run.
    install_requires=[
        'numpy==latest',
        'scikit-learn',
    ]
)