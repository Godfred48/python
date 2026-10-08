def calculate_average(student_list):
        average = sum(student_list) / len(student_list)
        return average

def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def class_report(student_names, student_average):
    for i in range(len(student_average)):
        if student_average[i] == max(student_average):
            best_student = student_names[i]
        if student_average[i] == min(student_average):
            worst_student = student_names[i]

    class_average = sum(student_average) / len(student_average)
    return best_student, worst_student, class_average
            

students = {
    "Kwame": [78, 85, 92, 67, 88],
    "Ama": [90, 91, 89, 95, 94],
    "Kofi": [55, 63, 58, 70, 61],
    "Abena": [82, 76, 85, 80, 79],
    "Yaw": [45, 50, 39, 60, 48]
}

student_names = []
student_average = []

print("Report")
for name, grades in students.items():
    average = calculate_average(grades)
    letter_grade = get_grade(average)

    student_names.append(name)
    student_average.append(average)

    print(name)
    print(f"Average: {average:.1f}")
    print(f"Grade: {letter_grade}")
    print()

best, weakest, class_average = class_report(
    student_names,
    student_average
)

print("==========================")
print(f"Best Student: {best}")
print(f"Weakest Student: {weakest}")
print(f"Class Average: {class_average:.1f}")
print("==========================")

