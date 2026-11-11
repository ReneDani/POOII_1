# Escriba su solución aquí
NCoop = 0
NTEC = 0
NCoopTEC =0
for i in range(1,31):
     if (i%3) ==0 and (i%5)==0:
       NCoopTEC = NCoopTEC +1
       print("CoopTEC")
     elif (i%5) ==0:
       NTEC= NTEC +1
       print("TEC")
     elif (i%3) == 0:
       NCoop = NCoop +1 
       print("Coop")      
print("En total se Imprimio la palabra Coop :",NCoop," veces")
print("En total se Imprimio la palabra TEC:",NTEC," veces")
print("En total se Imprimio la palabra CoopTEC :",NCoopTEC," veces")