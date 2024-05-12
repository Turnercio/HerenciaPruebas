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
        producto = Producto("id", "Libreta", 12.50, "Libreta azul")

def test_producto_identifyer_mayor_cero():
    with pytest.raises(TypeError):
        producto = Producto(-10, "Libreta", 12.50, "Libreta azul")   
        producto = Producto("-10", "Libreta", 12.50, "Libreta azul")  

def test_producto_pname_str_y_leng():
    with pytest.raises(TypeError):
        producto = Producto( 1, 12.50, 12.50, "Libreta azul")
        producto = Producto( 1, "abc", 12.50, "Libreta azul")

def test_price_mayor_cero_y_float():
    with pytest.raises(TypeError):
        producto = Producto( 1, "Libreta", "12.50", "Libreta azul")
        producto = Producto( 1, "Libreta", -12.50, "Libreta azul")

def test_description_type_and_len():
    with pytest.raises(TypeError):
        producto = Producto( 1, "Libreta", 12.50, 12.50)
        producto = Producto( 1, "Libreta", 12.50, "zul")    
        producto = Producto( 1, "Libreta", 12.50, "Libreta azul azul azul azul azul azul azul azul azulazulazul")    

def test_expires_type_and_today():
    with pytest.raises(TypeError):
        producto = ProductoAlimenticio(1, "Libreta", 12.50, "Libreta azul", "dslfahjksdñf")
        producto = ProductoAlimenticio(1, "Libreta", 12.50, "Libreta azul", date(2024, 5, 11))