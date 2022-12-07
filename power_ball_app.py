
# command to choose color

import colorama
from colorama import Fore
colorama.init(autoreset=True)


# Here we call  the White_ball class from power_ball_utiles file -
# that has winner and lucky random number from (1,20)
from power_ball_utiles import White_ball


# Here we call  the Power_ball class from power_ball_utiles file -
# that has big_ball and big_ball2 random number from (1,10
from power_ball_utiles import Power_ball


# And here we have the Result class that make the the white_ball class value in the list
# by using  (list.append) and sort them in order by using (list.sort)
# and print with color

class Result:
    random_numbers = White_ball()
    random_numbers.winner()
    winner_ball = Power_ball()
    winner_ball.big_ball1()
    lucky_ball = Power_ball()
    lucky_ball.big_ball2()


    list = []
    list.append(random_numbers.num1)
    list.append(random_numbers.num2)
    list.append(random_numbers.num3)
    list.append(random_numbers.num4)
    list.append(random_numbers.num5)
    list.sort()


    random_numbers.lucky()


    list2 = []
    list2.append(random_numbers.num1)
    list2.append(random_numbers.num2)
    list2.append(random_numbers.num3)
    list2.append(random_numbers.num4)
    list2.append(random_numbers.num5)
    list2.sort()


    print()
    print("Today's Powerball Winning Numbers:\n")
    print(Fore.MAGENTA + str(list), Fore.LIGHTYELLOW_EX + str(winner_ball.unique_number), "\n")
    print("Your lucky numbers:\n")
    print(Fore.MAGENTA + str(list2), Fore.LIGHTYELLOW_EX + str(lucky_ball.unique_number), "\n")
    print("___________________________")


# in this step we have 2 counters the first one
# 1 , power_ball_counter =  that count the amount same  number we have from list if we have same in list2
# 2 , White_ball_counter  =  that count if the  two Power_balls same value or not

# and  calculate  the result of each result and display it

    power_ball_counter = 0
    white_ball_counter = 0
    for i in list2:
        if i in list:
            white_ball_counter = white_ball_counter + 1
    if winner_ball.unique_number == lucky_ball.unique_number:
        power_ball_counter = power_ball_counter + 1

    if white_ball_counter == 5 and winner_ball.unique_number == lucky_ball.unique_number:
        print(white_ball_counter,"Correct White Balls and the Powerball: Jackpot $324,000,000")
    elif white_ball_counter == 5 and winner_ball.unique_number != lucky_ball.unique_number:
        print(white_ball_counter, "correct white ball and no power ball 1,000,000$")
    elif white_ball_counter == 4 and winner_ball.unique_number == lucky_ball.unique_number:
        print(white_ball_counter, "correct white ball and no power ball 10,000$")
    elif white_ball_counter == 4 and winner_ball.unique_number != lucky_ball.unique_number:
        print(white_ball_counter, "correct white ball and no power ball 100$")
    elif white_ball_counter == 3 and winner_ball.unique_number == lucky_ball.unique_number:
        print(white_ball_counter, "correct white ball and the power ball 100$")
    elif white_ball_counter == 3 and winner_ball.unique_number != lucky_ball.unique_number:
        print(white_ball_counter, "correct white ball and no power ball 7$")
    elif white_ball_counter == 2 and winner_ball.unique_number == lucky_ball.unique_number:
        print(white_ball_counter, "correct white ball and the power ball 7$")
    elif white_ball_counter == 1 and winner_ball.unique_number == lucky_ball.unique_number:
        print(white_ball_counter, "correct white ball and the power ball 4$")
    elif white_ball_counter == 0 and winner_ball.unique_number == lucky_ball.unique_number:
        print(white_ball_counter, "correct white ball and the power ball 4$")
    else:
        print("Try again please!!!")