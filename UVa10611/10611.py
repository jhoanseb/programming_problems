"""
UVa Online Judge
10611 - The Playboy Chimp problem
Made by: Jhoan Lozano (jhoanseb)
date: 22/12/2019
"""
from sys import stdin

def solve(ladies, x):
  """solution of the problem based on binary search.

  @param ladies: heights list of the chimpanzee ladies.
  @param x: height to consult.
  """
  ans, N = [-1,-1], len(ladies)
  if N>=1:
    lo,hi = 0,N
    while lo+1!=hi:
      mid = lo + ((hi-lo)>>1)
      if ladies[mid] > x: hi = mid
      else: lo = mid
      if lo+1==hi:
        if ladies[lo] > x: ans = [ladies[lo-1] if lo-1>=0 else -1,ladies[lo]]
        elif ladies[lo] < x: ans = [ladies[lo],ladies[lo+1] if lo+1<N else -1]
        else:
          i,j = lo-1,lo+1
          while (i>=0 and ladies[i]==x) or (j<N and ladies[j]==x):
            if i>=0 and ladies[i] == x: i-=1
            if j<N and ladies[j] == x: j+=1
          ans = [ladies[i] if i>=0 else -1, ladies[j] if j<N else -1]
  return ans

def main():
  inp = stdin
  inp.readline()
  ladies = [ int(x) for x in inp.readline().split() ]
  inp.readline()
  queries = [ int(x) for x in inp.readline().split() ]
  for x in queries:
    ans = solve(ladies, x)
    print(ans[0] if ans[0]!=-1 else 'X',ans[1] if ans[1]!=-1 else 'X')
main()

