import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyfbi-praneethkarnena',
    version='0.0.1',
    author='Praneeth Karnena',
    author_email='praneeth.codes@gmail.com',
    description='Python client for FBI crime data API of the United States',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/PraneethKarnena/pyfbicrime',
    packages=setuptools.find_packages(),
    classifiers=[
        'DEVELOPMENT STATUS :: 5 - PRODUCTION/STABLE',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: APACHE SOFTWARE LICENSE',
        'Operating System :: OS Independent',
    ],
    keywords='api-wrapper api united-states fbi federal-bureau-of-investigation crime-data crime-statistics crime crime-analysis',
    python_requires='>=3',
    install_requires='requests',
)