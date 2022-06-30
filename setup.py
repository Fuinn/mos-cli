from setuptools import setup, find_packages

setup(name='mos-cli',
      zip_safe=False,
      version='0.1.0',
      author='Fuinn',
      url='https://github.com/Fuinn/mos-cli',
      description='MOS command-line interface',
      license='BSD 3-Clause License',
      packages=find_packages(),
      include_package_data=True,
      entry_points={'console_scripts': ['mosctl=mos.cli.mosctl:main']},
      classifiers=['Development Status :: 4 - Beta',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: Microsoft :: Windows',
                   'Operating System :: MacOS',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 3.6'],
      install_requires=[
            "argparse==1.1",
            "mos-interface==0.1.0"])