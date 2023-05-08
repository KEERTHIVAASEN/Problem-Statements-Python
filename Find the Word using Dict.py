dict={"knowledge":"understanding","endeavour":"attempt","totemic":"resembling"}}
while True:
 print("\n1.search meaning \n2.add word\n3.exit")
 choice=int(input("Enter the choice"))
if choice==1:
   word=input("Enter the word to find meaning")
   if word in dict.keys():
    print("Meaning of",word,"is",dict[word])
   else:
    print("Word not in dictionary")
elif choice==2:
  word=input("Enter the word")
  meaning=input("Enter the meaning")
  dict[word]=meaning
  print("Word added successfully")
else:
  print("Exit")
  break