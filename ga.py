import random
import stack


class population:

    def __init__(self, s, cross, mutation):

        self.symbols = ['F', '[', ']', 'X', '+', '-']
        self.crossover_rate = cross
        self.mutation_rate = mutation
        self.size = s
        self.b_fit = 0
        self.w_fit = 0
        self.avg_fitness = 0.0
        self.chromosoms = list()
        self.chromosoms_new = list()
        self.cut = 0.0

    def random_rule(self):
        size = random.randrange(3, 8)
        s = ''
        for i in range(0, size):
            n = random.randrange(0, 4)
            if n == 0:
                s = s + '['
            elif n == 1:
                s = s + 'X]'
            elif n == 2:
                s = s + '-F'
            elif n == 3:
                s = s + '+F'
        s = self.balance(s)
        s = self.remove_empty_br(s)
        return s + 'F'

    def genarate(self):
        self.chromosoms = list()
        self.chromosoms_new = list()
        for i in range(0, self.size):
            s = self.random_rule()
            self.chromosoms.append(s)
            self.chromosoms_new.append(s)

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

    def balance(self, rule):
        st = stack.stack()
        s1 = ''
        s2 = ''
        for l in rule:
            if l == '[':
                st.push(l)
            elif l == ']':
                t = st.pop()
                if t == 0:
                    s1 = s1 + '['
        t = st.pop()
        while t != 0:
            s2 = s2 + ']'
            t = st.pop()

        return s1 + rule + s2

    def remove_char(self, s, n):

        newstr = s[:n] + s[n + 1:]
        return newstr

    def remove_empty_br(self, rule):
        char_list = list()
        for l in range(0, len(rule) - 1):
            a = rule[l]
            b = rule[l + 1]
            if a == '[' and b == ']':
                char_list.append(l)
                char_list.append(l + 1)

        if len(char_list) > 0:
            for n in range(len(char_list) - 1, -1, -1):
                rule = self.remove_char(rule, char_list[n])
        return rule

    def mutate(self, i1):

        if random.uniform(0, 100) < self.mutation_rate:
            l1 = random.randrange(0, len(self.chromosoms_new[i1]))
            l2 = l1
            while l1 != l2:
                l2 = random.randrange(0, len(self.chromosoms_new[i1]))

            ls = list(self.chromosoms_new[i1])
            c = ls[l1]
            ls[l1] = ls[l2]
            ls[l2] = c

    def cross_over(self, i1, i2, i):

        if random.uniform(0, 100) < self.crossover_rate:

            l1 = random.randrange(0, len(self.chromosoms[i1]))
            l2 = random.randrange(0, len(self.chromosoms[i2]))

            s11 = self.chromosoms[i1][:l1]
            s12 = self.chromosoms[i1][l1:]

            s21 = self.chromosoms[i2][:l2]
            s22 = self.chromosoms[i2][l2:]

            self.chromosoms_new[i] = s11 + s22
            self.chromosoms_new[i + 1] = s21 + s12

        else:
            self.chromosoms_new[i] = self.chromosoms[i1]
            self.chromosoms_new[i + 1] = self.chromosoms[i2]

    def copy(self, new, old):
        self.chromosoms_new[new] = self.chromosoms[old]

    def copy2(self, new, old):
        self.chromosoms[old] = self.chromosoms_new[new]

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
            self.chromosoms_new[i] = self.random_rule()

        for i in range(0, self.size):
            f = True
            for l in self.chromosoms_new[i]:
                if l == '+' or l == '-':
                    f = False
                    break
            if f:
                print 'lllllllllllllllllllllllllll'
                self.chromosoms_new[i] = self.random_rule()
        for l in range(0, self.size):
            self.copy2(l, l)

        for l in range(0, self.size):
            for m in range(l + 1, self.size):
                if self.chromosoms[l] == self.chromosoms[m]:
                    print "fucked"

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

        self.cross_over(i1, i2, i)
        self.mutate(i)
        self.mutate(i + 1)
        self.chromosoms_new[i] = self.balance(self.chromosoms_new[i])
        self.chromosoms_new[i] = self.remove_empty_br(self.chromosoms_new[i])

        self.chromosoms_new[i + 1] = self.balance(self.chromosoms_new[i + 1])
        self.chromosoms_new[i + 1] = self.remove_empty_br(self.chromosoms_new[i + 1])
