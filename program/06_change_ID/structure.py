class Position:
  def __init__(self, x, y, vx = 0, vy = 0, count = 0):
    self.x  = x
    self.y  = y
    self.vx = vx
    self.vy = vy
    self.leaveCount = count # 更新されなかった回数
  
  def update(self, x, y):
    self.vx = x - self.x
    self.vy = y - self.y
    
    self.x = x
    self.y = y
    
    self.leaveCount += 1
  
  def predict(self):
    x = self.x + self.vx
    y = self.y + self.vy
    
    return Position(x, y, self.vx, self.vy, self.leaveCount+1)

