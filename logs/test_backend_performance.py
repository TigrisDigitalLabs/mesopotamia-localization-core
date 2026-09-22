import unittest
import os

class TestBackendAutomationPipelines(unittest.TestCase):
    def test_sandbox_setup(self):
        path = "./test_sandbox_logs"
        if not os.path.exists(path):
            os.makedirs(path)
        self.assertTrue(os.path.exists(path))
        os.rmdir(path)

if __name__ == "__main__":
    unittest.main()
