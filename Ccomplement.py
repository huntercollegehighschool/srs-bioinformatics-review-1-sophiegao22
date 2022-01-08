"""
Define a function reversecomplement that takes a DNA string as an input. 

-First the function should check if it is a valid DNA strand (use the function defined in the 1st part). If it's not, return "error".

-If it is a valid DNA string, the function finds the reverse complement of that string. The reverse complement is found by first reversing the string, then taking the complement of each nucleotide. A and T are complements of each other, and C and G are complements of each other.

For example,
reversecomplement("AAGCT") should return "AGCTT".
"""

def reversecomplement(dna):
  from Antcheck import isDNA
  if not isDNA(dna):
    return "error"
  reversedna = dna [::-1]
  lst = [char for char in reversedna]
  lst2 = []
  for i in lst:
    if i == "A":
      lst2.append("T")
    if i == "T":
      lst2.append("A")
    if i == "C":
      lst2.append("G")
    if i == "G":
      lst2.append("C")
  new = ""
  return (new.join(lst2))
  