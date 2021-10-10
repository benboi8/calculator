import sys
sys.path.insert(1, "/Python Projects/GuiObjects")
from GUIObjects import *

width, height = 170, 210
sf = 2
screen = pg.display.set_mode((width * sf, height * sf))

Label(surface = screen, name = "output", rect = (10, 10, 150, 30), colors = ((45, 45, 45), (215, 215, 215)), drawData = {'drawBorder': True, 'borderWidth': 1, 'isFilled': False, 'roundedEdges': False, 'roundedCorners': False, 'roundness': 10, 'activeCorners': {'topLeft': True, 'topRight': True, 'bottomLeft': True, 'bottomRight': True}}, imageData = {'isAnimation': False, 'numOfFrames': 0, 'frameRate': 60, 'filePath': None, 'size': (120, 30)}, text = "", font = ("arial", 12, (255, 255, 255)), textData = {'alignText': 'center', 'drawText': True, 'multiline': False, 'isScrollable': False, 'scrollAmount': 28})
Button(surface = screen, name = "1", rect = (10, 50, 30, 30), colors = ((45, 45, 45), (215, 215, 215), (184, 39, 39)), drawData = {'drawBorder': True, 'borderWidth': 1, 'isFilled': False, 'roundedEdges': False, 'roundedCorners': False, 'roundness': 10, 'activeCorners': {'topLeft': True, 'topRight': True, 'bottomLeft': True, 'bottomRight': True}}, imageData = {'isAnimation': False, 'numOfFrames': 0, 'frameRate': 60, 'filePath': None, 'size': (120, 30)}, text = "1", font = ("arial", 12, (255, 255, 255)), textData = {'alignText': 'center', 'drawText': True, 'multiline': False, 'isScrollable': False, 'scrollAmount': 28}, inputData = {'active': False}, isHoldButton = True)
Button(surface = screen, name = "2", rect = (50, 50, 30, 30), colors = ((45, 45, 45), (215, 215, 215), (184, 39, 39)), drawData = {'drawBorder': True, 'borderWidth': 1, 'isFilled': False, 'roundedEdges': False, 'roundedCorners': False, 'roundness': 10, 'activeCorners': {'topLeft': True, 'topRight': True, 'bottomLeft': True, 'bottomRight': True}}, imageData = {'isAnimation': False, 'numOfFrames': 0, 'frameRate': 60, 'filePath': None, 'size': (120, 30)}, text = "2", font = ("arial", 12, (255, 255, 255)), textData = {'alignText': 'center', 'drawText': True, 'multiline': False, 'isScrollable': False, 'scrollAmount': 28}, inputData = {'active': False}, isHoldButton = True)
Button(surface = screen, name = "3", rect = (90, 50, 30, 30), colors = ((45, 45, 45), (215, 215, 215), (184, 39, 39)), drawData = {'drawBorder': True, 'borderWidth': 1, 'isFilled': False, 'roundedEdges': False, 'roundedCorners': False, 'roundness': 10, 'activeCorners': {'topLeft': True, 'topRight': True, 'bottomLeft': True, 'bottomRight': True}}, imageData = {'isAnimation': False, 'numOfFrames': 0, 'frameRate': 60, 'filePath': None, 'size': (120, 30)}, text = "3", font = ("arial", 12, (255, 255, 255)), textData = {'alignText': 'center', 'drawText': True, 'multiline': False, 'isScrollable': False, 'scrollAmount': 28}, inputData = {'active': False}, isHoldButton = True)
Button(surface = screen, name = "4", rect = (10, 90, 30, 30), colors = ((45, 45, 45), (215, 215, 215), (184, 39, 39)), drawData = {'drawBorder': True, 'borderWidth': 1, 'isFilled': False, 'roundedEdges': False, 'roundedCorners': False, 'roundness': 10, 'activeCorners': {'topLeft': True, 'topRight': True, 'bottomLeft': True, 'bottomRight': True}}, imageData = {'isAnimation': False, 'numOfFrames': 0, 'frameRate': 60, 'filePath': None, 'size': (120, 30)}, text = "4", font = ("arial", 12, (255, 255, 255)), textData = {'alignText': 'center', 'drawText': True, 'multiline': False, 'isScrollable': False, 'scrollAmount': 28}, inputData = {'active': False}, isHoldButton = True)
Button(surface = screen, name = "5", rect = (50, 90, 30, 30), colors = ((45, 45, 45), (215, 215, 215), (184, 39, 39)), drawData = {'drawBorder': True, 'borderWidth': 1, 'isFilled': False, 'roundedEdges': False, 'roundedCorners': False, 'roundness': 10, 'activeCorners': {'topLeft': True, 'topRight': True, 'bottomLeft': True, 'bottomRight': True}}, imageData = {'isAnimation': False, 'numOfFrames': 0, 'frameRate': 60, 'filePath': None, 'size': (120, 30)}, text = "5", font = ("arial", 12, (255, 255, 255)), textData = {'alignText': 'center', 'drawText': True, 'multiline': False, 'isScrollable': False, 'scrollAmount': 28}, inputData = {'active': False}, isHoldButton = True)
Button(surface = screen, name = "6", rect = (90, 90, 30, 30), colors = ((45, 45, 45), (215, 215, 215), (184, 39, 39)), drawData = {'drawBorder': True, 'borderWidth': 1, 'isFilled': False, 'roundedEdges': False, 'roundedCorners': False, 'roundness': 10, 'activeCorners': {'topLeft': True, 'topRight': True, 'bottomLeft': True, 'bottomRight': True}}, imageData = {'isAnimation': False, 'numOfFrames': 0, 'frameRate': 60, 'filePath': None, 'size': (120, 30)}, text = "6", font = ("arial", 12, (255, 255, 255)), textData = {'alignText': 'center', 'drawText': True, 'multiline': False, 'isScrollable': False, 'scrollAmount': 28}, inputData = {'active': False}, isHoldButton = True)
Button(surface = screen, name = "7", rect = (10, 130, 30, 30), colors = ((45, 45, 45), (215, 215, 215), (184, 39, 39)), drawData = {'drawBorder': True, 'borderWidth': 1, 'isFilled': False, 'roundedEdges': False, 'roundedCorners': False, 'roundness': 10, 'activeCorners': {'topLeft': True, 'topRight': True, 'bottomLeft': True, 'bottomRight': True}}, imageData = {'isAnimation': False, 'numOfFrames': 0, 'frameRate': 60, 'filePath': None, 'size': (120, 30)}, text = "7", font = ("arial", 12, (255, 255, 255)), textData = {'alignText': 'center', 'drawText': True, 'multiline': False, 'isScrollable': False, 'scrollAmount': 28}, inputData = {'active': False}, isHoldButton = True)
Button(surface = screen, name = "8", rect = (50, 130, 30, 30), colors = ((45, 45, 45), (215, 215, 215), (184, 39, 39)), drawData = {'drawBorder': True, 'borderWidth': 1, 'isFilled': False, 'roundedEdges': False, 'roundedCorners': False, 'roundness': 10, 'activeCorners': {'topLeft': True, 'topRight': True, 'bottomLeft': True, 'bottomRight': True}}, imageData = {'isAnimation': False, 'numOfFrames': 0, 'frameRate': 60, 'filePath': None, 'size': (120, 30)}, text = "8", font = ("arial", 12, (255, 255, 255)), textData = {'alignText': 'center', 'drawText': True, 'multiline': False, 'isScrollable': False, 'scrollAmount': 28}, inputData = {'active': False}, isHoldButton = True)
Button(surface = screen, name = "9", rect = (90, 130, 30, 30), colors = ((45, 45, 45), (215, 215, 215), (184, 39, 39)), drawData = {'drawBorder': True, 'borderWidth': 1, 'isFilled': False, 'roundedEdges': False, 'roundedCorners': False, 'roundness': 10, 'activeCorners': {'topLeft': True, 'topRight': True, 'bottomLeft': True, 'bottomRight': True}}, imageData = {'isAnimation': False, 'numOfFrames': 0, 'frameRate': 60, 'filePath': None, 'size': (120, 30)}, text = "9", font = ("arial", 12, (255, 255, 255)), textData = {'alignText': 'center', 'drawText': True, 'multiline': False, 'isScrollable': False, 'scrollAmount': 28}, inputData = {'active': False}, isHoldButton = True)
Button(surface = screen, name = "0", rect = (50, 170, 30, 30), colors = ((45, 45, 45), (215, 215, 215), (184, 39, 39)), drawData = {'drawBorder': True, 'borderWidth': 1, 'isFilled': False, 'roundedEdges': False, 'roundedCorners': False, 'roundness': 10, 'activeCorners': {'topLeft': True, 'topRight': True, 'bottomLeft': True, 'bottomRight': True}}, imageData = {'isAnimation': False, 'numOfFrames': 0, 'frameRate': 60, 'filePath': None, 'size': (120, 30)}, text = "0", font = ("arial", 12, (255, 255, 255)), textData = {'alignText': 'center', 'drawText': True, 'multiline': False, 'isScrollable': False, 'scrollAmount': 28}, inputData = {'active': False}, isHoldButton = True)
Button(surface = screen, name = "clear", rect = (10, 170, 30, 30), colors = ((45, 45, 45), (215, 215, 215), (184, 39, 39)), drawData = {'drawBorder': True, 'borderWidth': 1, 'isFilled': False, 'roundedEdges': False, 'roundedCorners': False, 'roundness': 10, 'activeCorners': {'topLeft': True, 'topRight': True, 'bottomLeft': True, 'bottomRight': True}}, imageData = {'isAnimation': False, 'numOfFrames': 0, 'frameRate': 60, 'filePath': None, 'size': (120, 30)}, text = "Clear", font = ("arial", 12, (255, 255, 255)), textData = {'alignText': 'center', 'drawText': True, 'multiline': False, 'isScrollable': False, 'scrollAmount': 28}, inputData = {'active': False}, isHoldButton = True)
Button(surface = screen, name = "=", rect = (90, 170, 30, 30), colors = ((45, 45, 45), (215, 215, 215), (184, 39, 39)), drawData = {'drawBorder': True, 'borderWidth': 1, 'isFilled': False, 'roundedEdges': False, 'roundedCorners': False, 'roundness': 10, 'activeCorners': {'topLeft': True, 'topRight': True, 'bottomLeft': True, 'bottomRight': True}}, imageData = {'isAnimation': False, 'numOfFrames': 0, 'frameRate': 60, 'filePath': None, 'size': (120, 30)}, text = "=", font = ("arial", 12, (255, 255, 255)), textData = {'alignText': 'center', 'drawText': True, 'multiline': False, 'isScrollable': False, 'scrollAmount': 28}, inputData = {'active': False}, isHoldButton = True)
Button(surface = screen, name = "+", rect = (130, 50, 30, 30), colors = ((45, 45, 45), (215, 215, 215), (184, 39, 39)), drawData = {'drawBorder': True, 'borderWidth': 1, 'isFilled': False, 'roundedEdges': False, 'roundedCorners': False, 'roundness': 10, 'activeCorners': {'topLeft': True, 'topRight': True, 'bottomLeft': True, 'bottomRight': True}}, imageData = {'isAnimation': False, 'numOfFrames': 0, 'frameRate': 60, 'filePath': None, 'size': (120, 30)}, text = "+", font = ("arial", 12, (255, 255, 255)), textData = {'alignText': 'center', 'drawText': True, 'multiline': False, 'isScrollable': False, 'scrollAmount': 28}, inputData = {'active': False}, isHoldButton = True)
Button(surface = screen, name = "-", rect = (130, 90, 30, 30), colors = ((45, 45, 45), (215, 215, 215), (184, 39, 39)), drawData = {'drawBorder': True, 'borderWidth': 1, 'isFilled': False, 'roundedEdges': False, 'roundedCorners': False, 'roundness': 10, 'activeCorners': {'topLeft': True, 'topRight': True, 'bottomLeft': True, 'bottomRight': True}}, imageData = {'isAnimation': False, 'numOfFrames': 0, 'frameRate': 60, 'filePath': None, 'size': (120, 30)}, text = "-", font = ("arial", 12, (255, 255, 255)), textData = {'alignText': 'center', 'drawText': True, 'multiline': False, 'isScrollable': False, 'scrollAmount': 28}, inputData = {'active': False}, isHoldButton = True)
Button(surface = screen, name = "/", rect = (130, 130, 30, 30), colors = ((45, 45, 45), (215, 215, 215), (184, 39, 39)), drawData = {'drawBorder': True, 'borderWidth': 1, 'isFilled': False, 'roundedEdges': False, 'roundedCorners': False, 'roundness': 10, 'activeCorners': {'topLeft': True, 'topRight': True, 'bottomLeft': True, 'bottomRight': True}}, imageData = {'isAnimation': False, 'numOfFrames': 0, 'frameRate': 60, 'filePath': None, 'size': (120, 30)}, text = "/", font = ("arial", 12, (255, 255, 255)), textData = {'alignText': 'center', 'drawText': True, 'multiline': False, 'isScrollable': False, 'scrollAmount': 28}, inputData = {'active': False}, isHoldButton = True)
Button(surface = screen, name = "*", rect = (130, 170, 30, 30), colors = ((45, 45, 45), (215, 215, 215), (184, 39, 39)), drawData = {'drawBorder': True, 'borderWidth': 1, 'isFilled': False, 'roundedEdges': False, 'roundedCorners': False, 'roundness': 10, 'activeCorners': {'topLeft': True, 'topRight': True, 'bottomLeft': True, 'bottomRight': True}}, imageData = {'isAnimation': False, 'numOfFrames': 0, 'frameRate': 60, 'filePath': None, 'size': (120, 30)}, text = "*", font = ("arial", 12, (255, 255, 255)), textData = {'alignText': 'center', 'drawText': True, 'multiline': False, 'isScrollable': False, 'scrollAmount': 28}, inputData = {'active': False}, isHoldButton = True)
Box(surface = screen, name = "boundingBox", rect = (0, 0, 170, 210), colors = ((45, 45, 45), (215, 215, 215)), drawData = {'drawBorder': True, 'borderWidth': 1, 'isFilled': False, 'roundedEdges': False, 'roundedCorners': False, 'roundness': 10, 'activeCorners': {'topLeft': True, 'topRight': True, 'bottomLeft': True, 'bottomRight': True}})

