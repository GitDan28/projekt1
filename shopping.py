#!/home/rebeka/programs/python_venv/bin/python

bevasarlas = open("bevasarlas.txt", "a")
bevasarlas.close()

def lista_beolvasás():
	lista = []

	with open("bevasarlas.txt", "r") as bevasarlolista:
		tartalom = bevasarlolista.readlines()

	for adat in tartalom:
		adat = adat.strip()
		lista.append(adat)

	return lista
lista = lista_beolvasas()

db = int(input("Hány terméket fogsz a bevásárló listára írni?"))

for i in range(db):
	fkeres = input("Mit írjunk fel?")

	if fkeres in lista:
		kerdezzfelel = input(fkeres + " már rajta van a listán. Töröljem?")

		if kerdezzfelel == ("igen") or kerdezzfelel == ("töröld") or kerdezzfelel == ("aha") or kerdezzfelel == ("ja"):
			lista.remove(fkeres)

	elif fkeres not in lista:
		kerdezzfelel = input(fkeres + " nincs a listán. Felírjam?")

		if kerdezzfelel == ("igen") or kerdezzfelel == ("aha") or kerdezzfelel == ("ja"):
			lista.append(fkeres)

with open("bevasarlas.txt", "w") as iras:

	for adat in lista:
		iras.write(adat + "\n")

print ("Ezek a termékek kellenek a boltból:\n")

for adat in lista:
	print (adat)

