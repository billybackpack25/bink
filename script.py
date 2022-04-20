from bink.functions import (
    print_welcome,
    print_menu,
    clear_the_screen,
    goodbye,
    signal_handler,
    read_csv,
    sort_csv,
    filter_csv, 
    total_rent,
    masts_per_tenant,
)
import signal
from tabulate import tabulate

TEST_DATA = './bink/Python Developer Test Dataset.csv'
MENU_OPTIONS = {
    1: 'Sort by Current Rent and output first 5 (1f for all columns)',
    2: 'Output lease years == 25',
    3: 'Output lease years == 25 total rent',
    4: 'Count of masts per tenant name',
    'q': 'Exit the program',
}
CSV_DATA = read_csv(filename=TEST_DATA)

def first_section(option: int) -> None:
    """
    Print out the first 5 rows of data with table formatting

    Args:
        option (int): Option chosen by the user
    """
    sorted_data = sort_csv(CSV_DATA, "Current Rent", order="asc")
    if option == "1":
        print(
            tabulate(
                [
                    {
                        "Property Name": x["Property Name"],
                        "Tenant Name": x["Tenant Name"],
                        "Lease Start Date": x["Lease Start Date"],
                        "Lease End Date": x["Lease End Date"],
                        "Current Rent": x["Current Rent"],
                    }
                    for x in sorted_data[:5]
                ],
                headers="keys",
                tablefmt="presto",
            )
        )
    else:
        print(tabulate(sorted_data[:5], headers="keys", tablefmt="presto"))

    print()

def second_section(option: int) -> None:
    """
    Print out data for lease year == 25 filter and sum of rent

    Args:
        option (int): Option chosen by the user
    """
    lease_years_filter = filter_csv(CSV_DATA, 'Lease Years', '25')
    if option == '2':
        print(tabulate(lease_years_filter, headers="keys", tablefmt="presto"))
    elif option == '3':
        sum_of_rent = total_rent(lease_years_filter)
        print(f'The sum of rent is £{sum_of_rent}')

def third_section(option: int) -> None:
    """
    Print out the mast count per tenant name

    Args:
        option (int): Option chosen by the user
    """
    print(tabulate(masts_per_tenant(CSV_DATA).items(), headers=['Tenant Name','Count of Masts']))

def menu_select(option):
    if option in ['1', '1f']:
        first_section(option)
    elif option in ['2','3']:
        second_section(option)
    elif option in ['4']:
        third_section(option)
    elif option == 'q':
        goodbye()
    else:
        print(
            "Sorry I didn't quite get that, have you tried one of the options in the list?"
        )

def main():
    print_welcome()
    while True:
        print_menu(menu_options = MENU_OPTIONS)
        option = input("")
        clear_the_screen()
        menu_select(option)

if __name__ == "__main__":
    # Catching Ctrl + C to say goodbye
    signal.signal(signal.SIGINT, signal_handler)
    main()
