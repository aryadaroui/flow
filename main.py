"""written by Arya Daroui"""

from flow import *


simple = Flow("test")


inp = simple.NewBlock(tex=r"X(s)")
func = simple.NewBlock(tex=r"H(s)")
out = simple.NewBlock(tex=r"Y(s)")

simple.Connect(inp, func)
simple.Connect(func, out)


simple.Draw()