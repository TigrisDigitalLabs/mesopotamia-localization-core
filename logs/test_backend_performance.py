import unittest
import os
import time
from api_performance_monitor import SystemPerformanceMonitor
from log_processor import RegionalLogProcessor

class TestBackendAutomationPipelines(unittest.TestCase):

    def test_telemetry(self):
        mock_endpoints = [
            "https://mesopotamia-core.org",
            "https://mesopotamia-core.org"
        ]
        monitor = SystemPerformanceMonitor(mock_endpoints)
        start = time.time()
        monitor.execute_ping_cycle(iterations=2)
        end = time.time()
        
        self.assertLess((end - start), 2.0)
        health = monitor.evaluate_system_health()
        for endpoint in mock_endpoints:
            self.assertIn(endpoint, health)

    def test_processor_io(self):
        processor = RegionalLogProcessor(target_directory="./test_sandbox_logs")
        processor.initialize_workspace()
        self.assertTrue(os.path.exists("./test_sandbox_logs"))
        if os.path.exists("./test_sandbox_logs"):
            os.rmdir("./test_sandbox_logs")

if __name__ == "__main__":
    unittest.main()
