def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Chyba: Dělení nulou se nedá!"
    return a / b

def save_history(history, file="historie.txt"):
    with open(file, "w") as f:
        for record in history:
            f.write(record + "\n")

def loading_history(file="historie.txt"):
    try:
        with open(file, "r") as f:
            history = f.readlines()
            history = [record.strip() for record in history]
            return history
    except FileNotFoundError:
        return []

def calculator():
    history = loading_history()

    while True:
        print("\nVyber prosím operaci:")
        print("1. Sčítání")
        print("2. Odčítání")
        print("3. Násobení")
        print("4. Dělení")
        print("5. Zobrazit historii")
        print("6. Ukončit")
        
        choice = input("Zadej prosím číslo operace: ")

        if choice == '6':
            save_history(history)
            print("Historie byla úspěšně uložena. Ukončuji program.")
            break

        if choice == '5':
            print("\nHistorie výpočtů:")
            for record in history:
                print(record)
            continue

        try:
            a = float(input("Zadej první číslo: "))
            b = float(input("Zadej druhé číslo: "))
        except ValueError:
            print("Neplatný vstup. Zadejte prosím čísla.")
            continue

        if choice == '1':
            result = add(a, b)
            operation = f"{a} + {b} = {result}"
        elif choice == '2':
            result = subtract(a, b)
            operation = f"{a} - {b} = {result}"
        elif choice == '3':
            result = multiply(a, b)
            operation = f"{a} * {b} = {result}"
        elif choice == '4':
            result = divide(a, b)
            operation = f"{a} / {b} = {result}"
        else:
            print("Neplatná volba. Zkuste to znovu.")
            continue

        print("Výsledek:", result)
        history.append(operation)

calculator()

