import subprocess
import os
import sys
# Define the command you want to run
command = "ls"

print("""
         ██                         ██                   ██
                        █████              ███                  ██
          ███       ██  ██████         █████████████            ██
          ████      ██     ████     █████████████████           ██
     ███    ██████████       ███████████   ████   ███   ██████████
     ██████ ██████████   ███████████████ ██████   ███   ██████████
       ███████      ██   ██████      ███████ ██   ██    ██      ██
        █████       ██     █████        ██   ██         ██      ██
           ██       ██       ████         █████         ██      ██
           ████     ██         ███       ██████         ██
            ███                ███       ███
                                         ████████
                                          ███████
        """)
while True:
    # Get user input
    user_input = input("> ")
    if len(user_input.split(' ')) > 1 and user_input != 'clear':
        word, number_of_words = user_input.split(' ')
        print(os.system(f"./en2sk.py {number_of_words} {word}"))
    elif user_input.split(' ')[0] == 'clear':
        os.system('clear')
    else:
        pass

