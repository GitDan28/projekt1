#!/home/rebeka/programs/python_venv/bin/python

bevasarlas = ["kenyér", "tej", "tojás", "sajt", "vaj"]

fkeres = input("Milyen terméket keresel?")

if fkeres not in bevasarlas:

	kerdezzfelel = input(fkeres + " nincs a listán. Felírjam?")

	if kerdezzfelel == ("igen") or kerdezzfelel == ("aha") or kerdezzfelel == ("ja"):
		bevasarlas.append(fkeres)
		print (bevasarlas)

	elif kerdezzfelel == ("nem") or kerdezzfelel == ("ne"):
		print (bevasarlas)

elif fkeres in bevasarlas:

	kerdezzfelel = input(fkeres + " már rajta van a listán. Töröljem?")

	if kerdezzfelel == ("igen") or kerdezzfelel == ("töröld") or kerdezzfelel == ("aha") or kerdezzfelel == ("ja"):
		bevasarlas.remove(fkeres)
		print (bevasarlas)

	elif kerdezzfelel == ("nem") or kerdezzfelel == ("ne"):
		print (bevasarlas)
