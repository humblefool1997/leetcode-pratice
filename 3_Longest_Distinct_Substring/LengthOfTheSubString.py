# BruteForce Solution

def areDistinct(string, i,j):
  visited = [0] * (26)
  for k in range(i,j+1):
    if (visited[ord(string[k])-ord('a')]== True):
      return False
    visited[ord(string[k])-ord('a')] = True
  return True
  
def longestUniqueString(string):
  n = len(string)
  result = 0 
  for i in range(n):
    for j in range(n):
      if (areDistinct(string,i,j)):
        result = max(result,j-i+1)
  return result

  




def Solution():
   s = "geeksforgeeks"
   print("The Length of SubString",longestUniqueString(s))
   print(len(set(s)))


Solution()
   


