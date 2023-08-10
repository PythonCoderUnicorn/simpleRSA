

# ----------------------------
# 
# by: PythonCoderUnicorn
# date: Aug 10, 2023
# description: This program is to show how the RSA algorithm works in a simple way for education.
# 
# ----------------------------


# ---------- VARIABLES
# - `p` , `q` are large prime numbers
# - `n` is product of p and q
# - public key = `n` , `e`
# - private key = `n` , `d`
# - plaintext message `m`
# - cipher encrypted message `c`

# -------- Reference -------
# https://docs.sympy.org/latest/modules/ntheory.html#sympy.ntheory.primetest.isprime

# --- Thanks to 
# https://muirlandoracle.co.uk/2020/01/29/rsa-encryption/
# for learning basis for this program


import math
from sympy.ntheory import isprime



print("""
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
      
""")

p = int(input("Enter p: "))
q = int(input("Enter q: "))

if p > 1 and q > 1:
  
  pp = isprime(p)
  qp = isprime(q)

  if pp and qp == True:
    n = p * q 
    bc = p.bit_count()
    bl = p.bit_length()
    phi = (p -1) * (q -1)
    gcd = math.gcd(n) 

    print("numbers are prime ✅") 
    print(f"n = {n} | bits: {bc} | length: {bl}")
    print(f"GCD = {gcd}")
    print(f"Phi = {phi}")

    # --- find encryption key 'e'   2 < e < phi
    possible_keys = []
    for x in range(2, phi):
       if math.gcd(n, x)== 1 and math.gcd(phi, x) == 1:
          possible_keys.append(x)
    print(f"number of e keys: {len(possible_keys)}")
    # print(f"possible keys: {possible_keys}")

    # e
    e = possible_keys[0]
    print(f"🔑 e = {e} (1st key in array)")


    # ----- find 'd' private decryption key
    possible_dkeys = []
    for x in range(phi +1, phi +1000):
       if x * e % phi == 1:
          possible_dkeys.append(x)
    print(f"number of d keys: {len(possible_dkeys)}")
    # print(f"possible d keys: {possible_dkeys}")

    # d
    d = possible_dkeys[0]
    print(f"🔑 d = {d} (1st key in array)")

    print("\n-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
    print(f" Public Key 🔑 : ({e}, {n})")
    print(f" Private Key 🔒 : ({d}, {n})")
    print("-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#\n")

    # encrypt k: kd = k^e % n
    # decrypt k: k = kd^d % n




    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")




  else:
      n = p * q 
      gcd = math.gcd(p, q)
      print(" p & q not prime")
      print(f"n = {n} ")
      print(f"GCD = {gcd}")
      print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")

else:
   print(" use values >1")





