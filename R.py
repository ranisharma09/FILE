#run file create raNii

import platform,os



os.system("git pull")
ass=platform.architecture()[0]

arc = str(platform.uname().machine)

if 'arm' in arc:

	__import__("FILE6").login()
