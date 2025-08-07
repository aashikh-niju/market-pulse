def calculate_daily_returns(prices):
    returns = []
    for i in range(1, len(prices)):
        daily_return = (prices[i] - prices[i - 1]) / prices[i - 1]
        returns.append(round(daily_return, 4))  # rounded to 4 decimal places
    return returns

def calculate_momentum_score(returns):
    if not returns:
        return 0
    avg_return = sum(returns) / len(returns)
    return round(avg_return, 4)
