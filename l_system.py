"""
Author : tharindra galahena (inf0_warri0r)
Project: GeneticL - L-System generator using genetic algorithms
Blog   : http://www.inf0warri0r.blogspot.com
Date   : 08/05/2013
License:

     Copyright 2013 Tharindra Galahena

GeneticL is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version. GeneticL is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
details.

* You should have received a copy of the GNU General Public License along with
GeneticL. If not, see http://www.gnu.org/licenses/.

"""


import stack
import math
from Tkinter import *


class l_system:

    def __init__(self, ax, x, y, width, height, l, angle, ang):
        self.symbols = {}
        self.axiom = ax
        self.axiom_o = ax
        self.st = stack.stack()
        self.possition = (0, 0)
        self.st_angle = angle
        self.st_x = x
        self.st_y = y
        self.length = l
        self.angle = angle
        self.rules = {}

        self.stop = False
        self.ang = ang

    def set_rules(self, rules):
        self.rules = {}

        for rule in rules:

            self.rules[rule[0]] = rule[1]

    def set_symbols(self, symbols):
        self.symbols = {}

        for symbol in symbols:
            self.symbols[symbol[0]] = symbol[1]

    def next_gen(self):
        nxt = ''
        for l in self.axiom:
            if self.rules.get(l, 'x') != 'x':
                nxt = nxt + self.rules[l]
            else:
                nxt = nxt + l
        self.axiom = nxt

    def move(self):

        a = self.possition[0]
        a = a - self.length * math.sin(self.angle * math.pi / 180.0)
        b = self.possition[1]
        b = b - self.length * math.cos(self.angle * math.pi / 180.0)

        pos_new = a, b

        t = self.possition, pos_new
        self.possition = pos_new
        return t

    def left(self):
        self.angle = self.angle - self.ang

    def right(self):
        self.angle = self.angle + self.ang

    def push(self):
        self.st.push((self.possition, self.angle))

    def pop(self):
        self.possition, self.angle = self.st.pop()

    def draw(self):
        line_list = list()
        for l in self.axiom:
            if self.symbols.get(l, 'x') != 'x':
                s = self.symbols[l]
                for m in s:
                    if m == 'L':
                        self.left()
                    elif m == 'R':
                        self.right()
                    elif m == 'P':
                        self.push()
                    elif m == 'O':
                        self.pop()
                    elif m == 'F':
                        t = self.move()
                        line_list.append(t)
        return line_list

    def run(self):

        self.reset()
        self.next_gen()
        return self.draw()

    def reset(self):
        self.possition = self.st_x, self.st_y
        self.angle = self.st_angle
