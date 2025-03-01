from database import db

class TaekwondoEntry:
    def __init__(self, name, category, description=None, filepath=None):
        self.name = name
        self.description = description
        self.category = category
        self.filepath = filepath

    def save(self):
        db.insert(self.__dict__)
        print(f"{self.category} '{self.name}' saved.")

    @staticmethod
    def search(name):
        from database import Taekwondo
        result = db.search(Taekwondo.name == name)
        return result if result else f"No entry for {name} found."
    
    @staticmethod
    def show_all():
        return db.all()
    
    @staticmethod
    def delete(name):
        from database import Taekwondo
        db.remove(Taekwondo.name == name)
        print(f"Entry '{name}' deleted.")

class Chong(TaekwondoEntry):
    def __init__(self, name, pseudonym, stepscount, steps=None, description=None, image_path=None):
        super().__init__(name, "Chong", description, image_path)
        self.pseudonym = pseudonym
        self.stepscount = stepscount
        self.steps = steps if steps else []  # Default to empty list if no steps are provided

    def save(self):
        entry = self.__dict__.copy()
        db.insert(entry)
        print(f"Chong '{self.name}' saved.")

    def show_pseudonym(self):
        print(f"Pseudonym for {self.name}: {self.pseudonym}")

    def show_steps(self):
        if self.steps:
            print(f"Steps for {self.name}:")
            for i, step in enumerate(self.steps, 1):
                print(f"{i}. {step}")
        else:
            print(f"No steps recorded for {self.name}.")

class FootPosition(TaekwondoEntry):
    def __init__(self, name, description=None, image_path=None):
        super().__init__(name, "FootPosition", description, image_path)

    def save(self):
        entry = self.__dict__.copy()
        db.insert(entry)
        print(f"Foot position '{self.name}' saved.")

    def show_details(self):
        print(f"Foot position: {self.name}")
        if self.description:
            print(f"Description: {self.description}")
        else:
            print("No description available.")


class Combination(TaekwondoEntry):
    def __init__(self, name, steps=None, description=None, image_path=None):
        super().__init__(name, "Combination", description, image_path)
        self.steps = steps if steps else []

    def save(self):
        entry = self.__dict__.copy()
        db.insert(entry)
        print(f"Combination '{self.name}'  saved.")

    def show_steps(self):
        if self.steps:
            print(f"Steps for {self.name}:")
            for i, step in enumerate(self.steps, 1):
                print(f"{i}. {step}")
        else:
            print(f"No steps recorded for {self.name}.")


class Kick(TaekwondoEntry):
    def __init__(self, name, description=None, image_path=None):
        super().__init__(name, "Kick", description, image_path)

class Punch(TaekwondoEntry):
    def __init__(self, name, description=None, image_path=None):
        super().__init__(name, "Punch", description, image_path)