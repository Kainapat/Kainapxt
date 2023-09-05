# Define the credit, grade level, and grade point dictionaries
credits = {"Computer Programming": 3, "Math": 3, "English": 3, "Physic": 3, "Dance": 1, "Electronic": 3}

grade_level = {"A": 90, "B": 80, "C": 70, "D": 60, "F": 0}

grade_point = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}

# Define student marks
students_marks = {
    "John": {"Computer Programming": 80, "Math": 90, "English": 70, "Physic": 50, "Dance": 60, "Electronic": 80},
    "Peter": {"Computer Programming": 85, "Math": 80, "English": 65, "Physic": 60, "Dance": 90, "Electronic": 95},
    "Mary": {"Computer Programming": 45, "Math": 70, "English": 60, "Physic": 65, "Dance": 80, "Electronic": 70},
    "Tom": {"Computer Programming": 80, "Math": 55, "English": 75, "Physic": 70, "Dance": 75, "Electronic": 80},
    "Jane": {"Computer Programming": 90, "Math": 95, "English": 80, "Physic": 75, "Dance": 80, "Electronic": 85}
}

# Calculate GPA for each student
for student, marks in students_marks.items():
    total_credit = 0
    weighted_points = 0
    
    print(student, end=" ")
    
    for subject, mark in marks.items():
        credit = credits.get(subject, 0)
        grade = None
        
        if mark >= grade_level["A"]:
            grade = "A"
        elif mark >= grade_level["B"]:
            grade = "B"
        elif mark >= grade_level["C"]:
            grade = "C"
        elif mark >= grade_level["D"]:
            grade = "D"
        else:
            grade = "F"
        
        total_credit += credit
        weighted_points += credit * grade_point[grade]
        
        print(f"{subject} : {grade}", end=" ")
    
    # Calculate GPA
    gpa = weighted_points / total_credit
    
    print(f"GPA: {gpa:.2f}")
