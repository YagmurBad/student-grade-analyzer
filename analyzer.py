import csv

grades = []
students = []

with open("grades.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["name"]
        grade = int(row["grade"])

        students.append(name)
        grades.append(grade)

average = sum(grades) / len(grades)
highest = max(grades)
lowest = min(grades)

passed = [g for g in grades if g >= 50]
failed = [g for g in grades if g < 50]

print("Student Grade Analyzer")
print("----------------------")
print("Total students:", len(students))
print("Average grade:", round(average, 2))
print("Highest grade:", highest)
print("Lowest grade:", lowest)
print("Passed:", len(passed))
print("Failed:", len(failed))