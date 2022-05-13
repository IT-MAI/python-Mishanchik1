#1
class Student:
    def __init__(self,name,surname,gender,age,nomber):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age
        self.nomber = nomber


    def __str__(self):
        return f'name: {self.name}\nsurname: {self.surname}\ngender: {self.gender}\nage: {self.age}\nid: {self.nomber}\n\n'

s1=Student('Oleg','Ivanov','man',19,837)
s2=Student('Kostia','Petrov','man',17,456)
s3=Student('Vika','Smirnova','woman',20,985)
s4=Student('Van','Smitt','man',23,948)
s5=Student('Anna','Jane','woman',21,395)

#2
list_s=[s1,s2,s3,s4,s5]

def sort_age(l_studs):
    for j in range(len(l_studs)-1):
        for i in range(len(l_studs)-1):
            if l_studs[i+1].age<l_studs[i].age:
                l_studs[i],l_studs[i+1]=l_studs[i+1],l_studs[i]
    for i in l_studs:
        print(i)
print(sort_age(list_s))


