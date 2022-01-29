import itertools

from data.actions import actions


def get_best_wallet(actions, capital):
    actions.sort(key=lambda x: x[1])
    highest_cost = actions[-1][1]

    best_wallet = [[], 0, 0]

    for evaluated_action in range(0, len(actions)+1):
        wallets_combination = itertools.combinations(actions, evaluated_action)
        for combination in wallets_combination:
            allocated_capital = capital
            combination_benefit = 0
            for current_action in combination:
                allocated_capital -= current_action[1]
            if 0 <= allocated_capital < highest_cost:
                for profitable_action in combination:
                    combination_benefit += (profitable_action[2]/100)*profitable_action[1]
                if combination_benefit > best_wallet[1]:
                    best_wallet = [combination, combination_benefit]
    return best_wallet


def get_wallet_invest_cost(actions):
    invest_cost = 0
    for action in actions:
        invest_cost += action[1]
    return invest_cost


best = get_best_wallet(actions,500)
invest = get_wallet_invest_cost(best[0])

print("Somme investie : %s€." % invest)
print("Bénéfices attendus /2ans : %s€." % best[1])
print("Rentabilité : %s%%." % (round(((best[1]/invest)*100),2)))
print("Pour %s actions acquises." % len(best[0]))
if input("\n************     1 = Afficher liste des actions     ************\n") == str(1):
    for action in best[0]:
        summary = "Nom : %s, Prix/Cout : %s, Bénéfices attendus : %s" % (action[0], action[1], action[2])
        print(summary)
