students = ["John Doe", "Jane Smith", "Alex Johnson", "Emily Davis", "Michael Brown"]
subjects = ["Mathematics", "Science", "English", "History", "Physical Education"]
marks = [
    [85, 90, 78, 82, 88],
    [92, 87, 84, 80, 91],
    [78, 85, 89, 75, 83],
    [88, 92, 81, 79, 86],
    [91, 89, 82, 77, 90]
]
for i in range(len(students)):
    print(f"Student: {students[i]}")
    for j in range(len(subjects)):
        print(f"{subjects[j]}: {marks[i][j]}")
    print()
]