from Tkinter import *
import l_system2
import ga


root = Tk()
root.title("L-system")
chart_1 = Canvas(root,
                    width=600,
                    height=600,
                    background="black")

chart_1.grid(row=0, column=0)

axiom = 'X'
angle = 0.0
ang = 25
lst_symbols = [
                ('F', 'F'),
                ('[', 'P'),
                (']', 'O'),
                ('+', 'L'),
                ('-', 'R')
            ]

l = l_system2.l_system(axiom, 300, 300, 600, 600, 5, angle, ang)
l.set_symbols(lst_symbols)
p = ga.population(10, 80, 10)

rules = p.genarate()

fit = list()
for i in range(0, 10):
    fit.append(10)

rl = list()
rl.append(('F', 'FF'))
rl.append(('', ''))
gen_count = 0
while 1:
    print "gen -> ", gen_count
    gen_count = gen_count + 1
    for i in range(0, 10):
        print i
        rl[1] = ('X', rules[i])
        l.set_rules(rl)
        l.axiom = 'X'
        for j in range(0, 5):
            print " -> ", j
            l.reset()
            l.next_gen()
            lst = l.draw()
            for li in lst:
                chart_1.create_line(li[0][0],
                                    li[0][1],
                                    li[1][0],
                                    li[1][1],
                                    fill='yellow')
            chart_1.update()
            chart_1.after(1000)
            chart_1.delete(ALL)
    rules = p.new_gen(fit)

room.mainloop()
