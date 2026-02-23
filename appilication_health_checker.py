def check_application_health(errors):
    if errors == 0:
        status = "Healthy"
    elif errors <= 5:
        status = "Minor Issues"
    else:
        status = "Critical Issues"
    
    print("Error Count:", errors)
    print("System Status:", status)

# Example
check_application_health(7)