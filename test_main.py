import unittest
import pandas as pd
import data_plotting

data = {'Close': [100, 200, 300]}
data = pd.DataFrame(data)

class Func_main_Test(unittest.TestCase):

    def test_add(self):
        self.assertEqual(data_plotting.calculate_and_display_average_price(data), second=None)

if __name__ == "__main__":
    unittest.main()