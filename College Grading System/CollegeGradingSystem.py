def grade_calc(marks=0):
    if marks > 90 and marks <= 100 :
        return "O "
    elif marks > 80 and marks <= 90 :
        return "A+"
    elif marks > 70 and marks <= 80 :
        return "A "
    elif marks > 60 and marks <= 70 :
        return "B+"
    elif marks > 50 and marks <= 60 :
        return "B "
    elif marks > 40 and marks <= 50 :
        return "C+"
    elif marks >= 33 and marks <= 40 :
        return "C "
    elif marks <= 32 :
        return "F "
    else :
        return "Invalid marks"

print("Enter marks of 5 subjects")
st_marks = [0, 0, 0, 0, 0]
for idx in range(5):
    st_marks[idx] = int(input(f"Marks of subject {idx+1}: "))

print("--------------------------------------------------")
print("STUDENT RESULT")

print("|---------------|-----------|-----------|")
print("| subject_name  |   marks   |   grade   |")
print("|---------------|-----------|-----------|")
for idx in range(5) :
    grade = grade_calc(st_marks[idx])
    print(f"|   subject {idx+1}   |     {st_marks[idx]}    |     {grade}    |")

print("|---------------|-----------|-----------|")
print("|                                       |")

total_marks = 0
for idx in range(5) :
    total_marks += st_marks[idx]
avg = total_marks / 5
avg_grade = grade_calc(avg)
sgpa = total_marks / 50

print(f"| Total Marks: {total_marks}                      |")
print(f"| Average Grade: {avg_grade}                     |")
print(f"| SGPA: {sgpa:.2f}                            |")
print("|                                       |")
print("|---------------|-----------|-----------|")

        
    
