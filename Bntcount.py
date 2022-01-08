"""
Define a function ntcount that takes a string representing a DNA string. 

-First the function should check if it is a valid DNA strand (use the function defined in the 1st part). If it's not, return "error".

-If it is a valid DNA strand, the function returns a dictionary with the counts of each nucleotide.

For example: 
ntcount("AACTGTA") 
returns {"A": 3, "C": 1, "G": 1, "T": 2}
"""

def ntcount(dna):
  from Antcheck import isDNA
  if not isDNA(dna):
    return "error"
  lst = [char for char in dna]
  d1 = dict()
  for i in lst:
    d1[i] = d1.get(i, 0) + 1
  return d1