#Autor: Gabriel Reyes
#Fecha: 08/17/2018
#Programa con 3 whiles anidados

def isPrimeFor(N):
	flag=True
	for i in range (2,N/2+1):
		if N%i==0:
			flag=False
			break
	if N==1:
		flag=False
	return flag

P=input("Dame un numero: ")

if isPrimeFor(P):
	print("Es Primo")
else:
	print("No Es Primo")
