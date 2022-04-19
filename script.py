from bink.functions import (
    print_welcome,
    print_menu,
    clear_the_screen,
    goodbye,
    signal_handler,
    read_csv,
    sort_csv,
)
import signal
from tabulate import tabulate

TEST_DATA = "./bink/Python Developer Test Dataset.csv"
MENU_OPTIONS = {
    1: "Sort by Current Rent and output first 5 (1f for all columns)",
    "q": "Exit the program",
}


def first_section(option):
    data = read_csv(filename=TEST_DATA)
    sorted_data = sort_csv(data, "Current Rent", order="asc")
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

def main():
    print_welcome()
    while True:
        print_menu(menu_options=MENU_OPTIONS)
        option = input("")
        clear_the_screen()
        if option == "1":
            first_section(option)
        elif option == "1f":
            first_section(option)
        elif option == "q":
            goodbye()
        else:
            print(
                "Sorry I didn't quite get that, have you tried one of the options in the list?"
            )

if __name__ == "__main__":
    # Catching Ctrl + C to say goodbye
    signal.signal(signal.SIGINT, signal_handler)
    main()
