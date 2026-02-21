class Father:
    def skills(self):
        print("Gardening, Driving")


class Mother:
    def skills(self):
        print("Cooking, Teaching")


class Child(Father, Mother):
    def skills(self):
        print("Programming")
        Father.skills(self)
        Mother.skills(self)


# Usage
child = Child()
child.skills()