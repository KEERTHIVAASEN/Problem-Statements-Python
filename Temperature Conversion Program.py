print("Temperature conversion Program")
print("------------------------------")
print("1.Celsius to Fahrenheit.")
print("2.Fahrenheit to Celsius.")
ch=int(input("Enter your Choice 1/2:"))
if ch==1:
 print("Celsius to Fahrenheit")
 celsius = float(input("Enter Celsius:"))
fahrenheit = (celsius * 1.8) +32
print('%0.1f degree celsius = %0.1f degree fahrenheit' %(celsius,fahrenheit))
if ch==2:
 print("Fahrenheit to Celsius")
 fahrenheit = float(input("Enter fahrenheit:"))
celsius =(fahrenheit - 32)/1.8
print('%0.1f degree fahrenheit = %0.1f degree celsius' %(fahrenheit,celsius))