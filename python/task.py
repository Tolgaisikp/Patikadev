#1
data = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flatten_data = []

def flatten(data):
  for i in data:
    if type(i) == list:
      flatten(i)
    else:
      flatten_data.append(i)

  return flatten_data

#2
data = [[1, 2], [3, 4], [5, 6, 7]]
reverse_data = []

def reverse(data):
  for i in data:
    if type(i) == list:
      reverse_data.append(i[::-1])
  return reverse_data[::-1]
