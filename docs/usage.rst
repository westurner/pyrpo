========
Usage
========

To use pyrpo in a project::

	import pyrpo

To use pyrpo as a shell command:

.. .. program-output:: pyrpo --help

::

    Usage: pyrpo [-h] [-v] [-q] [-s .] [-r <pip||full|status|hgsub|thg>] [--thg]

    Options:
      -h, --help            show this help message and exit
      -s SCAN, --scan=SCAN  Path(s) to scan for repositories
      -r REPORTS, --report=REPORTS
                            pip || full || status || hgsub || thg
      --thg                 Write a thg-reporegistry.xml file to stdout
      --template=REPORT_TEMPLATE
                            Report template
      -v, --verbose         
      -q, --quiet 
