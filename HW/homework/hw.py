# question 5: code tracing

# answer: 18,15

# Question #6 - Code Writing

def make_notification(user, *messages, urgent=False):
    message = " ".join(messages)
    result = f"{user} - {message}"
    if urgent:
        result = "URGENT : " + result
        return result
   
print(make_notification("admin","Server down!", urgent=True))

# question 7 - code tracing

# answer: SELECT name, email FROM users LIMIT 10

# question 8: code writing

def log_action(actor, *actions, timestamp=None, **context):
    action_str = ", ".join(actions)
    parts = [f"{actor}: {action_str}"]
    for key, value in context.items():
        parts.append(f"{key}={value}")
    return " | ".join(parts)
