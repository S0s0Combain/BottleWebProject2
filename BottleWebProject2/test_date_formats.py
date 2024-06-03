import unittest
import articles_handler as ah
from datetime import datetime

class Test_test_date_formats(unittest.TestCase):
    def test_correct_format(self):
        dates=['2024-06-03', datetime.now().strftime('%Y-%m-%d'), '2023-06-01', '2024-04-02', '2024-02-29', '2022-02-28', '2023-12-31', '2024-01-01', '2024-05-31', '2024-04-30', '2024-04-01', '2023-07-31', '2023-08-31']
        for date in dates:
            self.assertTrue(ah.check_date(date),  f"Test faild with {date}")
        
    def test_uncorrect_format(self):
        dates=['31.01.2024', '22-01-2024', '22/01/2022', '02-22-2022', '03/23/2022',  '14 March 2022', '14.03.22', '14-03-22', '14/03/22', '22-03-14', '22/03/14', '22.03.14', '14.3.22', '14-3-22', '14/3/22', '22-3-14', '22/3/14', '22.3.14']
        for date in dates:
            self.assertFalse(ah.check_date(date), f"Test faild with {date}")

if __name__ == '__main__':
    unittest.main()
