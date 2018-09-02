import re
from setuptools import setup, find_packages
from codecs import open


with open('onetoken/__init__.py', 'r', encoding='utf8') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)
    print('regex find version', version)
if not version:
    raise RuntimeError('Cannot find version information')

setup(name='onetoken',
      author='OneToken',
      url='https://github.com/1token-trade/onetoken-py-sdk',
      author_email='admin@1token.trade',
      packages=find_packages(),
      version=version,
      description='OneToken Trade System Python SDK',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Intended Audience :: Financial and Insurance Industry',
          'Intended Audience :: Information Technology',
          'Topic :: Software Development :: Build Tools',
          'Topic :: Office/Business :: Financial :: Investment',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Operating System :: OS Independent',
          'Environment :: Console'
      ],
      install_requires=[
          'arrow==0.12.1',
          'docopt==0.6.2',
          'PyJWT==1.6.4',
          'PyYAML==3.13',
      ],
      extras_require={
          ':python_version>="3.6.0"': [
              'aiohttp==3.1.3'
          ],
          'qa': [
              'flake8==3.5.0'
          ],
          'doc': [
              'Sphinx==1.7.0'
          ]
      },
      zip_safe=False,
      )
