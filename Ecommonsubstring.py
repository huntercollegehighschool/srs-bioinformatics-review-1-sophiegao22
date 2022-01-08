"""
Define a function commonsubstring that takes a list of DNA strings as an input.

-First the function should check if all strings in the list are valid DNA strands (use the function defined in the 1st part). If it's not, return "error".

-If all strings in the list are valid, the function then finds the longest nucleotide substring that is in all of the strings in the list and returns it as a list. If multiples such strings exist, the function should include them all in the returned list.

For example,
commonsubstring("ACGCT", "CGCCA", "ATTACGCT") should return ["CGC"]
"""


def listtostrings(s):
  str1 = " "
  return (str1.join(s))

def isDNANEW(dna):
  for i in dna:
    if i not in ["A", "T", "C", "G", " "]:
      return False
  else: 
    return True

def commonsubstring(dnalist):
  stringlist = listtostrings(dnalist)
  from Ecommonsubstring import isDNANEW
  if not isDNANEW(stringlist):
    return "error"
  x = len(dnalist)
  first = dnalist[0]
  firstlength = len(first)
  answer = ""
  for i in range (firstlength):
    for j in range (i+1, firstlength + 1):
      y = first[i:j]
      var=1
      for var in range (1,x):
        if y not in dnalist[var]:
          break
      if var+1 == x and len(answer)<len(y):
        answer = y
  return answer