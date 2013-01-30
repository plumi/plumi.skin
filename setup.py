from setuptools import setup, find_packages
import os

version = '4.5'

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    'Change history\n'
    '**************\n'
    + '\n' +
    read('CHANGES.txt')
    + '\n' +
    'Contributors\n'
    '************\n'
    + '\n' +
    read('CONTRIBUTORS.txt')
    )

setup(name='plumi.skin',
      version=version,
      description="Plumi Skin",
      long_description=long_description,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone plumi skin',
      author='Andy Nicholson',
      author_email='andy@infiniterecursion.com.au',
      url='http://plumi.org/',
      download_url = 'https://github.com/plumi/plumi.skin',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plumi'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.ContentWellPortlets',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=['PasteScript']
      )
