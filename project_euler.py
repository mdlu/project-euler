import math
import time
import csv

start = time.time()

def problem_44():
    pentagonals = {n*(3*n-1)/2 for n in range(1,10000)}
    for p in pentagonals:
        for q in pentagonals:
            if p != q and p+q in pentagonals and p-q in pentagonals:
                print(p, q, p-q)

def primes(n):
    count = 0
    if n%2==0:
        count += 1
        while n%2==0:
            n //= 2
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n%i==0:
            count += 1
            while n%i==0:
                n //= i
    if n>2:
        count += 1
    return count >= 4

def problem_47():
    n = 647
    while True:
        if primes(n) and primes(n+1) and primes(n+2) and primes(n+3):
            return n
        n += 1

def is_square(n):
    return int(math.sqrt(n) + 0.5) ** 2 == n    


# squares = {x**2 for x in range(1000000)}

def dio_solve(d):
    n = 2
    while n < 1000000:
        if d*n**2+1 in squares:
            return math.sqrt(1+d*n**2)
        n += 1
    return "oops"

def problem_66():
    largest = 0
    track = 0
    for d in range(10, 1001):
        if d not in squares:
            ans = dio_solve(d)
            print(ans, d)
            if ans > largest:
                largest = ans
                track = d
    return largest, track


def compute_primes(n):
    primes = []
    if n%2==0:
        primes.append(2)
        while n%2==0:
            n //= 2
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n%i==0:
            primes.append(i)
            while n%i==0:
                n //= i
    if n>2:
        primes.append(n)
    return primes


def rwh_primes(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*int((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

# all_primes = rwh_primes(10000000)

# def compute_primes_new(n):
#     primes = []
#     index = 0
#     stopp = int(math.sqrt(n)) + 1
#     while all_primes[index] < stopp:
#         p = all_primes[index]
#         if n%p==0:
#             primes.append(p)
#             while n%p==0:
#                 n //= p
#         index += 1
#     if n>2:
#         primes.append(n)
#     return primes

def totient(n):
    primes = compute_primes(n)
    hold = n
    for p in primes:
        hold = hold*(p-1)//p
    return hold

def problem_69():
    largest = 0
    answer = 0
    for n in range(2, 1000000):
        val = n/totient(n)
        if val > largest:
            largest = val
            answer = n
    return answer

# print(problem_69())

def digits(x):
    ds = [0]*10
    while x != 0:
        ones = x%10
        x = x//10
        ds[ones] += 1
    return ds

def is_permute(a, b):
    return digits(a) == digits(b)


def problem_70():
    ans = 1000000000
    tot = 1
    for n in range(3, 10000000):
        val = totient(n)
        if is_permute(n, val):
            if n*tot < ans*val:
                ans = n
                tot = val
                print(ans, tot)
    return ans, tot

def problem_72():
    sum = 0
    for n in range(2, 1000001):
        sum += totient(n)
    return sum

def problem_81():
    matrix = []
    with open('p081_matrix.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            matrix.append([int(elem) for elem in row])
    
    #first row
    for c in range(1, len(matrix[0])):
        matrix[0][c] += matrix[0][c-1]

    #first column
    for r in range(1, len(matrix)):
        matrix[r][0] += matrix[r-1][0]
    
    for r in range(1, len(matrix)):
        for c in range(1, len(matrix[0])):
            matrix[r][c] += min(matrix[r-1][c], matrix[r][c-1])
    
    return matrix


def square_sum(x):
    sum = 0
    while x != 0:
        sum += (x%10)**2
        x //= 10
    return sum

def problem_92():
    answers = {89}
    for n in range(2, 10000000):
        temp = n
        while temp != 1:
            temp = square_sum(temp)
            if temp in answers:
                answers.add(n)
                break
    return len(answers)

def problem_49():
    primes_four_digit = rwh_primes(10000)
    ps = [p for p in primes_four_digit if p>=1000]

    maps = {x: [] for x in range(10000)}

    for p in ps:
        in_order = int("".join(sorted(str(p))))
        maps[in_order].append(p)
    
    for key in maps:
        if len(maps[key]) >= 3:
            if any([(c-b) == (b-a) for a in maps[key] for b in maps[key] for c in maps[key] if a!=b]):
                print(key, maps[key])

def problem_50():
    primes_list = rwh_primes(1000000)
    # primes_set = set(primes_list)

    counts = {p: 0 for p in primes_list}

    for index in range(10000):
        count = 0
        sum = 0
        n = index

        while sum < 1000000:
            sum += primes_list[n]
            count += 1
            n += 1

            if sum in counts and count > counts[sum]:
                counts[sum] = count
    
    ans = max(counts, key=counts.get)
    return ans, counts[ans]


def problem_206():
    def is_valid(x):
        return x%10 == 0 and x//10**2%10 == 9 and x//10**4%10 == 8 and x//10**6%10==7 and x//10**8%10==6 and x//10**10%10==5 and x//10**12%10==4 and x//10**14%10==3 and x//10**16%10==2

    n = 1010101030
    while True:
        squared = n**2
        if is_valid(squared):
            return squared
        n += 40

        squared = n**2
        if is_valid(squared):
            return squared, n
        n += 60

def sum_digits(x):
    sum = 0
    while x != 0:
        sum += x%10
        x //= 10
    return sum

def problem_65():
    cs = [2, 1]
    for i in range(1, 34):
        cs.extend([2*i, 1, 1])
    
    a = 1
    b = cs[99]
    c = 0

    for n in range(98, -1, -1):
        c = b
        b = cs[n]*b + a
        a = c
    
    return sum_digits(b)

# def totient_fraction(n, frac):
#     primes = compute_primes(n)
#     hold = math.floor(n/frac)
#     for p in primes:
#         hold = hold*(p-1)/p
#     return math.ceil(hold)

def problem_73():
    # sum = 0
    # for n in range(4, 12001):
    #     sum += (totient_fraction(n, 2)-totient_fraction(n,3))
    # return sum
    sum = 0
    for n in range(4, 12001):
        for x in range(1, n):
            if math.gcd(x, n) == 1 and n<3*x and n>2*x:
                sum += 1
    return sum

def problem_61():
    n = 2
    while n*(5*n-3)//2 < 10000:
        hept =  n*(5*n-3)//2
        if hept > 1000:
            print(hept)
        n += 1

def problem_243():
    # primes = rwh_primes(1000000)
    # index = 0
    # product = 1
    # euler = 1
    # while True:
    #     p = primes[index]
    #     product *= p
    #     euler *= p-1
    #     if euler*94744 < 15499*(product-1):
    #         return product
    #     index += 1
    
    num = 223092870
    for i in range(1, 30):
        new_num = num*i
        if totient(new_num)*94744 < 15499*(new_num-1):
            return new_num
    return "failed"

def problem_89():
    numerals = []
    with open('p089_roman.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            numerals.extend(row)
    
    ans = 0

    for num in numerals:
        for i in range(len(num)-4):
            if num[i:i+5] in ['VIIII', 'LXXXX', 'DCCCC']:
                ans += 3
                # print(num, "one")
        if num[0:4] in ['IIII', 'XXXX', 'CCCC']:
            ans += 2
            # print(num, "two")

        for i in range(1, len(num)-3):
            if num[i:i+4] in ['IIII', 'XXXX', 'CCCC'] and num[i-1:i+4] not in ['VIIII', 'LXXXX', 'DCCCC']:
                ans += 2
                # print(num, "three")
    return ans

print(problem_89())

end = time.time()
print(end-start)
