import unittest

from bink.script import read_csv, masts_per_tenant


class TestFirstSection(unittest.TestCase):

    def test_masts_count_per_tenant(self):
        """
        Test the number of masts per tenant for this data set
        """
        csv_list_data = read_csv("./bink/Python Developer Test Dataset.csv")
        self.assertEqual(
            masts_per_tenant(csv_list_data)['Everything Everywhere Ltd'],
            4,
            "The sum of masts for 'Everything Everywhere Ltd' should be 4"
        )

if __name__ == "__main__":
    unittest.main()
