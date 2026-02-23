def check_transaction(amount):
    daily_limit = 50000
    
    if amount <= daily_limit:
        status = "Approved"
    else:
        status = "Rejected"
    
    print("Transaction Amount:", amount)
    print("Transaction Status:", status)

# Example
check_transaction(60000)