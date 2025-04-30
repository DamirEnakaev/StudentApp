import customtkinter as ctk
from tkinter import messagebox
from db import Database  # Убедись, что у тебя есть этот модуль
from datetime import datetime

class StudentGradeApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.db = Database("StudentRelational.db")  # предполагается, что класс уже реализован
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

        # ---- Students Tab Layout ----
        tab_students.columnconfigure((0, 3), weight=1)
        tab_students.columnconfigure((1, 2), weight=0)

        ctk.CTkLabel(tab_students, text="Name:").grid(row=0, column=0, sticky="e", padx=10, pady=10)
        name_entry = ctk.CTkEntry(tab_students, textvariable=self.name)
        name_entry.grid(row=0, column=1, padx=10, pady=10)

        ctk.CTkLabel(tab_students, text="Index Number:").grid(row=1, column=0, sticky="e", padx=10, pady=10)
        index_entry = ctk.CTkEntry(tab_students, textvariable=self.index_number)
        index_entry.grid(row=1, column=1, padx=10, pady=10)

        add_btn = ctk.CTkButton(tab_students, text="Add Student", command=self.add_student)
        add_btn.grid(row=2, column=0, columnspan=2, pady=20)

    def add_student(self):
        name = self.name.get().strip()
        index = self.index_number.get().strip()
        if not name or not index:
            messagebox.showerror("Error", "Please enter all fields.")
            return

        try:
            self.db.insert_student(name, index)
            messagebox.showinfo("Success", f"Student '{name}' added successfully.")
            self.name.set("")
            self.index_number.set("")
        except Exception as e:
            messagebox.showerror("Database Error", str(e))


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    app = StudentGradeApp()
    app.mainloop()


