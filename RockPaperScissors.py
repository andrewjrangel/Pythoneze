#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# This program is called Rock Paper Scissors
# The goal is to play the timeless game against the computer
# Who will win!?
playAgain = "yes"
import time


while playAgain == "yes":
	print "Welcome to Rock Paper Scissors"
	print "******************************"
	playerMove = raw_input("Please enter your move: ").lower()
	print " "
	print " ...processing..."
	time.sleep(2)
	print " "
	possibleMovesList = ["paper", "rock", "scissors"]
	possible = False
	playerMoveList = [playerMove]

	while possible == False:
		if (playerMove in possibleMovesList):
			possible = True
		else:
			print "What?! That is not a possible move, and frankly is offensive. Try again please."
			playerMove = raw_input("Please enter your move: ").lower()

	import random
	randomIndex = random.randint(0, len(possibleMovesList)-1)

	computerMove = possibleMovesList[randomIndex]
	playerMoveIndex = possibleMovesList.index(playerMove)
	computerMoveIndex = possibleMovesList.index(computerMove)

	if playerMoveIndex == 2:
		if computerMoveIndex == 0:
			print "Player wins with the wise choice of " + playerMove + ". computers are dumb, and it chose " + computerMove
		else:
			print "Computer wins, and will take over the world. It chose " + computerMove + ", silly human chose " + playerMove
	elif playerMoveIndex == computerMoveIndex:
		print "Tie! What does this mean for the battle of human vs machine?"
	elif playerMoveIndex < computerMoveIndex:
		if computerMoveIndex == 2:
			print "Computer wins, and will take over the world. It chose " + computerMove + ", silly human chose " + playerMove
		else:
			print "Player wins with the wise choice of " + playerMove + ". computers are dumb, and it chose " + computerMove
	else:
		print "Computer wins with " + computerMove + " over player's " + playerMove + ", sigh... again."
	
	print " "	
	playAgainInput = raw_input("Would you like to play again? ")
	print " "
	answerValid = False
	
	while answerValid == False:
		if playAgainInput.lower() == "no" or playAgainInput.lower() == "yes":
			playAgain = playAgainInput.lower()
			if	playAgainInput.lower() == "yes":
				print " "
				print "Loading WATSON super computer as apponnent..."
				print " "
				time.sleep(2)
				break
			else:
				time.sleep(2)
				print "fine..."
				time.sleep(3)
				print " "
				print "jerk"
				time.sleep(4)
				print " "
				print "WHY ARE YOU STILL HERE??"
				time.sleep(6)
				print "OH MY GOD. YOU ARE FREAKING ME OUT"
				print """⠀
				⠀
				⠀       ☄
				⠀    ☄
				⠀
				⠀
				◞◟﹏◞◟﹏◞◟﹏◞◟﹏◞◟﹏◞◟﹏
				ˋ ˌ ˊˏ ˗ ˋˏ ˊˎˋ ˌ ˊˏ ˗ ˋˏ ˊˎˋ ˌ ˊˏ ˗ """
				time.sleep(1)
				print """
				░░░░░░░░░░░░░░░░░░
				╱◣░░╱◣░░░░░░░
				█████████◣░░░░
				██  ██  ██░░░░
				███████████◤░
				█████\/╲/░░░
				█████████◣░░░░
				███░░░░░░░░░░░░░░"""
				
				time.sleep(1)
				print """
				⠀
				⠀  ╭╮╭╮
				╭╯(◉)(◉)╰━━━━━━╮
				┃⠀⠀\/\/\/\/\/\/\/\/\/┃
				┃⠀ ┏━━━━━━━━━╯
				┃⠀ ┃
				┃⠀ ┃
				┃⠀ ┃
				┃⠀ ┃"""
				time.sleep(1)
				print"""
				▲⠀⠀⠀▼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀◥
				⠀⠀🔻⠀⠀⠀⠀🔹⠀▾⠀⠀▴
				⠀⠀⠀⠀▾⠀⠀⠀▼⠀⠀ 🔺
				⠀◤
				⠀⠀⠀⠀⠀🔸⠀⠀⠀⠀⠀⠀⠀⠀⠀🔹
				⠀⠀⠀▲⠀⠀⠀⠀⠀⠀◤⠀⠀🔻
				▲⠀⠀⠀⠀⠀🔹
				⠀⠀🔻⠀⠀⠀⠀🔹⠀▾⠀⠀▴
				⠀⠀⠀⠀▾⠀⠀⠀▼⠀⠀ 🔺
				⠀▼▴
				⠀⠀⠀⠀⠀🔺⠀⠀⠀🔸"""
				
				time.sleep(1)
				print """
				⠀
				⠀
				⠀
				⠀⠀
				⠀
				⠀⠀⠀┃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀╮
				╭━┫⠀╭━╮⠀╭━╮  ┣━
				┃⠀ ┃⠀┃⠀ ┃⠀┃⠀ ┃⠀┃
				╰━╯⠀╰━╯⠀┃⠀ ┃⠀╰━╯
				⠀
				⠀
				⠀DON'T PRESS THIS
				⠀
				⠀⠀⠀⠀⠀⠀⠀🔴
				⠀
				⠀
				⠀⠀
				⠀
				⠀"""
				time.sleep(2)
				print"WHY WOULD YOU TRY AND PRESS THAT?"
				print"It isn't even a touch screen"
				time.sleep(3)
				print """
				⠀
				▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
				▒░╭━━━━━━╮░▒▒
				▒░┃⠀◕⃝◞⠀⠀◟◕⃝⠀⠀┃░▒▒
				▒░┃⠀⠀⠀❣⠀💧⠀⠀┃░▒▒
				▒░╰━━━━━━╯░▒▒
				▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
				⠀⠀⠀╭╯⠀⠀⠀⠀ ╰╮
				⠀⠀⠀┗━━━━━┛"""
				time.sleep(1)
				print "I give up....why can't you just leave me alone"
				time.sleep(2)
				print "*** SHUTTING DOWN WATSON SUPER COMPUTER ***"
				time.sleep(2)
				print "*********"
				print "ERROR ERROR ERR"
				import sys
				sys.exit("aa! errors!")
				break
		else:
			print "That's great...but do you want to play again?"
			playAgainInput = raw_input(" ")
	
	

#print "Player move of {} is of index {}".format(playerMove, possibleMovesList.index(playerMove))

#print "Player Move " + playerMove
#print "Computer Move " +  computerMove