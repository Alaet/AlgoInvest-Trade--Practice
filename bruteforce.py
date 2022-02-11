import itertools
from timeit import timeit
from wallet.view import display_top_wallet
from data.actions import stocks as small_stocks_list
from wallet.model import Wallet


def get_best_wallet(stocks, capital):
    """
    Take a list of stock and maximum capital to return the best profitable wallet,
    By generating every possible combination between stocks,
    Then, will calcul every combination cost and benefit and cache the one that have the best benefit until a new
    one is found or combination list ended.
    :param stocks: list[
                        [stock_name,
                         stock_price,
                         stock_percent_profitability]
                        ]
    :param capital: int
    :return: None
    """
    stocks.sort(key=lambda x: x[1])
    highest_cost = stocks[-1][1]
    best_wallet = Wallet([])

    for tested_stock in range(0, len(stocks) + 1):
        wallets_combination = itertools.combinations(stocks, tested_stock)
        for combination in wallets_combination:
            allocated_capital = capital
            combination_benefit = 0
            for current_stock in combination:
                allocated_capital -= current_stock[1]
            if 0 <= allocated_capital < highest_cost:
                for profitable_stock in combination:
                    combination_benefit += (profitable_stock[2]/100)*profitable_stock[1]
                if combination_benefit > best_wallet.benefit:
                    best_wallet.stocks = list(combination)
                    best_wallet.benefit = combination_benefit
                    best_wallet.cost = get_wallet_invest_cost(best_wallet.stocks)

    best_wallet.ratio = round(best_wallet.benefit / best_wallet.cost * 100, 2)

    return best_wallet


def get_wallet_invest_cost(stocks):
    """
    Take a list of stock and return the sum of their cost.
    :param stocks: list[
                        [stock_name,
                         stock_price,
                         stock_percent_profitability]
                        ]
    :return: int
    """
    invest_cost = 0
    for action in stocks:
        invest_cost += action[1]
    return invest_cost


time = timeit("get_best_wallet(stocks, 500)", setup="from data.actions import stocks", number=1, globals=globals())
final_wallet = get_best_wallet(small_stocks_list, 500)
print("************     Temps d'éxécution du calcul:     ************\n----------->     %s " % time)
display_top_wallet(final_wallet, small_stocks_list)
