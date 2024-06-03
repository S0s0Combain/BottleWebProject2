import unittest
from datetime import datetime, timedelta
import articles_handler as ah

class Test_test_uncorrect_date(unittest.TestCase):
    def test_uncorrect_date(self):
        values = ['2000', 'march', '03', '03-12', '2020-03', '03-03-03-03', '2024-06-03 12:00', '2024-06-03 00:00:00', '2025-06-03', '2030-06-03', (datetime.now()+timedelta(days=365)).replace(microsecond=0).isoformat(), (datetime.now()+timedelta(days=1)).replace(microsecond=0).isoformat(), '2022-06-31']
        for value in values:
            self.assertFalse(ah.check_date(value))

if __name__ == '__main__':
    unittest.main()
