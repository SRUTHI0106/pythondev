def factorial(n):
  fact = 1
 
  for i in range(1, n+1):
    fact = fact * i
  return fact
# To print n factorials
def fact_for_range(start,end):
  factorials = []
  for i in range(start, end+1):
    factorials.append(factorial(i))
  return factorials
#optimal way to print factorial
def opti_fact_for_range(start, end):
  factorials = []
  temp = factorial(start)
  factorials.append(temp)
  for i in range(start+1, end+1):
    temp = i * temp
    factorials.append(temp)
  return factorials

print(fact_for_range(1,10))
print(opti_fact_for_range(1,10))
