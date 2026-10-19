import Person

name="Shanmathi" 
age=18
address="Dubai"

#create a person1 list with these details
person1=[name,age,address]
print(person1)

#create the person attribute list
person_attributes=["name","age","address"]

#create a dictionary combining them both
person1_dict=dict(zip(person_attributes,person1))

person_class=Person.Person(name,age,address)

print(person1_dict)
print(person_class) #<
print(person_class.name)