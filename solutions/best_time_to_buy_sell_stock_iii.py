def max_profit(prices: list[int]) -> int:
    # We track 4 states simultaneously as we scan prices left to right.
    # Each state represents the best possible bank balance at that stage of the game.

    # hold1: best outcome after buying once but not yet selling
    # We start at negative infinity because we haven't bought anything yet —
    # any real purchase will be better than this placeholder.
    hold1 = float('-inf')

    # sold1: best profit after completing exactly one full buy-sell transaction
    # Starts at 0 because before any trade, profit is zero (we did nothing)
    sold1 = 0

    # hold2: best outcome after completing one trade AND buying a second time
    # Starts at negative infinity for the same reason as hold1 — no purchase yet
    hold2 = float('-inf')

    # sold2: best profit after completing both transactions (this is our final answer)
    # Starts at 0 because before any trade, profit is zero
    sold2 = 0

    # Walk through every price one day at a time — O(n), one pass
    for price in prices:

        # Update hold1: should I buy today for the first time?
        # -price means "I spent 'price' dollars today to buy the stock"
        # We keep whichever is better: buying today (-price) or what we had before (hold1)
        hold1 = max(hold1, -price)

        # Update sold1: should I sell today to close my first trade?
        # hold1 + price means "take my best first-buy position and sell at today's price"
        # We keep whichever is better: selling today or our previous best sold1
        sold1 = max(sold1, hold1 + price)

        # Update hold2: should I buy again today for the second trade?
        # sold1 - price means "take the cash from my first sale and spend 'price' to buy again"
        # We keep whichever is better: buying today or what we had before (hold2)
        hold2 = max(hold2, sold1 - price)

        # Update sold2: should I sell today to close my second trade?
        # hold2 + price means "take my best second-buy position and sell at today's price"
        # We keep whichever is better: selling today or our previous best sold2
        sold2 = max(sold2, hold2 + price)

    # sold2 is the maximum profit from at most two completed transactions
    # If no profitable trade existed, all updates leave it at 0 — correct per the problem
    return sold2
