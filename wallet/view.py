def display_top_wallet(top_wallet, actions):
    display_invested_amount(top_wallet.cost)
    display_benefit(top_wallet.benefit)
    display_profitability(top_wallet.ratio)
    print("Pour %s actions acquises." % len(top_wallet.actions))
    print(("Et %s actions scannées" % len(actions)))
    display_top_wallet_actions(top_wallet.actions)


def display_invested_amount(invest):
    print("Somme investie : %s€." % round(invest, 2))


def display_benefit(benefit):
    print("Bénéfices attendus /2ans : %s€." % round(benefit, 2))


def display_profitability(wallet_ratio):
    print("Rentabilité : %s%%." % wallet_ratio)


def display_top_wallet_actions(wallet):
    wallet.sort(key=lambda x: x[1], reverse=True)
    if input("\n************    1 = Afficher liste des actions     ************\n") == str(1):
        for action in wallet:
            action_summary = "Nom : %s, Prix/Cout : %s, Bénéfices attendus /2ans : %s%% (%s€)" % (action[0],
                                                                                                  float(action[1]),
                                                                                                  float(action[2]),
                                                                                                  round((float(action[
                                                                                                             2])/100)
                                                                                                  *
                                                                                                  action[1], 2))
            print(action_summary)
