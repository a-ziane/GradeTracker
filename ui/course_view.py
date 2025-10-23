""" import customtkinter as ctk
import json
import os
from models.course import Course
from ui.main_view import MainView


#courseview class
class CourseView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # Title
        self.label = ctk.CTkLabel(self, text=f"Course: {self.course.name}", font=("Helvetica", 18, "bold"))
        self.label.pack(pady=20)

        # Current grade
        grade_label = ctk.CTkLabel(self, text=f"Current Grade: {self.course.current_grade():.2f}%")
        grade_label.pack(pady=5)

        # Back button
        back_button = ctk.CTkButton(self, text="Back", command=lambda: master.switch_frame(master.current_frame.__class__))
        back_button.pack(pady=10) """