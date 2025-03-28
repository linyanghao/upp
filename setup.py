import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='upp',
    version='0.2.4',
    author='Samir Ibradžić',
    description='Uplift Power Play',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sibradzic/upp',
    package_dir={'': 'src'},
    packages=['upp', 'upp/atom_gen'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7, <4',
    install_requires=[
        'click',
        'setuptools'
    ],
    entry_points={
        'console_scripts': [
            'upp=upp.upp:main',
        ],
    },
)
