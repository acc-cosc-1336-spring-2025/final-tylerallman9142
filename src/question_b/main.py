#add import

from question_b import get_stock_list


def main():
    while True:
        print("Menu:")
        print("1 - Display stock purchase history")
        print("2 - Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            stocks = get_stock_list()
            if stocks:
                print("\nStock Report")
                print("{:<15}{}".format("Company", "Symbol"))
                print("-" * 30)
                for stock in stocks:
                    print("{:<15}{}".format(stock.get_company_name(), stock.get_symbol()))
                print()
        elif choice == "2":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please enter 1 or 2.\n")


if __name__ == "__main__":
    main()