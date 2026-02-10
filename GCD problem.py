import math


def get_ans(a, p, queries):
   cnt = 0
   g = 0

   for x in a:
       if x % p == 0:
           cnt += 1
           g = math.gcd(g, x)

   ans = 0

   for i, val in queries:
       i -= 1

       # remove old
       if a[i] % p == 0:
           cnt -= 1

       a[i] = val

       # add new
       if val % p == 0:
           cnt += 1

       # recompute gcd of divisible numbers (simplified)
       g = 0
       for x in a:
           if x % p == 0:
               g = math.gcd(g, x)

       if cnt > 0 and g == p:
           ans += 1

   return ans



numbers= [6, 10, 14, 9, 25]   # initial array
p = 2                    # we care about elements divisible by 2
q = 0                    # unused

querys = [
   (2, 22),   # change a[1]0 -> 22
   (4, 8),    # change a[3]9 -> 8
   (5, 18),   # change a[4]25 -> 18
   (1, 12),   # change a[0]6 -> 12
   (3, 7),    # change a[2]14 -> 7
]

print(get_ans(numbers,2,querys))