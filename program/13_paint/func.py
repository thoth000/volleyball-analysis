def func(data):
  left = data[5*3:5*3+2]
  right = data[6*3:6*3+2]
  
  mid = [(left[0]+right[0])/2,  (left[1]+right[1])/2, 0]
  
  data = mid + data
  return data

def paint(data, id1, id2, color):
  x1 = data[id1]
  y1 = data[id1+1]
  x2 = data[id2]
  y2 = data[id+1]
  
  