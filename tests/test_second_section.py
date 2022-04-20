import unittest

from bink.script import filter_csv, read_csv, total_rent


class TestFirstSection(unittest.TestCase):
    def test_filter_lease_years(self):
        """
        Test the filter on lease years == 25
        """
        csv_list_data = read_csv("./bink/Python Developer Test Dataset.csv")
        self.lease_years_filter = filter_csv(csv_list_data, "Lease Years", "25")

        self.assertEqual(
            len(self.lease_years_filter),
            4,
            "There should only be 4 entries where the lease year is 25 in this data set",
        )

        self.assertTrue(
            all([x["Lease Years"] == "25" for x in self.lease_years_filter]),
            "The resulting data returned proves the filter did not work",
        )

    def test_total_rent(self):
        """
        Test the total rent for filtered data
        """
        self.test_filter_lease_years()
        self.assertEqual(
            total_rent(self.lease_years_filter),
            46500,
            "The sum for this data set with lease years == 25 filter, should be 46500",
        )


if __name__ == "__main__":
    unittest.main()
