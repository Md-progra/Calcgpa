import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QLabel

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QLabel

def calculate_gpa(report_card):
    grades = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}
    if not report_card:
        return 0.0
    total = 0.0
    for grade in report_card.values():
        if grade not in grades:  # Validate grade
            continue
        points = grades[grade]
        total += points
    if len(report_card) == 0:  # Avoid division by zero
        return 0.0
    gpa = total / len(report_card)
    return float(f"{gpa:.2f}")

class GPAWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(" Simple GPA Calculator")
        self.layout = QVBoxLayout()
        self.form_layout = QFormLayout()

        self.courses = []
        self.grades = []
        for i in range(8):
            course_input = QLineEdit() #Added QLineEdit for course name input
            course_input.setPlaceholderText("Enter course naeme")
            grade_input = QLineEdit()
            grade_input.setPlaceholderText("Enter grade (A-F)")  # Add placeholder for clarity
            self.form_layout.addRow(f"Course {i+1} Name:", course_input)
            self.form_layout.addRow(f"Course {i+1} Grade (A-F):", grade_input)
            self.courses.append(course_input)
            self.grades.append(grade_input)

        self.layout.addLayout(self.form_layout)

        self.calculate_button = QPushButton("Calculate GPA")
        self.calculate_button.clicked.connect(self.calculate_gpa)
        self.layout.addWidget(self.calculate_button)

        self.result_label = QLabel("Your GPA will appear here.")
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

    def calculate_gpa(self):
        report_card = {}
        invalid_inputs = False
        for course, grade in zip(self.courses, self.grades):
            course_name = course.text().strip()
            grade_value = grade.text().strip().upper()
            if course_name and grade_value in {"A", "B", "C", "D", "F"}:
                report_card[course_name] = grade_value
            elif course_name or grade_value:  # Invalid input detected
                invalid_inputs = True

        if invalid_inputs:
            self.result_label.setText("Some inputs were invalid and ignored.")
        
        if not report_card:
            self.result_label.setText("Please enter valid courses and grades.")
            return

        gpa = calculate_gpa(report_card)
        self.result_label.setText(f"Your GPA is: {gpa}")
