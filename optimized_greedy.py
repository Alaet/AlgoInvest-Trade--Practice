import csv
from data.actions import stocks as small_list_stocks
from wallet.view import display_top_wallet
from wallet.model import Wallet
from timeit import timeit

# region CSV READ FUNCTIONS


def read_files(files_names):
    """
    Take a list of csv file path to return csv files data's as a single list
    :param files_names: list[%path%,*] -> type(.csv)
    :return: list[csv_files_datas]
    """
    file_stocks_list = []
    for file_name in files_names:
        file = open(file_name)
        csvreader_file = csv.reader(file)
        for stock_row in csvreader_file:
            if stock_row[1] != "price":
                stock_row[1] = float(stock_row[1])
                stock_row[2] = float(stock_row[2])
                if stock_row[1] > 0 and stock_row[2] > 0:
                    file_stocks_list.append(stock_row)
    return file_stocks_list


def read_file(file_name):
    """
    Take a csv file path to return csv data's as a single list
    :param file_name: %path% -> type(.csv)
    :return: list[csv_datas]
    """
    file_stock_list = []
    file = open(file_name)
    csvreader_file = csv.reader(file)
    for stock_row in csvreader_file:
        if stock_row[1] != "price":
            stock_row[1] = float(stock_row[1])
            stock_row[2] = float(stock_row[2])
            if stock_row[1] > 0 and stock_row[2] > 0:
                file_stock_list.append(stock_row)
    return file_stock_list
# endregion


def get_best_wallet(stocks, capital):
    """
    Take list of stock and maximum capital to return, one, of the most profitable wallet possible
    By using a greedy approach, list get sorted by profitability, then from top stock :
    Will add every stock until capital is reach and keep as best wallet based on benefit.
    Then, will test with the same process starting from next stock in ordered by benefit list in case a better
    combination exist,
    If so, replace best_combination in cache by the new one until every stock was tested.
    Finally, display the best Wallet().
    :param stocks: list[
                        [stock_name,
                         stock_price,
                         stock_percent_profitability]
                        ]
    :param capital: int
    :return: None
    """
    for stock in stocks:
        benef = stock[2]/100*stock[1]
        ratio = benef/stock[1]
        stock.append(ratio)
    stocks = sorted(stocks, key=lambda tup: (-tup[3], tup[0]))
    best_wallet = Wallet([])
    allocated_capital = capital
    current_wallet = Wallet([])
    for current_stock in stocks:
        if 0 <= current_stock[1] <= allocated_capital:
            current_wallet.stocks.append(current_stock)
            allocated_capital -= current_stock[1]
            current_wallet.benefit += (current_stock[2] / 100) * current_stock[1]
            current_wallet.cost += current_stock[1]
    if current_wallet.benefit > best_wallet.benefit:
        best_wallet = current_wallet
    best_wallet.ratio = round(best_wallet.benefit/best_wallet.cost*100, 2)
    return best_wallet


stocks_list = small_list_stocks
all_csv_stocks = read_files(["data/dataset1_Python.csv", "data/dataset2_Python.csv"])
csv_stocks1 = read_file("data/dataset1_Python.csv")
csv_stocks2 = read_file("data/dataset2_Python.csv")

time = timeit("get_best_wallet(csv_stocks2, 500)", number=1, globals=globals())
final_wallet = get_best_wallet(csv_stocks2, 500)
print("************     Temps d'??x??cution du calcul:     ************\n----------->     %s (secondes)     "
      "<-----------" % round(time, 5))
display_top_wallet(final_wallet, csv_stocks2)
