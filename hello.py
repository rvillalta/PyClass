for i in range(2):
    #var = str(i*10) + " Hola Mundo"
    print("el numeros es {}".format(i))
print("Termine !!")

ASD = 1.123456789

class Persona:
	def __init__(self, _nombre, _edad):
		self.nombre = _nombre
		self.edad = _edad

	def getInfo(self):
		print("Hola, me llamo {0} y tengo {1} anos".format(self.nombre, self.edad))

class Estudiante(Persona):
	def __init__(self, nom, ed, carrera):
		Persona.__init__(self, nom, ed)
		self.carrera = carrera
	def getInfo(self):
		print("Hola, me llamo {0} y tengo {1} anos y estudio {2}".format(self.nombre, self.edad, self.carrera))


raul = Persona("Raul", 23)
raul.getInfo()
ed = Estudiante("Ed", 23, "Ingenieria")
ed.getInfo()
