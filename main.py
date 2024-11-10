import os
from load_dotenv import load_dotenv

load_dotenv()

name = os.getenv("NAME")
password = os.getenv("PASSWORD")

print("Hellow, world")
print(f"My name is {name}")
print (f"My password is {password}")