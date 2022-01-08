"""
Define a function hammingdistance that takes 2 DNA string inputs.

-First the function should check if both strings are valid DNA strands (use the function defined in the 1st part). If it's not, return "error".

-Next, if the strings are of different lengths, the function should also return "error".

-If they are both valid DNA strands and the same length, the function calculates how many of the corresponding nucleotides in each string do not match (known as the Hamming Distance)

For example, hammingdistance("TTAC", "TGAA") should return 2.
"""

def hammingdistance(dna1, dna2):
  from Antcheck import isDNA
  if not isDNA(dna1):
    return "error"
  if not isDNA(dna2):
    return "error"

  lst = [char for char in dna1]
  lst2 = [char for char in dna2]
  lengthlist1 = len(lst)
  lengthlist2 = len(lst2)
  if lengthlist1 != lengthlist2:
    return "error"

  distance = 0
  for i in range(lengthlist1):
    if dna1[i] != dna2[i]:
      distance += 1
  return distance

  