# Question 1:
#  The vierwers are 1240, 1580, 2100, 1890 and alsi 2300. thenm peak takes the first id in viewers which is 1240.. meaning peak = 1240. The i = 1. and while 1 < length of viewerswhich would be 4, if viewers is 4, because the lenght of the first index has 4 printed. it keeps checking all the ids in viewers until it gets to 2300/. meaning the code would print 2300.

# Question 2:
# The message is wow poggers wow lfg with a few capitals i didnt put in, but ill edplainit as we go on/. it then says words = message.split which would be splitting the message in half. filtered = "" meaning that it has to be defined yet. then we get a for loop sayign if word in words and if the length of word is <= 15 filtered wpould then be word + ""/ thyen the final print would be giving us WOW WOW LFG

# Question 3:

def find_top_donor(donations):
    top_name = ""
    top_amount = -1
    for name, amount in donations.items():
        if amount > top_amount:
            top_amount = amount
            top_name = name 
        return top_name