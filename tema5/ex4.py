class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        return f"{self.name} is working."

    def get_salary(self):
        return self.salary


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def work(self):
        return f"{self.name} is managing a team of {self.team_size} employees."

    def conduct_meeting(self):
        return f"{self.name} is conducting a meeting."


class Engineer(Employee):
    def __init__(self, name, salary, specialty):
        super().__init__(name, salary)
        self.specialty = specialty

    def work(self):
        return f"{self.name} is developing {self.specialty} solutions."

    def debug_code(self):
        return f"{self.name} is debugging code."


class Salesperson(Employee):
    def __init__(self, name, salary, region):
        super().__init__(name, salary)
        self.region = region

    def work(self):
        return f"{self.name} is selling products in the {self.region} region."

    def make_sale(self):
        return f"{self.name} made a sale in the {self.region} region."


m = Manager("Alice", 90000, 5)
e = Engineer("Bob", 80000, "AI")
s = Salesperson("Charlie", 70000, "East")

print(m.work())
print(e.work())
print(s.work())