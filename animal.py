class animal: 
    def speak(self):
        raise 
not implementodError("Subclea sses must implement this!")

class dog(animal):
    def speak(self):
        return "bark"

class cat(animal):
    def speak (self):
        return "meow"

def make_animal_speak(animal):
print(animal.speak())


dog = dog()
cat = cat ()

make_animal_speak(dog)
make_animal_speak(cat)
