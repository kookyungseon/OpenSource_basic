 # 학생 수와 과목 수 설정
num_students = 5
num_subjects = 3

# 과목 이름 설정
subjects = ["영어", "C-언어", "파이썬"]

# 각 학생의 과목별 성적과 이름을 저장할 딕셔너리 생성
students_grades = {}

# 학생별로 성적과 이름 입력 받기
student_index = 0
while student_index < num_students:
    student_name = input("학생의 이름을 입력하세요: ")
    student_number = input(student_name + "의 학번을 입력하세요: ")
    print(student_name + "의 성적을 입력하세요:")
    student_grades = []
    subject_index = 0
    while subject_index < num_subjects:
        grade = float(input(subjects[subject_index] + " 성적: "))
        student_grades.append(grade)
        subject_index += 1
    students_grades[student_name] = {"학번": student_number, "성적": student_grades}
    student_index += 1

# 각 학생의 총점 계산
total_scores = {name: sum(data["성적"]) for name, data in students_grades.items()}

# 등수 계산
rank = {name: 1 for name in total_scores}
for name, score in total_scores.items():
    for other_name, other_score in total_scores.items():
        if score < other_score:
            rank[name] += 1

# 학생별로 성적, 총점, 등수, 평균, 학점 출력
print("\n성적표:")
print("학생\t학번\t", end="")
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

for name, data in students_grades.items():
    print(name + "\t" + data["학번"] + "\t", end="")
    total_grade = sum(data["성적"])
    average_grade = total_grade / num_subjects
    total_score = total_scores[name]
    grade = calculate_grade(average_grade)
    print("\t".join([str(grade) for grade in data["성적"]]) + "\t{:.2f}\t{:.2f}\t{}\t{}".format(total_score, average_grade, grade, rank[name]))
