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

import Tkinter as tk
import l_system
import ga
import thread
from threading import Lock
import time
#import tkMessageBox as dialog
import ttk


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()

        self.run = [False, False, False, False,
                    False, False, False, False,
                    False, False]

        self.l_sys = list()
        for i in range(0, 10):
            self.l_sys.append(None)
        self.pause = False
        self.file = ''
        self.mutex = Lock()
        self.p = ga.population(10, 90, 30)
        self.fit = list()
        for i in range(0, 10):
            self.fit.append(10)

        self.axiom = 'X'
        self.angle = 0.0
        self.ang = 25.0
        self.lst_symbols = [
                ('F', 'F'),
                ('[', 'P'),
                (']', 'O'),
                ('+', 'L'),
                ('-', 'R')
            ]

        self.rl = list()
        self.rl.append(('F', 'FF'))
        self.rl.append(('', ''))
        self.gen_count = 0

        self.iter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.x = 300
        self.y = 500
        self.length = 5

        self.rules = self.p.genarate()
        self.createWidgets()

    def createWidgets(self):

        self.tabs = ttk.Notebook()
        self.tab_list = list()
        for i in range(0, 10):
            tb = ttk.Frame(self.tabs)
            self.tab_list.append(tb)
            self.tabs.add(self.tab_list[i], text="   " + str(i + 1) + "   ")

        self.load_button = tk.Button(self, text='next generation',
                                        command=self.next_gen)

        self.load_button.grid(column=0, row=0,
                                columnspan=4, sticky=tk.W + tk.E)

        self.content = tk.StringVar()
        self.max_entry = tk.Entry(textvariable=self.content)
        self.max_entry.insert(0, '6')
        self.gen_entry = tk.Entry()
        self.gen_entry.insert(0, '0')

        tk.Label(text="maximum iterations :").grid(column=0,
                                                    row=9, sticky=tk.W)
        self.max_entry.grid(column=0, row=10)
        tk.Label(text="current generation :").grid(column=0,
                                                    row=11, sticky=tk.W)
        self.gen_entry.grid(column=0, row=12)

        tk.Label(text="").grid(column=0, row=13, rowspan=9, sticky=tk.W)
        self.canvases = list()
        self.vote_entrys = list()
        self.vote_buttons = list()
        self.content_list = list()
        self.start_buttons = list()

        but1 = tk.Button(self.tab_list[0], text='start / stop',
                            command=lambda: self.start(0))
        but1.pack(side=tk.TOP, expand=tk.YES)
        self.start_buttons.append(but1)

        but1 = tk.Button(self.tab_list[1], text='start / stop',
                            command=lambda: self.start(1))
        but1.pack(side=tk.TOP, expand=tk.YES)
        self.start_buttons.append(but1)
        but1 = tk.Button(self.tab_list[2], text='start / stop',
                            command=lambda: self.start(2))
        but1.pack(side=tk.TOP, expand=tk.YES)
        self.start_buttons.append(but1)
        but1 = tk.Button(self.tab_list[3], text='start / stop',
                            command=lambda: self.start(3))
        but1.pack(side=tk.TOP, expand=tk.YES)
        self.start_buttons.append(but1)
        but1 = tk.Button(self.tab_list[4], text='start / stop',
                            command=lambda: self.start(4))
        but1.pack(side=tk.TOP, expand=tk.YES)
        self.start_buttons.append(but1)
        but1 = tk.Button(self.tab_list[5], text='start / stop',
                            command=lambda: self.start(5))
        but1.pack(side=tk.TOP, expand=tk.YES)
        self.start_buttons.append(but1)
        but1 = tk.Button(self.tab_list[6], text='start / stop',
                            command=lambda: self.start(6))
        but1 = but1.pack(side=tk.TOP, expand=tk.YES)
        self.start_buttons.append(but1)
        but1 = tk.Button(self.tab_list[7], text='start / stop',
                            command=lambda: self.start(7))
        but1 = but1.pack(side=tk.TOP, expand=tk.YES)
        self.start_buttons.append(but1)
        but1 = tk.Button(self.tab_list[8], text='start / stop',
                            command=lambda: self.start(8))
        but1 = but1.pack(side=tk.TOP, expand=tk.YES)
        self.start_buttons.append(but1)
        but1 = tk.Button(self.tab_list[9], text='start / stop',
                            command=lambda: self.start(9))
        but1 = but1.pack(side=tk.TOP, expand=tk.YES)
        self.start_buttons.append(but1)

        but2 = tk.Button(self.tab_list[0], text='vote',
                            command=lambda: self.vote(0))
        but2 = but2.pack(side=tk.BOTTOM, expand=tk.YES)
        self.vote_buttons.append(but2)

        but2 = tk.Button(self.tab_list[1], text='vote',
                            command=lambda: self.vote(1))
        but2 = but2.pack(side=tk.BOTTOM, expand=tk.YES)
        self.vote_buttons.append(but2)
        but2 = tk.Button(self.tab_list[2], text='vote',
                            command=lambda: self.vote(2))
        but2 = but2.pack(side=tk.BOTTOM, expand=tk.YES)
        self.vote_buttons.append(but2)

        but2 = tk.Button(self.tab_list[3], text='vote',
                            command=lambda: self.vote(3))
        but2 = but2.pack(side=tk.BOTTOM, expand=tk.YES)
        self.vote_buttons.append(but2)
        but2 = tk.Button(self.tab_list[4], text='vote',
                            command=lambda: self.vote(4))
        but2 = but2.pack(side=tk.BOTTOM, expand=tk.YES)
        self.vote_buttons.append(but2)
        but2 = tk.Button(self.tab_list[5], text='vote',
                            command=lambda: self.vote(5))
        but2 = but2.pack(side=tk.BOTTOM, expand=tk.YES)
        self.vote_buttons.append(but2)
        but2 = tk.Button(self.tab_list[6], text='vote',
                            command=lambda: self.vote(6))
        but2 = but2.pack(side=tk.BOTTOM, expand=tk.YES)
        self.vote_buttons.append(but2)
        but2 = tk.Button(self.tab_list[7], text='vote',
                            command=lambda: self.vote(7))
        but2 = but2.pack(side=tk.BOTTOM, expand=tk.YES)
        self.vote_buttons.append(but2)
        but2 = tk.Button(self.tab_list[8], text='vote',
                            command=lambda: self.vote(8))
        but2 = but2.pack(side=tk.BOTTOM, expand=tk.YES)
        self.vote_buttons.append(but2)
        but2 = tk.Button(self.tab_list[9], text='vote',
                            command=lambda: self.vote(9))
        but2 = but2.pack(side=tk.BOTTOM, expand=tk.YES)
        self.vote_buttons.append(but2)

        for i in range(0, 10):

            self.canvases.append(tk.Canvas(self.tab_list[i],
                            width=600, height=600,
                            background="black"))

            self.content_list.append(tk.StringVar())

            s_start = tk.Scrollbar(self.tab_list[i])
            s_start.pack(side=tk.RIGHT, fill=tk.Y)
            s_start.config(command=self.canvases[i].yview)
            self.canvases[i].config(yscrollcommand=s_start.set)

            self.vote_entrys.append(tk.Entry(self.tab_list[i],
                                    textvariable=self.content_list[i]))
            self.vote_entrys[i].insert(0, '0.0')
            self.vote_entrys[i].pack(side=tk.BOTTOM, expand=tk.NO)

            s_start = tk.Scrollbar(self.tab_list[i], orient=tk.HORIZONTAL)
            s_start.pack(side=tk.BOTTOM, fill=tk.X)
            s_start.config(command=self.canvases[i].xview)
            self.canvases[i].config(xscrollcommand=s_start.set)

            self.canvases[i].pack(side=tk.LEFT, fill=tk.BOTH)

        self.tabs.grid(row=0, rowspan=22,
                        column=4, sticky=tk.W + tk.E + tk.N + tk.S)
        self.x_scale = 1
        self.y_scale = 1

    def vote(self, n):
        text = self.content_list[n].get()
        self.fit[n] = float(text)

    def start(self, n):
        if self.run[n] is False:
            self.run[n] = True
            try:
                thread.start_new_thread(self.thread_func, (n, ))
            except Exception, e:
                print "Exception ", Exception, e
        else:
            self.run[n] = False

    def stop(self):
        pass

    def next_gen(self):
        self.rules = self.p.new_gen(self.fit)
        self.gen_entry.delete(0, tk.END)
        self.gen_entry.insert(0, str(self.gen_count + 1))
        self.gen_count = self.gen_count + 1
        for i in range(0, 10):
            self.fit[i] = 0.0

    def thread_func(self, n):

        self.l_sys[n] = l_system.l_system(self.axiom,
                                        self.x, self.y,
                                        600, 600,
                                        self.length,
                                        self.angle, self.ang)

        self.l_sys[n].set_symbols(self.lst_symbols)
        self.rl[1] = ('X', self.rules[n])
        self.l_sys[n].set_rules(self.rl)
        self.run[n] = True
        self.pause = False
        text = self.content.get()
        self.max = int(text)
        self.iter[n] = 0

        while self.run[n]:
            self.l_sys[n].reset()

            if self.iter[n] < self.max:
                self.iter[n] = self.iter[n] + 1
                self.l_sys[n].next_gen()
            lst = self.l_sys[n].draw()

            self.canvases[n].delete(tk.ALL)

            st = 'iteration = ' + str(self.iter[n])
            while len(st) < 50:
                st = st + ' '

            self.canvases[n].create_text(120, 20,
                                        text=st,
                                        fill='white')

            st = 'rule 1    = ' + str(self.rl[0][1])
            while len(st) < 50:
                st = st + ' '

            self.canvases[n].create_text(120, 40,
                                        text=st,
                                        fill='white')

            st = 'rule 2    = ' + str(self.rl[1][1])
            while len(st) < 50:
                st = st + ' '
            print len(st)
            self.canvases[n].create_text(120, 60,
                                        text=st,
                                        fill='white')
            for li in lst:
                if not self.run[n]:
                    break
                self.canvases[n].create_line(li[0][0],
                                        li[0][1],
                                        li[1][0],
                                        li[1][1],
                                        fill='yellow')
                self.canvases[n].update()
            while self.iter[n] >= self.max:
                time.sleep(0.01)
                if not self.run[n]:
                    break

            time.sleep(1)
        self.canvases[n].delete(tk.ALL)

if __name__ == '__main__':

    app = Application()
    app.master.title('gen_l_viewer')
    app.mainloop()
