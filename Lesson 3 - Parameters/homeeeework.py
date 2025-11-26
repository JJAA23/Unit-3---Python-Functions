# Question 1:

def search_user_database(query):
    """
    Processes a user search query and returns:
      - result  (None, False, 0, or positive integer)
      - message (string)
      - success (boolean)
    """

    # 1. Handle empty or whitespace-only queries
    if not query or query.strip() == "":
        return None, "Query is empty.", False

    # 2. Validate characters (only allow alphabetic + spaces)
    if not all(ch.isalpha() or ch.isspace() for ch in query):
        return False, "Query contains invalid characters.", False

    # --- Simulated database lookup ---
    # Example dataset of usernames
    user_db = ["alice", "bob", "charlie", "bobette", "alicia"]

    # Perform case-insensitive substring search
    query_lower = query.lower()
    matches = [u for u in user_db if query_lower in u]

    count = len(matches)

    # 3. Return 0 if valid but no users found
    if count == 0:
        return 0, "No users found.", True

    # 4. Return positive integer when matches found
    return count, f"Found {count} user(s).", True

# Question 2:
