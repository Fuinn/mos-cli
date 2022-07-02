.. mos-cli documentation master file, created by
   sphinx-quickstart on Thu Jun 30 23:40:50 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

##########################
MOS Command-Line Interface
##########################

############
Installation
############

Install the MOS command-line interface ``mosctl`` by executing::

   pip install mos-cli

#####
Usage
#####

.. argparse::
   :module: mos.cli.mosctl
   :func: create_parser
   :prog: mosctl