
import os
import unittest

from pyrpo.pyrpo import main, itersplit, BzrRepository

THISDIR = os.path.join(os.path.dirname(__file__))
REPODIR = os.path.join(THISDIR, '../..')

class TestPyrpoCLI(unittest.TestCase):
    def test_cli_main(self):
        with self.assertRaises(SystemExit):
            main(['-h'])

    def test_cli_scan(self):
        retcode = main(['-s', REPODIR])

    def test_cli_scan_multiple(self):
        retcode = main(['-s', REPODIR, '-s', REPODIR])

    def test_cli_scan_report_origin(self):
        retcode = main(['-s', REPODIR, '-r', 'origin'])

    def test_cli_scan_report_status(self):
        retcode = main(['-s', REPODIR, '-r', 'status'])

    def test_cli_scan_report_status_verbose(self):
        retcode = main(['-s', REPODIR, '-r', 'status', '-v'])

    def test_cli_scan_report_status_quiet(self):
        retcode = main(['-s', REPODIR, '-r', 'status', '-q'])

    def test_cli_scan_report_full(self):
        retcode = main(['-s', REPODIR, '-r', 'full'])

    def test_cli_scan_report_gitmodule(self):
        retcode = main(['-s', REPODIR, '-r', 'gitmodule'])

    def test_cli_scan_report_json(self):
        retcode = main(['-s', REPODIR, '-r', 'json'])

    def test_cli_scan_report_sh(self):
        retcode = main(['-s', REPODIR, '-r', 'sh'])

    def test_cli_scan_report_str(self):
        retcode = main(['-s', REPODIR, '-r', 'str'])

    def test_cli_scan_report_pip(self):
        retcode = main(['-s', REPODIR, '-r', 'pip'])

    def test_cli_scan_report_hgsub(self):
        retcode = main(['-s', REPODIR, '-r', 'hgsub'])

    def test_cli_scan_report_thg(self):
        retcode = main(['-s', REPODIR, '--thg'])

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
