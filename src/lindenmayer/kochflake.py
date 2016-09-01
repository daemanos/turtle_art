"""
kochflake.py

A Lindenmayer system to draw a Koch snowflake.

:author Daman Morris
"""

from lindenmayer import SimpleLindenmayer, prompt
import turtle

class Kochflake(SimpleLindenmayer):

    def __init__(self):
        cmds = {
            'F': turtle.forward,
            '-': lambda x: turtle.left(60),
            '+': lambda x: turtle.right(120)
        }

        super().__init__('F+F+F', {'F': 'F-F+F-F'}, cmds)


if __name__ == '__main__':
    prompt(Kochflake)
