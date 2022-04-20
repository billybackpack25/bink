import csv
import os
import signal
from datetime import datetime
from decimal import Decimal


def filter_csv(csv_list_data: list, key: str, equals: str) -> list:
    """
    Take in a list of dicts, and return a subset where the key matches the equals value

    Args:
        csv_list_data (list): List of CSV dictionary data
        key (str): Key used to match the equals
        equals (str): Value used to match against the key

    Returns:
        list: Filtered list of dictionaries
    """
    return [x for x in csv_list_data if x[key] == equals]


def total_rent(csv_list_data: list) -> int:
    """
    Sum up the rent for all entries of  the list

    Args:
        csv_list_data (list): List of CSV property data

    Returns:
        int: Sum of rent
    """
    return sum([Decimal(x["Current Rent"]) for x in csv_list_data])


def print_menu(menu_options: dict) -> None:
    """
    Print out the menu options provided

    Args:
        menu_options (dict): Menu options with the key being used to validate user input
    """
    print("\n\nOPTIONS: \n")
    for key, value in menu_options.items():
        print(f"{key}: {value}")

    print()


def print_welcome() -> None:
    """
    Read and print out a welcome.txt file that includes ascii art
    """
    with open("./bink/welcome.txt", "r") as file:
        ascii_art = file.readlines()

    # Join the lines
    print("".join(ascii_art))


def goodbye() -> None:
    """
    Clear the screen and print a goodbye statement
    """
    clear_the_screen()
    print("Thank you for using Bink, hope to see you again soon.")
    exit(0)


def signal_handler(sig, frame) -> None:
    """
    Handle the user hitting Crtl + C, print goodbye message and exit
    """
    goodbye()
    exit(0)


def clear_the_screen() -> None:
    """
    Clear the terminal for both Windows and Linux OS
    """
    os.system("cls" if os.name == "nt" else "clear")


def read_csv(filename: str) -> list:
    """
    Read in a csv file

    Args:
        filename (str): Location for the csv file to read

    Returns:
        list: List of CSV data read in from the file as a list of ordered dictionaries
    """
    with open(filename, newline="") as csv_infile:
        csv_data = [x for x in csv.DictReader(csv_infile)]
    return csv_data


def sort_csv(csv_data: list, key: str, order: str = "asc") -> list:
    """
    Sort given csv data by a key in ascending order unless specified otherwise.

    Args:
        csv_data (list): List of dictionaries as csv data
        key (str): Used to select which field to sort the data from the CSV table headers
        order (str, optional): asc for ascending or anything else for decending, e.g. desc. Defaults to 'asc'.

    Returns:
        list: List of sorted dictionaries by the key provided
    """
    try:
        newlist = sorted(
            csv_data, key=lambda d: d[key], reverse=False if order == "asc" else True
        )
    except KeyError:
        print("That key doesn't exist")
    return newlist


def masts_per_tenant(csv_list_data: list) -> dict:
    """
    Count the number of masts per tenant

    Args:
        csv_list_data (list): List of CSV dictionary data

    Returns:
        dict: Dictionary of tenent name and count of masts
    """
    data = {}
    for mast in csv_list_data:
        try:
            data[mast["Tenant Name"]] += 1
        except:
            data[mast["Tenant Name"]] = 1

    return data


def filter_dates(csv_list_data: list, start: datetime, end: datetime, key: str) -> list:
    """
    Filter through the data and return masts between two dates given a key

    Args:
        csv_list_data (list): List of dictionaries as csv data
        start (datetime): Date to begin the filter range
        end (datetime): Date to end the filter range
        key (str): Column used to calculate the date range, must be a date column in format %d %b %Y

    Returns:
        list: Masts between the times given
    """
    return [
        mast
        for mast in csv_list_data
        if start <= datetime.strptime(mast[key], "%d %b %Y") <= end
    ]


def change_date_formatting(date: datetime) -> str:
    return datetime.strptime(date, "%d %b %Y").strftime("%d/%m/%Y")
