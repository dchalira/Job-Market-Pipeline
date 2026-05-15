import unittest
from app.extract import fetch_jobs


class TestExtract(unittest.TestCase):

    def test_fetch_jobs(self):
        df = fetch_jobs()

        self.assertFalse(df.empty)


if __name__ == '__main__':
    unittest.main()