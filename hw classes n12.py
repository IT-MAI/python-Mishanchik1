# 12
# x1,y1,z1,i1 - координаты точек начала и конца вектора №1 (аналогично для второго вектора)

import math

class Vector:
	# ИНИЦИАЛИЗАЦИЯ ПЕРВОГО ВЕКТОРА
	def plus(self, x1,y1,z1,i1,x2,y2,z2,i2):
		self.X1 = z1 - x1
		self.Y1 = i1 - y1
		self.X2 = z2 - x2
		self.Y2 = i2 - y2

		print("Результирующий вектор:", '{', self.X1 + self.X2, self.Y1 + self.Y2, '}')

	def umnozhenie_na_chislo(self,x1,y1,z1,i1, k):
		self.X1 = z1 - x1
		self.Y1 = i1 - y1
		print('Вектор после умножения на число:','{',self.X1 * k, self.Y1 *k, '}')

	def dlina(self, x1,y1,z1,i1):
		self.X1 = z1 - x1
		self.Y1 = i1 - y1
		print('Длина вектора:', math.sqrt(self.X1 ^ 2 + self.Y1 ^ 2))

	def skalyarnoe_p(self, x1,y1,z1,i1,x2,y2,z2,i2):
		self.X1 = z1 - x1
		self.Y1 = i1 - y1
		self.X2 = z2 - x2
		self.Y2 = i2 - y2
		print('Скалярное произведение векторов:', self.X1*self.X2 + self.Y1*self.Y2)

	def print(self, x1,y1,z1,i1):
		self.X1 = z1 - x1
		self.Y1 = i1 - y1
		print('Координаты вектора:', self.X1, self.Y1)

vector = Vector()

vector.plus(1,2,3,4,1,3,4,5)
vector.umnozhenie_na_chislo(1,2,3,4,10)
vector.dlina(1,2,3,4)	
vector.skalyarnoe_p(1,2,3,4,1,3,4,5)

vector.print(1,2,3,4)