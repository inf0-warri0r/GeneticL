"""
Author : tharindra galahena (inf0_warri0r)
Project: L-system
Blog   : http://www.inf0warri0r.blogspot.com
Date   : 30/04/2013
License:

     Copyright 2013 Tharindra Galahena

This is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version. This is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
details.

* You should have received a copy of the GNU General Public License along with
this. If not, see http://www.gnu.org/licenses/.

"""

from Tkinter import *
import l_system2


def read_file(name):
    f = open(name, 'r')
    cat = f.read()
    f.close()
    lst_rules = list()
    lst_symbols = list()
    lines = cat.splitlines()
    axiom = lines[0]
    angle = float(lines[1])
    ang = float(lines[2])
    num_rules = int(lines[3])
    for i in range(4, num_rules + 4):
        rule = lines[i].split('=')
        lst_rules.append((rule[0], rule[1]))

    num_symbols = int(lines[num_rules + 4])
    print num_rules + 1
    for i in range(num_rules + 5, num_rules + 5 + num_symbols):
        symbol = lines[i].split('=')
        commands = symbol[1].split(',')
        lst_symbols.append((symbol[0], commands))

    return axiom, angle, ang, lst_symbols, lst_rules


root = Tk()
root.title("L-system")
chart_1 = Canvas(root,
                    width=600,
                    height=600,
                    background="black")

chart_1.grid(row=0, column=0)

axiom, angle, ang, lst_symbols, lst_rules = read_file('system5')
l = l_system2.l_system(axiom, 300, 300, 600, 600, 5, angle, ang)
l.set_symbols(lst_symbols)
l.set_rules(lst_rules)

while 1:
    lst = l.run()
    for li in lst:
        chart_1.create_line(li[0][0],
                            li[0][1],
                            li[1][0],
                            li[1][1],
                            fill='yellow')
    chart_1.update()
    chart_1.after(1000)

    chart_1.delete(ALL)
room.mainloop()
