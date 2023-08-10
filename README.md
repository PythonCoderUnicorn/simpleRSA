# simpleRSA
a simple Python program to learn how RSA cryptography works


What the program looks like

```
  ------------------------------------------
      
  ooooooooo.    .oooooo..o       .o.       
  `888   `Y88. d8P'    `Y8      .888.      
  888   .d88' Y88bo.          .8"888.     
  888ooo88P'   `"Y8888o.     .8' `888.    
  888`88b.         `"Y88b   .88ooo8888.   
  888  `88b.  oo     .d8P  .8'     `888.  
  o888o  o888o 8""88888P'  o88o     o8888o
      
  Rivest-Shamir-Adleman public-key cryptosystem
      
      * for education only ! *
  ------------------------------------------
      

Enter p: 11
Enter q: 13
numbers are prime ✅
n = 143 | bits: 3 | length: 4
GCD = 143
Phi = 120
number of e keys: 27
🔑 e = 7 (1st key in array)
number of d keys: 8
🔑 d = 223 (1st key in array)

-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
 Public Key 🔑 : (7, 143)
 Private Key 🔒 : (223, 143)
-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```

This code followed a blog explanation and is meant to be used for educational purposes. This is why the 1st element in the key arrays are selected for examples. 

## 

- to encrypt `k` (k is an integer) : `kd = k^e % n`
- to decrypt `k` (kd is key to decrypt) `k = kd^d % n`






