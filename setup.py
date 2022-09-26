from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name='NlpToolkit-PosTagger',
    version='1.0.8',
    packages=['PosTagger'],
    url='https://github.com/StarlangSoftware/PosTagger-Py',
    license='',
    author='olcaytaner',
    author_email='olcay.yildiz@ozyegin.edu.tr',
    description='English PosTagger Library',
    install_requires=['NlpToolkit-Corpus', 'NlpToolkit-Hmm'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
