class Section:
    def __init__(self, name, weight, grade=None, counts=True, modifiable=True):
        self.name = name
        self.weight = weight
        self.grade = grade
        self.counts = counts
        self.modifiable = modifiable
    def to_dict(self):
        return {
            "name": self.name,
            "weight": self.weight,
            "grade": self.grade,
            "counts": self.counts,
            "modifiable": self.modifiable
        }
    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            weight=data["weight"],
            grade=data.get("grade"),
            counts=data.get("counts", True),
            modifiable=data.get("modifiable", True)
        )
    def is_active(self):
        return self.counts and self.modifiable
    

