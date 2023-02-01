import new
import old
import time
import numpy as np

def create3dVector():
  ret = (np.random.rand(3) - 0.5) * 1000
  return ret

sampleNum = 12**2
digit     = len(str(sampleNum))
coords =  []
vectors = []
for i in range(sampleNum + 1):
  coord  = create3dVector()
  vector = create3dVector()
  coords.append(coord)
  vectors.append(vector)

# 古い方
result_old = []
start = time.perf_counter()
for i in range(sampleNum):
  t1 = coords[i]
  v1 = vectors[i]
  
  t2 = coords[i+1]
  v2 = vectors[i+1]
  
  coord, error = old.oldCompute3dCoord(t1, v1, t2, v2)
  result_old.append(coord)
end = time.perf_counter()
print("old", end-start)

# 新しい方
result_new = []
start = time.perf_counter()
for i in range(sampleNum):
  t1 = coords[i]
  v1 = vectors[i]
  
  t2 = coords[i+1]
  v2 = vectors[i+1]
  
  coord, error = new.newCompute3dCoord(t1, v1, t2, v2)
  result_new.append(coord)
end = time.perf_counter()
print("new", end-start)

for i in range(sampleNum):
  print(str(i).zfill(digit), result_old[i], result_new[i])