import subprocess
import unittest


class testOverview(unittest.TestCase):
    def test(self):
        subprocess.call("python indexnow.py", shell=True)


if __name__ == '__main__':
    unittest.main()
