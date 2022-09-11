def first_non_repeating_character(str1):
  char_order = []
  ctr = {}
  for i in str1:
    if i in ctr:
      ctr[i] += 1
    else:
      ctr[i] = 1 
      char_order.append(i)
  for i in char_order:
    if ctr[i] == 1:
      return i
  return None

print(first_non_repeating_character('abcdef'))
print(first_non_repeating_character('abcabcdef'))
print(first_non_repeating_character('aabbcc'))