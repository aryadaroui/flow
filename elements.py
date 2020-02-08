
from aenum import Enum
from typing import List

# is this a stupid way of doing this? TODO: determine if this is stupid
SQUARE = 'square'
RECT = 'rect'
CIRC = 'circ'
TRI = 'tri'
NONE = 'None'
SOLID = 'solid'
DOTTED = 'dotted'
DASHED = 'dashed'

GRAY = (0.5, 0.5, 0.5, 1.0)
WHITE = (0.0, 0.0, 0.0, 1.0)
BLACK = (1.0, 1.0, 1.0, 1.0)

class Shape():
	SQUARE = SQUARE
	RECT = RECT
	CIRC = CIRC
	TRI = TRI

class Style():
	SOLID = SOLID
	DASHED = DASHED
	DOTTED = DOTTED

class Block:
	def __init__(self, shape=SQUARE, tex=None):
		if shape is None:
			shape = NONE
		if not hasattr(Shape, str.upper(shape)):
			raise ValueError("Bad input '" + str(shape) +  r"'. Input string must be 'square', 'rect', 'circ', or 'tri'")

		self.cx = 0.0
		self.cy = 0.0

		self.width = 20.0
		self.height = 20.0

		self.left = self.cx - 0.5 * self.width
		self.right = self.cx + 0.5 * self.width
		self.top = self.cy + 0.5 * self.height
		self.bottom = self.cy - 0.5 * self.height

		self.shape = shape
		self.stroke = Stroke()
		self.fill = Fill()

		# if shape == '':
		# 	self.stroke.color = (0.5, 0.5, 0.5, 1.0)

		self.tex = tex
		self.rotation = 0.0

		self.numInputs = 1
		self.numOutputs = 1

		self.leftText = ""
		self.rightText = ""
		self.topText = ""
		self.bottomText = ""

		self.input: List[Block] = []
		self.output: List[Block] = []

	def SetPosition(self, x: float, y: float):
		self.cx = x
		self.cy = y

		self.left = self.cx - 0.5 * self.width
		self.right = self.cx + 0.5 * self.width
		self.top = self.cy + 0.5 * self.height
		self.bottom = self.cy - 0.5 * self.height

	def SetDimensions(self, width: float, height: float):
		self.width = width
		self.height = height

		self.left = self.cx - 0.5 * self.width
		self.right = self.cx + 0.5 * self.width
		self.top = self.cy + 0.5 * self.height
		self.bottom = self.cy - 0.5 * self.height


class Node:
	def __init__(self):
		self.x = 1.0
		self.y = 1.0
		self.width = 1.0
		self.height = 1.0
		self.stroke = Stroke()
		self.media = ''

class Line:
	def __init__(self, x0, y0, x1, y1):
		self.x0 = x0
		self.y0 = y0
		self.x1 = x1
		self.y1 = y1
		self.stroke = Stroke()
		# self.media = media

class Stroke:
	def	__init__(self, width=0.5, style='solid', color=WHITE):

		self.width = width
		self.style = style
		self.color = color

class Fill:
	def __init__(self, color=BLACK, style='solid'):
		self.color = color
		self.style = style

