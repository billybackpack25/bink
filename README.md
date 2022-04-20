# Python Developer Test

Welcome to my solution using `Python 3.8.10` :)



## The repo

I've organised this git repo as such:

```
./bink/
│
├── images/
│   └── ...
|
├── tests/
│   ├── __init__.py
│   ├── test_first_section.py
│   ├── test_second_section.py
│   ├── test_third_section.py
│   └── test_fourth_section.py
|
├── data/
│   └── Python Developer Test Dataset.csv
│
├── __init__.py
├── .gitignore
├── welcome.txt
├── README.md
├── functions.py
└── script.py
```



## Assumptions

Firstly I'd like to tell you about any assumptions I've made:

1. User doesn't get to select the file being read in
2. The CSV data doesn't need to be validated
3. Since a user will be interacting with it, I'll be returning print statements for caught errors
4. Simple terminal and printing of data will not be evaluated
5. Lease years total rent is a sum of current rent of all rows in the list, and not the sum of rent for the lease period per tenant



## My Approach

The test files are split into the sections provided by the requirements, I first created unit tests and then coded the solution to pass the tests following TDD.
The majority of functions have their own file `functions.py`, this was to make the `script.py` easier to read.
`Script.py` contains the functions per section, the `main` and the `menu_options`.
`isort` and `black` was used to maintain a standard of formatting throughout the package.

Until the fourth section I was commiting on the main branch, then on the forth section to demonstrate branching I created a separate branch.

Along the way I've taken screenshots of the terminal as I build the program, these will be in the `images` directory. 

A requirements file has been captured from the python virtual environment used to allow for easy environment replication. 

## How to use the script?

1. Create your python environment `python -m venv your_python_environment`
2. Active it `source your_python_environment/bin/activate`
3. Clone the repo run `git clone https://github.com/billybackpack25/bink.git`
4. Install the requirements `pip install -r bink/requirements.txt`
6. Then run `python -m bink.script`

This will provide you with a menu... You can take it away from there. :)



## Running the tests

Running `python -m unittest -v` will run all the tests and print out the results on the console.
For example after writting my first test file we can see the below 2 test cases `test_read_csv` and `test_sorted_by_current_rent_asc` have failed.


```
EE
======================================================================
ERROR: test_read_csv (bink.tests.test_first_section.TestFirstSection)
Test reading in the example csv data
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/hassonb/envs/bink_env/bink/tests/test_first_section.py", line 13, in test_read_csv
    len(self.csv_list_data) >= 1,
TypeError: object of type 'NoneType' has no len()

======================================================================
ERROR: test_sorted_by_current_rent_asc (bink.tests.test_first_section.TestFirstSection)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/hassonb/envs/bink_env/bink/tests/test_first_section.py", line 19, in test_sorted_by_current_rent_asc
    self.test_read_csv()
  File "/home/hassonb/envs/bink_env/bink/tests/test_first_section.py", line 13, in test_read_csv
    len(self.csv_list_data) >= 1,
TypeError: object of type 'NoneType' has no len()

----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (errors=2)
```

> You can run the test files separately by doing `python -m unittest bink.tests.test_first_section`

A complete test run is below

```
(bink_env) hassonb@btp190116-ubuntuserver:~/envs/bink_env$ python -m unittest -v
test_read_csv (bink.tests.test_first_section.TestFirstSection)
Test reading in the example csv data ... ok
test_sorted_by_current_rent_asc (bink.tests.test_first_section.TestFirstSection)
Test that the data has been sorted by Current Rent ASC ... ok
test_filter_dates (bink.tests.test_fourth_section.TestFirstSection)
Test the date filter works by returning data between two dates ... ok
test_filter_lease_years (bink.tests.test_second_section.TestFirstSection)
Test the filter on lease years == 25 ... ok
test_total_rent (bink.tests.test_second_section.TestFirstSection)
Test the total rent for filtered data ... ok
test_masts_count_per_tenant (bink.tests.test_third_section.TestFirstSection)
Test the number of masts per tenant for this data set ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.052s

OK
```
