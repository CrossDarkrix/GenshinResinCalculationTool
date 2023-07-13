import base64, ui, locale, datetime, concurrent.futures, time
from datetime import datetime as dt
from scene import *
from math import pi, sin, cos
locale.normalize('ja_JP.UTF-8')
TimeText = ['']
v = ui.load_view_str(base64.b64decode('WwogIHsKICAgICJub2RlcyIgOiBbCiAgICAgIHsKICAgICAgICAibm9kZXMiIDogWwoKICAgICAgICBdLAogICAgICAgICJmcmFtZSIgOiAie3sxOSwgNTR9LCB7MjMzLCA1NH19IiwKICAgICAgICAiY2xhc3MiIDogIkRhdGVQaWNrZXIiLAogICAgICAgICJhdHRyaWJ1dGVzIiA6IHsKICAgICAgICAgICJjbGFzcyIgOiAiRGF0ZVBpY2tlciIsCiAgICAgICAgICAiZnJhbWUiIDogInt7OTAsIDI5Mn0sIHszMjAsIDIxNn19IiwKICAgICAgICAgICJmbGV4IiA6ICIiLAogICAgICAgICAgIm5hbWUiIDogIlN0YXJ0UmVzaW5UaW1lIiwKICAgICAgICAgICJtb2RlIiA6IDIsCiAgICAgICAgICAidXVpZCIgOiAiNUQwOTkxM0UtMUNCOS00MzkxLUFFMDItNDRBQTY3OEQwMDA4IgogICAgICAgIH0sCiAgICAgICAgInNlbGVjdGVkIiA6IGZhbHNlCiAgICAgIH0sCiAgICAgIHsKICAgICAgICAibm9kZXMiIDogWwoKICAgICAgICBdLAogICAgICAgICJmcmFtZSIgOiAie3szOCwgMzQ3fSwgezI2NywgOTB9fSIsCiAgICAgICAgImNsYXNzIiA6ICJMYWJlbCIsCiAgICAgICAgImF0dHJpYnV0ZXMiIDogewogICAgICAgICAgImZsZXgiIDogIiIsCiAgICAgICAgICAibmFtZSIgOiAiUmVzdWx0IiwKICAgICAgICAgICJ0ZXh0X2NvbG9yIiA6ICJSR0JBKDAuMDU2NzM4LDAuMDU2NzM4LDAuMDU2NzM4LDEuMDAwMDAwKSIsCiAgICAgICAgICAiZnJhbWUiIDogInt7NzUsIDEzNH0sIHsxNTAsIDMyfX0iLAogICAgICAgICAgInV1aWQiIDogIjc5MjFCRTRBLTVENDMtNDRBMy1BQ0RDLUZGNjNCNkJBMjM1RCIsCiAgICAgICAgICAiY2xhc3MiIDogIkxhYmVsIiwKICAgICAgICAgICJhbGlnbm1lbnQiIDogImxlZnQiLAogICAgICAgICAgInRleHQiIDogIiIsCiAgICAgICAgICAiZm9udF9zaXplIiA6IDE1LAogICAgICAgICAgImZvbnRfbmFtZSIgOiAiPFN5c3RlbS1Cb2xkPiIKICAgICAgICB9LAogICAgICAgICJzZWxlY3RlZCIgOiBmYWxzZQogICAgICB9LAogICAgICB7CiAgICAgICAgIm5vZGVzIiA6IFsKCiAgICAgICAgXSwKICAgICAgICAiZnJhbWUiIDogInt7MjgsIDE3Nn0sIHsyNTAsIDY4fX0iLAogICAgICAgICJjbGFzcyIgOiAiQnV0dG9uIiwKICAgICAgICAiYXR0cmlidXRlcyIgOiB7CiAgICAgICAgICAiZmxleCIgOiAiIiwKICAgICAgICAgICJib3JkZXJfd2lkdGgiIDogMSwKICAgICAgICAgICJhY3Rpb24iIDogIiIsCiAgICAgICAgICAiZnJhbWUiIDogInt7MTEwLCAxMzR9LCB7ODAsIDMyfX0iLAogICAgICAgICAgInRpdGxlIiA6ICLmnJ015pmC44G+44Gn44Gr44Gn44GN44KL5r+D57iu5qi56ISC44KS6KiI566XIiwKICAgICAgICAgICJ1dWlkIiA6ICI2MTZERTU1NS02QzJFLTQwMjEtOUI5Qy04MTVCRDdEM0MwQ0YiLAogICAgICAgICAgImNsYXNzIiA6ICJCdXR0b24iLAogICAgICAgICAgImNvcm5lcl9yYWRpdXMiIDogMSwKICAgICAgICAgICJib3JkZXJfY29sb3IiIDogIlJHQkEoMC4wMDAwMDAsMC4wMDAwMDAsMC4wMDAwMDAsMS4wMDAwMDApIiwKICAgICAgICAgICJuYW1lIiA6ICJDYWxjIiwKICAgICAgICAgICJmb250X3NpemUiIDogMTUKICAgICAgICB9LAogICAgICAgICJzZWxlY3RlZCIgOiBmYWxzZQogICAgICB9LAogICAgICB7CiAgICAgICAgIm5vZGVzIiA6IFsKCiAgICAgICAgXSwKICAgICAgICAiZnJhbWUiIDogInt7MTksIDQ0NX0sIHszMTEsIDQwfX0iLAogICAgICAgICJjbGFzcyIgOiAiTGFiZWwiLAogICAgICAgICJhdHRyaWJ1dGVzIiA6IHsKICAgICAgICAgICJ1dWlkIiA6ICJGRDM4RUY3Mi1EMkY2LTRDRDAtQjkwNi1GRDM5QTJCQjk5MDIiLAogICAgICAgICAgImZvbnRfc2l6ZSIgOiAxOCwKICAgICAgICAgICJiYWNrZ3JvdW5kX2NvbG9yIiA6ICJSR0JBKDEuMDAwMDAwLDEuMDAwMDAwLDEuMDAwMDAwLDEuMDAwMDAwKSIsCiAgICAgICAgICAiZnJhbWUiIDogInt7NzUsIDE3OH0sIHsxNTAsIDMyfX0iLAogICAgICAgICAgInRpbnRfY29sb3IiIDogIlJHQkEoMC4wNTQzNzQsMC4wNTQzNzQsMC4wNTQzNzQsMS4wMDAwMDApIiwKICAgICAgICAgICJhbGlnbm1lbnQiIDogImNlbnRlciIsCiAgICAgICAgICAidGV4dF9jb2xvciIgOiAiUkdCQSgwLjAwMDAwMCwwLjAwMDAwMCwwLjAwMDAwMCwxLjAwMDAwMCkiLAogICAgICAgICAgInRleHQiIDogIiIsCiAgICAgICAgICAiZm9udF9uYW1lIiA6ICI8U3lzdGVtLUJvbGQ+IiwKICAgICAgICAgICJjbGFzcyIgOiAiTGFiZWwiLAogICAgICAgICAgIm5hbWUiIDogIk5vd1RpbWUiLAogICAgICAgICAgImZsZXgiIDogIiIKICAgICAgICB9LAogICAgICAgICJzZWxlY3RlZCIgOiBmYWxzZQogICAgICB9LAogICAgICB7CiAgICAgICAgIm5vZGVzIiA6IFsKCiAgICAgICAgXSwKICAgICAgICAiZnJhbWUiIDogInt7MzgsIDI2MH0sIHsyNjcsIDg3fX0iLAogICAgICAgICJjbGFzcyIgOiAiVGV4dFZpZXciLAogICAgICAgICJhdHRyaWJ1dGVzIiA6IHsKICAgICAgICAgICJ1dWlkIiA6ICJBQ0E1NjExQy0wRTY1LTRBMUQtOEZDMS0yMzQ5NEM0NEQ5RjAiLAogICAgICAgICAgImZvbnRfc2l6ZSIgOiAxNywKICAgICAgICAgICJmcmFtZSIgOiAie3s1NCwgMTMyfSwgezIwMCwgMjAwfX0iLAogICAgICAgICAgImVkaXRhYmxlIiA6IGZhbHNlLAogICAgICAgICAgImFsaWdubWVudCIgOiAibGVmdCIsCiAgICAgICAgICAiYXV0b2NvcnJlY3Rpb25fdHlwZSIgOiAiZGVmYXVsdCIsCiAgICAgICAgICAidGV4dF9jb2xvciIgOiAiUkdCQSgwLjAwMDAwMCwwLjAwMDAwMCwwLjAwMDAwMCwxLjAwMDAwMCkiLAogICAgICAgICAgImZvbnRfbmFtZSIgOiAiPFN5c3RlbT4iLAogICAgICAgICAgInNwZWxsY2hlY2tpbmdfdHlwZSIgOiAiZGVmYXVsdCIsCiAgICAgICAgICAiY2xhc3MiIDogIlRleHRWaWV3IiwKICAgICAgICAgICJuYW1lIiA6ICJHZXRSZXNpblRpbWUiLAogICAgICAgICAgImZsZXgiIDogIiIKICAgICAgICB9LAogICAgICAgICJzZWxlY3RlZCIgOiBmYWxzZQogICAgICB9LAogICAgICB7CiAgICAgICAgIm5vZGVzIiA6IFsKCiAgICAgICAgXSwKICAgICAgICAiZnJhbWUiIDogInt7MTcxLCAxMTZ9LCB7OTMsIDMyfX0iLAogICAgICAgICJjbGFzcyIgOiAiVGV4dEZpZWxkIiwKICAgICAgICAiYXR0cmlidXRlcyIgOiB7CiAgICAgICAgICAidXVpZCIgOiAiNjQ1NkYyMTMtNzE4RS00OTVELTkyRTItODVBMDM3NDI1QkFGIiwKICAgICAgICAgICJjb3JuZXJfcmFkaXVzIiA6IDEsCiAgICAgICAgICAiZnJhbWUiIDogInt7NTYsIDI4Mn0sIHsyMDAsIDMyfX0iLAogICAgICAgICAgImJvcmRlcl9jb2xvciIgOiAiUkdCQSgwLjM2NTI0OCwwLjM2NTI0OCwwLjM2NTI0OCwxLjAwMDAwMCkiLAogICAgICAgICAgImJvcmRlcl93aWR0aCIgOiAxLAogICAgICAgICAgImFsaWdubWVudCIgOiAiY2VudGVyIiwKICAgICAgICAgICJhdXRvY29ycmVjdGlvbl90eXBlIiA6ICJkZWZhdWx0IiwKICAgICAgICAgICJ0ZXh0X2NvbG9yIiA6ICJSR0JBKDAuMTM4Mjk4LDAuMTM4Mjk4LDAuMTM4Mjk4LDEuMDAwMDAwKSIsCiAgICAgICAgICAicGxhY2Vob2xkZXIiIDogIjAiLAogICAgICAgICAgImZvbnRfbmFtZSIgOiAiPFN5c3RlbT4iLAogICAgICAgICAgInNwZWxsY2hlY2tpbmdfdHlwZSIgOiAiZGVmYXVsdCIsCiAgICAgICAgICAiY2xhc3MiIDogIlRleHRGaWVsZCIsCiAgICAgICAgICAibmFtZSIgOiAibm93UmVzaW4iLAogICAgICAgICAgImZvbnRfc2l6ZSIgOiAxNwogICAgICAgIH0sCiAgICAgICAgInNlbGVjdGVkIiA6IGZhbHNlCiAgICAgIH0sCiAgICAgIHsKICAgICAgICAibm9kZXMiIDogWwoKICAgICAgICBdLAogICAgICAgICJmcmFtZSIgOiAie3syOCwgMTE2fSwgezE0MywgMzJ9fSIsCiAgICAgICAgImNsYXNzIiA6ICJMYWJlbCIsCiAgICAgICAgImF0dHJpYnV0ZXMiIDogewogICAgICAgICAgImZvbnRfc2l6ZSIgOiAxOCwKICAgICAgICAgICJmcmFtZSIgOiAie3s4MSwgMjgyfSwgezE1MCwgMzJ9fSIsCiAgICAgICAgICAidXVpZCIgOiAiMkEwRTgwMTQtRDVGMS00ODZCLUE0QkQtMkY1RjJCMDYwRUMxIiwKICAgICAgICAgICJjbGFzcyIgOiAiTGFiZWwiLAogICAgICAgICAgImFsaWdubWVudCIgOiAibGVmdCIsCiAgICAgICAgICAidGV4dCIgOiAi5pei44Gr44GC44KL5qi56ISC5pWwOiIsCiAgICAgICAgICAibmFtZSIgOiAiIiwKICAgICAgICAgICJmb250X25hbWUiIDogIjxTeXN0ZW0+IgogICAgICAgIH0sCiAgICAgICAgInNlbGVjdGVkIiA6IGZhbHNlCiAgICAgIH0sCiAgICAgIHsKICAgICAgICAibm9kZXMiIDogWwoKICAgICAgICBdLAogICAgICAgICJmcmFtZSIgOiAie3s5NCwgNDkzfSwgezE3MCwgMTcwfX0iLAogICAgICAgICJjbGFzcyIgOiAiTGFiZWwiLAogICAgICAgICJhdHRyaWJ1dGVzIiA6IHsKICAgICAgICAgICJmb250X3NpemUiIDogMTgsCiAgICAgICAgICAiZnJhbWUiIDogInt7MTA2LCAyODB9LCB7MTUwLCAzMn19IiwKICAgICAgICAgICJ1dWlkIiA6ICIwRUQ0Njk1OC1BNTkyLTRGMjAtOTYwQy1FQkFGNDY1NTJDQTEiLAogICAgICAgICAgImNsYXNzIiA6ICJMYWJlbCIsCiAgICAgICAgICAiYWxpZ25tZW50IiA6ICJsZWZ0IiwKICAgICAgICAgICJ0ZXh0IiA6ICIiLAogICAgICAgICAgIm5hbWUiIDogIkNsb2NrIiwKICAgICAgICAgICJmb250X25hbWUiIDogIjxTeXN0ZW0+IgogICAgICAgIH0sCiAgICAgICAgInNlbGVjdGVkIiA6IHRydWUKICAgICAgfQogICAgXSwKICAgICJmcmFtZSIgOiAie3swLCAwfSwgezM3MiwgNjUwfX0iLAogICAgImNsYXNzIiA6ICJWaWV3IiwKICAgICJhdHRyaWJ1dGVzIiA6IHsKICAgICAgInRpbnRfY29sb3IiIDogIlJHQkEoMC4wMDAwMDAsMC40NzgwMDAsMS4wMDAwMDAsMS4wMDAwMDApIiwKICAgICAgImVuYWJsZWQiIDogdHJ1ZSwKICAgICAgImJvcmRlcl9jb2xvciIgOiAiUkdCQSgwLjAwMDAwMCwwLjAwMDAwMCwwLjAwMDAwMCwxLjAwMDAwMCkiLAogICAgICAiYmFja2dyb3VuZF9jb2xvciIgOiAiUkdCQSgxLjAwMDAwMCwxLjAwMDAwMCwxLjAwMDAwMCwxLjAwMDAwMCkiLAogICAgICAibmFtZSIgOiAiUmVzaW5DYWxjdWxhdGlvblRvb2wiLAogICAgICAiZmxleCIgOiAiIgogICAgfSwKICAgICJzZWxlY3RlZCIgOiBmYWxzZQogIH0KXQ=='))

