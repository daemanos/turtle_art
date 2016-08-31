"""
plant.py

A Lindenmayer system to draw a plant. Adapted from
https://www.wikipedia.com/wiki/L-system.

author: Daman Morris <damanm72@gmail.com>
"""

from lindenmayer import Lindenmayer, prompt
import turtle

class Plant(Lindenmayer):

    def __init__(self):
        rules = {
            'X': 'F-[[X]+X]+F[+FX]-X',
            'F': 'FF'
        }
        super().__init__('X', rules)

        self.stack = []

    def draw(self, length):
        for c in self.content:
            if c == 'F':
                turtle.forward(length)
            elif c == '-':
                turtle.left(25)
            elif c == '+':
                turtle.right(25)
            elif c == '[':
                self.stack += [(turtle.pos(), turtle.heading())]
            elif c == ']':
                pos, heading = self.stack.pop()

                turtle.up()
                turtle.goto(pos)
                turtle.setheading(heading)
                turtle.down()


if __name__ == '__main__':
    turtle.setheading(60)
    prompt(Plant)
