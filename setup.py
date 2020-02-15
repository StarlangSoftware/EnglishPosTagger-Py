from setuptools import setup

setup(
    name='NlpToolkit-PosTagger',
    version='1.0.4',
    packages=['PosTagger'],
    url='https://github.com/olcaytaner/PosTagger-Py',
    license='',
    author='olcaytaner',
    author_email='olcaytaner@isikun.edu.tr',
    description='English PosTagger Library',
    install_requires=['NlpToolkit-Corpus', 'NlpToolkit-Hmm']
)
