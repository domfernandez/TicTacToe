global user_input
global user_coordinates
global user_lst
global new_input
global coord_input
global x_user
global o_user

x_user = True
o_user = False

user_input = []
user_lst = []
user_coordinates = []

def board_display(usr_input) :
    global user_input
    print(f"{'-' * len(usr_input)}")
    print("|" + " " + usr_input[0] + " " + usr_input[1] + " " + usr_input[2] + " " + "|")
    print("|" + " " + usr_input[3] + " " + usr_input[4] + " " + usr_input[5] + " " + "|")
    print("|" + " " + usr_input[6] + " " + usr_input[7] + " " + usr_input[8] + " " + "|")
    print(f"{'-' * len(usr_input)}")

def coord_check(usr_input):
    global new_input
    global user_input
    global x_user
    global o_user
    global coord_input

    coord_input = True
    usr_ip_position = 0

    while coord_input:
        user_coord = input("Enter Two Numerals, Separated By Space: ")
        if len(user_coord) != 3:
            print("Co-ordinates should be Two Numerals Separated By Space!")
        else:
            coord_trim = user_coord[0] + user_coord[2]
            if coord_trim.isnumeric():
                if int(coord_trim[0]) >= 1 and int(coord_trim[0]) <= 3 and int(coord_trim[1]) >= 1 and int(coord_trim[1]) <= 3 :
                    if coord_trim == "11":
                        usr_ip_position = 0
                    elif coord_trim == "12":
                        usr_ip_position = 1
                    elif coord_trim == "13":
                        usr_ip_position = 2
                    elif coord_trim == "21":
                        usr_ip_position = 3
                    elif coord_trim == "22":
                        usr_ip_position = 4
                    elif coord_trim == "23":
                        usr_ip_position = 5
                    elif coord_trim == "31":
                        usr_ip_position = 6
                    elif coord_trim == "32":
                        usr_ip_position = 7
                    elif coord_trim == "33":
                        usr_ip_position = 8

                    new_input = ""
                    if user_input[usr_ip_position] == "X" or user_input[usr_ip_position] == "O":
                        print("This cell is occupied! Choose another one!")
                    else:
                        for i in range(0, 9):
                            if i == usr_ip_position:
                                if user_input[i] == "X" or user_input[i] == "O":
                                    print("This cell is occupied! Choose another one!")
                                else:
                                    if x_user == True:
                                        new_input = new_input + "X"
                                        x_user = False
                                    else:
                                        new_input = new_input + "O"
                                        o_user = False
                                        x_user = True
                            else:
                                new_input = new_input + user_input[i]

                        board_display(new_input)
                        user_input = new_input
                        XO_check(user_input)
            else:
                print("Coordinates should be from 1 to 3!")

def XO_check(usr_lst):
    #    global user_input
    global coord_input
    count_XO = user_input.count('X') + user_input.count('O')

    if count_XO > 4:
        if usr_lst[0] == usr_lst[1] == usr_lst[2] == 'X':
            coord_input = False
            print("X wins")
        elif usr_lst[0] == usr_lst[1] == usr_lst[2] == 'O':
            coord_input = False
            print("O wins")
        elif usr_lst[3] == usr_lst[4] == usr_lst[5] == 'X':
            coord_input = False
            print("X wins")
        elif usr_lst[3] == usr_lst[4] == usr_lst[5] == 'O':
            coord_input = False
            print("O wins")
        elif usr_lst[6] == usr_lst[7] == usr_lst[8] == 'X':
            coord_input = False
            print("X wins")
        elif usr_lst[6] == usr_lst[7] == usr_lst[8] == 'O':
            coord_input = False
            print("O wins")
        elif usr_lst[0] == usr_lst[3] == usr_lst[6] == 'X':
            coord_input = False
            print("X wins")
        elif usr_lst[0] == usr_lst[3] == usr_lst[6] == 'O':
            coord_input = False
            print("O wins")
        elif usr_lst[1] == usr_lst[4] == usr_lst[7] == 'X':
            coord_input = False
            print("X wins")
        elif usr_lst[1] == usr_lst[4] == usr_lst[7] == 'O':
            coord_input = False
            print("O wins")
        elif usr_lst[2] == usr_lst[5] == usr_lst[8] == 'X':
            coord_input = False
            print("X wins")
        elif usr_lst[2] == usr_lst[5] == usr_lst[8] == 'O':
            coord_input = False
            print("O wins")
        elif usr_lst[0] == usr_lst[4] == usr_lst[8] == 'X':
            coord_input = False
            print("X wins")
        elif usr_lst[0] == usr_lst[4] == usr_lst[8] == 'O':
            print("O wins")
        elif usr_lst[2] == usr_lst[4] == usr_lst[6] == 'X':
            coord_input = False
            print("X wins")
        elif usr_lst[2] == usr_lst[4] == usr_lst[6] == 'O':
            print("O wins")
            coord_input = False
        elif count_XO == 9:
            print("Draw")
            coord_input = False


# write your code here
user_input = "         "
board_display(user_input)
coord_check(user_input)

