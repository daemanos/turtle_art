"""
sierpinski.py

A Lindenmayer system for drawing a Sierpinski triangle. Adapted from
https://www.wikipedia.com/wiki/L-system.

author: Daman Morris <damanm72@gmail.com>
"""

from lindenmayer import SimpleLindenmayer
import turtle

class Sierpinski(SimpleLindenmayer):

    def __init__(self):
        rules = {'A': '+B-A-B+', 'B': '-A+B+A-'}
        cmds = {
            'A': turtle.forward,
            'B': turtle.forward,
            '+': lambda x: turtle.left(60),
            '-': lambda x: turtle.right(60)
        }
        super().__init__('A', rules, cmds)


if __name__ == '__main__':
    tri = Sierpinski()
    tri.iterate(int(input('Number of iterations: ')))
    turtle.speed(0)
    tri.draw(int(input('Segment length: ')))
    turtle.mainloop()
