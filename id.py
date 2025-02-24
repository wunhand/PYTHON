print("Welcome to my id program.")

class Person():
    def __init__(self, age):
        self.age = age
        
fab = Person(39)

print(fab.age)
print(id(fab))
print('\n')
fab.age = 25
print(fab.age)
print(id(fab))

