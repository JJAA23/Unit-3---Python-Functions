# using Keyword Arguments
def create_gamer(username, level, xp, rank, online):
    '''Create a gamer profile.'''
    return {
        "username": username,
        "level": level,
        "xp": xp,
        "rank": rank,
        "online": online
    }
    
player1 = create_gamer(username = "BigDihRandy", 
                       level = "67",
                       rank = "Silver",
                       xp = "67676767676767",
                       online = True)

def send_message(sender, recipient, message, urgent):
    return {
        "sender" : sender,
        "recipient": recipient,
        "message": message,
        "urgent": urgent,
    }
    
message1 = send_message(sender = "Alex",
                       recipient = "Jordan",
                       message = "Check Discord",
                       urgent = True)

print(message1)

def post_content(username, text, likes = 0, retweets = 0):
    return {
    "username": username,
    "text": text,
    "likes": 0,
    "retweets": 0
}
    
content1 = post_content( username = "techguru",
                        text = "Randydagoat",
                        likes = "0",
                        retweets = "0")

print(content1)
     
    
    
print(content1)
     
    

     
    
    