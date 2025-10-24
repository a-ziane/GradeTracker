# 🎓 Grade Tracker

**Grade Tracker** is a simple desktop app built with **Python** and **CustomTkinter** that helps students track their grades by course and section.  
Each course can have multiple grading sections (like Homework, Exams, Projects), and the app automatically calculates your overall grade — letting you know whether you're earning an **A** or not.

---

## 🧩 Features

- 🏫 Add, view, and manage courses  
- 📊 Add sections within each course (with weights and grades)  
- 🔄 Recalculate grades instantly after editing  
- 🌗 Light/Dark Mode toggle  
- 💾 Auto-save to JSON — your grades persist even after you close the app  
- 📈 Displays current grade and A-status for each course  

---

## 🖥️ Preview

**Main View**  
- Displays all courses  
- Shows current grade and whether it’s an A  
- Lets you open individual courses  

**Course View**  
- View and edit grading sections  
- Add new sections  
- Recalculate total grade anytime  

---

## ⚙️ Tech Stack

- **Python 3.10+**  
- **CustomTkinter** — for the modern UI  
- **JSON** — for lightweight local data storage  
- **Object-Oriented Design** — modular structure for scalability  

---

## 🧱 Project Structure


GradeTracker/
├── main.py # Entry point (App + MainView + CourseView)
├── models/
│ ├── course.py # Course model (handles sections, grade calculation)
│ └── section.py # Section model (name, weight, grade)
├── grades.json # Saved data file (auto-generated)
└── README.md # Project documentation


---

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/grade-tracker.git
   cd grade-tracker
   
2. **Install dependencies**
   ```bash
   pip install customtkinter

3. **Run the app**
   ```bash
   python main.py
  
## 💡 Usage

- **Add a new course** — enter a course name and threshold (e.g., 90 for an A).  
- **Open a course** — view all sections (assignments, quizzes, exams).  
- **Add sections** — each with a name and weight.  
- **Enter grades** — update section grades and press **Recalculate**.  
- **Switch themes** — toggle between Light and Dark mode using the switch at the top.  

---

## 🧠 How It Works

Each **Course** stores:
- Name  
- A-threshold (minimum grade for an A)  
- A list of **Sections**

Each **Section** has:
- Name (e.g., “Homework”)  
- Weight (percentage of total grade)  
- Grade (optional)

The total grade is a **weighted sum** of section grades.

---

## 🪄 Example

| Section  | Weight | Grade |
|-----------|--------|-------|
| Homework  | 40%    | 95    |
| Midterm   | 30%    | 88    |
| Final     | 30%    | 90    |

**Total Grade:**  
`(0.4 × 95) + (0.3 × 88) + (0.3 × 90) = 91.1% → ✅ A`

---

## 🗂️ Data Persistence

All your courses and grades are stored locally in `grades.json` — no database setup required.

---

## 🔮 Future Improvements

- 📅 Add due dates for sections  
- 📈 Add charts to visualize grade progress  
- 🧮 Weighted vs. unweighted GPA calculation  
- ☁️ Cloud sync across devices  

---

## 🧑‍💻 Author

**Amani Ziane**  
📚 Applied & Computational Mathematics & Computer Science Minor @ USC  
💻 Passionate about building smart academic productivity tools


