def solve(s, t):
   if len(s) != len(t):
      return False
   s = s + s
   return True if s.find(t) != -1 else False

s = "koLKAta"
t = "KAtakoL"
print(solve(s, t))