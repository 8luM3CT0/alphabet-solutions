#FOOBAR challenge #1

def decryption(m):
    initial = [i for i in range(97, 123)]
    final = [j for j in range(122, 96, -1)]
    cipher = {initial[k]: final[k] for k in range(len(initial))}

    dArray = []

    for l in m:
        if cipher.__contains__(ord(l)):
            dArray.append(chr(cipher[ord(l)]))
        else:
            dArray.append(l)
            
    return ''.join(dArray)

##FOOBAR challenge #2

def first_con(a, c):
    num = []
    while a > 0:
        num.insert(0, str(a % c))
        a  = a / c
    return ''.join(num)

def second_con(e, f):
  n = 0
  for d in str(e):
    n = f * n + int(d)
  return n

def final_con(x, y, b):
  if b==10:
    return int(x) - int(y)

  dx=second_con(x,b)
  dy=second_con(y,b)
  dz=dx-dy
  return first_con(dz, b)

def solution(n, b):
    arr=[]
    while True:
        i = "".join(sorted(str(n), reverse=True))
        j = "".join(sorted(str(n)))
        k = final_con(i,j,b)

        k2 = len(str(k))
        i2 = len(str(i))

        if (k2) != i2:
            k = k * pow(10 ,(i2-k2))

        for index, item in enumerate(arr):
          if item == k:
            return index + 1
        arr = [k] + arr
        n = k

#FOOBAR challenge #3.1

def bunnyMessages(l):
    initLen = len(l)
    max = 1 << initLen
    l.sort(reverse=True)
    fullTest = 0

    for mask in reversed(range(max)):
        attempt = ""
        for index in range(mask.bit_length()):
            attempt += str(l[index]) if (mask >> index) & 1 == 1 else ''
        if attempt == '':
            attempt = 0
        attempt = int(attempt)
        if attempt % 3 == 0:
            if attempt > fullTest:
                fullTest = attempt

    return fullTest

#Solution usage

if __name__ == "__main__":

    print('FOOBAR CHALLENGE 1 ')

    print('-----------------------------------------------')

    t1 = "wrw blf hvv ozhg mrtsg'h vkrhlwv?"
    print(decryption(t1))

    t2 =  "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
    print(decryption(t2))

    t3 = input("Enter the encrypted message >>>>>>")
    print(decryption(t3))
    
    print('-----------------------------------------------')

    
    print('FOOBAR CHALLENGE 2 ')

    print('-----------------------------------------------')
    
    print(solution(1211, 10))

    print(solution(210022, 3))
    
    print('-----------------------------------------------')

    print('FOOBAR CHALLENGE 3.1 ')

    print('-----------------------------------------------')
    
    print(bunnyMessages.solution([3, 1, 4, 1]))

    print('-----------------------------------------------')