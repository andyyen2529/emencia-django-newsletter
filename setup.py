import os
from setuptools import setup
from setuptools import find_packages

from emencia.django import newsletter


setup(name='emencia.django.newsletter',
      version='0.3.dev',
      description='A Django app for sending newsletter by email to a contact list.',
      long_description=open('README.rst').read() + '\n' +
                       open(os.path.join('docs', 'HISTORY.txt')).read(),
      keywords='django, newsletter, mailing',
      classifiers=[
          'Framework :: Django',
          'Programming Language :: Python',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: BSD License',
          'Development Status :: 5 - Production/Stable',
          'Topic :: Software Development :: Libraries :: Python Modules',],

      license='BSD License',
      packages=find_packages(exclude=['demo']),
      namespace_packages=['emencia', 'emencia.django'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'html2text==2015.11.4',
                        'python-dateutil==1.5',
                        'beautifulsoup4==4.6.0',
                        'django-tagging==0.4',
                        'vobject==0.8.2',
                        'xlwt==1.0.0',
                        'xlrd==0.9.4',
                        'Django==1.8.6'])
