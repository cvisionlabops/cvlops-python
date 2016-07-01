from setuptools import setup
import os,sys

# Following Lapin example
# https://bitbucket.org/CVisionLab/cvl-python/src/51308c1155a6242fbb914870732187adfc8881f0/setup.py?at=default&fileviewer=file-view-default

root_pkg = 'cvlops'

# find all subpackages
root = os.path.join(os.path.dirname(__file__), root_pkg)

packages = []
for subdir, _, _ in os.walk(root):
        subpath = subdir[len(root):].replace(os.path.sep, '.')
        packages.append(root_pkg + subpath)

setup(
    name=root_pkg,
    description='CVISIONLAB OPS Python Utils',
    version='1.0',
    author='Skubriev Vladimir',
    author_email='skubriev@cvisionlab.com',
    license='GPL',
    install_requires=[
                  'smtplib',
                  'jinja2'
    ],
    packages=packages
)