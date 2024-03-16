def clasificar_edad(edad):
    if edad < 0:
        return "Edad inválida. Debe ser un número positivo."
    elif edad < 2:
        return "Infante"
    elif edad < 13:
        return "Niño/a"
    elif edad < 18:
        return "Adolescente"
    elif edad < 65:
        return "Adulto"
    else:
        return "Tercera edad"

    edad1 = 10
    edad2 = 25
    edad3 = 70
    edad4 = -5

    print(f"Edad 1: {clasificar_edad(edad1)}")
    print(f"Edad 2: {clasificar_edad(edad2)}")
    print(f"Edad 3: {clasificar_edad(edad3)}")
    print(f"Edad 4: {clasificar_edad(edad4)}")