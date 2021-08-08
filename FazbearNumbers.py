import time
import random
import colorama
from colorama import Fore, Back, Style
colorama.init()
print(Fore.MAGENTA)
time.sleep(1.4)
print("""                ----------|
	        |. -------|
	        | |
	        | |
	        | |======
	        |.|
	        |.|
	        |-|""")
time.sleep(0.8)
print(Fore.YELLOW)
#sekilli yazmak zor
print("""
	         ==============\                       
	        |.              |
	        |.     ---      |
	        |.    |  |      |
	        |.     ---      |
	        |.               ----
	        |.    ------         |
	        |.    |     |         |
	        |.    |      |         |
	        |.     -------         |
	        |=====================""")
time.sleep(1)
print(Fore.BLUE)
print("""
         -------------
         |.    ----  |
         |.   |   |  |
         |.   ----   |
         |. _______  /
         |. |     | |
         |. |     | |
         |. |     | |
         |. |     | |
         |. |     | |
         |__|     |_|
""")
time.sleep(1)
print(Fore.MAGENTA + Back.BLUE)
print("FREDDY FAZBEAR EĞLENCEYE HOŞGELDİNİZ!")
time.sleep(2.5)
time.sleep(1)
time.sleep(0.9)
tutulan = random.randint(1 , 10)
söylenen = input('sence hangi sayıyı tuttum :')
if(söylenen==tutulan):
    print(Fore.YELLOW + Back.GREEN)
    print('Great job!👌!')
    
else:
    print(Fore.YELLOW + Back.RED)
    print('Bad👎')
    print(Fore.MAGENTA + Back.BLUE)
    print('Tutuğum sayı')
    time.sleep(1)
    print(tutulan)
