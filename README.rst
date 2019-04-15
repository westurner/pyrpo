===============================
pyrpo
===============================


`GitHub`_ |
`PyPI`_ |
`Documentation`_ |
`Travis-CI`_


.. image:: http://img.shields.io/pypi/v/pyrpo.svg
        :target: https://pypi.python.org/pypi/pyrpo

.. image:: http://img.shields.io/pypi/dm/pyrpo.svg
        :target: https://warehouse.python.org/project/pyrpo/

.. image:: http://img.shields.io/github/release/westurner/pyrpo.svg
        :target: https://github.com/westurner/pyrpo/releases

.. .. image:: https://travis-ci.org/westurner/pyrpo.png?branch=master
..       :target: https://travis-ci.org/westurner/pyrpo

.. image:: http://img.shields.io/travis/westurner/pyrpo/master.svg
        :target: https://travis-ci.org/westurner/pyrpo


.. _GitHub: https://github.com/westurner/pyrpo
.. _PyPI: https://pypi.org/project/pyrpo
.. _Warehouse: https://warehouse.python.org/project/pyrpo
.. _Documentation:  https://pyrpo.readthedocs.org/en/latest
.. _Travis-CI:  https://travis-ci.org/westurner/pyrpo

pyrpo: a shell command wrapper for hg, git, bzr, svn


Features
==========

* Wrap and parse shell commands (largely as a reference)
* Walk for repository directories
* Generate reports for one or more repositories
* Call ``hg status``, ``git status``, etc. 
* Generate mercurial ``.hgsubs``
* Generate git ``.gitsubmodule``
* Generate pip ``requirements.txt``
* Generate shell script (to rebuild environment)

  * TODO: replicate branches/tags/revisions

* Functional `namedtuples`_, `iterators`_ ``yield`` -ing `generators`_
* `optparse`_ argument parsing (``-h``, ``--help``)
* `cookiecutter-pypackage`_ project templating  


.. _namedtuples: https://docs.python.org/2/library/collections.html#collections.namedtuple 
.. _iterators: https://docs.python.org/2/howto/functional.html#iterators
.. _generators: https://docs.python.org/2/howto/functional.html#generators    
.. _optparse: https://docs.python.org/2/library/optparse.html 
.. _cookiecutter-pypackage: https://github.com/audreyr/cookiecutter-pypackage 



Installing
============
Install from `PyPi`_::

    pip install pyrpo

Install from `GitHub`_ as editable (add a ``pyrpo.pth`` in ``site-packages``)::

    pip install -e git+https://github.com/westurner/pyrpo#egg=pyrpo


Usage
=========

Print help::

    pyrpo --help

Scan for files::

    # Scan and print a shell report
    pyrpo -s . -r sh
    pyrpo

Generate a TortoiseHG ``thg-reporegistry.xml`` file::

    pyrpo -s . --thg

Generate a pip report::

    pyrpo -r pip

Generate a status report::

    pyrpo -r status

Generate an `.hgsubs` file::

    pyrpo -r hgsub

Generate a ``.gitmodules`` file::

    pyrpo -r gitmodule

Generate an origin report::

    pyrpo -r origin

Generate a string report::

    pyrpo -r str



License
========
`BSD Software License
<https://github.com/westurner/pyrpo/blob/master/LICENSE>`_
