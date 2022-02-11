import csv
from data.actions import stocks as small_stocks_list
from wallet.view import display_top_wallet
from wallet.model import Wallet
from timeit import timeit


# region CSV READ FUNCTION


def read_files(files_names):
    """
    Take a list of csv file path to return csv files data's as a single list
    :param files_names: list[path,*]
    :return: list[csv_files_datas]
    """
    file_stocks_list = []
    for file_name in files_names:
        file = open(file_name)
        csvreader_file = csv.reader(file)
        for action_row in csvreader_file:
            if action_row[1] != "price":
                action_row[1] = round(float(action_row[1]))
                action_row[2] = round(float(action_row[2]))
                if action_row[1] > 0 and action_row[2] > 0:
                    file_stocks_list.append(action_row)
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
    for action_row in csvreader_file:
        if action_row[1] != "price":
            action_row[1] = round(float(action_row[1]))
            action_row[2] = round(float(action_row[2]))
            if action_row[1] > 0 and action_row[2] > 0:
                file_stock_list.append(action_row)
    return file_stock_list


# endregion

def calculate_stock_benefit(stocks):
    """
    Take a list of stock and for each stock will add the profitability for it to it
    (stock_percent_profitability/100*stock_price)
    :param stocks: list[
                        [stock_name,
                         stock_price,
                         stock_percent_profitability]
                        ]
    :return: list[
                        [stock_name,
                         stock_price,
                         stock_percent_profitability,
                         stock_profitability]
                        ]
    """
    for stock in stocks:
        benef = stock[2]/100*stock[1]
        stock.append(benef)
    return stocks


def get_best_wallet(stocks, capital):
    """
    Take list of stock and maximum capital to return the most profitable wallet possible.
    By using Knapsack dynamic approach, will set a matrix with each possibility of capital investment as row,
    and number of stocks as line.
    Will then search through existing result for the best combination based on profitability and capital invested.
    :param stocks: list[
                        [stock_name,
                         stock_price,
                         stock_percent_profitability]
                        ]
    :param capital: int
    :return: None
    """

    calculate_stock_benefit(stocks)
    best_wallet = Wallet([])
    number_of_stocks = len(stocks)
    Matrix = [[0 for x in range(capital+1)] for x in range(number_of_stocks+1)]
    for i in range(1, number_of_stocks + 1):
        for j in range(1, capital + 1):
            if stocks[i - 1][1] <= j:
                Matrix[i][j] = max(stocks[i - 1][3] + Matrix[i - 1][j - stocks[i - 1][1]], Matrix[i - 1][j])
            else:
                Matrix[i][j] = Matrix[i - 1][j]

    while capital >= 0 and number_of_stocks >= 0:
        if Matrix[number_of_stocks][capital] != Matrix[number_of_stocks - 1][capital]:
            best_wallet.stocks.append(stocks[number_of_stocks - 1])
            best_wallet.benefit += stocks[number_of_stocks - 1][3]
            best_wallet.cost += stocks[number_of_stocks - 1][1]
            capital -= stocks[number_of_stocks - 1][1]
        number_of_stocks -= 1

    best_wallet.ratio = round(best_wallet.benefit/best_wallet.cost*100, 2)

    return best_wallet


stocks_list = small_stocks_list
all_csv_stocks = read_files(["data/dataset1_Python.csv", "data/dataset2_Python.csv"])
csv_stocks1 = read_file("data/dataset1_Python.csv")
csv_stocks2 = read_file("data/dataset2_Python.csv")

time = timeit("get_best_wallet(csv_stocks2, 500)", number=1, globals=globals())
final_wallet = get_best_wallet(csv_stocks2, 500)
print("************     Temps d'éxécution du calcul:     ************\n----------->     %s " % time)
display_top_wallet(final_wallet, csv_stocks2)
