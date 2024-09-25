import random

def ordenador_decide_jugada():
    
    opciones=["piedra","papel","tijeras"]
    resultado=random.choice(opciones)
    
    return resultado

def usuario_decide_jugada():
    
    eleccion_usuario = input('Elige piedra, papel o tijeras: ')
    while eleccion_usuario not in ["piedra","papel","tijeras"]:
        print("Opción no válida")
        eleccion_usuario = input('Elige piedra, papel o tijeras: ')
    
    return eleccion_usuario

def determina_ganador(jugada_usuario,jugada_ordenador):
    print(f"El usuario ha elegido {jugada_usuario}, y el ordenador ha elegido {jugada_ordenador}")
    if jugada_usuario == jugada_ordenador:
        return "Empate"
    elif jugada_usuario == "piedra" and jugada_ordenador == "tijeras":
        return "El jugador ha ganado"
    elif jugada_usuario == "papel" and jugada_ordenador == "piedra":
        return "El jugador ha ganado"
    elif jugada_usuario == "tijeras" and jugada_ordenador == "papel":
        return "El jugador ha ganado"
    else:
        return "El ordenador ha ganado"

def jugar():
    print("Bienvenido al juego de Piedra, Papel o Tijeras \n")
    jugada_ordenador = ordenador_decide_jugada()
    jugada_usuario = usuario_decide_jugada()
    print(f"El ordenador ha elegido {jugada_ordenador}")
    resultado=determina_ganador(jugada_ordenador, jugada_usuario)
    print(f"Resultado: {resultado} \n")


if __name__ == "__main__":
    jugar()