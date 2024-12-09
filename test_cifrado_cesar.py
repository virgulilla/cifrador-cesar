import cifrado_cesar

assert cifrado_cesar.cifrar("zig", 3) == "BLJ"
assert cifrado_cesar.cifrar("blj", -3) == "ZIG"

cifrador2 = cifrado_cesar.creaCifrador(2)

assert cifrador2("A Z") == "CBA"

cifra2, descifra2 = cifrado_cesar.creaParCesar(2)
assert cifra2("A Z") == "CBA"
assert descifra2("CBA") == "A Z"


