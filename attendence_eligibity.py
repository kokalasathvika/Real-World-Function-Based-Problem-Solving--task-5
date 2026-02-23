def check_attendance(attendance_list):
    total_classes = len(attendance_list)
    attended = 0
    
    for status in attendance_list:
        if status == "Present":
            attended += 1
    
    percentage = (attended / total_classes) * 100
    
    if percentage >= 75:
        eligibility = "Eligible"
    else:
        eligibility = "Not Eligible"
    
    print("Attendance Percentage:", percentage)
    print("Exam Eligibility:", eligibility)

# Example
check_attendance(["Present", "Present", "Absent", "Present", "Present"])