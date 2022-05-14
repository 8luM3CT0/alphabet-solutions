##FOOBAR--CHALLENEGE #3.3

#Making fuel for the LAMBCHOP's reactor core is a tricky process because of the exotic mter involved. It starts as raw ore, then during processing, begins randomly changing between forms, eventually reaching a stable form. There may be multiple stable forms that a sample could ultimely reach, not all of which are useful as fuel. 

#Commander Lambda has tasked you to help the scientists increase fuel creation efficiency by predicting the end state of a given ore sample. You have carefully studied the different structures that the ore can take and which transitions it undergoes. It appears that, while random, the probability of each structure transforming is fixed. That is, each time the ore is in 1 state, it has the same probabilities of entering the next state (which might be the same state).  You have recorded the observed transitions in a mrix. The others in the lab have hypothesized more exotic forms that the ore can become, but you haven't seen all of them.

#Write a function solution(m) that takes an array of array of nonnegative ints representing how many times that state has gone to the next state and return an array of ints for each terminal state giving the exact probabilities of each terminal state, represented as the numerator for each state, then the denominator for all of them at the end and in simplest form. The mrix is at most 10 by 10. It is guaranteed that no mter which state the ore is in, there is a path from that state to a terminal state. That is, the processing will always eventually end in a stable state. The ore starts in state 0. The denominator will fit within a signed 32-bit integer during the calculation, as long as the fraction is simplified regularly. 

#For example, consider the mrix m:
#[
#  [0,1,0,0,0,1],  
  # s0, the initial state, goes to s1 and s5 with equal probability
#  [4,0,0,3,2,0],  
  # s1 can become s0, s3, or s4, but with different probabilities
 # [0,0,0,0,0,0],  
 # # s2 is terminal, and unreachable (never observed in practice)
 # [0,0,0,0,0,0],  
 # s3 is terminal
 # [0,0,0,0,0,0],  
 # # s4 is terminal
 # [0,0,0,0,0,0],  
 # # s5 is terminal
#]
#So, we can consider different paths to terminal states, such as:
#s0 -> s1 -> s3
#s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
#s0 -> s1 -> s0 -> s5
#Tracing the probabilities of each, we find that
#s2 has probability 0
#s3 has probability 3/14
#s4 has probability 1/7
#s5 has probability 9/14
#So, putting that together, and making a common denominator, gives an answer in the form of
#[s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
#[0, 3, 2, 9, 14].

#URLS to check

#solution here

from fractions import Fraction

def greatest_common(x, y):
    def gc1(x, y):
        if y == 0:
            return x
        return gc1(y, x%y)
    return gc1(abs(x), abs(y))

def simplify(x, y):
    g = greatest_common(x, y)
    return Fraction(long(x/g), long(y/g))

def least_common(x, y):
    return long(x*y/greatest_common(x,y))

def transform(m):
    sum_list = list(map(sum, m))
    bool_indices = list(map(lambda x: x == 0, sum_list))
    indices = set([i for i, x in enumerate(bool_indices) if x])
    new_m = []
    for i in range(len(m)):
        new_m.append(list(map(lambda x: Fraction(0, 1) if(sum_list[i] == 0) else simplify(x, sum_list[i]), m[i])))
    transform_m = []
    zeros_m = []
    for i in range(len(new_m)):
        if i not in indices:
            transform_m.append(new_m[i])
        else:
            zeros_m.append(new_m[i])
    transform_m.extend(zeros_m)
    tm = []
    for i in range(len(transform_m)):
        tm.append([])
        extend_m = []
        for j in range(len(transform_m)):
            if j not in indices:
                tm[i].append(transform_m[i][j])
            else:
                extend_m.append(transform_m[i][j])
        tm[i].extend(extend_m)
    return [tm, len(zeros_m)]

def copy_m(m):
    cm = []
    for i in range(len(m)):
        cm.append([])
        for j in range(len(m[i])):
            cm[i].append(Fraction(m[i][j].numerator, m[i][j].denominator))
    return cm

def ge(m, values):
    m = copy_m(m)
    for i in range(len(m)):
        index = -1
        for j in range(i, len(m)):
            if m[j][i].numerator != 0:
                index = j
                break
        if index == -1:
            raise ValueError('Gauss elimination failed!')
        m[i], m[index] = m[index], m[j]
        values[i], values[index] = values[index], values[i]
        for j in range(i+1, len(m)):
            if m[j][i].numerator == 0:
                continue
            ratio = -m[j][i]/m[i][i]
            for k in range(i, len(m)):
                m[j][k] += ratio * m[i][k]
            values[j] += ratio * values[i]
    res = [0 for i in range(len(m))]
    for i in range(len(m)):
        index = len(m) -1 -i
        end = len(m) - 1
        while end > index:
            values[index] -= m[index][end] * res[end]
            end -= 1
        res[index] = values[index]/m[index][index]
    return res

def transpose(m):
    tm = []
    for i in range(len(m)):
        for j in range(len(m)):
            if i == 0:
                tm.append([])
            tm[j].append(m[i][j])
    return tm

def inverse(m):
    tm = transpose(m)
    m_inv = []
    for i in range(len(tm)):
        values = [Fraction(int(i==j), 1) for j in range(len(m))]
        m_inv.append(ge(tm, values))
    return m_inv

def matTimes(first_m, second_m):
    res = []
    for i in range(len(first_m)):
        res.append([])
        for j in range(len(second_m[0])):
            res[i].append(Fraction(0, 1))
            for k in range(len(first_m[0])):
                res[i][j] += first_m[i][k] * second_m[k][j]
    return res

def split_two(m, length_r):
    length_q = len(m) - length_r
    Q = []
    R = []
    for i in range(length_q):
        Q.append([int(i==j)-m[i][j] for j in range(length_q)])
        R.append(m[i][length_q:])
    return [Q, R]

def solution(m):
    res = transform(m)
    if res[1] == len(m):
        return [1, 1]
    Q, R = split_two(*res)
    inv = inverse(Q)
    res = matTimes(inv, R)
    row = res[0]
    l = 1
    for item in row:
        l = least_common(l, item.denominator)
    res = list(map(lambda x: long(x.numerator*l/x.denominator), row))
    res.append(l)
    return res
