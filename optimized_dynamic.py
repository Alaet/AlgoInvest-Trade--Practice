import csv
import math
from data.actions import stocks as small_stocks_list
from wallet.view import display_top_wallet
from wallet.model import Wallet
import time

timer = time.time()


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
                action_row[1] = float(action_row[1])
                action_row[2] = float(action_row[2])
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
            action_row[1] = float(action_row[1])
            action_row[2] = float(action_row[2])
            if action_row[1] > 0 and action_row[2] > 0:
                file_stock_list.append(action_row)
    return file_stock_list


def get_best_wallet(stocks, capital):
    """
    Take list of stock and maximum capital to return, one, of the most profitable wallet possible.
    By using Knapsack dynamic approach, will set a matrix with capital as W(eight), and V(alue) being the
    profitability for each stock.
    After rentability of a given stock for every given capital, will search from end of the matrix the best values,
    add them to an object(Wallet()) and therefore, stocks that were included based on precedent cell values and so
    on until max value is found.
    :param stocks: list[
                        [stock_name,
                         stock_price,
                         stock_percent_profitability]
                        ]
    :param capital: int
    :return: None
    """
    best_wallet = Wallet([])
    capital_invest = capital
    col = len(stocks)
    Matrix = [[0 for row in range(capital_invest+1)] for column in range(col+1)]
    stock_name = stocks[0]
    for i_column in range(1, col + 1):
        for j_row in range(1, capital_invest + 1):
            best_price = math.trunc(stocks[i_column - 1][1])
            if best_price <= j_row:
                Matrix[i_column][j_row] = max(
                    (stocks[i_column - 1][2] / 100 * stocks[i_column - 1][1]) + Matrix[i_column - 1][j_row -
                                                                                                     best_price],
                    Matrix[i_column - 1][j_row])
            else:
                Matrix[i_column][j_row] = Matrix[i_column - 1][j_row]

    while col > 1:
        stock = stocks[col - 1]
        capital_invest = math.trunc(capital_invest)
        if Matrix[col][capital_invest] == Matrix[col - 1][capital_invest - math.trunc(stock[1])] \
                + (stock[2]/100)*stock[1]:
            best_wallet.stocks.append(stock_name)
            capital_invest -= stock[1]
            best_wallet.cost += stock[1]
        col -= 1
    best_wallet.benefit = Matrix[-1][-1]
    best_wallet.ratio = round(best_wallet.benefit/best_wallet.cost*100, 2)
    print("************     Temps d'éxécution du calcul:"
          "     ************\n----------->     %s " % (time.time() - timer))
    display_top_wallet(best_wallet, all_csv_stocks)


stocks_list = small_stocks_list
all_csv_stocks = read_files(["data/dataset1_Python.csv", "data/dataset2_Python.csv"])
csv_stocks1 = read_file("data/dataset1_Python.csv")
csv_stocks2 = read_file("data/dataset2_Python.csv")
get_best_wallet(all_csv_stocks, 500)
