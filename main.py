import customtkinter as ctk
from tkinter import ttk, messagebox
from db import Database
from datetime import datetime

class StudentGradeApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.db = Database("StudentRelational.db")
        self.title("Student Grade Management System")
        self.geometry("1200x800")
        self.configure(fg_color="#2c3e50")

        self.name = ctk.StringVar()
        self.index_number = ctk.StringVar()
        self.course_name = ctk.StringVar()
        self.grade = ctk.StringVar()

        self._selected_student_id = None
        self._selected_course_id = None 
        self.create_widgets()

    def create_widgets(self):
        tabview = ctk.CTkTabview(self)
        tabview.pack(expand=True, fill="both", padx=20, pady=20)

        tab_students = tabview.add("Students")
        tab_courses = tabview.add("Courses")
        tab_grades = tabview.add("Grades")

        # Пример добавления виджета в вкладку
        label = ctk.CTkLabel(tab_students, text="List of Students")
        label.pack(pady=10)

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    app = StudentGradeApp()
    app.mainloop()
