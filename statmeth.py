class Employee:
    def __init__(self,name,position):
        self.name=name
        self.position=position
    def get_info(self):
        return f"{self.name}: {self.position}"
    @staticmethod
    def is_valid_position(position):
        valid_position=['Manager','CEO','CTO','CFO']
        return position in valid_position

print(Employee.is_valid_position('CEO'))
print(Employee.is_valid_position('Cook'))

employee1=Employee('Snehil','CEO')
employee2=Employee('Rajiv','CFO')
employee3=Employee('Nidhi','CTO')

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())