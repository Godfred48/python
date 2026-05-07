# finding the grade of a student based on the marks obtained
print()
class_score = int(input(" Enter your class score: "))
exams_score = int(input(" Enter your exams score: "))
grade = ''

classScore = class_score / 100 * 30
examsScore = exams_score / 100 * 70
total_score = classScore + examsScore

if total_score >= 90:
    if total_score >= 94:
        grade = "A"
    else:
        grade = "A-"
elif total_score >= 80:
    if total_score >= 87:
        grade = "B+"
    elif total_score < 83:  
        grade = "B-"
    else:
        grade = "B"
elif total_score >= 70:
    if total_score >= 77:
        grade = "C+"
    elif total_score < 73:   
        grade = "C-"
    else:
        grade = "C"
elif total_score >= 60:
    if total_score >= 67:
        grade = "D+"
    elif total_score < 63:   
        grade = "D-"
    else:
        grade = "D"
else:
    grade = "F"

# ✅ fixed: separate pass/fail message
if total_score >= 70:
    print(f"Congratulations, you passed with a Score: {total_score:.1f}  Grade: {grade}")
else:
    print(f"Unfortunately, you failed with a Score: {total_score:.1f}  Grade: {grade}")