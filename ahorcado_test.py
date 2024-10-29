# ahorcado_test.py

import ahorcado

def test_mostrar_progreso():
    assert ahorcado.mostrar_progreso("python", ['p', 'y']) == 'p y _ _ _ _'

def test_verificar_letra():
    assert ahorcado.verificar_letra('p', 'python') is True
    assert ahorcado.verificar_letra('z', 'python') is False

