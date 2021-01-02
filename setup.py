from setuptools import setup

setup(
    name='NlpToolkit-PosTagger',
    version='1.0.5',
    packages=['PosTagger'],
    url='https://github.com/StarlangSoftware/PosTagger-Py',
    license='',
    author='olcaytaner',
    author_email='olcay.yildiz@ozyegin.edu.tr',
    description='English PosTagger Library',
    install_requires=['NlpToolkit-Corpus', 'NlpToolkit-Hmm']
)
