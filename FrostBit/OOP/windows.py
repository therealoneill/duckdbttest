def set_dpi_awareness():
#Adding in logic for high DPI widgets
	try:
		from ctypes import windll
		windll.shcore.SetProcessDpiAwareness(1)
	except:
		pass