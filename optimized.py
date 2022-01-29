import csv


def read_files(files_names):
    actions = []
    for file_name in files_names:
        file = open(file_name)
        csvreader_file = csv.reader(file)
        for action in csvreader_file:
            if action[1] != "price":
                action[1] = float(action[1])
                action[2] = float(action[2])
                if action[1] > 0 and action[2] > 0:
                    actions.append(action)
    return actions


actions = read_files(["data/dataset1_Python.csv", "data/dataset2_Python.csv"])


def get_wallet_benefit(actions):
    benefit_best_wallet = 0
    for act in actions:
        benefit_best_wallet += (act[2] / 100) * act[1]
    return benefit_best_wallet


def get_wallet_invest_cost(actions):
    invest = 0
    for act in actions:
        invest += act[1]
    return invest


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

        benefit = get_wallet_benefit(best_wallet)
        if current_wallet_benefit > benefit and len(current_wallet) > 0:
            best_wallet = current_wallet
        i += 1

    return best_wallet


wallet = get_best_wallet(actions, 500)
benefit_wallet = get_wallet_benefit(wallet)
invest = get_wallet_invest_cost(wallet)

print("Somme investie : %s€." % round(invest, 2))
print("Bénéfices attendus /2ans : %s€." % round(benefit_wallet, 2))
print("Rentabilité : %s%%." % (round((benefit_wallet/invest)*100,2)))
print("Pour %s actions acquises." % len(wallet))
if input("\n************     1 = Afficher liste des actions     ************\n") == str(1):
    for action in wallet:
        summary = "Nom : %s, Prix/Cout : %s, Bénéfices attendus : %s" % (action[0], float(action[1]), float(action[2]))
        print(summary)
