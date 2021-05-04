import random
import time


print("╔═══╗             ╔═══╗        
║╔═╗║             ║╔═╗║        
║╚═╝║╔══╗ ╔══╗╔══╗║║ ╚╝╔══╗╔═╗ 
║╔══╝╚ ╗║ ║══╣║══╣║║╔═╗║╔╗║║╔╗╗
║║   ║╚╝╚╗╠══║╠══║║╚╩═║║║═╣║║║║
╚╝   ╚═══╝╚══╝╚══╝╚═══╝╚══╝╚╝╚╝
                               
                               
")
print("                                                                           
                                                                           
                                                                           
╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗
╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝
                                                                           
                                                                           
                                                                           
")
print("Please answer some questions in order to generate your password...")
time.sleep(2)

def passwordgen(length):
    capital_fav_song = fav_song.capitalize()
    char = [capital_fav_song, str(fav_num1), str(fav_num2), fav_symbol, fav_color]
    for w in range(length):
        password = ''.join(random.sample(char, length))
        print("Password number {0} : ".format(w), password)
    return " Check how strong is your password on these sites: https://password.kaspersky.com or https://www.security.org/how-secure-is-my-password "

fav_num1= int(input("What's your favorite first number between [0-9] >> "))
fav_num2 = int(input("What's your favorite second number between [0-9] >> "))
fav_song = input("What's your favorite song's name [NO SPACES] >> ")
fav_color = input("What's your favorite color >> ")
fav_symbol = input("Choose one of these symbols [ !, @, #, $, %, ^, &, *, _, + ]: ")
fav_symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '_', '+']


if fav_num1 not in range(0, 10):
    print("Please choose your favorite first number between [0-9] ")
    exit()
elif fav_num2 not in range(0, 10):
    print("Please choose your favorite second number between [0-9] ")
    exit()
elif fav_symbol not in fav_symbols:
    print("Please choose one of these symbols [ @, #, $, %, & ] ")
    exit()
else:
    print(passwordgen(5))








