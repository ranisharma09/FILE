import platform,os
os.system("termux-setup-storage")
os.system("git pull")
arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("FILE6").login()
elif 'aarch' in arc:
	__import__("FIL6").login()
