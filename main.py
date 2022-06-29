import time
import math
import sys
import random
import os

x = 0
z = 1
z = 1
y = 0
n = 0
p = 0

number = random.randint(1000, 9999)

pre_save = 0
cookie_bal = 0
cookie_per_sec = 1
load = 0
#granny
gran = 0
gran_price = 15
gran_add = 1
gran_info = "Gran info:\n\nThe cost of one gran is 15 cookies.\n\nYes, we pay our workers in cookies, you may think well you're paying someone cookies to just make you more cookies. Yes, your exactly right except the grans are so old that they don't understand this.\n\nWhat a gran does is like what any other gran does make cookies but our grans are genetically modified to work 10x faster than your average gran and in 5x a smaller environment. We have complained that our grans are practical sweatshop workers but we think not as our grans are genetically modified not to feel mental or physical pain.\n\nTo return to info menu type *info*"

#farm
farm = 0
farm_price = 100
farm_add = 10
farm_info = "Farm info: \n \nThe cost of one farm is 100 cookies. \n Yes, that is right we pay pur farm with cookies which act as a fertaliser, you may think this is stupid ‘why fertalie farms with cookies, why not manur’ well its because oiur cookie plants taste like s**t literally if we do. Using fertilizer cookies adds a cookie depth to out cookies. \n \n What a farm does is obviously grows cookies just like a normal farm but with genetically modified wheat plants. The plant has been modified to have the wheat as a basis but also, eggs, butter, sugar and so on. So the plant literally grows cookies. It is the best method otherwise we wouldn't use it. We employ grans to work on the farm not as slaves but rather un-payed pensioners. \n \n To return to info menu type *info*"
#mine
mine = 0
mine_price = 5000
mine_add = 50
mine_info = ""
#factory
factory = 0
factory_price = 10000
factory_add = 1000
factory_info = ""
#bank
bank = 0
bank_price = 500000
bank_add = 10000
bank_info = ""

import loadingscreen

words = "Log-In or Make account\n"
for char in words:
    time.sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()
time.sleep(0.5)
username = input("Username: ")
password = input("Password: ")

import loading

newuser = 1
f = open("saves.txt", "r")
f1 = f.readlines()
for line in f1:
    line2 = line.split(":")
    if line2[0] == username and line2[1] != password:
        words = "That username already exists, what to do\n - If you spelt the password wrong then hit [Run >]\n - If your making a new account and want to use that username then try adding number onto the end E.G " + str(
            username
        ) + str(
            number
        ) + "\n - If you dont want to do any of these things then you might want to have a complety new username all together\n"
        for char in words:
            time.sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush
        import loading
        username = input("Username: ")
        password = input("Password: ")
    if line2[0] == username and line2[1] == password:
        mySave = line
        success = 1
        cookie_bal = line2[2]
        cookie_per_sec = line2[3]
        gran = line2[4]
        farm = line2[5]
        mine = line2[6]
        factory = line2[7]
        bank = line2[8]
        pre_save = line2[9]
        newuser = 0
        print("\nWelcome back " + username)
        time.sleep(2)
        import loading

if newuser == 1:
    import loading
    print("Welcome new user - " + username)
    time.sleep(2)
    import loading

    f = open("saves.txt", "a")
    f.write(username + ":" + password + ":" + str(cookie_bal) + ":" +
            str(cookie_per_sec) + ":" + str(gran) + ":" + str(farm) + ":" +
            str(mine) + ":" + str(factory) + ":" + str(bank) + ":" +
            str(pre_save))
    f.close()

x = 0

z = 1

