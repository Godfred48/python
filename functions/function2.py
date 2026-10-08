def find_student(student_name, student_list):
    for student in student_list:
        if student == student_name:
            return f"{student_name} was found!"

    return f"{student_name} not Found!"

students = ["John", "Mary", "David", "Sarah"]

student_entry = input("Enter student name: ")
result = find_student(student_entry, students)
print(result)



