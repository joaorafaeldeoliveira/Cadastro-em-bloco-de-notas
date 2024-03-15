def new_dictionary(keys,values):
    dictionary = {}

    for key,value in zip(keys,values):
        dictionary[key] = value

    return dictionary

def new_registers():
    persons =[]

    while True:
        Name = str(input("What is your name ? "))
        Age = str(input("How old are you ? "))
        City = str(input("What city do you live ? "))

        keys = ['nome', 'idade', 'cidade']
        values =[Name, Age, City]
        person = new_dictionary(keys,values)
        persons.append(person)

        Answer = str(input("Do you want to continue ? [Y/N] "))

        if Answer in 'Nn':
            break
    return persons

Persons_List = new_registers()

for person in (Persons_List):
    with open("Cadastro_de_Pessoas.txt","a") as file:
        file.write(f"{person}\n")

