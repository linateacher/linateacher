text = ["hello","byebye","hua","james", "after merge"]

for letter in text:
    print(letter)

class Person:
    def __init__(self, name):
        self.name = name

def is_handsome(person):
    if person.name == "JamesX":
        return True
    
jx = Person("JamesX")

print("Is JamesX handsome? ")
print(is_handsome(jx))