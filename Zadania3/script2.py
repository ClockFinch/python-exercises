import json

# 2. Napisac prosta klase przechowujaca np. dane osobowe (imie, nazwisko, adres zamieszkania, kod pocztowy, pesel)
# i metode zapisujaca obiekty typu tej klasy do json, oraz metode odczytuja json'a i ladujace dane do klasy


class UserId:
    def __init__(self, name, surname, address, zip_code, pesel):
        self.name = name
        self.surname = surname
        self.address = address
        self.zip_code = zip_code
        self.pesel = pesel

    @classmethod
    def from_dict(cls, data):
        return cls(name=data["name"],
                   surname=data["surname"],
                   address=data["address"],
                   zip_code=data["zip_code"],
                   pesel=data["pesel"])

    def to_dict(self):
        return {"name": self.name,
                "surname": self.surname,
                "address": self.address,
                "zip_code": self.zip_code,
                "pesel": self.pesel}

    def save_to_json(self, path):
        with open(path, "w") as file:
            json.dump(self.to_dict(), file)

    @classmethod
    def load_from_json(cls, path):
        with open(path, "r") as file:
            data = json.load(file)
        return cls.from_dict(data)

    def __str__(self):
        return f"{self.name} {self.surname}\n{self.address}, {self.zip_code}\n{self.pesel}"


if __name__ == "__main__":
    tester = UserId("John", "Smith", "Oakfield 46", "23-54", "129734432")
    tester.save_to_json("test1.json")
    loaded_tester = UserId.load_from_json("test1.json")
    print(loaded_tester)