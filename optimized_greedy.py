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
    actions.sort(key=lambda x: x[2], reverse=True)
    best_wallet = Wallet([])
    allocated_capital = capital
    current_wallet = Wallet([])
    for current_action in actions:
        if current_action[1] <= allocated_capital:
            current_wallet.actions.append(current_action)
            allocated_capital -= current_action[1]
            current_wallet.benefit += (current_action[2] / 100) * current_action[1]
            current_wallet.cost += current_action[1]
    if current_wallet.benefit > best_wallet.benefit:
        best_wallet = current_wallet
    print("************     Temps d'éxécution du calcul:"
          "     ************\n----------->     %s " % (time.time() - timer))
    best_wallet.ratio = round(best_wallet.benefit/best_wallet.cost*100, 2)
    display_top_wallet(best_wallet, all_csv_actions)


list_actions = small_list_actions
all_csv_actions = read_files(["data/dataset1_Python.csv", "data/dataset2_Python.csv"])
csv_actions1 = read_file("data/dataset1_Python.csv")
csv_actions2 = read_file("data/dataset2_Python.csv")
get_best_wallet(all_csv_actions, 500)
