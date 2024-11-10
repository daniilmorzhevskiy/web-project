import os
from load_dotenv import load_dotenv

load_dotenv()

name = os.getenv("NAME")
password = os.getenv("PASSWORD")

print("Hellow, world")
print(f"My name is {name}")
print(f"My password is {password}")

for i in range(1, 11):
    print(f"Your number is {i}")

with open("colour.txt", "r+") as f:
    print(f.read())

with open("horse.txt", "r+") as f:
    print(f.read())

rabbit = """
            /|      __
           / |   ,-~ /
          Y :|  //  /
          | jj /( .^
          >-"~"-v"
         /       Y
        jo  o    |
       ( ~T~     j
        >._-' _./
       /   "~"  |
      Y     _,  |
     /| ;-"~ _  l
    / l/ ,-"~    \
    \//\/      .- \
     Y        /    Y    -Row
     l       I     !
     ]\      _\    /"\
    (" ~----( ~   Y.  )
~~~~~~~~~~~~~~~~~~~~~~~~~\\
"""

print(rabbit)
