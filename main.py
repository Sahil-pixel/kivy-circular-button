from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.vector import Vector
from kivy.graphics import*
from kivy.uix.label import*
from kivy.app import*
from kivy.uix.gridlayout import*
from kivy.uix.button import*
class CircularButton(ButtonBehavior,Label):
	def __init__(self,**k):
		super().__init__(**k)
		self.bind(pos=self.update_rect, size=self.update_rect)
		with self.canvas.before:
			self.clr=Color(rgba=(0,0,1,1)) # green; colors range from 0-1 instead of 0-255
			
			self.rect=Ellipse(size=self.size,pos=self.pos)
		
		

	def update_rect(self,instance, value):
		instance.rect.pos = instance.pos
		instance.rect.size = instance.size

					  
	def on_press(self):
		self.clr.rgba=(1,0,0,1)
	def on_release(self):
		self.clr.rgba=(0,0,1,1)
	def collide_point(self, x, y):
		return Vector(x, y).distance(self.center) <= self.width / 2

class A(App):
	def build(self):
		g=GridLayout(cols=4)
		for i in range(10):
			g.add_widget(CircularButton(text='hhh',on_release=self.p))
			g.add_widget(Button())
		return g
	def p(self,o):
		print('hhhhhh')
A().run()

