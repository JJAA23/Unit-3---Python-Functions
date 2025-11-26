# Question 1

# It gives us the prices and it also tell us that the gajns are nothing meanign they have to be filled in. ajand while i is less than the length of  prices.  anmd thenm if the difference is greater than a set number ti prints out gains. meanign the outputs would be 3 and 6700.


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Question 2:

# It tells us that wallet = "......." and it also gives us that short is blank. and it alsogives us that i = 0 so it has to be filled out.the output is the wallet. soo it woul;d ptrint the string in the wallet.

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Question 3:

def portfolio_value(holdings,prices):
    total = 0.0
    for coin, amount in holdings:
        total += amount * prices[coin]
        return round(total,2)