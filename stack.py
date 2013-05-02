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


class stack:

    def __init__(self):
        self.lst = list()
        self.count = 0
        self.top = -1

    def push(self, t):
        self.lst.append(t)
        self.count = self.count + 1
        self.top = self.top + 1

    def pop(self):
        if self.count <= 0:
            return 0
        t = self.lst[self.top]
        self.lst.remove(t)
        self.count = self.count - 1
        self.top = self.top - 1
        return t
