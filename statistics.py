import math

def calculateStats(numbers):
  if(len(numbers) == 0):
    return {"avg" = nan, "max" = nan, "min" = nan}
  else:
  return{"avg" = sum(numbers)/len(numners), "max" = max(numbers), "min" = min(numbers)}
