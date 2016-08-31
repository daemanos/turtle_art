"""
pythag_tree.py

A Lindenmayer system for drawing a Pythagorean tree. Adapted from
https://www.wikipedia.com/wiki/L-system.

author: Daman Morris <damanm72@gmail.com>
"""

from lindenmayer import Lindenmayer, prompt
import turtle

class PythagTree(Lindenmayer):

    def __init__(self):
        rules = {'1': '11', '0': '1[0]0'}
        super().__init__('0', rules)

        self.stack = []

    def draw(self, length):
        for c in self.content:
            if c == '0' or c == '1':
                turtle.forward(length)
            elif c == '[':
                self.stack += [(turtle.pos(), turtle.heading())]
                turtle.left(45)
            elif c == ']':
                pos, heading = self.stack.pop()

                turtle.up()
                turtle.goto(pos)
                turtle.setheading(heading)
                turtle.down()

                turtle.right(45)

if __name__ == '__main__':
    prompt(PythagTree)
