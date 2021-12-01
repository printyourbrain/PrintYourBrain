#! /usr/bin/env python

import os
import setuptools  # noqa; we are using a setuptools namespace
from setuptools import setup

descr = """Print Your Prain"""

version = None
with open(os.path.join('pyb', '__init__.py'), 'r') as fid:
    for line in (line.strip() for line in fid):
        if line.startswith('__version__'):
            version = line.split('=')[1].strip().strip('\'')
            break
if version is None:
    raise RuntimeError('Could not determine version')


DISTNAME = 'pyb'
DESCRIPTION = descr
MAINTAINER = 'Anuja Negi'
MAINTAINER_EMAIL = 'anuja.negi@bccn-berlin.de'
LICENSE = 'BSD (3-clause)'
DOWNLOAD_URL = 'https://github.com/printyourbrain/PrintYourBrain.git'
VERSION = version
URL = 'https://github.com/printyourbrain/PrintYourBrain'


def package_tree(pkgroot):
    """Get the submodule list."""
    # Adapted from VisPy
    path = os.path.dirname(__file__)
    subdirs = [os.path.relpath(i[0], path).replace(os.path.sep, '.')
               for i in os.walk(os.path.join(path, pkgroot))
               if '__init__.py' in i[2]]
    return sorted(subdirs)


if __name__ == "__main__":
    setup(name=DISTNAME,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          license=LICENSE,
          version=VERSION,
          url=URL,
          download_url=DOWNLOAD_URL,
          long_description=open('README.md').read(),
          long_description_content_type='text/x-rst',
          classifiers=['Intended Audience :: Science/Research',
                       'Intended Audience :: Developers',
                       'License :: OSI Approved',
                       'Programming Language :: Python',
                       'Topic :: Scientific/Engineering',
                       'Operating System :: Microsoft :: Windows',
                       'Operating System :: Unix',
                       'Operating System :: MacOS',
                       'Programming Language :: Python :: 3',
                       ],
          platforms='any',
          python_requires='>=3.5',
          install_requires=[
              'conda',
          ],
          packages=package_tree('pyb'),
          )
