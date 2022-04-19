# Python Developer Test

Welcome to my solution using `Python 3.8.10` :)



## The repo

I've organised this git repo as such:

```
./bink/
│
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
├── README.md
└── script.py
```



## Assumptions

Firstly I'd like to tell you about any assumptions I've made:

1. User doesn't get to select the file being read in
2. The CSV data doesn't need to be validated
3. Since a user will be interacting with it, I'll be returning print statements for caught errors
4. Create a simple terminal menu as not to rely on outside code for this small script



## My Approach

I split the test files into the sections provided by the requirements, created my unit tests and then coded the solution to pass the tests.
I used `isort` and `black` to format my code



## How to use the script?

1. To clone the repo run `git clone https://github.com/billybackpack25/bink.git`
2. Then run `python -m bink.script`

This will provide you with a menu... You can take it away from there. :)



## Running the tests

Running `python -m unittest` will run all the tests and print out the results on the console.
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