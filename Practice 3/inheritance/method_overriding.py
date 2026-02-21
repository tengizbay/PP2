class Animal:
    def speak(self):
        print("The animal makes a sound")


class Dog(Animal):
    def speak(self):  # overriding parent method
        print("The dog barks")


class Cat(Animal):
    def speak(self):  # overriding parent method
        print("The cat meows")


# Usage
a = Animal()
d = Dog()
c = Cat()

a.speak()   # Parent method
d.speak()   # Overridden method
c.speak()   # Overridden method