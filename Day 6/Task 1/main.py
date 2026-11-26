# Task 1 - Python Core, OOP and Errors

class InvalidSalaryError(Exception):
    pass

def bonus(salary, rate=0.1, *extras, **options):
    result = salary * rate + sum(extras)
    if "cap" in options and result > options["cap"]:
        result = options["cap"]
    return result

class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary: {salary}")
        self.name = name
        self.salary = salary
    def annual_salary(self):
        return self.salary * 12
    def get_details(self):
        return f"{self.name} - {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
    def get_details(self):
        return f"{self.name} - {self.salary} - Team Size: {self.team_size}"

employees = [
    {"id": 1, "name": "Arun", "department": "Sales", "salary": 30000, "city": "Chennai"},
    {"id": 2, "name": "Priya", "department": "HR", "salary": 45000, "city": "Chennai"},
    {"id": 3, "name": "Rahul", "department": "IT", "salary": 60000, "city": "Bangalore"},
    {"id": 4, "name": "Divya", "department": "IT", "salary": 75000, "city": "Chennai"},
    {"id": 5, "name": "Karthik", "department": "Finance", "salary": 90000, "city": "Mumbai"},
    {"id": 6, "name": "Meena", "department": "Sales", "salary": 52000, "city": "Bangalore"},
    {"id": 7, "name": "Suresh", "department": "IT", "salary": 68000, "city": "Chennai"},
    {"id": 8, "name": "Anitha", "department": "HR", "salary": 48000, "city": "Mumbai"},
]

above_50000 = [e["name"] for e in employees if e["salary"] > 50000]
print(f"Above 50000: {above_50000}")

raised = list(map(lambda e: e["salary"] * 1.10, employees))
print(f"After 10% Raise: {raised}")

chennai = list(filter(lambda e: e["city"] == "Chennai", employees))
print(f"Chennai: {[e['name'] for e in chennai]}")

for e in employees:
    if e["salary"] == 0:
        continue
    print(e["name"], e["salary"])
    if e["salary"] > 85000:
        break

try:
    emp = Employee("Test", -500)
except InvalidSalaryError as e:
    print(f"Error: {e}")
finally:
    print("Transaction finished")

print(f"Bonus: {bonus(50000, 0.1, 1000, 2000, cap=8000)}")
m = Manager("Divya", 75000, 5)
print(m.get_details())
print(f"Annual: {m.annual_salary()}")