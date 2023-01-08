import cv2, numpy as np
import winreg, os

class Theme():
	def __init__(self, webcam:int):
		self.webcam = cv2.VideoCapture(webcam)
		self.ConstantKey = winreg.CreateKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize")
		self.current, _ = winreg.QueryValueEx(self.ConstantKey, 'AppsUseLightTheme')
		
	def changeTheme(self, new):
		winreg.SetValueEx(self.ConstantKey,'AppsUseLightTheme',0,winreg.REG_DWORD, new)	

theme = Theme(0) #change webcam

if os.name == 'nt':

	while True:
		_, frames = theme.webcam.read()
		gray_frame = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

		is_light = round(np.average(gray_frame)) > 60 #change value of gray average

		if is_light != theme.current:
			theme.changeTheme(is_light)
			theme.current = is_light
		
		cv2.waitKey(2300)
