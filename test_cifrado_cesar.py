import cifrado_cesar

def test_cifrado_simple_con_distancia():
    assert cifrado_cesar.cifrar("zig", 3) == "BLJ"
    assert cifrado_cesar.cifrar("blj", -3) == "ZIG"

def test_cifrado_simple_con_caracteres_raros():
    assert cifrado_cesar.cifrar("hola, mundo!", 1) == "IPMB,ANVÑEP!"        

def test_crea_cifrador():
    cifrador2 = cifrado_cesar.creaCifrador(2)
    assert cifrador2("A Z") == "CBA"

def test_crea_par_cessar():
    cifra2, descifra2 = cifrado_cesar.creaParCesar(2)
    assert cifra2("A Z") == "CBA"
    assert descifra2("CBA") == "A Z"


