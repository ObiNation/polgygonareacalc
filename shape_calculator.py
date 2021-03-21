class Rectangle:
  def __init__(self, width = 0, height = 0):
    self.height = height
    self.width = width
  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"
  
  
  def get_area(self):
    return self.width * self.height
  
  def get_perimeter(self):
    return (2 *self.width + 2* self.height)
  
  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2 ) ** .5)

  def get_picture(self):
    if self.height < 50 and self.width < 50:
      w = "*" * self.width
      picture = ""
      for line in range(self.height):
        picture = picture + w + "\n"
      return picture
    elif self.height > 50 or self.width > 50:
      return "Too big for picture." 
  
  def set_width(self, x):
    self.width = x
  
  def set_height(self, y):
    self.height = y
  
  def get_amount_inside(self, shape):
    areaGuest = shape.get_area()
    areaHome = self.get_area()
    i = 0
    while areaHome>=areaGuest:
      areaHome = areaHome - areaGuest
      i = i + 1
    return i
  
  


class Square(Rectangle):
  def __init__(self, side = 0):
    self.width = side
    self.height = side
    self.side = side
    Rectangle.__init__(self, width=side, height=side)
  def __str__(self):
    return "Square(side={})".format(self.width)
  
  
  def set_side(self, z):
    self.width = z
    self.height = z
  
  
