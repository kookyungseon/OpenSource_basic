class Student:
    def __init__(self, name, student_number, grades):
        self.name = name
        self.student_number = student_number
        self.grades = grades
        self.total_score = sum(grades)
        self.average_score = self.total_score / len(grades)
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.average_score >= 90:
            return "A"
        elif self.average_score >= 80:
            return "B"
        elif self.average_score >= 70:
            return "C"
        elif self.average_score >= 60:
            return "D"
        else:
            return "F"


class GradeManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def delete_student(self, student_number):
        for student in self.students:
            if student.student_number == student_number:
                self.students.remove(student)
                print(f"{student.name} 학생의 정보가 삭제되었습니다.")
                return
        print("입력한 학번을 가진 학생을 찾을 수 없습니다.")

    def search_student(self, search_criteria):
        for student in self.students:
            if search_criteria in (student.name, student.student_number):
                return student
        print("해당 학생을 찾을 수 없습니다.")
        return None

    def grade_report(self):
        print("\n성적표:")
        print("학생\t학번\t영어\tC-언어\t파이썬\t총점\t평균\t학점")

        for student in self.students:
            print(f"{student.name}\t{student.student_number}\t" +
                  "\t".join(map(str, student.grades)) +
                  f"\t{student.total_score}\t{student.average_score:.2f}\t{student.grade}")

    def count_students_above_80(self):
        count = sum(1 for student in self.students if student.average_score >= 80)
        print("80점 이상 학생 수:", count)


def grade_management():
    grade_manager = GradeManager()
    subjects = ["영어", "C-언어", "파이썬"]

    while True:
        print("\n1. 학생 추가")
        print("2. 학생 삭제")
        print("3. 학생 검색")
        print("4. 성적 보고서 출력")
        print("5. 80점 이상 학생 수")
        print("6. 종료")

        choice = input("원하는 작업을 선택하세요: ")

        if choice == "1":
            name = input("학생의 이름을 입력하세요: ")
            student_number = input(name + "의 학번을 입력하세요: ")
            print(name + "의 성적을 입력하세요:")
            grades = [float(input(subject + " 성적: ")) for subject in subjects]
            student = Student(name, student_number, grades)
            grade_manager.add_student(student)
        elif choice == "2":
            student_number = input("삭제할 학생의 학번을 입력하세요: ")
            grade_manager.delete_student(student_number)
        elif choice == "3":
            search_criteria = input("학번 또는 이름으로 학생을 검색하세요: ")
            student = grade_manager.search_student(search_criteria)
            if student:
                print("\n학생 정보:")
                print("이름:", student.name)
                print("학번:", student.student_number)
                print("성적:", student.grades)
                print("총점:", student.total_score)
                print("평균:", student.average_score)
                print("학점:", student.grade)
        elif choice == "4":
            grade_manager.grade_report()
        elif choice == "5":
            grade_manager.count_students_above_80()
        elif choice == "6":
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")


if __name__ == "__main__":
    grade_management()
