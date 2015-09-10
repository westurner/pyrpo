.. :changelog:

History
=========

::

    git log --format='* %s [%h]' master..develop
    # [ ... ]


0.2.2 (2015-09-10)
+++++++++++++++++++
* CLN: cmd = [c,m,d] style [51a02e4]
* BUG,SEC,DOC: shell=False by default, tuples, find git submodules [977ecec]
* BLD: setup.py: remove download_url='https://github.com/westurner/pyrpo/releases' [0cdf644]
* BUG,ENH,SEC: pyrpo.py: try to parse .git/ symlinks, and ./.git submodules files [48aab61]

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
