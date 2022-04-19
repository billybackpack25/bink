import unittest

from bink.script import read_csv, sort_csv


class TestFirstSection(unittest.TestCase):
    def test_read_csv(self):
        """
        Test reading in the example csv data
        """
        self.csv_list_data = read_csv("./bink/Python Developer Test Dataset.csv")
        # At least one entry
        self.assertTrue(
            len(self.csv_list_data) >= 1,
            "There needs to be at least one row of data entered into the CSV, excluding the headers",
        )

    def test_sorted_by_current_rent_asc(self):
        """
        Test that the data has been sorted by Current Rent ASC
        """
        # Read in the CSV
        self.test_read_csv()
        # Get the sorted data
        sorted_by_current_rent = sort_csv(self.csv_list_data, "Current Rent")
        # Assert that the order is ASC with all = True
        self.assertTrue(
            all(
                sorted_by_current_rent[i]["Current Rent"]
                <= sorted_by_current_rent[i + 1]["Current Rent"]
                for i in range(len(sorted_by_current_rent) - 1)
            )
        )


if __name__ == "__main__":
    unittest.main()
