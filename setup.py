from setuptools import setup, find_packages



VERSION = '0.1.5'
DESCRIPTION = '''Get Today's Share Price'''
LONG_DESCRIPTION = '''This package can show today's share price of Nepal and store it in csv file. Source: https://www.sharesansar.com/'''

# Setting up
setup(
    name="share-price-nepal",
    version=VERSION,
    author="Aayam Shrestha",
    author_email="aayamthebest555@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['beautifulsoup4', 'requests', 'pandas', 'lxml'],
    keywords=['python', 'share sansar', 'share price',
              'share nepal', 'share price in nepal', 'share market of nepal', 'Aayam Shrestha'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
