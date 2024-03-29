def t_score(grades):
    return sum(grades)

def average(total_score, num_subjects):  # 수정된 부분
    return total_score / num_subjects

def cal_rank(scores):
    s_scores = sorted(scores, reverse=True)
    rank_dict = {score: i + 1 for i, score in enumerate(s_scores)}
    return rank_dict

def grade_report(num_students, num_subjects, subjects):
    students_grades = []

    for _ in range(num_students):
        student_name = input("학생의 이름을 입력하세요: ")
        student_number = input(student_name + "의 학번을 입력하세요: ")
        print(student_name + "의 성적을 입력하세요:")
        student_grades = [float(input(subject + " 성적: ")) for subject in subjects]
        total_score = t_score(student_grades)
        avg_grade = average(total_score, num_subjects)  # 수정된 부분
        grade = calculate_grade(avg_grade)
        students_grades.append((student_name, student_number, student_grades, total_score, avg_grade, grade))

    total_scores = [student[3] for student in students_grades]
    rank_dict = cal_rank(total_scores)

    print("\n성적표:")
    print("학생\t학번\t", end="")
    for subject in subjects:
        print(subject + "\t", end="")
    print("총점\t평균\t학점\t등수")

    for student in students_grades:
        rank = rank_dict[student[3]]
        print("{}\t{}\t{}\t{:.2f}\t{:.2f}\t{}\t{}".format(student[0], student[1], "\t".join(map(str, student[2])), student[3], student[4], student[5], rank))

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

grade_report(5, 3, ["영어", "C-언어", "파이썬"])



# # def calculate_total_score(grades):
#     return sum(grades)

# def calculate_average_score(total_score, num_subjects):
#     return total_score / num_subjects

# def generate_grade_report(num_students, num_subjects, subjects):
#     students_grades = []
    
#     for _ in range(num_students):
#         student_name = input("학생의 이름을 입력하세요: ")
#         student_number = input(student_name + "의 학번을 입력하세요: ")
#         print(student_name + "의 성적을 입력하세요:")
#         student_grades = [float(input(subject + " 성적: ")) for subject in subjects]
#         total_score = calculate_total_score(student_grades)
#         average_grade = calculate_average_score(total_score, num_subjects)
#         grade = calculate_grade(average_grade)
#         students_grades.append((student_name, student_number, student_grades, total_score, average_grade, grade))

#     total_scores = [student[3] for student in students_grades]
#     rank_dict = calculate_rank(total_scores)
    
#     print("\n성적표:")
#     print("학생\t학번\t", end="")
#     for subject in subjects:
#         print(subject + "\t", end="")
#     print("총점\t평균\t학점\t등수")

#     rank = 1
#     for student in students_grades:
#         rank_score = student[3]
#         rank = rank_dict[rank_score]
#         print("{}\t{}\t{}\t{:.2f}\t{:.2f}\t{}\t{}".format(student[0], student[1], "\t".join(map(str, student[2])), student[3], student[4], student[5], rank))

# def calculate_grade(score):
#     if score >= 90:
#         return "A"
#     elif score >= 80:
#         return "B"
#     elif score >= 70:
#         return "C"
#     elif score >= 60:
#         return "D"
#     else:
#         return "F"

# # 사용 예시
# generate_grade_report(5, 3, ["영어", "C-언어", "파이썬"])
