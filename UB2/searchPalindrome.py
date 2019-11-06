
class MemoryUnit:
	def __init__(self, content):
		self.content = content
		self.has_special_sign = False

	def isEmpty(self):
		if self.content = '\0':
			return True
		return False

	def setSpecialSign(self):
		self.has_special_sign = True

	def boolSpecialSign(self)
		if self.has_special_sign:
			return True
		return False


class Memory:
	def __init__(self , content):
		self.memory = content
		self.current_index = 0

	def moveLeft(self):
		return self.memory[self.current_index-1]

	def moveRight(self):
		return self.memory[self.current_index+1]


class Palindrome_TM:
	def __init__(self , memory , buffer_size):
		self.memory = memory
		self.buffer_size = buffer_size
		self.buffer = []
		self.num_of_steps = 0 

	def ifPalindrome(self):
		temp_buffer = 0 
		while self:
			self.memory.moveRight()


		