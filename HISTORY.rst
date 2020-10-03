.. :changelog:

History
=========

release/0.2.3 (2020-10-02 21:36:25 -0400)
+++++++++++++++++++++++++++++++++++++++++
::

   git log --reverse --pretty=format:'* %s [%h]' v0.2.2..release/0.2.3

* BLD: setup.py: add sarge to install_requires \[2e38b51\]
* RLS: __init__,setup.py: v0.2.3, add 3.8 trove classifier \[e35e91f\]


0.2.2 (2019-04-15)
+++++++++++++++++++
* Python 3.7 Support
* Minimal tests for each report type

::

    git log --format='* %s [%h]' master..develop
    # [ ... ]

0.2.1 (2015-05-24)
+++++++++++++++++++
* BUG: pyrpo.py: sh_full report: ``cat > %r << EOF`` [91d5fb7]
* BUG,CLN: pyrpo.py: logname='pyrpo' [e029abe]
* BLD: Makefile: pull, push, BROWSERCMD lookups [59cbc66]
* BLD: Makefile: twine [d636e15]

0.2.0 (2015-04-25)
+++++++++++++++++++
* Development: https://github.com/westurner/pyrpo/commits/develop
* Master: https://github.com/westurner/pyrpo/commits/master

0.1.0 (2014-05-12)
++++++++++++++++++
* First release on PyPI.
* Re-packaged from https://github.com/westurner/dotfiles/blob/2813e4ad/scripts/repos.py
