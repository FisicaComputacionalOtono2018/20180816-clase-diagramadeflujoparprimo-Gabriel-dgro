#Autor: Gabriel Reyes
#Fecha: 16/08/2018
#Programa para excentar

S=12
A=2
B=1
P=input("Dame un numero: ")

while P%2==0:
	P=P+1
	if P%2!=0:
		while A<P:
			R=P%A
			if R==0:
				B=0
				break
			A=A+1
			while B==1:
				if P<S:
					S=S-P
					P=P+2
				else:
					S=S-1
					if S==0:
						print(P)
						break
					else: 
						P=P+2
			break
		P=P+2
