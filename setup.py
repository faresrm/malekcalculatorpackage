from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='malekcalculatorpackage',
    version='0.0.1',
    description='A very basic calculator',
    author='Fares Ladib',
    author_email='fares.ladib@muutaa.com',
    url="https://github.com/faresrm/malekcalculatorpackage",
    license='MIT',
    classifiers=classifiers,
    keywords='calculator',
    packages=find_packages(),
    install_requires=[]
)

