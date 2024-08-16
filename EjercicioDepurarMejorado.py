opciones={
    "izquierda": "Te encontaste con un dragon",
    "derecha": "Encontraste un tesoro",
    "delante": "Caiste en un pozo",
    "Izquierda": "Te encontaste con un dragon",
    "Derecha": "Encontraste un tesoro",
    "Delante": "Caiste en un pozo",
    "IZQUIERDA": "Te encontaste con un dragon",
    "DERECHA": "Encontraste un tesoro",
    "DELANTE": "Caiste en un pozo"}
eleccion=input("Estas en un cruce, ¿Quieres ir a la derecha, izquierda o adelante?: ")

if eleccion in opciones:
    print("Respuesta:", opciones[eleccion])
else:
    print("opcion equivocada")
    