from person import Person
from ventilador import Ventilador

ventilador1 = Ventilador('branco', 250, 220, 100)
person1 = Person('Fabio', 1000)
person1.comprar_ventilador(ventilador1)

ventilador2 = Ventilador('branco', 250, 220, 10000)
person2 = Person('Maria', 1000)
person2.comprar_ventilador(ventilador2)

print(person1)
print(person2)