while x == 0:
    try:
        if cookie_bal == int(10 * z):
            print("\033[H\033[J")
            y = y + 1
            n = n + 1
            words = "Cookie Balance Achievment Earned For Gaining More Than " + str(
                10 * z) + " Cookies!"
            for char in words:
                time.sleep(0.05)
                sys.stdout.write(char)
                sys.stdout.flush()
            print("\033[H\033[J")
            z = z * 10
            time.sleep(1)
        else:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\033[H\033[J")

        do = input("What do you want to do?\n  -  ")
        if do == 'save':
            savefile = ""
            f = open("saves.txt", "r")
            f1 = f.readlines()
            for l in f1:
                savefile = savefile + l
            f.close()
            mySave = username + ":" + password + ":" + str(
                cookie_bal) + ":" + str(cookie_per_sec) + ":" + str(
                    gran) + ":" + str(farm) + ":" + str(mine) + ":" + str(
                        factory) + ":" + str(bank) + ":" + str(pre_save)

            f2 = savefile.replace(
                mySave, username + ":" + password + ":" + str(cookie_bal) +
                ":" + str(cookie_per_sec) + ":" + str(gran) + ":" + str(farm) +
                ":" + str(mine) + ":" + str(factory) + ":" + str(bank) + ":" +
                str(pre_save))

            f = open("saves.txt", "w")
            f.write(f2)
            f.close()
            import loading
        elif do == 'buy gran':
            cookie_div = cookie_bal
            cookie_div = cookie_div // gran_price
            math.trunc(cookie_div)
            print("\033[H\033[J")
            multiply = input(
                "How many grans do you want to buy?  -  The max you can buy is "
                + str(f"{cookie_div:,}") +
                " or you can type *all*\nYour buying - ")
            if multiply == 'all':
                multiply = cookie_div
            import loading
            cookie_bank = cookie_bal
            cookie_bal = (cookie_bal) - (gran_price * int(multiply))
            if cookie_bal < 0:
                print("You dont have enough cookies!")
                import loading
                cookie_bal = cookie_bank
            elif cookie_bal >= 0:
                gran = int(gran) + int(multiply)
                cookie_per_sec = int(cookie_per_sec) + int(
                    int(gran_add) * int(multiply))
                print("\033[H\033[J")
                print("You own " + str(gran) + " grans!")
                import loading

        #buy farm...
        elif do == 'buy farm':
            cookie_div = int(cookie_bal)
            cookie_div = cookie_div // farm_price
            math.trunc(cookie_div)
            print("\033[H\033[J")
            multiply = input(
                "How many farms do you want to buy?  -  The max you can buy is "
                + str(f"{cookie_div:,}") +
                " or you can type *all*\nYour buying - ")
            if multiply == 'all':
                multiply = cookie_div
            import loading
            cookie_bank = cookie_bal
            cookie_bal = (cookie_bal) - (farm_price * int(multiply))
            if cookie_bal < 0:
                print("You dont have enough cookies!")
                cookie_bal = cookie_bank
            elif cookie_bal >= 0:
                farm = int(farm) + int(multiply)
                cookie_per_sec = int(cookie_per_sec) + int(
                    int(farm_add) * int(multiply))
                print("\033[H\033[J")
                print("You own " + str(farm) + " farms!")
        #buy mine...
        elif do == 'buy mine':
            cookie_div = cookie_bal
            cookie_div = cookie_div // mine_price
            math.trunc(cookie_div)
            print("\033[H\033[J")
            multiply = input(
                "How many mine do you want to buy?  -  The max you can buy is "
                + str(f"{cookie_div:,}") +
                " or you can type *all*\nYour buying - ")
            if multiply == 'all':
                multiply = cookie_div
            cookie_bank = cookie_bal
            cookie_bal = (cookie_bal) - (mine_price * int(multiply))
            if cookie_bal < 0:
                print("You dont have enough cookies!")
                cookie_bal = cookie_bank
            elif cookie_bal >= 0:
                mine = int(mine) + int(multiply)
                cookie_per_sec = int(cookie_per_sec) + int(
                    int(mine_add) * int(multiply))
                print("\033[H\033[J")
                print("You own " + str(mine) + " mines!")
        #factory
        elif do == 'buy factory':
            cookie_div = int(cookie_bal)
            cookie_div = cookie_div // factory_price
            math.trunc(cookie_div)
            print("\033[H\033[J")
            multiply = input(
                "How many factory do you want to buy?  -  The max you can buy is "
                + str(f"{cookie_div:,}") +
                " or you can type *all*\nYour buying - ")
            if multiply == 'all':
                multiply = cookie_div
            cookie_bank = cookie_bal
            cookie_bal = (cookie_bal) - (factory_price * int(multiply))
            if cookie_bal < 0:
                print("You dont have enough cookies!")
                cookie_bal = cookie_bank
            elif cookie_bal >= 0:
                factory = int(factory) + int(multiply)
                cookie_per_sec = int(cookie_per_sec) + int(
                    int(factory_add) * int(multiply))
                print("\033[H\033[J")
                print("You own " + str(factory) + " factorys!")
        #BANK
        elif do == 'buy bank':
            cookie_div = cookie_bal
            cookie_div = cookie_div // bank_price
            math.trunc(cookie_div)
            print("\033[H\033[J")
            multiply = input(
                "How many banks do you want to buy?  -  The max you can buy is "
                + str(f"{cookie_div:,}") +
                " or you can type *all*\nYour buying - ")
            if multiply == 'all':
                multiply = cookie_div
            cookie_bank = cookie_bal
            cookie_bal = (cookie_bal) - (bank_price * int(multiply))
            if cookie_bal < 0:
                print("You dont have enough cookies!")
                cookie_bal = cookie_bank
            elif cookie_bal >= 0:
                bank = int(bank) + int(multiply)
                cookie_per_sec = int(cookie_per_sec) + int(
                    int(bank_add) * int(multiply))
                print("\033[H\033[J")
                print("You own " + str(bank) + " bank!")
        elif do == 'shop':
            print(
                "In the shop we have\n - *buy gran* to buy a granny and the price is "
                + str(gran_price) +
                "!\n - *buy farm* to buy a farm and the price is " +
                str(farm_price) +
                "!\n - *buy mine* to buy a mine and the price is " +
                str(mine_price) +
                "!\n - *buy factory* to buy a factory and the price is " +
                str(factory_price) +
                "!\n - *buy bank* to buy a bank and the price is " +
                str(bank_price))
        elif do == 'info':
            print("\033[H\033[J")
            selection = input(
                "To view:\n1 - For gran\n2 - For farm\n3 - For mine\n4 - For factory\n5 - For bank\n\nWhat would you like info about - "
            )
            if selection == '1':
                print("\033[H\033[J")
                words = gran_info
                for char in words:
                    time.sleep(0.05)
                    sys.stdout.write(char)
                    sys.stdout.flush()
        else:
            print("\033[H\033[J")
            print("Error 404\nCheack case and spelling\nNow continuing...")

    else:
        print("\033[H\033[J")
        cookie_bal = (int(cookie_bal) + int(cookie_per_sec))
        print(
            "Help list:\n - To save the game type *save*\n - Cookies Per Second is "
            + str(cookie_per_sec) + "\n - You have earned " + str(y) +
            " achievments!\n - You own " + str(gran) + " grans\n - You own " +
            str(farm) + " farms\n - You own " + str(mine) +
            " mines\n - You own " + str(factory) + " factorys\n - You own " +
            str(bank) +
            " banks\n - Ctrl+c to start the command and then...\n - *info* To view item info and then type the item you want info about!"
            + "!\n\n" + str(cookie_bal) + " Cookies")
