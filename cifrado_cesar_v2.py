from typing import Callable, Tuple

ALFABETO = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ '
LONGITUD_ALFABETO = len(ALFABETO)

def desplazar(letra: str, dist: int) -> str:
    if letra in ALFABETO:
        nueva_pos = (ALFABETO.find(letra) + dist) % LONGITUD_ALFABETO
        return ALFABETO[nueva_pos]
    return letra

def creaCifrador(dist: int) -> Callable:
    return lambda mensaje: ''.join(desplazar(letra, dist) for letra in mensaje.upper())

def creaParCesar(dist: int) -> Tuple[Callable, Callable]:
    cifrar = creaCifrador(dist)
    decifrar = creaCifrador(-dist)
    return cifrar, decifrar

# Crear funciones de cifrado y descifrado
cifrar, decifrar = creaParCesar(3)

# Frase de ejemplo
frase_original = "HOLA MUNDO"

assert cifrar('zig') == "BLJ"
assert decifrar('blj') == "ZIG"
    
# Cifrar la frase
frase_cifrada = cifrar(frase_original)
print(f"Frase cifrada: {frase_cifrada}")

# Descifrar la frase
frase_descifrada = decifrar(frase_cifrada)
print(f"Frase descifrada: {frase_descifrada}")

 