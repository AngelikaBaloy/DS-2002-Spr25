# Lab 3 script 2 
#!/Users/angelikabaloy/DS-2002-Spr25/.venv/bin/python3

import os

# assigning var 
os.environ["computing_id"] = "ybm4rn"
os.environ["hometown"] = "Norfolk"
os.environ["uva_year"] = "2"

# prompt for input > fetch/print var
computing_id = input("What is your computing id?")
print(os.getenv("computing_id"))

hometown = input("What is your hometown?")
print(os.getenv("hometown"))

uva_year = input("What year are you?")
print(os.getenv("uva_year"))
 