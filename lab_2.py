# initialization student's name, final quizzes, final research/assignment, final project, and final exam ratings

students_name = ""
final_quizzes = 0
final_research = 0
final_project = 0
final_grade = 0

# getting the  student's name, final quizzes, final research/assignment, final project, and final exam ratings

students_name = input("Students name:")
final_quizzes = float(input("Final quizzes:"))
final_research = float(input("Final research: "))
final_project = float(input("Final project: "))
final_grade = float(input("Final grade: "))


#calculate_final_grade_value
final_grade = 0.30 * final_quizzes + 0.10 * final_research + 0.40 * final_project + 0.40

# the_equivalent_grade(final_grade):
if 98 <= final_grade <= 100:
    remark =  4.00
elif 95 <= final_grade <= 97:
    remark = 3.75
elif 92 <= final_grade <= 94:
    remark =  3.50
elif 89 <= final_grade <= 91:
    remark =  3.25
elif 86 <= final_grade <= 88:
    remark =  3.00
elif 83 <= final_grade <= 85:
    remark  =  2.75
elif 80 <= final_grade <= 82:
    remark = 2.50
elif 77 <= final_grade <= 79:
    remark = 2.25
elif 74 <= final_grade <= 76:
    remark = 2.00
elif 74 <= final_grade <= 76:
    remark =  1.75
elif 68 <= final_grade <= 70:
    remark = 1.50
elif 64 <= final_grade <= 67:
    remark = 1.25
elif 60 <= final_grade <= 63:
    remark = 1.00

else:
     remark = str(" Final grade exceeds 100!")

#display all inputs
print("Student name:", students_name)
print("Final quizzes:", final_quizzes)
print("Final project :", final_project)
print("Final research:", final_research)
print(" Final grade:", final_grade)
print("Remark:", remark)
