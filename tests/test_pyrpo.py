
import unittest

from pyrpo.pyrpo import itersplit, BzrRepository

# class TestThese(unittest.TestCase):
#   def test_00_files(self):
#       for f in list_files('.'):
#           log.info(f)
#
#    def test_01_find_repos(self):
#        for r in do_repo_report('.'):
#            for f in r.lately():
#                log.debug(f)


class TestBzr(unittest.TestCase):

    def test_bzr_logparse(self):
        s = '''------------------------------------------------------------
revno: 377
tags: 0.8.99~alpha2
committer: Siegfried-Angel Gevatter Pujals <siegfried@gevatter.com>
branch nick: zeitgeist
timestamp: Fri 2012-01-27 16:39:16 +0100
message:
  Release 0.8.99~alpha2.
------------------------------------------------------------
revno: 376
committer: Siegfried-Angel Gevatter Pujals <siegfried@gevatter.com>
branch nick: bluebird
timestamp: Fri 2012-01-27 15:33:29 +0100
message:
  Update NEWS file.
------------------------------------------------------------
revno: 375 [merge]
committer: Siegfried-Angel Gevatter Pujals <siegfried@gevatter.com>
branch nick: bluebird
timestamp: Fri 2012-01-27 14:34:18 +0100
message:
  Implement find_storage_for_uri
'''
        records = itersplit(s, '-' * 60)
        for r in records:
            # entries = itersplit(r, '\n')
            _parsed_records = BzrRepository._parselog(r)
            if _parsed_records:
                print(list(_parsed_records))
