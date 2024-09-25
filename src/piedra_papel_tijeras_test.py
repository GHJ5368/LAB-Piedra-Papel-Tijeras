from piedra_papel_tijeras import *

def test_ordenador_decide_jugada():
    print("Testeando que el ordenandor decide una jugada...")
    resultado = ordenador_decide_jugada()
    print("El ordenandor ha elegido",resultado)

def test_usuario_decide_jugada():
    print("Testeando que el usuario decide una jugada...")
    resultado = usuario_decide_jugada()
    print("El usuario ha elegido",resultado)

def test_determina_ganador(eleccion_jugador, eleccion_ordenador):
    print("Testeando determina_ganador...")        
    print(f"Jugador: {eleccion_jugador} vs. Ordenador: {eleccion_ordenador}")
    resultado = determina_ganador(eleccion_jugador, eleccion_ordenador)
    print("Resultado:", resultado)



# Función principal
if __name__ == "__main__":
    test_ordenador_decide_jugada()
    test_usuario_decide_jugada()
    test_determina_ganador("piedra", "tijeras")
    test_determina_ganador("piedra", "papel")
    test_determina_ganador("piedra", "piedra")
    test_determina_ganador("tijeras", "tijeras")
    test_determina_ganador("tijeras", "papel")
    test_determina_ganador("tijeras", "piedra")
    test_determina_ganador("papel", "tijeras")
    test_determina_ganador("papel", "papel")
    test_determina_ganador("papel", "piedra")


