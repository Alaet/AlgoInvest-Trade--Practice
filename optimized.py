import csv


def read_files(files_names):
    actions = []
    for file_name in files_names:
        file = open(file_name)
        csvreader_file = csv.reader(file)
        for action in csvreader_file:
            if action[1] != "price":
                action[1] = (action[1])
                action[2] = (action[2])
                if float(action[1]) > 0 and float(action[2]) > 0:
                    actions.append(action)
    return actions


actions = read_files(["data/dataset1_Python.csv", "data/dataset2_Python.csv"])


def calcul_wallet_benefit(actions):
    benefit_best_wallet = 0
    for act in actions:
        benefit_best_wallet += (act[2] / 100) * act[1]
    return benefit_best_wallet


def get_best_wallet(actions, capital):
    i = 0
    actions.sort(key=lambda x:x[2], reverse=True)
    best_wallet = []

    while i <= capital:
        allocated_capital = i
        current_wallet = []

        current_wallet_benefit = 0
        for current_action in actions:
            if current_action[1] <= allocated_capital:
                current_wallet.append(current_action)
                allocated_capital -= current_action[1]
                current_wallet_benefit += (current_action[2]/100)*current_action[1]

        benefit = calcul_wallet_benefit(best_wallet)

print(actions)