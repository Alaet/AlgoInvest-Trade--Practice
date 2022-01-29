import itertools
import time
from view.view import display_top_wallet
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


def get_wallet_benefit(actions_to_evaluate):
    benefit_best_wallet = 0
    for act in actions_to_evaluate:
        benefit_best_wallet += (act[2] / 100) * act[1]
    return benefit_best_wallet


def get_wallet_invest_cost(actions):
    invest_cost = 0
    for action in actions:
        invest_cost += action[1]
    return invest_cost


timer = time.time()
best = get_best_wallet(actions, 500)
print("************     Temps d'éxécution du calcul:     ************\n----------->     %s seconde(s)" % (
        time.time()-timer))
invest = get_wallet_invest_cost(best[0])
benefit = get_wallet_benefit(best[0])
display_top_wallet(invest, benefit, best[0], actions)
