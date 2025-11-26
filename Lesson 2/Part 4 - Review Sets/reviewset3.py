# Question 1:

# It tells us kills is 3,0,5,2,8,1, and also 7. then streaks is blank. and current is 0. Then we get a for loop saying for k in kills, and then an if else statement, when k > 0 current is added to k. and else as in if current is greater than or equal to 5, append the current which means add the current to the end of the string.  so the final print would be giving us 20,8, and 7

# Question 2:

# It tells us that the player is "[NEXUS]" is ShadowVIper. it tells us that tag is empty and i is one. then it also say while player 1, is != tag =+ player 1 and that increases i by 1/ then print tag. if i increases by one that means it will go up to N E X U S. and woudlnt print Stargazer. So the printout should just be NEXUS


# Question 3:

def match_mvp(players):
    best_player = ""
    best_ratio = 0.0
    for name, stats in players.items():
        ratio = stats["kills"] / stats["deaths"]
        if ratio > best_ratio:
            best_ratio = ratio
            best_player = name
    return best_player
        