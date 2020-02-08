class BoundingBox():
	def __init__(self, cx, cy, width, height):
		self.width = width
		self.height = height

		self.cx = cx
		self.cy = cy

		self.left = self.cx - 0.5 * self.width
		self.right = self.cx + 0.5 * self.width
		self.top = self.cy + 0.5 * self.height
		self.bottom = self.cy - 0.5 * self.height

	@property
    def cx(self):
        return self.cx

	@property
    def cy(self):
        return self.cy

    @cx.setter
    def cx(self, value):
        self.cx = value
		self.left = self.cx - 0.5 * self.width
		self.right = self.cx + 0.5 * self.width


	@cy.setter
    def cy(self, value):
        self.cx = value
		self.top = self.cy + 0.5 * self.height
		self.bottom = self.cy - 0.5 * self.height
