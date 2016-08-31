"""
lindenmayer.py

Generic classes for the development of Lindenmayer systems for turtle drawing.

author: Daman Morris <damanm72@gmail.com>
"""

class Lindenmayer:
    """
    A Lindenmayer system (intended for drawing turtle graphics).

    Each system has an axiom, or start, and a dictionary of rules, which maps
    input characters onto output characters. The rules are iteratively applied
    to the axiom to generate a result string.

    All subclasses, if they are meant to be useful, must override the draw
    method, which is not implemented in this class.
    """

    def __init__(self, axiom, rules):
        self.axiom = axiom
        self.content = axiom
        self.rules = rules

    def apply(self):
        """
        Apply the rules once.
        """
        new_content = ""
        for c in self.content:
            if c in self.rules:
                new_content += self.rules[c]
            else:
                new_content += c

        self.content = new_content

    def iterate(self, n):
        """
        Iterate the rules n times.
        """
        for _ in range(n):
            self.apply()

    def draw(self, length):
        """
        Draw an image using the alphabet.
        """
        pass


class SimpleLindenmayer(Lindenmayer):
    """
    A simple, general implementation of a Lindenmayer system.

    Images are drawn with a dictionary of commands that maps symbols in the
    Lindenmayer content to drawing functions.
    """

    def __init__(self, axiom, rules, cmds):
        super().__init__(axiom, rules)
        self.cmds = cmds

    def draw(self, length):
        """
        Draw an image using the commands dictionary.
        """
        for c in self.content:
            if c in self.cmds:
                self.cmds[c](length)
