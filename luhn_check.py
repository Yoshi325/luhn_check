#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#pylint: disable=C0326
"""\
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      -- Credit Card Number Luhn Check --      ┃
┃                                               ┃
┠───────────────────────────────────────────────┨
┃        Writen by Jamie Murdock 'b0dach'       ┃
┠───────────────────────────────────────────────┨
┃         Checks to see if numbers in a         ┃
┃         file or single input are valid        ┃
┃         credit card numbers                   ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""

import os
import sys
from textwrap import dedent

class BashColor:
    @staticmethod
    def _wrap(c, s):
        return "{0}{1}{2}".format(c, s, '\033[0m')
    @staticmethod
    def wrap_b(s):
        return BashColor._wrap('\033[94m', s)
    @staticmethod
    def wrap_r(s):
        return BashColor._wrap('\033[91m', s)
    @staticmethod
    def wrap_g(s):
        return BashColor._wrap('\033[92m', s)
    @staticmethod
    def wrap_y(s):
        return BashColor._wrap('\033[93m', s)

def luhn_checksum(card_number):
    """ Luhn check algorithm """
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits      = digits_of(card_number)
    odd_digits  = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum    = 0
    checksum   += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

def is_luhn_valid(card_number):
    return luhn_checksum(card_number) == 0

def is_card_length_valid(card_number):
    card_length = len(card_number)
    return (12 <= card_length) and (19 >= card_length)

def is_card_chars_valid(card_number):
    return card_number.isdigit()

def is_card_valid(card_number):
    card_number = card_number.strip()
    if "" == card_number:
        message = "Skipping blank number."
        return message, BashColor.wrap_y(message)
    if not is_card_length_valid(card_number):
        message = "Credit card numbers must be 12 and 19 digits."
        return message, BashColor.wrap_r(message)
    if not is_card_chars_valid(card_number):
        message = "Credit card numbers must be only digits"\
                  " (no letters or special characters)."
        return message, BashColor.wrap_r(message)
    card_masked = "{0}xxxxxx{1}".format(card_number[:6], card_number[-4:])
    message_format = "{0}    {1}"
    if is_luhn_valid(card_number):
        message = "Valid card number"
        message_colored = BashColor.wrap_r(message)
    else:
        message = "Not a valid card number"
        message_colored = BashColor.wrap_g(message)
    return message_format.format(card_masked, message), message_format.format(card_masked, message_colored)

def ui():
    menu_text = """\
    Do you want to:
    1. Enter the location and file of the list (i.e. /tmp/cards.csv)
    2. Enter a single number to evaluate

    * Enter any other value to exit *

    Please enter your selection:
    """
    menu_text = dedent(menu_text)

    os.system('clear')
    # Main Menu
    sys.stdout.write(BashColor.wrap_b(__doc__) + "\n" + menu_text)
    main_menu_choice = input()
    main_menu_choice = main_menu_choice[:1]
    if not main_menu_choice.isdigit():
        sys.exit(0)

    # Evaluate numbers in a file
    if '1' == main_menu_choice:
        try:
            input_file_path=input("Please enter the full path of the csv file: ")
            with open(input_file_path, "r") as file:
                lines = file.read().replace('\r', '\n').split('\n')

            print_output = lambda m, c: print(c)
            output_methods = [print_output]
            print("Do you want to save the results to a file in the current directory?")
            output_to_file = input()

            if output_to_file == "y" or output_to_file == "Y" or output_to_file == "Yes" or output_to_file == "yes":
                output_file_name = input("What do you want the output file to be named? ")
                with open(output_file_name,"w") as output:
                    write_output = lambda m, c: output.write("{0}\n".format(m))
                    for m,c in [is_card_valid(l) for l in lines]:
                        write_output(m,c)
                        print_output(m,c)
                    print(" \nResults have been saved to: {0}".format(output_file_name))
            else:
                for m,c in [is_card_valid(l) for l in lines]:
                    print_output(m,c)
        except Exception as error:
            print(BashColor.wrap_r("\n\n Something went wrong, printing the error: {0}".format(str(error))))

    # Evaluate single number
    if main_menu_choice == '2':
        while True:
            card_input = input(BashColor.wrap_g("Please enter the card number: "))
            input_valid = is_card_chars_valid(card_input)
            if not input_valid:
                print("Please enter numbers only")
            else:
                _, c = is_card_valid(card_input)
                print(c)
                break

    # Exit
    input('Press Enter to exit')
    os.system('clear')

if __name__ == "__main__":
    ui()
