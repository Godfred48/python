"""Create a new dictionary averages where each key is a student’s name and each value is their average score, rounded to 1 decimal place.
Find and print the student with the highest average.
Create a dictionary grades that maps each student to a letter grade based on their average: 80+ is “A”, 70-79 is “B”, 60-69 is “C”, below 60 is “F”.
Add a new student, “Abena”, with scores [77, 81, 69], and update averages and grades to include her."""

scores = {

    "Ama": [85, 90, 78],
    "Kofi": [60, 72, 65],
    "Efua": [92, 88, 95],
    "Yaw": [45, 58, 50],
}
averages = {}

def main():
    for key, value in scores.items():
        average = max(value)/len(value)#find average
        averages[key] = round(average, 1) # average and key inserted into average dict
        student = max(averages, key=averages.get) #get student with max average 
        score = averages[student] #retieve the score
    print(averages)
    print(f"The higest average score is {score} by {student}")


if __name__ == "__main__":
    main()