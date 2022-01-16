import sys
import os

taken_spots = []

if sys.platform == 'win32': 
    clear = 'cls'
else: 
    clear = 'clear'

all_pos = ["a1","a2","a3","b1","b2","b3","c1","c2","c3"]

a1=" "
a2=" "
a3=" "
a4=" "
a5=" "
a6=" "
a7=" "
a8=" "
a9=" "

def print_board(a1,a2,a3,a4,a5,a6,a7,a8,a9):
    a1 = a1.upper()
    a2 = a2.upper()
    a3 = a3.upper()
    a4 = a4.upper()
    a5 = a5.upper()
    a6 = a6.upper()
    a7 = a7.upper()
    a8 = a8.upper()
    a9 = a9.upper()
    print("   A  B  C  ")
    print(f"1 {a1} | {a2} | {a3}")
    print("  ---------          ")
    print(f"2 {a4} | {a5} | {a6}")
    print("  ---------          ")
    print(f"3 {a7} | {a8} | {a9}")

def place(spot, user):
    global a1, a2, a3, a4, a5, a6, a7, a8, a9
    if spot.lower() not in ["a1","a2","a3","b1","b2","b3","c1","c2","c3"]:
        print("Invalid spot")
        return False
    else:
        if spot.lower() == "a1":
            if "a1" in taken_spots:
                print("Spot taken")
                return False
            else:
                a1 = user
                taken_spots.append(spot.lower())
        elif spot.lower() == "a2":
            if "a2" in taken_spots:
                print("Spot taken")
                return False
            else:
                a4 = user
                taken_spots.append(spot.lower())
        elif spot.lower() == "a3":
            if "a3" in taken_spots:
                print("Spot taken")
                return False
            else:
                a7 = user
                taken_spots.append(spot.lower())
        elif spot.lower() == "b1":
            if "b1" in taken_spots:
                print("Spot taken")
                return False
            else:
                a2 = user
                taken_spots.append(spot.lower())
        elif spot.lower() == "b2":
            if "b2" in taken_spots:
                print("Spot taken")
                return False
            else:
                a5 = user
                taken_spots.append(spot.lower())
        elif spot.lower() == "b3":
            if "b3" in taken_spots:
                print("Spot taken")
                return False
            else:
                a8 = user
                taken_spots.append(spot.lower())
        elif spot.lower() == "c1":
            if "c1" in taken_spots:
                print("Spot taken")
                return False
            else:
                a3 = user
                taken_spots.append(spot.lower())
        elif spot.lower() == "c2":
            if "c2" in taken_spots:
                print("Spot taken")
                return False
            else:
                a6 = user
                taken_spots.append(spot.lower())
        elif spot.lower() == "c3":
            if "c3" in taken_spots:
                print("Spot taken")
                return False
            else:
                a9 = user
                taken_spots.append(spot.lower())
        return True

def check_board(aa1,aa2,aa3,aa4,aa5,aa6,aa7,aa8,aa9):
    a1 = aa1.upper()
    a2 = aa4.upper()
    a3 = aa7.upper()
    b1 = aa2.upper()
    b2 = aa5.upper()
    b3 = aa8.upper()
    c1 = aa3.upper()
    c2 = aa6.upper()
    c3 = aa9.upper()
    if a1 == a2 == a3:
        return a1
    elif b1 == b2 == b3:
        return b1
    elif c1 == c2 == c3:
        return c1
    elif a1 == b1 == c1:
        return a1
    elif a2 == b2 == c2:
        return a2
    elif a3 == b3 == c3:
        return a3
    elif a1 == b2 == c3:
        return a1
    elif a3 == b2 == c1:
        return a3
    else:
        for pos in all_pos:
            if pos not in taken_spots:
                return False
            else:
                pass
        return "tie"


os.system(clear)
x_player = input("'X' Player, what is your name? ")
o_player = input("'O' Player, what is your name? ")
os.system(clear)
while True:
    print_board(a1,a2,a3,a4,a5,a6,a7,a8,a9)
    
    if check_board(a1,a2,a3,a4,a5,a6,a7,a8,a9) != False:
        if check_board(a1,a2,a3,a4,a5,a6,a7,a8,a9) == "X":
            print(f"{x_player} wins")
            break
        elif check_board(a1,a2,a3,a4,a5,a6,a7,a8,a9) == "O":
            print(f"{o_player} wins")
            break
        elif check_board(a1,a2,a3,a4,a5,a6,a7,a8,a9) == "tie":
            print("Tie")
            break
    else:
        pass

    while True:
        if place(input(f"{x_player}, where would you like to place your 'X'? "), "X") == False:
            pass
        else:
            break
    os.system(clear)
    print_board(a1,a2,a3,a4,a5,a6,a7,a8,a9)

    if check_board(a1,a2,a3,a4,a5,a6,a7,a8,a9) != False:
        if check_board(a1,a2,a3,a4,a5,a6,a7,a8,a9) == "X":
            print(f"{x_player} wins")
            break
        elif check_board(a1,a2,a3,a4,a5,a6,a7,a8,a9) == "O":
            print(f"{o_player} wins")
            break
        elif check_board(a1,a2,a3,a4,a5,a6,a7,a8,a9) == "tie":
            print("Tie")
            break
    else:
        pass

    while True:
        if place(input(f"{o_player}, where would you like to place your 'O'? "), "O") == False:
            pass
        else:
            break
    os.system(clear)