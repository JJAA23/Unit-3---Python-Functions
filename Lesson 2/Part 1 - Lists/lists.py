# index [0] for javascript and python
# # slice .slice(start,end) [start:end]
# length len.list
# 

daily_likes = [500,600,650,400]
usernames = ["@nasa", "@netflix", "@tswift"]
mixed_data = [500,"likes", "@user123", True]
# Accesing Elements
first_day = daily_likes[0]
last_day = daily_likes[-1]
third_day = daily_likes[2]

# # Information
# length = len(engagements)
# maximum = max(engagements)
# minimum = min(engagements)
# total = sum(engagements)

# Code along - post analyzer
def analyze_post(likes_list):
    if likes_list:
        total = sum(likes_list)
        average = total / len(likes_list)
        best_day = max(likes_list)
        return (average, best_day)
    return "The list is empty!"

def format_usernames(handles):
    formatted = []
    for handle in handles:
        formatted.append("@" + handle)
    return formatted

result = format_usernames(["nasa", "tswift", "netflix"])
print(result)

def filter_trending_posts(likes_list):
    filter_trending_posts = []
    
    if likes_list > 100:
        return likes_list
    


def filter_events(numbers):
    even = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
#             return num
        
# def list_stats(numbers):
#     for num in numbers:4
#         if not numbers:


def create_username(first_name, last_name):
    combined_username = first_name + last_name
    return combined_username.lower()
    

def check_email(email):
    email = input("Enter an email: ")
    if "@" in email.lower and (".com"):
        return True
    else:
        return False
    

def create_slug(title):
    changed_title = title.lower() and title.append() 
    
