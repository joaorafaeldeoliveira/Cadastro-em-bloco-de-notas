class Cadastro:

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

def main():
    Persons = []

    while True:
        Name = str(input("What is your name ? "))
        Age = str(input("How old are you ? "))
        City = str(input("Where do you live ?"))

        Person = Cadastro(Name, Age, City)
        Persons.append(Person)

        Answer = str(input("Do you want no continue ? [YES/NO]")).upper()

        if Answer != 'YES':
            break

    for Person in Persons:
        with open("Cadastro_por_Classe.txt", "a") as file:
            file.write(f"Nome: {Person.name},Idade: {Person.age},Cidade: {Person.city} \n")

if __name__ == "__main__":
    main()