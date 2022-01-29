def display_top_wallet(invest, benefit, top_wallet, actions):
    display_invested_amount(invest)
    display_benefit(benefit)
    display_profitability(benefit, invest)
    print("Pour %s actions acquises." % len(top_wallet))
    print(("Et %s actions scannées" % len(actions)))
    display_top_wallet_actions(top_wallet)


def display_invested_amount(invest):
    print("Somme investie : %s€." % round(invest, 2))


def display_benefit(benefit):
    print("Bénéfices attendus /2ans : %s€." % round(benefit, 2))


def display_profitability(benefit, invest):
    print("Rentabilité : %s%%." % (round((benefit / invest) * 100, 2)))


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
