import json
import os
import unittest

class TestLocalizationFramework(unittest.TestCase):
    def test_file_load(self):
        targets = ["ar_game_config.json", "ar_tetris_config.json", "ar_calculator_config.json", "ar_weather_config.json"]
        for file_name in targets:
            if os.path.exists(file_name):
                with open(file_name, "r", encoding="utf-8") as f:
                    self.assertIsInstance(json.load(f), dict)

if __name__ == "__main__":
    unittest.main()
