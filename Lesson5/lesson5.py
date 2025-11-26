try:
    #try something risky
    score = int(input("Enter score: "))
except ValueError:
    #Runs if it FAILED
    print("Invalid Score!")
else:
    #Runs if it SUCCEEDED
    print(f"Score rewarded!")
    

def parse_command(message):
    """Parse a discord command like"""
    try:
        parts = message.split("-")