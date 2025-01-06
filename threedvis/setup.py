from setuptools import setup, find_packages

setup(
    name='viz3d',
    version='1.0.0',
    description='A library for easy 3D visualizations using Matplotlib.',
    author='Ammar Jamshed & MOmina Sheikh ',
    author_email='ammarjamshed123@gmail.com',
    packages=find_packages(),
    install_requires=[
        'matplotlib>=3.0.0',
        'numpy>=1.17.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Visualization'
    ],
    python_requires='>=3.7',
)
