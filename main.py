def cipher(key):
 caesar = {"":""}
 x = 65
 while x < 91:
   number = x + key
   if number > 90:
     number = number - 26
   caesar[chr(x)] = chr(number)
   x = x + 1
 return caesar
 
print("What is the encryption key?")
key = int(input())
caesar = cipher(key)
print("Enter the text to encrypt:")
text = input().upper()
text2 = ""
for letter in text:
 try:
  text2 = text2 + caesar[letter]
 except:
   text2 = text2 + letter
print("Encrypted text:")
print(text2)