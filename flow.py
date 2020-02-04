"""Module for easy creation of block diagrams"""

from elements import *
import pyx

# TODO: make a Series() method that takes in list of blocks to connect in series

pyx.unit.set(defaultunit="pt")
pyx.text.set(pyx.text.LatexEngine)
pyx.text.preamble(r"\usepackage{amsmath}")

class Flow():
	"""Flow class for easy creation of block diagrams"""
	def __init__(self, name: str):
		self.name = name
		self._blocks: List[Block] = []
		self._nodes: List[Node] = []
		self._lines: List[Line] = []

	def NewBlock(self, shape='square', tex=None):
		newBlock = Block(shape=shape, tex=tex)
		self._blocks.append(newBlock)
		return newBlock

	def NewNode(self):
		newNode = Node()
		self._blocks.append(newNode)
		return newNode

	def NewLine(self, x0, y0, x1, y1):
		newLine = Line(x0, y0, x1, y1)
		self._lines.append(newLine)
		return newLine

	def Connect(self, fro: Block, to: Block):
		fro.output.append(to)
		to.input.append(fro)
	
		to.SetPosition(fro.cx + 40.0, fro.cy)

		newline = self.NewLine(fro.right, fro.cy, to.left, to.cy)

		return newline
		
	def Draw(self):
		canvas = pyx.canvas.canvas()

		# LOOP blocks
		for block in self._blocks:
			canvas.stroke(pyx.path.rect(block.left, block.bottom, block.width, block.height))

			if block.tex is not None:
				canvas.text(block.cx, block.cy, block.tex, [pyx.text.mathmode, pyx.text.size.footnotesize, pyx.text.halign.center, pyx.text.valign.middle])

		# LOOP lines
		for line in self._lines:
			canvas.stroke(pyx.path.line(line.x0, line.y0, line.x1, line.y1))


		# LOOP process node attributes and place

		canvas.writePDFfile(self.name)

		1+1
