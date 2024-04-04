def t_score(grades):
    return sum(grades)

def average(total_score, num_subjects):  
    return total_score / num_subjects

def cal_rank(scores):
    s_scores = sorted(scores, reverse=True)
    rank_dict = {score: i + 1 for i, score in enumerate(s_scores)}
    return rank_dict

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

def add_student(students_grades, subjects):
    student_name = input("학생의 이름을 입력하세요: ")
    student_number = input(student_name + "의 학번을 입력하세요: ")
    print(student_name + "의 성적을 입력하세요:")
    student_grades = [float(input(subject + " 성적: ")) for subject in subjects]
    total_score = t_score(student_grades)
    avg_grade = average(total_score, len(subjects))
    grade = calculate_grade(avg_grade)
    students_grades.append((student_name, student_number, student_grades, total_score, avg_grade, grade))

def delete_student(students_grades):
    student_number = input("삭제할 학생의 학번을 입력하세요: ")
    for student in students_grades:
        if student[1] == student_number:
            students_grades.remove(student)
            print(f"{student[0]} 학생의 정보가 삭제되었습니다.")
            return
    print("입력한 학번을 가진 학생을 찾을 수 없습니다.")

def search_student(students_grades):
    search_criteria = input("학번 또는 이름으로 학생을 검색하세요: ")
    for student in students_grades:
        if search_criteria in (student[0], student[1]):
            print("\n학생 정보:")
            print("이름:", student[0])
            print("학번:", student[1])
            print("성적:", student[2])
            print("총점:", student[3])
            print("평균:", student[4])
            print("학점:", student[5])
            return
    print("해당 학생을 찾을 수 없습니다.")

def grade_report(students_grades, subjects):
    num_students = len(students_grades)
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

def count_students_above_80(students_grades):
    count = sum(1 for student in students_grades if student[4] >= 80)
    print("80점 이상 학생 수:", count)

def grade_management():
    subjects = ["영어", "C-언어", "파이썬"]
    students_grades = []

    while True:
        print("\n1. 학생 추가")
        print("2. 학생 삭제")
        print("3. 학생 검색")
        print("4. 성적 보고서 출력")
        print("5. 80점 이상 학생 수")
        print("6. 종료")

        choice = input("원하는 작업을 선택하세요: ")

        if choice == "1":
            add_student(students_grades, subjects)
        elif choice == "2":
            delete_student(students_grades)
        elif choice == "3":
            search_student(students_grades)
        elif choice == "4":
            grade_report(students_grades, subjects)
        elif choice == "5":
            count_students_above_80(students_grades)
        elif choice == "6":
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")

if __name__ == "__main__":
    grade_management()
