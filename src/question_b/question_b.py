#write functions here, don't add input('') statements here!

class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name


def get_stock_list():
    stock_list = []
    try:
        with open("stock_file.dat", "r") as file:
            for line in file:
                parts = line.strip().split(maxsplit=1)
                if len(parts) == 2:
                    symbol, company_name = parts
                    stock = Stock(symbol, company_name)
                    stock_list.append(stock)

    except FileNotFoundError:
        #print("Error: stock_file.dat not found.")
        return stock_list