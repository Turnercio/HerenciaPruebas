from herencias import *
import pytest

def test_producto():
    producto = Producto(1, "Libreta", 12.50, "Libreta azul")
    assert producto.identifyer == 1
    assert producto.p_name == "Libreta"
    assert producto.price == 12.50
    assert producto.description == "Libreta azul"

def test_producto_identifyer_number():
    with pytest.raises(TypeError):
        producto = Producto("id")
