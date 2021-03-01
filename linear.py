#---- 2D Vectors ----

class vector2:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def add2D(v1, v2):
	return vector2(v1.x + v2.x, v1.y + v2.y)

def sub2D(v1, v2):
	return vector2(v1.x - v2.x, v1.y - v2.y)

def dot2D(v1, v2):
	return v1.x*v2.x + v1.y*v2.y

def scalar2D(s, v):
	return vector2(s*v.x, s*v.y)

#---- 3D Vectors ----

class vector3:
	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z

def add3D(v1, v2, v3):
	return vector3(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z)

def sub3D(v1, v2):
	return vector3(v1.x - v2.x, v1.y - v2.y, v1.z - v2.z)

def dot3D(v1, v2):
	return v1.x*v2.x + v1.y*v2.y + v1.z*v2.z

def scalar3D(s, v):
	return vector3(s*v.x, s*v.y, s*v.z)

#---- RGB Values ----

class rgb:
	def __init__(self,r,g,b):
		self.r = r
		self.g = g
		self.b = b

def addColor():
	return

def subColor():
	return

def multiplyColor():
	return

def scalarColor():
	return

#---- Transforms ----


#---- Images ----
class image:
	def __init__(self,src):
		self.src = src

	def display():
		return

