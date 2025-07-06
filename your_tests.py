import unittest
from your_app_code import hello_world
import io
import sys

class TestMyApp(unittest.TestCase):
    def test_hello_world(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        hello_world()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "Hello, DevOps!\n")

if __name__ == '__main__':
    unittest.main()