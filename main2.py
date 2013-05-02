#st = 'abcdefg'
#st[0] = 'b'
#print st
import stack
import ga


def balance(ss):
    st = stack.stack()
    s1 = ''
    s2 = ''
    for l in ss:
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

    ss = s1 + ss + s2

    return ss

print balance('[a][]b')

s ="abcdefghijklmnop"

print s[:2]
print s[2:]

p = ga.population(10, 80, 10)

p.genarate()
fit = list()
for i in range(0, 10):
    fit.append(10)

print p.new_gen(fit)
print p.new_gen(fit)
print p.new_gen(fit)
