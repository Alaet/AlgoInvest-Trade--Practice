import csv
from data.actions import actions as small_list_actions
from wallet.view import display_top_wallet
from wallet.model import Wallet
import time


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


def get_wallet_benefit(actions_to_evaluate):
    benefit_best_wallet = 0
    for act in actions_to_evaluate:
        benefit_best_wallet += (act[2] / 100) * act[1]
    return benefit_best_wallet


def get_wallet_invest_cost(actions_to_evaluate):
    wallet_investment = 0
    for act in actions_to_evaluate:
        wallet_investment += act[1]
    return wallet_investment


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
            current_wallet.cost = get_wallet_invest_cost(current_wallet.actions)
    if current_wallet.benefit > best_wallet.benefit:
        best_wallet = current_wallet
    return best_wallet


list_actions = small_list_actions
all_csv_actions = read_files(["data/dataset1_Python.csv", "data/dataset2_Python.csv"])
csv_actions1 = read_file("data/dataset1_Python.csv")
csv_actions2 = read_file("data/dataset2_Python.csv")
timer = time.time()
wallet = get_best_wallet(all_csv_actions, 500)

print("************     Temps d'éxécution du calcul:"
      "     ************\n----------->     %s seconde(s)" % (time.time()-timer))
display_top_wallet(wallet, all_csv_actions)

