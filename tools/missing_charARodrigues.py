def missing_char(str, n):
  front = str[:n]   # up to but not including n
  back = str[n+1:]  # n+1 through end of string
  return front + back

  #Test code for missing_char

print(missing_char('football', 1))
print(missing_char('football', 0))
print(missing_char('football', 4))


'''
def missing_char(str, n):

    return str[0:n] + str[n + 1;len(str)]

'''