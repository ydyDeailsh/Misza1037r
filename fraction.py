def dc(n):
  k = n
  r = []
  while k != 1:
    i = 2
    while k%i!=0:
      i+=1
    r.append(i)
    k = k//i
  return r if len(r) != 0 else [1]


def common(a,b): 
  c = [value for value in a if value in b] 
  return c


class Fraction:
  def __init__(self, l):
    if type(l) != list: raise TypeError('')
    if len(l) != 2: raise ValueError('')
    self.l = l
  def cut(self):
    if self.l[0]//self.l[1] == self.l[0]/self.l[1]:
      self.l[0] = self.l[0]//self.l[1]
      self.l[1] = 1
      return self.l
    n = common(dc(self.l[0]), dc(self.l[1]))
    if n == []: return self.l 
    m = 1
    for i in n:
      m *= i
    self.l[0] /= m
    self.l[1] /= m
    return self.l
      