from setuptools import setup, find_packages

setup(
    name='toshl',
    version='0.0.2',
    url='https://github.com/andreagrandi/toshl-python',
    download_url='https://github.com/andreagrandi/toshl-python/tarball/0.0.2',
    author='Andrea Grandi',
    author_email='a.grandi@gmail.com',
    description='Python client library for Toshl API.',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    license='MIT',
    install_requires=[
        'mock==1.3.0',
        'pytest==2.9.1',
        'requests==2.9.1',
    ],
)
