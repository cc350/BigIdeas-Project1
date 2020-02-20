name = input("Input a name: ")
alphabet = "ABCDEFGHIJKLMNOPQRSTUVQXYZ0123456789,.?!@#$"
print("Here is our alphabet: " + alphabet)
length = len(alphabet)
plaintext = input("Input a message for us to encrpt using a Caesar Cypher: ")
shift = ""
while(type(shift) is not int):
  shift = input("What shift would you like to use?\n(Enter an integer [0," + str(length) + "): ")
  try: 
    shift = int(shift)
  except: 
    shift = ""
ciphertext = ""
plaintext = plaintext.upper()
for c in plaintext: 
  if c in alphabet: 
    index = alphabet.index(c)
    index = index + shift
    index = index % length
    ciphertext += alphabet[index]
  else: 
    print(c + " is not a valid symbol in our alphabet.")
    cophertext += " "
print("Hello, " + name + "! Your encrypted message is: " + ciphertext)
