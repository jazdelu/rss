import os

for root, dirs, files in os.walk(r'e:/code/rss'):
	for file in files:
		if file.endswith('.ui'):
			os.system('pyuic4 -o %s.py ui/%s' % (file.rsplit('.',1)[0].capitalize(),file))