import json
import os
import unittest

class TestLocalizationFramework(unittest.TestCase):
    
    def setUp(self):
        self.target_files = [
            "ar_game_config.json",
            "ar_tetris_config.json",
            "ar_calculator_config.json",
            "ar_weather_config.json"
        ]

    def test_file_load(self):
        for file_name in self.target_files:
            with self.subTest(file=file_name):
                self.assertTrue(os.path.exists(file_name))
                try:
                    with open(file_name, "r", encoding="utf-8") as f:
                        payload = json.load(f)
                    self.assertIsInstance(payload, dict)
                except json.JSONDecodeError:
                    self.fail(f"Failed parsing: {file_name}")

    def test_strings(self):
        for file_name in self.target_files:
            if not os.path.exists(file_name):
                continue
            with open(file_name, "r", encoding="utf-8") as f:
                data = json.load(f)
                for k, v in data.items():
                    if isinstance(v, dict):
                        for sub_k, sub_v in v.items():
                            self.assertTrue(len(str(sub_v)) > 0)
                    else:
                        self.assertTrue(len(str(v)) > 0)

if __name__ == "__main__":
    unittest.main()
python3 -m unittest test_localization_integrity.py test_backend_performance.py
