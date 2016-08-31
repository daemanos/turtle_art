"""
dust.py

A Lindenmayer system for drawing Cantor dust. Adapted from
https://www.wikipedia.com/wiki/L-system.

author: Daman Morris <damanm72@gmail.com>
"""

from lindenmayer import SimpleLindenmayer
import turtle

def move_forward(length):
    turtle.up()
    turtle.forward(length)
    turtle.down()

class Dust(SimpleLindenmayer):

    def __init__(self):
        rules = {'A': 'ABA', 'B': 'BBB'}
        cmds = {'A': turtle.forward, 'B': move_forward}
        super().__init__('A', rules, cmds)


if __name__ == '__main__':
    dust = Dust()
    dust.iterate(int(input('Number of iterations: ')))
    dust.draw(int(input('Segment length: ')))
