def grade_calc(marks=0):
    if marks >= 45 and marks <= 50 :
        return "O "
    elif marks >= 40 and marks <= 44 :
        return "A+"
    elif marks >= 35 and marks <= 39 :
        return "A "
    elif marks >= 30 and marks <= 34 :
        return "B+"
    elif marks >= 25 and marks <= 29 :
        return "B "
    elif marks >= 20 and marks <= 24 :
        return "C+"
    elif marks >= 14 and marks <= 19 :
        return "C "
    elif marks <= 13 :
        return "F "
    else :
        return "Invalid marks"

def point_calc(marks):
    point = 0
    if marks >= 45 and marks <= 50 :
        point = 10
    elif marks >= 40 and marks <= 44 :
        point = 9
    elif marks >= 35 and marks <= 39 :
        point = 8
    elif marks >= 30 and marks <= 34 :
        point = 7
    elif marks >= 25 and marks <= 29 :
        point = 6
    elif marks >= 20 and marks <= 24 :
        point = 5
    elif marks >= 15 and marks <= 19 :
        point = 4
    elif marks >= 10 and marks <= 14 :
        point = 3
    elif marks >= 5 and marks <= 9 :
        point = 2
    elif marks >= 1 and marks <= 4 :
        point = 1
    elif marks < 1 :
        point = 0   
    return point

print("Enter marks of 11 subjects from your semester")
st_marks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for idx in range(11):
    st_marks[idx] = int(input(f"Marks of subject {idx+1}: "))

print("-------------------------------------------------------")
print("                    STUDENT RESULT")
print("")

print("|---------------|-----------|-----------|-------------|")
print("| subject_name  |   marks   |   grade   | grade point |")
print("|---------------|-----------|-----------|-------------|")
for idx in range(11) :
    grade = grade_calc(st_marks[idx])
    point = point_calc(st_marks[idx])
    if idx<9 :
        if point < 10 :
            print(f"|   subject {idx+1}   |     {st_marks[idx]}    |     {grade}    |      {point}      |")
        else :
            print(f"|   subject {idx+1}   |     {st_marks[idx]}    |     {grade}    |     {point}      |")

    else :
        if point < 10 :
            print(f"|   subject {idx+1}  |     {st_marks[idx]}    |     {grade}    |      {point}      |")
        else :
            print(f"|   subject {idx+1}  |     {st_marks[idx]}    |     {grade}    |     {point}      |")     

print("|---------------|-----------|-----------|-------------|")
print("|                                                     |")

total_marks = 0
tot_points = 0

for idx in range(11) :
    total_marks += st_marks[idx]
    point = point_calc(st_marks[idx])
    tot_points += point
    
avg = total_marks // 11
avg_grade = grade_calc(avg)

sgpa = tot_points / 11

print(f"| Total Marks: {total_marks}                                    |")
print(f"| Average Grade: {avg_grade}                                   |")
print(f"| SGPA: {sgpa:.2f}                                          |")
print("|                                                     |")
print("|---------------|-----------|-----------|-------------|")

        
    
