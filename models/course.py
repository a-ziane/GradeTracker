from models.section import Section
class Course:
    def __init__(self, name, a_threshold, sections=None):
        self.name = name
        self.a_threshold = a_threshold
        self.sections = sections if sections is not None else []
        
    def add_section(self, section):
        self.sections.append(section) 

    def remove_section(self, section):
        self.sections.remove(section)    

    def current_grade(self):
        if not self.sections:
            return 0.0
        grade_sum = 0
        total_weight = 0

        for section in self.sections:
            if section.grade is not None:
                grade_sum += section.grade * section.weight
                total_weight += section.weight

        return grade_sum / total_weight if total_weight > 0 else 0.0
    def isA(self):
           if(self.a_threshold <= self.current_grade()):
               return True
           else:
               return False

    def to_dict(self):
        return{
            "name": self.name,
            "a_threshold": self.a_threshold,
            "sections" : [section.to_dict() for section in self.sections],

        }        
    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            a_threshold=data["a_threshold"],
            sections=[Section.from_dict(s) for s in data.get("sections", [])],
            
        )


