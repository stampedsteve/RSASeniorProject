#!/usr/bin/env python
# coding: utf-8

# In[5]:


#2

#Ensures all message lengths are divisible by 3, by adding 'a' chars to fill in the message
def fillin(msg):
    count = 0
    while (len(msg)+count) % 3 != 0:
        count += 1
    return (msg + ('a'*count))

#Shaves off extra a characters when the message is output
def shave(msg, target):
    """
    count = -1
    char = msg[count]
    while char != target:
        msg = msg[:len(msg)-1]
        char = msg[count]
    return msg
    """
    msg = msg[:target]
    return msg

def pickppickq():
  p = int(input("Enter Prime Interger p between 137 and 54601: "))
  while isPrimeCandidate(p) == False:
    p = int(input("Enter Prime Interger p between 137 and 54601: "))
  q = int(input("Enter Different Prime Interger q between 137 and 54601: "))
  while isPrimeCandidate(q) == False:
    q = int(input("Enter Different Prime Interger q between 137 and 54601: "))
  return [p,q]

#Determines if number is within parameters
def isPrimeCandidate(prospectivePrime):
  if prospectivePrime < 137 or prospectivePrime > 54601:
    return False
  for num in range(2,prospectivePrime):
    if prospectivePrime % num == 0:
      return False
  return True

#3
#Unions the two factors list to provide list of all euler factors
def unionList(lista,listb):
  union = []
  for num in lista:
    if num in listb:
      union.append(num)
  return union

#Finds factors of any number through brute force
def findFactors(num):
  fac = []
  for i in range(1,num):
    if num % i == 0:
      fac.append(i)
  return fac

#Determines if two numbers are relatively prime
def isRelPrime(prime, num):
  while num > 99 or num < 0:
    num = int(input("Enter two digit integer"))
  n = findFactors(num)
  p = findFactors(prime)
  rels = unionList(n,p)
  if len(rels) > 1:
    return False
  return True

#Generates private key by finding first number multiplied by the public key that when % by euler totient produces 1
def privateKeyGen(pubKey, euler):
    count = 1
    privateCan = (count*pubKey)%euler
    while privateCan != 1:
        count+=1
        privateCan = (count*pubKey)%euler
    return count

#6
#Creates substrings from a string of any length desired
def subDivider(message, num, length):
  msg = message[:length]
  sub = []
  result = []
  count = 0
  for n in msg:
      sub.append(n)
      count += 1
      if count%num == 0:
         result.append(sub)
         sub = []
  return result

#Finds the number sum equivalent of a string
def tricode(message):
  trigraphs = subDivider(message, 3, len(message))
  crypt = []
  for graphs in trigraphs:
    count = 2
    code = 0
    for char in graphs:
      num = (ord(char) - 97) * 26**count
      count -= 1
      code += num
    crypt.append(code)
  return crypt

#Encodes tricode with the public key
def cipherCode(codes,pubKey,modulus):
  ciphernumbers = []
  for code in codes:
    ciphernum = (code**pubKey)%modulus
    ciphernumbers.append(ciphernum)
  print('CipherCodes Created:',ciphernumbers)
  return ciphernumbers

#Changes cipherCodes into readable text in blocks of seven
def heptgraph(cipherCodes):
  chars = ""
  for num in cipherCodes:
    count = 6
    while count != -1:
      s1 = int(num / 26**count)
      s2 = s1 % 26
      s3 = s2 + 97
      count-=1
      chars += chr(s3)
  return chars

#9
#Decodes Heptgraphs using the private key back into tricodes
def decodeHept(cryptmsg, privateKey, modulus):
  result = []
  codes = subDivider(cryptmsg, 7, len(cryptmsg))
  print('Hept Codes: ', codes, '\n')
  for quad in codes:
    d0 = (ord(quad[0])-97)*(26**6)
    d1 = (ord(quad[1])-97)*(26**5)
    d2 = (ord(quad[2])-97)*(26**4)
    d3 = (ord(quad[3])-97)*(26**3)
    d4 = (ord(quad[4])-97)*(26**2)
    d5 = (ord(quad[5])-97)*(26)
    d6 = (ord(quad[6])-97)
    num = d0+d1+d2+d3+d4+d5+d6
    print('Hept decoded into Cipher Code:', num, '\n')
    a = (num**privateKey)%modulus
    print('Cipher Code decoded into tri number', a, '\n')
    result.append(a)
  return result

#Decodes tricodes into plaintext substrings
def decodeTriNum(tricodes):
  result = ""
  for code in tricodes:
    char1 = int(code/(26**2))
    char2 = (int(code/26)) % 26
    char3 = code % 26
    result += (chr(char1+97))
    result += (chr(char2+97))
    result += (chr(char3+97))
    print('Tri number decoded into plaintext substring: ', result, '\n')
  return str(result)

#Creates all relevant numbers from p and q
def pickSet():
  [p,q] = pickppickq()
  modulus = p* q
  euler = (p-1) * (q-1)
  eulerFactors = findFactors(euler)
  print(' ')
  print('Euler Factors: ',eulerFactors,'\n')
  pubKey = int(input("Enter two digit number that shares no factors with euler: "))
  while isRelPrime(euler, pubKey) == False:
    pubKey = int(input("Enter two digit number that shares no factors with euler: "))
  privateKey = privateKeyGen(pubKey, euler)
  return [p,q,modulus,euler,pubKey,privateKey,eulerFactors]
  
# Running

print('This program will encrypt a plaintext message of any length with no spaces or numbers')
print('This is done using the RSA Algorithm, which will take two primes p and q to create a public and private key')

data = pickSet()
print('\n')

p = data[0]
q = data[1]
modulus = data[2]
euler = data[3]
pubKey = data[4]
privateKey = data[5]
eulerFactors = data[6]

print("p:", data[0])
print("q:", data[1])
print("modulus:", data[2])
print("Euler Totient:", data[3])
print("public Key:", data[4])
print("private Key:", data[5])

#Cleans string of spaces and uppercase letters
msg = str(input("Enter string no spaces or numbers: ")).lower()
print(msg)
msg = msg.replace(" ", "")
print(msg)


print('\n')

lastChar = len(msg)



def encode(msg, modulus, pubKey):
  msg = fillin(msg)
  tri = tricode(msg)
  print('tricodes:', tri, '\n')
  cryptedmessage = heptgraph(cipherCode(tri,pubKey,modulus))
  print('The encrypted message is: ',cryptedmessage, '\n')
  return cryptedmessage

def decode(cryptedmsg, modulus, privateKey):
  decoded = decodeHept(cryptedmsg, privateKey, modulus)
  print("Cipher Codes:", decoded , '\n')
  result = decodeTriNum(decoded)
  return result
  


cryptmsg = encode(msg, modulus, pubKey)
result = decode(cryptmsg, modulus, privateKey)
print('The decoded message is: ', shave(result, lastChar))


# In[ ]:





# In[ ]:




