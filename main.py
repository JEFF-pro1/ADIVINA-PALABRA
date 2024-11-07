import random

# Lista de palabras (puedes agregar más palabras si deseas)
palabras = [
    "manzana", "plátano", "naranja", "fresa", "cereza", "kiwi", "pera",
    "mango", "sandía", "uva", "piña", "melón", "frambuesa", "arándano", 
    "coco", "papaya", "mandarina", "granada", "limón", "durazno", "aguacate"
]

# Función para obtener un número que representa la cercanía de una palabra
def calcular_diferencia(palabra1, palabra2):
    return sum([1 for i in range(min(len(palabra1), len(palabra2))) if palabra1[i] != palabra2[i]])

# Juego principal
def juego_adivinanza():
    print("Bienvenido al juego de adivinanza de palabras.")
    print("Debes adivinar una palabra de la lista.")
    
    palabra_secreta = random.choice(palabras)
    intentos = 0
    
    while True:
        palabra_usuario = input("\nEscribe una palabra: ").lower()
        
        if palabra_usuario not in palabras:
            print("La palabra no está en la lista. Intenta con otra.")
            continue
        
        intentos += 1
        
        # Calcular la diferencia entre la palabra adivinada y la secreta
        diferencia = calcular_diferencia(palabra_usuario, palabra_secreta)
        
        if palabra_usuario == palabra_secreta:
            print(f"¡Felicidades! Adivinaste la palabra '{palabra_secreta}' en {intentos} intentos.")
            break
        elif diferencia == 0:
            print(f"¡Estás muy cerca! La palabra es exactamente igual.")
        else:
            print(f"La palabra '{palabra_usuario}' tiene una diferencia de {diferencia} letras con la palabra secreta.")
    
# Iniciar el juego
if __name__ == "__main__":
    juego_adivinanza()
