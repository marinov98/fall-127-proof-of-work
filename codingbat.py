Homework#1:
#######ZAMANSKY HOMEWORK 1
def string_times(str, n):
    return str*n
##################################Homework 2
def front_times(str, n):
    return str[:3]*n     ## CHO CHO
##########################Homework 3
def front_times(str, n):
  return str[:3]*n
#############################################
def lone_sum(a, b, c):
  if a==b==c:
    a,b,c = 0,0,0
  elif a==c:
    a,c=0,0
  elif b==c:
    b,c=0,0
  elif a==b:
    a,b=0,0
  return a+b+c
##################################################
def string_splosion(str):
  result = ""
    result = result + str[:i+1]
  return result
############################################
if is_weekend:
    return 40<=cigars
  elif 40<=cigars<=60:
      return True
  elif cigars<40 or cigars>60:
      return False
#############################################
def caught_speeding(speed, is_birthday):
  if is_birthday:
    if speed<=65:
      return 0
    elif 66<=speed<=85:
      return 1
    elif 86<=speed:
      return 2
  else:
    if speed<=60:
      return 0
    elif 61<=speed<=80:
      return 1
    elif 81<=speed:
      return 2
##################################################

print(caught_speeding(67,True))
print(cigar_party(50, is_weekend))
print(string_splosion('Base'))
print(front_times('hello',6)
print(lone_sum(5,4,3))
print(string_times('maybe',5))
print(front_times('hello',6))
