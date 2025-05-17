#add import
from question_a import stock_purchase_history

def main():
    while True:
        print("Menu:")
        print("1 - Display stock purchase history")
        print("2 - Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            stock_purchase_history()
        elif choice == "2":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please enter 1 or 2.\n")


if __name__ == "__main__":
    main()