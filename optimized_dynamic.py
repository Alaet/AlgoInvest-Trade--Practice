import csv
from data.actions import actions as small_list_actions
from wallet.view import display_top_wallet
from wallet.model import Wallet
import time

timer = time.time()


def read_files(files_names):
    actions_list = []
    for file_name in files_names:
        file = open(file_name)
        csvreader_file = csv.reader(file)
        for action_row in csvreader_file:
            if action_row[1] != "price":
                action_row[1] = float(action_row[1])
                action_row[2] = float(action_row[2])
                if action_row[1] > 0 and action_row[2] > 0:
                    actions_list.append(action_row)
    return actions_list


def read_file(file_name):
    actions_list = []
    file = open(file_name)
    csvreader_file = csv.reader(file)
    for action_row in csvreader_file:
        if action_row[1] != "price":
            action_row[1] = float(action_row[1])
            action_row[2] = float(action_row[2])
            if action_row[1] > 0 and action_row[2] > 0:
                actions_list.append(action_row)
    return actions_list


def get_best_wallet(actions, capital):
    import math
    best_wallet = Wallet([])
    capital_invest = capital
    col = len(actions)
    Matrix = [[0 for row in range(capital_invest+1)] for column in range(col+1)]
    stock_price, stock_name = actions[1], actions[0]
    for i_column in range(1, col + 1):
        for j_row in range(1, capital_invest + 1):
            best_price = math.trunc(actions[i_column - 1][1])
            if best_price <= j_row:
                Matrix[i_column][j_row] = max(
                    (actions[i_column - 1][2]/100*actions[i_column - 1][1])+Matrix[i_column - 1][j_row - best_price],
                    Matrix[i_column - 1][j_row])
            else:
                Matrix[i_column][j_row] = Matrix[i_column - 1][j_row]

    while col > 1:
        stock = actions[col - 1]
        capital_invest = math.trunc(capital_invest)
        if Matrix[col][capital_invest] == Matrix[col - 1][capital_invest - math.trunc(stock[1])] + (stock[
                                                                                                      2]/100)*stock[1]:
            best_wallet.actions.append(stock_name)
            capital_invest -= stock[1]
            best_wallet.cost += stock[1]
        col -= 1
    best_wallet.benefit = Matrix[-1][-1]
    best_wallet.ratio = round(best_wallet.benefit/best_wallet.cost*100, 2)
    print("************     Temps d'éxécution du calcul:"
          "     ************\n----------->     %s " % (time.time() - timer))
    display_top_wallet(best_wallet, all_csv_actions)


list_actions = small_list_actions
all_csv_actions = read_files(["data/dataset1_Python.csv", "data/dataset2_Python.csv"])
csv_actions1 = read_file("data/dataset1_Python.csv")
csv_actions2 = read_file("data/dataset2_Python.csv")
get_best_wallet(all_csv_actions, 500)
