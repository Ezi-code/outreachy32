"""test the app.py file."""

import unittest
import os 
from app.app import get_url_from_file, get_status_code, create_error_file

class TestApp(unittest.TestCase):
    """test the app.py file."""
    
    def test_get_url_from_file(self):
        """test get_url_from_file function."""
        urls = get_url_from_file("test.csv")
        self.assertEqual(urls, ["http://www.google.com", "http://nonexistent.url.test", "http://www.github.com"])

    def test_get_status_code(self):
        """test get_status_code function."""
        status = get_status_code("http://www.google.com")
        self.assertEqual(status, 200)

    def test_get_status_code_nonexistent(self):
        """test get_status_code function with nonexistent url."""
        status = get_status_code("http://nonexistent.url.test")
        self.assertIsNone(status)

    def test_get_status_code_github(self):
        """test get_status_code function with github url."""
        status = get_status_code("http://www.github.com")
        self.assertEqual(status, 200)

    def test_create_error_file(self):
        """test create_error_file function."""
        create_error_file("test error")
        with open("errors.txt", "r") as f:
            self.assertIn("test error", f.read())
        os.remove("errors.txt")

if __name__ == "__main__":
    unittest.main()
