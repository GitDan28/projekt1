#!/home/rebeka/programs/python_venv/bin/python

bevasarlas = open("bevasarlas.txt", "a")
bevasarlas.close()

def lista_beolvasas():
	lista = []

	with open("bevasarlas.txt", "r") as bevasarlolista:
		tartalom = bevasarlolista.readlines()

	for adat in tartalom:
		adat = adat.strip()
		nev, mennyiseg = adat.split(";")

		termek = {
			"nev": nev,
			"mennyiseg": int(mennyiseg)
		}

		lista.append(termek)
	return lista
lista = lista_beolvasas()

def adat_modositas(lista):
	db = int(input("Hány terméket szeretnél felírni?"))

	for i in range(db):
		nev = input("Mi kell a boltból?")
		mennyiseg = int(input("Mennyi kell belőle?"))

		termek = {
			"nev": nev,
			"mennyiseg": mennyiseg
		}

		lista.append(termek)

	return lista
lista = adat_modositas(lista)

def lista_mentes(lista):
	with open("bevasarlas.txt", "w") as iras:

		for termek in lista:
			iras.write(termek["nev"] + ";" + str(termek["mennyiseg"]) + "\n")

lista_mentes(lista)

print ("Ezek a termékek kellenek a boltból:\n")

for termek in lista:
	print (f"{termek['nev']} {termek['mennyiseg']} db")