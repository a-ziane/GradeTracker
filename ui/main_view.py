""" import customtkinter as ctk
from models.course import Course
from ui.course_view import CourseView


class MainView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.courses = master.courses

        self.main_label = ctk.CTkLabel(master=self, text="Welcome to Grade Tracker")
        self.main_label.pack(pady=20)

        # Scrollable frame
        self.scroll = ctk.CTkScrollableFrame(master=self)
        self.scroll.pack(padx=10, pady=10, fill="both", expand=True)

        # Entry fields for adding a course
        self.name_entry = ctk.CTkEntry(master=self, placeholder_text="Course Name")
        self.name_entry.pack(pady=5)

        self.a_entry = ctk.CTkEntry(master=self, placeholder_text="A Threshold (e.g. 90)")
        self.a_entry.pack(pady=5)

        # Add Course button
        self.add_button = ctk.CTkButton(
            master=self,
            text="Add Course",
            command=self.add_course
        )
        self.add_button.pack(pady=10)

        self.display_courses()

    def display_courses(self):
        Display all courses in the scrollable frame.
        for widget in self.scroll.winfo_children():
            widget.destroy()

        for course in self.courses:
            frame = ctk.CTkFrame(master=self.scroll)
            frame.pack(pady=5, fill="x", padx=10)

            label = ctk.CTkLabel(master=frame, text=course.name)
            label.pack(side="left", padx=10)

            open_btn = ctk.CTkButton(
                master=frame,
                text="Open",
                command=lambda c=course: self.master.switch_frame(CourseView, c)
            )
            open_btn.pack(side="right", padx=10)

    def add_course(self):
        Add a new course and refresh the display.
        name = self.name_entry.get().strip()
        a_threshold = self.a_entry.get().strip()

        if not name or not a_threshold:
            return  # ignore empty entries

        try:
            a_threshold = float(a_threshold)
        except ValueError:
            return  # invalid threshold, ignore

        new_course = Course(name, a_threshold)
        self.courses.append(new_course)

        self.name_entry.delete(0, "end")
        self.a_entry.delete(0, "end")

        self.master.save_courses_to_json()
        self.display_courses()


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