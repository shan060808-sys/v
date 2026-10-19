class Person:
    def __init__(self,name,age=20,address=''):
        self.name=name
        self.age=age
        self.address=address

    def __str__(self):
        return f"This is the string representation of the Person-{self.name} age:{self.age} address:{self.address}" 
