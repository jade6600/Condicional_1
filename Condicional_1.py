#input 
cant_minutos=input("Digite cantidad,minutos: ")
cant_minutos=int(cant_minutos)

#processing
if cant_minutos <= 3: 
    valor_llamada= 300
else:
    valor_llamada= 300+50*(cant_minutos-3)

#output
print("El valor de la llamada es: " +str (valor_llamada))