class Clock (Scene):
	def setup(self):
		r = min(self.size)/2 * 0.9
		circle = ui.Path.oval(0, 0, r*2, r*2)
		circle.line_width = 6
		if 18 <= dt.now().hour and dt.now().hour:
			shadow = ('white', 0, 0, 10)
			self.face = ShapeNode(circle, 'black', 'white', shadow=shadow)
		elif datetime.now().hour <= 5:
			shadow = ('white', 0, 0, 10)
			self.face = ShapeNode(circle, 'black', 'white', shadow=shadow)
		else:
			shadow = ('black', 0, 0, 10)
			self.face = ShapeNode(circle, 'white', 'silver', shadow=shadow)
		self.add_child(self.face)
		for i in range(12):
			label = LabelNode(str(i+1), font=('HelveticaNeue-UltraLight', 0.2*r))
			if 18 <= dt.now().hour:
				label.color = 'white'
			elif dt.now().hour <= 5:
				label.color = 'white'
			else:
				label.color = 'black'
			a = 2 * pi * (i+1)/12.0
			label.position = sin(a)*(r*0.85), cos(a)*(r*0.85)
			self.face.add_child(label)
		self.hands = []
		if 18 <= dt.now().hour:
			hand_attrs = [(r*0.6, 8, 'white'), (r*0.9, 8, 'white'), (r*0.9, 4, 'red')]
		elif dt.now().hour <= 5:
			hand_attrs = [(r*0.6, 8, 'white'), (r*0.9, 8, 'white'), (r*0.9, 4, 'red')]
		else:
			hand_attrs = [(r*0.6, 8, 'black'), (r*0.9, 8, 'black'), (r*0.9, 4, 'red')]
		
		for l, w, color in hand_attrs:
			shape = ShapeNode(ui.Path.rounded_rect(0, 0, w, l, w/2), color)
			shape.anchor_point = (0.5, 0)
			self.hands.append(shape)
			self.face.add_child(shape)
		self.face.add_child(ShapeNode(ui.Path.oval(0, 0, 15, 15), 'red'))
		self.label2 = LabelNode('', font=('HelveticaNeue-UltraLight', 70))
		self.label2.position = -5, -250
		self.did_change_size()

	def did_change_size(self):
		self.face.position = self.size/2

	def update(self):
		if not 10 <= dt.now().hour:
			Hour = '0{}'.format(dt.now().hour)
		else:
			Hour = '{}'.format(dt.now().hour)
		if not 10 <= dt.now().minute:
			Min = '0{}'.format(dt.now().minute)
		else:
			Min = '{}'.format(dt.now().minute)
		if not 10 <= dt.now().second:
			Sec = '0{}'.format(dt.now().second)
		else:
			Sec = '{}'.format(dt.now().second)
		TimeText[0] = '{}:{}:{}'.format(Hour, Min, Sec)
		self.label2.text = TimeText[0]
		t = dt.now()
		tick = -2 * pi / 60.0
		seconds = t.second + t.microsecond/1000000.0
		minutes = t.minute + seconds/60.0
		hours = (t.hour % 12) + minutes/60.0
		self.hands[0].rotation = 5 * tick * hours
		self.hands[1].rotation = tick * minutes
		self.hands[2].rotation = tick * seconds
		self.face.add_child(self.label2)

