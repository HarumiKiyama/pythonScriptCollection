# -*- coding: utf-8 -*-
from setuptools import setup,find_packages

VERSION = '0.1'
setup(name='send2kindle',
      version=VERSION,
      description='A tool to push ebook to kindle',
      keywords='python kindle push',
      author='uruk1993',
      author_email='lucius0720@hotmail.com',
      url='https://github.com/uruk1993/Python_project',
      license='GPL',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      install_requires=[],
      entry_points={
          'console_scripts':[
              'send2kindle=send2kindle.cli.cli:main',
          ]
      },
)
