"""
Author : tharindra galahena (inf0_warri0r)
Project: evolutionary art generator
Blog   : http://www.inf0warri0r.blogspot.com
Date   : 08/03/2013
License:

     Copyright 2013 Tharindra Galahena

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version. This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
details.

* You should have received a copy of the GNU General Public License along with
This program. If not, see http://www.gnu.org/licenses/.

"""

import random


class population:

    def __init__(self, s, n, cross, mutation):

        self.crossover_rate = cross
        self.mutation_rate = mutation
        self.size = s
        self.gnum = n
        self.b_fit = 0
        self.w_fit = 0
        self.avg_fitness = 0.0
        self.chromosoms = list()
        self.chromosoms_new = list()
        self.cut = 0.0
        self.mx = 0b00000000111111111111111111111111

    def genarate(self):
        self.chromosoms = list()
        self.chromosoms_new = list()
        for i in range(0, self.size):
            self.chromosoms.append(list())
            self.chromosoms_new.append(list())

        for i in range(0, self.size):
            r = random.randrange(0, 256)
            g = random.randrange(0, 256)
            b = random.randrange(0, 256)
            for j in range(0, self.gnum):
                #d = c  # - j / 200
                #if d < 0:
                    #d = 0
                rd = r - j / 400
                gd = g - j / 400
                bd = b - j / 400
                if rd < 0:
                    rd = 0
                if gd < 0:
                    gd = 0
                if bd < 0:
                    bd = 0
                self.chromosoms[i].append((rd, bd, gd))
                self.chromosoms_new[i].append((rd, bd, gd))
        return self.chromosoms

    def genarate2(self, pix):
        self.chromosoms = list()
        self.chromosoms_new = list()
        for i in range(0, self.size):
            self.chromosoms.append(list())
            self.chromosoms_new.append(list())

        for i in range(0, self.size):
            #c = random.randrange(0, 0b00000000111111111111111111111111)
            #lst = pix[i].keys()
            #for j in range(0, self.gnum):

            for i in range(0, self.size):
                print self.gnum, " ", i
                for y in range(0, 200):
                    for x in range(0, 200):
                        r, b, g = pix[i][x, y]
                        #d = c  # - j / 200
                        #if d < 0:
                            #d = 0
                        #r = (r << 16) & 0b00000000111111110000000000000000
                        #b = (b << 8) & 0b00000000000000001111111100000000
                        #g = g & 0b00000000000000000000000011111111
                        #d = g | b | r
                        #d = d + b << 8
                        #d = d + r << 16
                        self.chromosoms[i].append((r, b, g))
                        self.chromosoms_new[i].append((r, b, g))
        return self.chromosoms

    def get_total(self, fit):
        s = 0.0
        for i in range(0, self.size):
            if fit[i] >= self.cut:
                s = s + fit[i]
        return s

    def choose(self, fit, m):
        ind = 0
        ft = self.get_total(fit)
        if ft == 0.0:
            return random.randrange(0, self.size)
        rd = random.uniform(0, 100)
        count = 0.0
        for i in range(0, self.size):
            f = fit[i]
            if f >= self.cut - m:
                f = (f / ft) * 100.0
                count = count + f
                if count >= rd:
                    ind = i
                    break

        if ind <= 0:
            ind = 0
        return ind

    def mutate(self, i1):

        for i in range(0, self.gnum):
            if random.uniform(0, 100) < self.mutation_rate:
                sh_r = random.uniform(-10, 10)
                sh_b = random.uniform(-10, 10)
                sh_g = random.uniform(-10, 10)
                r, b, g = self.chromosoms_new[i1][i]
                self.chromosoms_new[i1][i] = (r + sh_r, b + sh_b, g + sh_g)

    def cross_over(self, i1, i2, i):

        if random.uniform(0, 100) < self.crossover_rate:

            x = random.randrange(0, 200)
            y = random.randrange(0, 200)
            r = random.uniform(1000000, 4000000)

            for j in range(0, self.gnum):
                #print "j = ", j
                xx = j % 200
                yy = j / 200
                xx = xx - x
                yy = yy - y
                f = (xx * xx + yy * yy) ** 2.0

                lr, lb, lg = self.chromosoms[i1][j]
                mr, mb, mg = self.chromosoms[i2][j]
                #print "j2 = ", (xx + x, yy + y, r)
                if f <= r:
                    #print "j3 = ", (j, f, r)
                    self.chromosoms_new[i][j] = ((lr + mr) / 2,
                                                (lb + mb) / 2,
                                                (lg + mg) / 2)  # self.mx
                    self.chromosoms_new[i + 1][j] = self.chromosoms[i1][j]
                else:
                    self.chromosoms_new[i][j] = self.chromosoms[i2][j]
                    self.chromosoms_new[i + 1][j] = ((lr + mr) / 2,
                                                    (lb + mb) / 2,
                                                    (lg + mg) / 2)

        else:
            for j in range(0, self.gnum):
                self.chromosoms_new[i][j] = self.chromosoms[i1][j]
                self.chromosoms_new[i + 1][j] = self.chromosoms[i2][j]

    def cross_over2(self, i1, i2, i):

        if random.uniform(0, 100) < self.crossover_rate:

            x1 = random.randrange(0, 100)
            #y1 = random.randrange(0, 180)
            x2 = random.randrange(x1 + 10, 200)
            #y2 = random.randrange(y1, 200)

            for j in range(0, self.gnum):
                #print "j = ", j
                x = j % 200
                #y = j / 200

                lr, lb, lg = self.chromosoms[i1][j]
                mr, mb, mg = self.chromosoms[i2][j]
                if x >= x1 and x <= x2:
                    a = float(x - x1 + 1)
                    b = float(x2 - x)

                    lr, lb, lg = self.chromosoms[i1][j]
                    mr, mb, mg = self.chromosoms[i2][j]

                    r = int((lr * a + mr * b) / (a + b))
                    b = int((lb * a + mb * b) / (a + b))
                    g = int((lg * a + mg * b) / (a + b))
                    self.chromosoms_new[i][j] = r, b, g

                    r = int((mr * a + lr * b) / (a + b))
                    b = int((mb * a + lb * b) / (a + b))
                    g = int((mg * a + lg * b) / (a + b))
                    self.chromosoms_new[i + 1][j] = r, b, g
                elif x < x1:
                    self.chromosoms_new[i][j] = self.chromosoms[i2][j]
                    self.chromosoms_new[i + 1][j] = self.chromosoms[i1][j]
                else:
                    self.chromosoms_new[i][j] = self.chromosoms[i1][j]
                    self.chromosoms_new[i + 1][j] = self.chromosoms[i2][j]

        else:
            for j in range(0, self.gnum):
                self.chromosoms_new[i][j] = self.chromosoms[i1][j]
                self.chromosoms_new[i + 1][j] = self.chromosoms[i2][j]

    def cross_over3(self, i1, i2, i):

        if random.uniform(0, 100) < self.crossover_rate:

            #x1 = random.randrange(0, 180)
            y1 = random.randrange(0, 100)
            #x2 = random.randrange(x1 + 10, 200)
            y2 = random.randrange(y1 + 10, 200)

            for h in range(0, 200):
                for k in range(0, 200):
                    #print "j = ", j
                    #x = j % 200
                    y = k  # j / 200
                    j = 200 * y + h

                    lr, lb, lg = self.chromosoms[i1][j]
                    mr, mb, mg = self.chromosoms[i2][j]
                    if y > y1 and y < y2:
                        a = float(y - y1)
                        b = float(y2 - y)

                        lr, lb, lg = self.chromosoms[i1][j]
                        mr, mb, mg = self.chromosoms[i2][j]

                        r = int((lr * a + mr * b) / (a + b))
                        b = int((lb * a + mb * b) / (a + b))
                        g = int((lg * a + mg * b) / (a + b))
                        self.chromosoms_new[i][j] = r, b, g

                        r = int((mr * a + lr * b) / (a + b))
                        b = int((mb * a + lb * b) / (a + b))
                        g = int((mg * a + lg * b) / (a + b))
                        self.chromosoms_new[i + 1][j] = r, b, g
                    elif y <= y1:
                        self.chromosoms_new[i][j] = self.chromosoms[i2][j]
                        self.chromosoms_new[i + 1][j] = self.chromosoms[i1][j]
                    else:
                        self.chromosoms_new[i][j] = self.chromosoms[i1][j]
                        self.chromosoms_new[i + 1][j] = self.chromosoms[i2][j]

        else:
            for j in range(0, self.gnum):
                self.chromosoms_new[i][j] = self.chromosoms[i1][j]
                self.chromosoms_new[i + 1][j] = self.chromosoms[i2][j]

    def copy(self, new, old):
        for i in range(0, self.gnum):
            self.chromosoms_new[new][i] = self.chromosoms[old][i]

    def copy2(self, new, old):
        for i in range(0, self.gnum):
            self.chromosoms[old][i] = self.chromosoms_new[new][i]

    def new_gen(self, fit):

        self.fitness = fit
        self.cal_b_fit(fit)

        self.copy(0, 0)
        self.copy(1, 1)

        max1 = -1.0
        max2 = -1.0
        i1 = 0
        i2 = 1

        for i in range(0, self.size):
            if max1 < fit[i]:
                max1 = fit[i]
                i1 = i
        for i in range(0, self.size):
            if max1 > fit[i] and max2 < fit[i]:
                max2 = fit[i]
                i2 = i

        if(i1 == i2):
            print "i1 == i2"

        self.copy(0, i1)
        self.copy(1, i2)

        newfit = sorted(fit)
        ind = 0  # 3 * self.size / 4
        self.cut = newfit[ind]

        i = 2

        while i < self.size - 2:
            self.operation(fit, i)
            i += 2

        for i in range(self.size - 2, self.size):
            r = random.randrange(0, 256)
            g = random.randrange(0, 256)
            b = random.randrange(0, 256)
            for j in range(0, self.gnum):

                rd = r - j / 400
                gd = g - j / 400
                bd = b - j / 400
                if rd < 0:
                    rd = 0
                if gd < 0:
                    gd = 0
                if bd < 0:
                    bd = 0
                #self.chromosoms[i].append((rd, bd, gd))
                self.chromosoms_new[i].append((rd, bd, gd))

        for l in range(0, self.size):
            self.copy2(l, l)

        for l in range(0, self.size):
            for m in range(l + 1, self.size):
                sm = 0
                for n in range(0, self.gnum):
                    if self.chromosoms[l][n] == self.chromosoms[m][n]:
                        sm = sm + 1
                if sm >= self.gnum:
                    print "fucked"
                    #color = (random.randrange(0, 256),
                            #random.randrange(0, 256),
                            #random.randrange(0, 256))
                    #color = (random.randrange(0, 256),
                            #random.randrange(0, 256),
                            #random.randrange(0, 256))
                    #for n in range(0, self.gnum):
                        #self.chromosoms[m][n] = color

        return self.chromosoms

    def cal_b_fit(self, fit):
        mx = -1.0
        for i in range(0, self.size):
            if mx < fit[i]:
                mx = fit[i]
                self.b_fit = i

        return self.b_fit

    def cal_w_fit(self, fit):
        mn = 1000
        for i in range(0, self.size):
            if mn > fit[i]:
                mn = fit[i]
            self.w_fit = i

    def cal_avg_fit(self, fit):
        self.fitness = fit
        self.avg_fit = self.get_total(fit) / self.size
        return self.avg_fit

    def operation(self, fit, i):

        nfit = fit[:]
        i1 = self.choose(nfit, 0.0)
        i2 = i1
        tmp = nfit[i1]
        nfit[i1] = 0.0
        for j in range(0, self.size):
            i2 = self.choose(nfit, tmp)
            if i1 != i2:
                break

        if i1 == i2:
            i2 = (i1 + 1) % self.size

        r = random.randrange(0, 10)
        print r
        if r < 5:
            self.cross_over2(i1, i2, i)
        else:
            self.cross_over3(i1, i2, i)
        #for l in range(0, self.size):
            #self.copy2(l, l)
        #self.cross_over2(i1, i2, i)
        #for l in range(0, self.size):
            #self.copy2(l, l)
        #self.cross_over3(i2, i1, i)
        #for l in range(0, self.size):
            #self.copy2(l, l)
        #self.cross_over3(i2, i1, i)
        #self.mutate(i)
        #self.mutate(i + 1)