def RealtimeClock():
	Cc = SceneView()
	Cc.scene = Clock()
	Cc.width = 170
	Cc.height = 170
	v['Clock'].add_subview(Cc)

ui.Label.add_subview
def RealtimeRefresh():
	r = [0]
	for _i in r:
		v['NowTime'].text = '現在時刻: {}'.format(dt.now().strftime('%Y/%m/%d %H:%M:%S'))
		time.sleep(0.98)
		r.append(_i+1)

def calcTime():
	v['nowResin'].end_editing()
	if v['nowResin'].text == '':
		nowResin = 0
		v['nowResin'].text = '0'
	else:
		nowResin = int(v['nowResin'].text)
	Time = [v['StartResinTime'].date]
	resin_time_count = []
	LoopTime = [0]
	for _i in LoopTime:
		if not Time[0].day == v['StartResinTime'].date.day:
			break
		elif 5 <= Time[0].hour and v['StartResinTime'].date.day == Time[0].day:
			if not nowResin == 0:
				Time[0] = (Time[0] + datetime.timedelta(minutes=int((40 - nowResin) * 8 - 1)))
				nowResin = 0
			else:
				Time[0] = (Time[0] + datetime.timedelta(minutes=5*60))
			resin_time_count.append('推定時刻: {}'.format(Time[0].strftime('%Y/%m/%d %H:%M:%S')))
		else:
			break
		LoopTime.append(_i+1)
	v['Result'].text = '今から数えて濃縮樹脂が作れる回数: {}'.format(len(resin_time_count))
	v['GetResinTime'].text = '\n'.join(resin_time_count)

def main(v):
	concurrent.futures.ThreadPoolExecutor().submit(calcTime)
concurrent.futures.ThreadPoolExecutor().submit(RealtimeRefresh)
concurrent.futures.ThreadPoolExecutor().submit(RealtimeClock).result()
v['Calc'].action = main
v.present('popover', orientations=['portrait'])
