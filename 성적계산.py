# 학생 수와 과목 수 설정
num_students = 5
num_subjects = 3

# 학생 및 과목 이름 설정
students = ["학생1", "학생2", "학생3", "학생4", "학생5"]
subjects = ["영어", "C-언어", "파이썬"]

grades = []

# 학생별로 성적 입력 받기
for student in students:
    print(student + "의 성적을 입력하세요:")
    student_grades = []
    for subject in subjects:
        grade = float(input(subject + " 성적: "))
        student_grades.append(grade)
    grades.append(student_grades)

# 각 학생의 총점 계산
total_scores = [sum(grade) for grade in grades]

# 등수 계산
rank = [1] * num_students
for i in range(num_students):
    for j in range(num_students):
        if total_scores[i] < total_scores[j]:
            rank[i] += 1

# 학생별로 성적, 총점, 등수, 평균, 학점 출력
print("학생\t", end="")
for subject in subjects:
    print(subject + "\t", end="")
print("총점\t평균\t학점\t등수")

def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

for i in range(num_students):
    print(students[i] + "\t", end="")
    total_grade = 0
    for j in range(num_subjects):
        print(str(grades[i][j]) + "\t", end="")
        total_grade += grades[i][j]
    average_grade = total_grade / num_subjects
    total_score = total_scores[i]
    grade = calculate_grade(average_grade)
    print("{:.2f}\t{:.2f}\t{}\t{}".format(total_score, average_grade, grade, rank[i]))
