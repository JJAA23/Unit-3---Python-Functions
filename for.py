def search_data(query):
    if query == "":
        return None
    if query == "empty":
        return 0
    if query == "error":
        return False
    return len(query)

# Return Type - None - "No Value"
# Meaning: Absense of value, not set, not found
# Use for: Missing data, search failure, optional parameters
result = None
print(result is None) #True - Identity Check
print(result == None) #True - Equality Check
print(not result)     #True - Falsly Check

# 2 Return Type - False = Boolean False
# Meaning - Explicit False Condition, Validation Failure, Negative Result
# Use for: Validation Result, Boolean Operations, Success/Failure status.
result = False
print(result is False) #True - Identity Check
print(not result)      #True - Boolean Negation
print(result == 0)     #True - Falsy Check

# 3 Return Zero - A Valid Number
# Zero is VALID numeric value, not absense of value!
result = 0
print(result == 0)      #True - Numeric Equality
print(not result)       #True - Falsy Check
print(result is None)   #False - Different Object
print(result is False)  #False - Different Types


# multiple returns - pthon packs multiple returns into a tuple!
def calculate_room(length,width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter #Turns into a tupke(area,perimeter)

result = calculate_room(10,5)
print(result)
print(type(result))

print(type((42)))#int
print(type((42,)))#tuple for single item
print(type(1,2,3))



# Student Grade Analyzer:

def analyze_grades(grades):
    """ Returns Avg, High, Low, Passed
        If no grades, return 000
    """
    if not grades:
        return 0,0,0, False
    average = sum(grades)
    
    
    