equation = ""


def Calculate(num1, op, num2):
	if op == "+":
		return num1 + num2
	if op == "-":
		return num1 - num2
	if op == "*":
		return num1 * num2
	if op == "/":
		return num1 / num2

def GetCalc(equation):
	args = equation.split(" ")
	numbers = []
	ops = []

	for a in args:
		try:
			numbers.append(float(a))
		except:
			ops.append(a)

	result = numbers[0]
	print(numbers, ops)
	for i in range(len(ops)):
		print(numbers[i + 1], ops[i], result)
		result = Calculate(result, ops[i], numbers[i + 1])

	print(result)

	return f"{equation} = {result}"

def Quit():
	global running
	running = False

def DrawLoop():
	screen.fill(darkGray)

	DrawGui()

	pg.display.update()

inputEnabled = True
text = ""
def HandleEvents(event):
	global equation, inputEnabled, text
	HandleGUI(event)

	for button in allButtons:
		if button.active:
			if button.name == "clear":
				equation = ""
				text = equation
				inputEnabled = True

			if inputEnabled:
				if button.name == "0":
					equation += "0"
				if button.name == "1":
					equation += "1"
				if button.name == "2":
					equation += "2"
				if button.name == "3":
					equation += "3"
				if button.name == "4":
					equation += "4"
				if button.name == "5":
					equation += "5"
				if button.name == "6":
					equation += "6"
				if button.name == "7":
					equation += "7"
				if button.name == "8":
					equation += "8"
				if button.name == "9":
					equation += "9"
				text = equation

				if len(equation) > 1:
					if equation[-1] not in "+-/*":
						if button.name == "+":
							equation += " + "
						if button.name == "-":
							equation += " - "
						if button.name == "/":
							equation += " / "
						if button.name == "*":
							equation += " * "
						text = equation

					if equation[-1] in "023456789":
						if button.name == "=":
							text = GetCalc(equation)
							inputEnabled = False
						else:
							text = equation

			button.active = False

	for label in allLabels:
		if label.name == "output":
			label.UpdateText(text, ("arial", 12, (255, 255, 255)))


while running:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			Quit()

		if event.type == pg.KEYDOWN:
			if event.key == pg.K_ESCAPE:
				Quit()

		HandleEvents(event)

	DrawLoop()
