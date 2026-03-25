

class Animal:
   

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def speak(self):
        return "..."

    def describe(self):
        return f"{self.name} is {self.age} year(s) old and has {self.color} color."

    def __str__(self):
        return f"{self.__class__.__name__}(name={self.name}, age={self.age}, color={self.color})"


class Dog(Animal):

    def __init__(self, name, age, color, breed):
        super().__init__(name, age, color)
        self.breed = breed

    def speak(self):
        return "Woof!"

    def fetch(self):
        return f"{self.name} fetches the ball!"

    def __str__(self):
        return (f"Dog(name={self.name}, age={self.age}, "
                f"color={self.color}, breed={self.breed})")


class Cat(Animal):


    def __init__(self, name, age, color, is_indoor):
        super().__init__(name, age, color)
        self.is_indoor = is_indoor

    def speak(self):
        return "Meow!"

    def purr(self):
        return f"{self.name} is purring... Purrr~"

    def __str__(self):
        indoor_status = "indoor" if self.is_indoor else "outdoor"
        return (f"Cat(name={self.name}, age={self.age}, "
                f"color={self.color}, type={indoor_status})")
