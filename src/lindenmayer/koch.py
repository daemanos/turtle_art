"""
koch.py

A Lindenmayer system to draw a Koch curve (using right angles). Adapted from
https://www.wikipedia.com/wiki/L-system.

author: Daman Morris <damanm72@gmail.com>
"""

from lindenmayer import SimpleLindenmayer, prompt
import turtle

class Koch(SimpleLindenmayer):

    def __init__(self):
        cmds = {
            'F': turtle.forward,
            '+': lambda x: turtle.left(90),
            '-': lambda x: turtle.right(90)
        }
        super().__init__('F', {'F': 'F+F-F-F+F'}, cmds)

if __name__ == '__main__':
    prompt(Koch)
