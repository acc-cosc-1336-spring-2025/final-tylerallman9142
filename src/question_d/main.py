#add import

from question_d import create_multiplication_table, display_multiplication_table


def main():
    while True:
        table = create_multiplication_table()
        display_multiplication_table(table)

        cont = input("Do you want to generate the table again? (y/n): ").strip().lower()
        if cont != 'y':
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()