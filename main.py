"""
Bingo Card Generator
This will generate a BINGO card with 24 random numbers and a free space in the middle.
This is intended to be used to print a bingo card for the support staff to use for team building.
@author Michael Nickey
@date 12/31/2022
"""

import random


def columns(start, stop):
    x1 = random.randint(start, stop)
    x2 = x3 = x4 = x5 = x1
    while x2 == x1:
        x2 = random.randint(start, stop)
    while x3 == x1 or x3 == x2:
        x3 = random.randint(start, stop)
    while x4 == x1 or x4 == x2 or x4 == x3:
        x4 = random.randint(start, stop)
    while x5 == x1 or x5 == x2 or x5 == x3 or x5 == x4:
        x5 = random.randint(start, stop)
    return x1, x2, x3, x4, x5


def print_header():
    print("\n")
    print_line()
    print("*   B  *   I  *   N  *   G  *   O  *")


def print_first_row():
    print_line()
    print_spacer()
    print("*  {0:2d}  *  {1}  *  {2}  *  {3}  *  {4}  *"
          .format(b_column[0], i_column[0], n_column[0], g_column[0], o_column[0]))
    print_spacer()


def print_second_row():
    print_line()
    print_spacer()
    print("*  {0:2d}  *  {1}  *  {2}  *  {3}  *  {4}  *"
          .format(b_column[1], i_column[1], n_column[1], g_column[1], o_column[1]))
    print_spacer()


def print_third_row():
    print_line()
    print_spacer()
    print("*  {0:2d}  *  {1}  * {2} *  {3}  *  {4}  *"
          .format(b_column[2], i_column[2], "Free", g_column[2], o_column[2]))
    print_spacer()


def print_fourth_row():
    print_line()
    print_spacer()
    print("*  {0:2d}  *  {1}  *  {2}  *  {3}  *  {4}  *"
          .format(b_column[3], i_column[3], n_column[3], g_column[3], o_column[3]))
    print_spacer()


def print_last_row():
    print_line()
    print_spacer()
    print("*  {0:2d}  *  {1}  *  {2}  *  {3}  *  {4}  *"
          .format(b_column[4], i_column[4], n_column[4], g_column[4], o_column[4]))
    print_spacer()


def print_card():
    print_header()
    print_first_row()
    print_second_row()
    print_third_row()
    print_fourth_row()
    print_last_row()
    print_footer()
    
    
def print_footer():
    print_line()


def print_spacer():
    print("*      *      *      *      *      *")
    return


def print_line():
    print("*" * 36)


if __name__ == '__main__':
    b_column = columns(1, 15)
    i_column = columns(16, 30)
    n_column = columns(31, 45)
    g_column = columns(46, 60)
    o_column = columns(61, 75)
    print_card()
