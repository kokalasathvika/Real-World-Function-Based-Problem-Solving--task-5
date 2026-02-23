def detect_duplicates(usernames):
    if len(usernames) != len(set(usernames)):
        result = "Yes"
    else:
        result = "No"
    
    print("Duplicate Accounts Found:", result)

# Example
detect_duplicates(["user1", "user2", "user3", "user1"])