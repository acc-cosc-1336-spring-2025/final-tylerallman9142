#write functions here, don't add input('') statements here!

def create_multiplication_table():
    table = []
    # Create 5 rows (1 to 5)
    for i in range(1, 6):
        row = []
        # Create 10 columns (1 to 10)
        for j in range(1, 11):
            row.append(i * j)
        table.append(row)
    return table


def display_multiplication_table(table):
    for row in table:
        # Print each number in the row separated by space, formatted for alignment
        print(" ".join(f"{num:2}" for num in row))