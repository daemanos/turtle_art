# Turtle Art

## Lindenmayer systems

A Lindenmayer system (or L-system) is a parallel rewriting system consisting of
an alphabet of symbols, a collection of rules that maps each symbol to another
symbol, an initial starting string (the "axiom"), and a method to render an
image from the result string (see [the Wikipedia
article](https://wikipedia.org/wiki/L-system) for more information).

Within this project, the `Lindenmayer` class represents a generic L-system,
but it does not provide any facility to draw the result string. If each
symbol corresponds to an atomic action (i.e., there is no additional state
involved), then the `SimpleLindenmayer` class can be used which features a
mapping from symbols to functions used to draw the result string.

### Pythagoras tree

The [pythagoras tree](https://wikipedia.org/wiki/Pythagoras_tree_(fractal)) is
an example of an L-system that requires additional state. It is constructed
as follows:

- **alphabet**: 0, 1, \[, \]
- **axiom**: 0
- **rules**: 1 → 11, 0 → 1\[0\]0

To draw the tree, the symbols are interpreted as follows:

- 0 and 1: draw a line segment
- \[: push position and angle, turn left 45°
- \]: pop position and angle, turn right 45°

Here, push and pop refer to an internal stack used to navigate the tree.

The number of iterations controls how many branches are drawn; for example,
with $n = 5$ the following tree results:

![pythagoras tree](../blob/master/ex/pythagoras_tree.png)

## Kochpinski

The Kochpinski is a majestic combination of a Koch curve and a Sierpinski
triangle. For added majesty, make a Koch snowflake and fill in the middle with
another Sierpinski triangle:

![kochpinski snowflake](../blob/master/ex/kochpinski.png)
