class GradeManager:
    def __init__(self):
        self.grades = {}
        
    def input_grades(self):
        while True:
            subject = input("Enter subject (or 'exit' to finish): ")
            if subject.lower() == 'exit':
                break
            try:
                grade = float(input(f"Enter grade for {subject} (0-100): "))
                if 0 <= grade <= 100:
                    self.grades[subject] = grade
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numeric grade.")

    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def determine_letter_grade(self, average):
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    def calculate_gpa(self, average):
        if average >= 90:
            return 4.0
        elif average >= 80:
            return 3.0
        elif average >= 70:
            return 2.0
        elif average >= 60:
            return 1.0
        else:
            return 0.0

    def display_results(self):
        average = self.calculate_average()
        letter_grade = self.determine_letter_grade(average)
        gpa = self.calculate_gpa(average)

        print("\n--- Student Grade Report ---")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {average:.2f}")
        print(f"Letter Grade: {letter_grade}")
        print(f"GPA: {gpa:.2f}")


if __name__ == "__main__":
    manager = GradeManager()
    
    # Input grades from user
    manager.input_grades()
    
    # Display results
    manager.display_results()
