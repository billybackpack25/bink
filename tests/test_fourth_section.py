import unittest
from datetime import datetime

from bink.script import filter_dates, read_csv


class TestFirstSection(unittest.TestCase):
    def test_filter_dates(self):
        """
        Test the date filter works by returning data between two dates
        """
        csv_list_data = read_csv("./bink/Python Developer Test Dataset.csv")
        filtered_dates = filter_dates(
            csv_list_data=csv_list_data,
            start=datetime(1999, 6, 1),
            end=datetime(2007, 8, 31),
            key="Lease Start Date",
        )

        self.assertEqual(
            len(filtered_dates),
            5,
            "The total count of masts in this dataset should be 5",
        )


if __name__ == "__main__":
    unittest.main()
