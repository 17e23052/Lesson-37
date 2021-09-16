def cipher(key):
 caesar = {"":""}
 x = 65 #65 is the ASCII value for A.
 while x < 91:
   number = x + key #This adds the key value.
   if number > 90: #If the cipher goes above the ASCII value of Z,
     number = number - 26 #It minuses 26 as to roll back to letter A.
   caesar[chr(x)] = chr(number) #This stores the letter in the dictionary.
   x = x + 1
 return caesar #This returns the dictionary.
 
print("What is the encryption key?")
key = int(input()) #Input the encryption key.
caesar = cipher(key)
print("Enter the text to encrypt:")
text = input().upper() #Input text to encrypt. It translates it to upper case.
text2 = ""
for letter in text:
 try:
  text2 = text2 + caesar[letter] #This encrypts each letter.
 except:
   text2 = text2 + letter #This prints any string that is not a letter.
print("Encrypted text:")
print(text2) #The encrypted text is printed at the end.