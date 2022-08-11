import numpy as np

def calculate(list):
  if len(list)!=9:
    raise ValueError("List must contain nine numbers.")
  else:
    arr1=[]
    arr1.append(list[0:3])
    arr1.append(list[3:6])
    arr1.append(list[6:])
    calculations={}
    

  calculations=0
  return calculations