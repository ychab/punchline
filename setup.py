from setuptools import setup, find_packages

setup(
    name='Punchline',
    version='0.1',
    author="Yannick Chabbert",
    author_email="yannick.chabbert@gmail.com",
    license="MIT",
    url="",
    description='Collect the best punchlines!',
    long_description='Collect the best punchlines, from various environment (music, politics, book, and so on).',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
)
