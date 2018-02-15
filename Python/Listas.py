print("hi")
print("""
	live

	live

	live
""")
print("like")
print(5+3+2)
print("talk")
first = "\nlaura" + " " + "all"
print(first)
last = "python"
print(last)
full = first + last
print(full)
print(5==10)
print(5<10)
print(5!=10)

num = 8
if num<3 and num==3 or num==8:
	print("Retreat!")
	print("Raice the white")
elif num==5:
	print("yes")
else:
	print("NOT")
uno=1
dos=2
day = int(input("dame un numero"))
print("you entered", day)
daytwo = int(input("dame otro numero"))
print("you entered", daytwo)
daytres = (day * daytwo)

lista = [19,10]
lista.append(12)
lista.append(15)
lista.append(daytres)
	


archivo=open("Nombres.txt", "r")
variabledos= archivo.readlines()
variabledos.sort()
for linea in variabledos:

	lista.append(int(linea))
lista.sort()
print(variabledos)
promedio = sum(lista) / len(lista)
print(promedio)
print(lista)




