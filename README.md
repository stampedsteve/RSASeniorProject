# RSASeniorProject
Short implementation and explanation of the RSA algorithm in Python.

This project allows for the entering of prime numbers all the way up to 54601
This project was based off of the implementation of the RSA excel spreadsheet, which used quadgraphs,
This spreadsheet was limited to primes between 137 and 311. In order to exceed this limitation heptgraphs are used
These heptgraphs are able to work with up to 5 digit primes without losing data when converted into the encrypted message.
  
 Built With:
 
  ======Python programming language
  
  ======jupyter notebook
  
  ======replit online IDE
 
 When the code is run it will ask you for a p and q which must be prime numbers inbetween 137 and 54601
 After displaying the common factors of the euler totient it will ask you for a two digit number that does not share any of those factors
 The last thing the program will ask for is a message that has no spaces or caps, however this program is capable of correcting spaces and caps
 The program will then run through the encode and decode process and display most of the operations going on behind the scenes
 
 Limitations
  Because of the increasing length of the ciphernumber with an increasingly large p and q the limit for the primes is 54601
  This could be mitigated by scaling the graph size with the p and q size, however for this project that was unncesecary as the run time increases exponetially
  For this reason the code and notebook are freely available for modification along with the word document that breaks down every function
  The function could be sped up significantly if a faster modulus function is found, as this takes the bulk of the time
  
 Acknowledgements
  First 10,000 primes https://primes.utm.edu/lists/small/10000.txt
  
  RSA article https://en.wikipedia.org/wiki/RSA_(cryptosystem)
  
  article on key cryptographic systems https://pneumannsecurity.blogspot.com/2020/06/why-should-people-worry-about-existing.html
  
