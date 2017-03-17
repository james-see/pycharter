#!/usr/bin/bash
# Author: James Campbell
# Date: 17 March 2017
# What: Does simple charts in terminal 

#!/usr/bin/env python

from os import system
import curses
import redis

def get_param(prompt_string):
	screen.clear()
	screen.border(0)
	screen.addstr(2, 2, prompt_string)
	screen.refresh()
	input = screen.getstr(10, 10, 60)
	return input

def execute_cmd(cmd_string):
	system("clear")
	a = system(cmd_string)
	print ("")
	if a == 0:
		print ("Command executed correctly")
	else:
		print ("Command terminated with error")
	input("Press enter")
	print ("")

x = 0
while x != ord('4'):
	screen = curses.initscr()

	screen.clear()
	screen.border(0)
	screen.addstr(2, 2, "Please enter a number...")
	screen.addstr(4, 4, "1 - Connect to Redis & Generate a Chart")
	screen.addstr(7, 4, "4 - Exit")
	screen.refresh()

	x = screen.getch()

	if x == ord('1'):
		ipadd = get_param("redis ip address, eg 127.0.0.1").decode('utf8')
		port = get_param("Enter the redis port")
		charttype = get_param("chart type? (bar, or bar)")
		numberofcolumns = get_param("how many columns? (1-4)")
		print('Trying to connect {}:{} to grab data for ({}) column {} chart'.format(ipadd,port,numberofcolumns, charttype))
		r = get_param("press enter")
		re = redis.Redis(host=ipadd,port=port)
		if re.ping():
			r = get_param("Connected! Press enter to exit")
			x = ord('4')
			curses.endwin()
		#execute_cmd("useradd -d " + homedir + " -g 1000 -G " + groups + " -m -s " + shell + " " + username)
	if x == ord('2'):
		curses.endwin()
		execute_cmd("apachectl restart")
	if x == ord('3'):
		curses.endwin()
		execute_cmd("df -h")

curses.endwin()