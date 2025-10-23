import customtkinter as ctk
import json
import os
from models.course import Course
from models.section import Section

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Grade Tracker")
        self.geometry("800x600")

        # Header bar
        self.header_bar = ctk.CTkFrame(master=self, width=600, height=200)
        self.header_bar.pack(padx=20, pady=20, fill="both", expand=True)
        self.header_label = ctk.CTkLabel(master=self.header_bar, text="Grade Tracker", font=("Helvetica", 18, "bold"))
        self.header_label.pack(pady=10)

        self.switch = ctk.CTkSwitch(master=self.header_bar, text="Dark Mode")
        self.switch.pack()
        self.switch.configure(command=self.toggle_mode)

        self.current_frame = None
        self.courses = []

        self.load_courses_from_json()
        self.switch_frame(MainView)

    def switch_frame(self, new_frame_class, *args, **kwargs):
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = new_frame_class(master=self, *args, **kwargs)
        self.current_frame.pack(fill="both", expand=True)

    def toggle_mode(self):
        if self.switch.get() == 1:
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")

    def refresh(self):
        self.switch_frame(self.current_frame)

    def save_courses_to_json(self):
        data = [course.to_dict() for course in self.courses]
        with open("grades.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_courses_from_json(self):
        if not os.path.exists("grades.json"):
            self.courses = []
            return
        with open("grades.json", "r") as file:
            data = json.load(file)
        self.courses = [Course.from_dict(course_dict) for course_dict in data]


class MainView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.courses = master.courses

        self.main_label = ctk.CTkLabel(master=self, text="Welcome to Grade Tracker")
        self.main_label.pack(pady=20)

        # Scrollable frame for courses
        self.scroll = ctk.CTkScrollableFrame(master=self)
        self.scroll.pack(padx=10, pady=10, fill="both", expand=True)

        # Add course fields
        self.name_entry = ctk.CTkEntry(master=self, placeholder_text="Course Name")
        self.name_entry.pack(pady=5)
        self.a_entry = ctk.CTkEntry(master=self, placeholder_text="A Threshold (e.g. 90)")
        self.a_entry.pack(pady=5)

        self.add_button = ctk.CTkButton(master=self, text="Add Course", command=self.add_course)
        self.add_button.pack(pady=10)

        self.display_courses()

    def display_courses(self):
        for widget in self.scroll.winfo_children():
            widget.destroy()

        for course in self.courses:
            frame = ctk.CTkFrame(master=self.scroll)
            frame.pack(pady=5, fill="x", padx=10)

            # Course name
            label = ctk.CTkLabel(master=frame, text=course.name, font=("Helvetica", 14, "bold"))
            label.pack(side="left", padx=10, pady=20)

            # Show grade info
            grade = course.current_grade()
            grade_text = f"{grade:.2f}%"
            grade_label = ctk.CTkLabel(master=frame, text=f"Grade: {grade_text}")
            grade_label.pack(side="left", padx=10)

            # Show if it's an A or not
            status = "✅ A" if grade >= course.a_threshold else "❌ Below A"
            status_label = ctk.CTkLabel(master=frame, text=status)
            status_label.pack(side="left", padx=10)

            open_btn = ctk.CTkButton(
                master=frame,
                text="Open",
                command=lambda c=course: self.master.switch_frame(CourseView, course=c)
            )
            open_btn.pack(side="right", padx=10)

    def add_course(self):
        name = self.name_entry.get().strip()
        a_threshold = self.a_entry.get().strip()
        if not name or not a_threshold:
            return
        try:
            a_threshold = float(a_threshold)
        except ValueError:
            return

        new_course = Course(name, a_threshold)
        self.courses.append(new_course)
        self.name_entry.delete(0, "end")
        self.a_entry.delete(0, "end")

        self.master.save_courses_to_json()
        self.display_courses()


class CourseView(ctk.CTkFrame):
    def __init__(self, master, course):
        super().__init__(master)
        self.master = master
        self.course = course

        self.label = ctk.CTkLabel(self, text=f"Course: {self.course.name}", font=("Helvetica", 18, "bold"))
        self.label.pack(pady=20)

        # Current grade label (updatable)
        self.grade_label = ctk.CTkLabel(self, text=self.get_grade_text())
        self.grade_label.pack(pady=5)

        # Recalculate button
        recalc_btn = ctk.CTkButton(self, text="Recalculate Grade", command=self.recalculate_grade)
        recalc_btn.pack(pady=5)

        # Back button
        back_button = ctk.CTkButton(self, text="Back", command=lambda: master.switch_frame(MainView))
        back_button.pack(pady=10)

        # Add Section inputs
        self.name_entry = ctk.CTkEntry(master=self, placeholder_text="Section Name")
        self.name_entry.pack(pady=5)
        self.weight_entry = ctk.CTkEntry(master=self, placeholder_text="Weight (e.g. 20)")
        self.weight_entry.pack(pady=5)

        add_button = ctk.CTkButton(self, text="Add Section", command=self.add_section)
        add_button.pack(pady=10)

        # Scrollable section frame
        self.scroll = ctk.CTkScrollableFrame(master=self)
        self.scroll.pack(padx=10, pady=10, fill="both", expand=True)

        self.display_sections()

    def get_grade_text(self):
        grade = self.course.current_grade()
        status = "✅ A" if grade >= self.course.a_threshold else "❌ Below A"
        return f"Current Grade: {grade:.2f}% ({status})"

    def display_sections(self):
        # Clear old widgets
        for widget in self.scroll.winfo_children():
            widget.destroy()

        # Display all sections
        for section in self.course.sections:
            frame = ctk.CTkFrame(master=self.scroll)
            frame.pack(pady=5, fill="x", padx=10)

            name_label = ctk.CTkLabel(master=frame, text=section.name)
            name_label.pack(side="left", padx=5)

            grade_entry = ctk.CTkEntry(master=frame, placeholder_text="Enter grade (e.g. 85)")
            if section.grade is not None:
                grade_entry.insert(0, str(section.grade))
            grade_entry.pack(side="left", padx=5)

            # Save edited grade immediately
            grade_entry.bind("<FocusOut>", lambda e, s=section, entry=grade_entry: self.update_section_grade(s, entry))

    def update_section_grade(self, section, entry):
        value = entry.get().strip()
        if not value:
            section.grade = None
            return
        try:
            section.grade = float(value)
        except ValueError:
            section.grade = None

    def add_section(self):
        name = self.name_entry.get().strip()
        weight = self.weight_entry.get().strip()
        if not name or not weight:
            return
        try:
            weight = float(weight)
        except ValueError:
            return

        new_section = Section(name, weight)
        self.course.sections.append(new_section)
        self.name_entry.delete(0, "end")
        self.weight_entry.delete(0, "end")

        self.master.save_courses_to_json()
        self.display_sections()

    def recalculate_grade(self):
        # Save updated grades and refresh display
        self.master.save_courses_to_json()
        self.grade_label.configure(text=self.get_grade_text())
        self.display_sections()


if __name__ == "__main__":
    app = App()
    app.mainloop()
