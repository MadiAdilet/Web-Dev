# main.py
# Lab 7 - Task 2: Demonstrating OOP usage

from models import Animal, Dog, Cat


def main():
    # Create objects from each class
    generic_animal = Animal(name="Unknown", age=3, color="grey")
    dog = Dog(name="Buddy", age=4, color="golden", breed="Labrador")
    cat = Cat(name="Whiskers", age=2, color="white", is_indoor=True)

    # Store objects in a list
    animals = [generic_animal, dog, cat]

    print("=" * 40)
    print("       ALL ANIMALS")
    print("=" * 40)

    # Iterate over the list and print each animal
    for animal in animals:
        print(animal)

    print("\n" + "=" * 40)
    print("       DESCRIPTIONS")
    print("=" * 40)

    for animal in animals:
        print(animal.describe())

    print("\n" + "=" * 40)
    print("  POLYMORPHISM: speak() method")
    print("=" * 40)

    # Demonstrate polymorphism - same method, different results
    for animal in animals:
        print(f"{animal.name} says: {animal.speak()}")

    print("\n" + "=" * 40)
    print("    UNIQUE METHODS")
    print("=" * 40)

    # Call unique methods on child class objects
    print(dog.fetch())
    print(cat.purr())


if __name__ == "__main__":
    main()
