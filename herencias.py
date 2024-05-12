from datetime import date


    


class Producto:
    def __init__(self, identifyer, p_name, price, description):
        self.identifyer = identifyer
        self.p_name = p_name
        self.price = price
        self.description = description

        self.validar_tipos()
        self.validar_inputs()

    def __repr__(self):
        return f"ID: {self.identifyer}, p_name: {self.p_name}, Precio: {self.price}, Descripción: {self.description}"
    
    def validar_tipos(self):
        if not isinstance(self.identifyer, int):
            raise TypeError("The identifyer must be an integer")
        
        if not isinstance(self.p_name, str):
            raise TypeError("The product name must be a String")

        if not isinstance(self.price, float):
            raise TypeError("The prices must be a float")
        
        if not isinstance(self.description, str):
            raise TypeError("Description must be a String")




    def validar_inputs(self):
        if self.identifyer <= 0:
            raise TypeError("Identifyer number must be above 0")
        
        if len(self.p_name) < 5:
            raise TypeError("Product name has to be more of five characters")
        
        if self.price <= 0:
            raise TypeError("Price can´t be 0 or negative")
        
        if not (len(self.description) < 20 or len(self.description) > 5):
            raise TypeError("Description must be between 5 and 20 characters")

       

class ProductoAlimenticio(Producto):
    def __init__(self, identifyer, p_name, price, description, expires):
        super().__init__(identifyer, p_name, price, description)
        
        self.expires = expires

        self.validar_expires()

    def __repr__(self):
        return f"ID: {self.identifyer}, p_name: {self.p_name}, Precio: {self.price}, Descripción: {self.description}, Expires: {self.expires}"
    
    def validar_expires(self):

        if self.expires < date.today():
            raise ValueError("La fecha no puede ser anterior al dia de hoy")  
        
class ProductoFresco(ProductoAlimenticio):
    def __init__(self, identifyer, p_name, price, description, expires, origin):
        super().__init__(identifyer, p_name, price, description, expires)         

        self.origin = origin