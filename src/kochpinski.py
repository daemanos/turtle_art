"""
kochpinski.py

All hail the majestic Kochpinski.

author: Daman Morris <damanm72@gmail.com>
"""

import turtle
turtle.speed(0)

def sierpinski(side, thresh, outline = True, turn = turtle.left):
    """
    Draw a Sierpinski triangle with a given side length.

    :param side: the side length
    :param thresh: the minimum line segment (controls granularity)
    :param outline: whether to draw an outline around the triangle
    :param turn: what direction to turn in (controls orientation)
    """

    # the bottom-left corner
    A = turtle.pos()

    # draw the outline
    if outline:
        for _ in range(3):
            turtle.forward(side)
            turn(120)

    # get to the middle of the triangle and prep for drawing
    turtle.up()
    turtle.forward(side / 2)
    turn(60)
    turtle.down()

    # draw the inner triangle
    for _ in range(3):
        # HACKY: sets the current position to the current vertex
        # will wind up as the top vertex once the loop finishes
        D = turtle.pos()
        turtle.forward(side / 2)
        turn(120)

    turn(300)

    # recurse into the new sub-triangles if we have enough room
    if side > thresh:
        sierpinski(side / 2, thresh, False, turn)

        turtle.up()
        turtle.goto(D)
        sierpinski(side / 2, thresh, False, turn)

        turtle.up()
        turtle.goto(A)
        sierpinski(side / 2, thresh, False, turn)
        turtle.goto(A)


def koch(side, thresh, post = None):
    """
    Draw a Koch curve with the given length.

    :param side: the length
    :param thresh: the minimum line segment (controls granularity)
    :param post: an optional function to fill in the triangle
    """

    if side < thresh:
        # finish drawing
        cmd = lambda: turtle.forward(side / 3)
    else:
        # recurse into the next level
        cmd = lambda: koch(side / 3, thresh, post)

    # draw first segment
    cmd()

    # fill in the triangle, if applicable
    if post:
        p = turtle.pos()
        post(side / 3, thresh)
        turtle.up()
        turtle.goto(p)
        turtle.down()

    # turn to draw the remaining three segments
    turtle.left(60)
    cmd()
    turtle.right(120)
    cmd()
    turtle.left(60)
    cmd()

def koch_flake(side, thresh, post = None):
    """
    Draw a Koch snowflake with the given side length.

    :param side: the side length
    :param thresh: the minimum line segment (controls granularity)
    :param post: an optional function to fill in the triangle
    """
    for _ in range(3):
        koch(side, thresh, post)
        turtle.right(120)


def kochpinski(side, thresh):
    """
    Draw a Kochpinski curve (Koch curve with a Sierpinski triangle).
    """
    koch(side, thresh, sierpinski)

def kochpinski_flake(side, thresh):
    """
    Draw a Kochpinski snowflake.
    """
    sierpinski(side, thresh, turn = turtle.right)
    koch_flake(side, thresh, sierpinski)
