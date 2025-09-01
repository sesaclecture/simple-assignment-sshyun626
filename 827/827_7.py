spring = [3.5, 3, 4, 4.5]
fall = [3, 2.8, 3.7, 4.3, 4.1]

semesters = [spring, fall]
semester_names = ["Spring", "Fall"]

print(f"Spring semester grades: {spring}")
print(f"Fall semester grades: {fall}")

total_grades = spring + fall
overall_avg = sum(total_grades) / len(total_grades)
print(f"\nOverall GPA: {overall_avg:.2f}")

print("\n(Highest & Lowest Grades per Semester)")
for i in range(len(semesters)):
    max_score = max(semesters[i])
    min_score = min(semesters[i])
    print(f"{semester_names[i]} -> Max: {max_score}, Min: {min_score}")