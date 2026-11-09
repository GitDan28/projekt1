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
		mennyiseg = int(mennyiseg)

		for termek in lista:
			if termek["nev"] == nev:
				termek["mennyiseg"] += mennyiseg
				break

		else:
			termek = {
				"nev": nev,
				"mennyiseg": int(mennyiseg)
				}
			lista.append(termek)
	return lista
lista = lista_beolvasas()

def adat_modositas(lista):

	while True:
		try:
			db = int(input("Hány terméket szeretnél felírni?"))

		except ValueError:
			print("Számot adj meg, kérlek!")

		else:
			if db == 0:
				print("Nem adtál meg terméket!")
				return lista

			elif db < 0:
				print("Pozitív egész számot adj meg!")

			else:
				break

	for i in range(db):
		nev = input("Mi kell a boltból?")

		while True:
			try:
				mennyiseg = int(input("Mennyi kell belőle?"))
				if mennyiseg > 0:
					break
				else:
					print("pozitív egész számot adj meg!")

			except ValueError:
				print("Számot adj meg, kérlek!")

		for termek in lista:
			if termek["nev"] == nev:
				while True:
					valasz = input(
						f"A termék már a listán van {termek['mennyiseg']} db-bal. "
						"Hozzáadjam vagy levonjam a megadott mennyiséget? "
						"(add hozzá/vond le) "
						)

					if valasz == "add hozzá":
						termek["mennyiseg"] += mennyiseg
						break

					elif valasz == "vond le":
						termek["mennyiseg"] -= mennyiseg

						if termek["mennyiseg"] <= 0:
							lista.remove(termek)
						break

					else:
						print("Nem ismert válasz. Írd be: (add hozzá/vond le)")

				break

		else:
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
