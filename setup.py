from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='plumi.skin',
      version=version,
      description="A Plumi 0.3 Skin Product",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone plumi skin',
      author='Andy Nicholson',
      author_email='andy@engagemedia.org',
      url='http://plumi.org/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plumi'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [distutils.setup_keywords]
      paster_plugins = setuptools.dist:assert_string_list

      [egg_info.writers]
      paster_plugins.txt = setuptools.command.egg_info:write_arg
      """,
      paster_plugins = ["ZopeSkel"],
      )
