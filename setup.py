import setuptools


setuptools.setup(
    name='pyqt5collector',
    author='Kyle Altendorf',
    author_email='sda@fstab.net',
    url='https://github.com/altendky/pyqt5collector',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'pyqt5collector = pyqt5collector.cli:cli',
        ],
    },
    install_requires=[
        'attrs',
        'click',
        'scrapy',
    ],
    extras_require={
        'dev': [
            'gitignoreio',
        ],
    },
)
