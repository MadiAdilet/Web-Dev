

from models import Animal, Dog, Cat


def main():

    generic_animal = Animal(name="Unknown", age=3, color="grey")
    dog = Dog(name="Buddy", age=4, color="golden", breed="Labrador")
    cat = Cat(name="Whiskers", age=2, color="white", is_indoor=True)


    animals = [generic_animal, dog, cat]

    print("=" * 40)
    print("       ALL ANIMALS")
    print("=" * 40)


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


    for animal in animals:
        print(f"{animal.name} says: {animal.speak()}")

    print("\n" + "=" * 40)
    print("    UNIQUE METHODS")
    print("=" * 40)

    print(dog.fetch())
    print(cat.purr())


if __name__ == "__main__":
    main()
