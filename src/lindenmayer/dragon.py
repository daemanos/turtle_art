"""
dragon.py

A dragon curve.

author: Daman Morris <damanm72@gmail.com>
"""

from lindenmayer import SimpleLindenmayer, prompt
import turtle

class Dragon(SimpleLindenmayer):

    def __init__(self):
        rules = {'X': 'X+YF+', 'Y': '-FX-Y'}
        cmds = {
            'F': turtle.forward,
            '-': lambda x: turtle.left(90),
            '+': lambda x: turtle.right(90)
        }

        super().__init__('FX', rules, cmds)


if __name__ == '__main__':
    prompt(Dragon)
