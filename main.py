from tkinter import *
import tkinter.messagebox as msg

root = Tk()
root.title("Tic Tac Toe")

digits= list(range(1,10))
mark = ''""
count = 0
panels = ['panel']*10

def checker(digit):
	global count, mark, digits
	if digit==1 and digit in digits:
		digits.remove(digit)
		if count%2 == 0:
			mark = 'X'
			panels[digit]=mark
		elif count%2 != 0:
			mark = 'O'
			panels[digit]= mark
		button1.config(text=mark)
		count = count+1
		sign = mark
		if (win(panels, sign) and sign == 'X'):
			msg.showinfo("Result", "Player 1 Wins")
			root.destroy()
		elif (win(panels, sign) and sign=='O'):
			msg.showinfo("Result", "Player 2 Wins")
			root.destroy()
	if digit==2 and digit in digits:
		digits.remove(digit)
		if count%2 == 0:
			mark = 'X'
			panels[digit]=mark
		elif count%2 != 0:
			mark = 'O'
			panels[digit]= mark
		button2.config(text=mark)
		count = count+1
		sign = mark
		if (win(panels, sign) and sign == 'X'):
			msg.showinfo("Result", "Player 1 Wins")
			root.destroy()
		elif (win(panels, sign) and sign=='O'):
			msg.showinfo("Result", "Player 2 Wins")
			root.destroy()


	if digit==3 and digit in digits:
		digits.remove(digit)
		if count%2 == 0:
			mark = 'X'
			panels[digit]=mark
		elif count%2 != 0:
			mark = 'O'
			panels[digit]= mark
		button3.config(text=mark)
		count = count+1
		sign = mark
		if (win(panels, sign) and sign == 'X'):
			msg.showinfo("Result", "Player 1 Wins")
			root.destroy()
		elif (win(panels, sign) and sign=='O'):
			msg.showinfo("Result", "Player 2 Wins")
			root.destroy()
	if digit==4 and digit in digits:
		digits.remove(digit)
		if count%2 == 0:
			mark = 'X'
			panels[digit]=mark
		elif count%2 != 0:
			mark = 'O'
			panels[digit]= mark
		button4.config(text=mark)
		count = count+1
		sign = mark
		if (win(panels, sign) and sign == 'X'):
			msg.showinfo("Result", "Player 1 Wins")
			root.destroy()
		elif (win(panels, sign) and sign=='O'):
			msg.showinfo("Result", "Player 2 Wins")
			root.destroy()
	if digit==5 and digit in digits:
		digits.remove(digit)
		if count%2 == 0:
			mark = 'X'
			panels[digit]=mark
		elif count%2 != 0:
			mark = 'O'
			panels[digit]= mark
		button5.config(text=mark)
		count = count+1
		sign = mark
		if (win(panels, sign) and sign == 'X'):
			msg.showinfo("Result", "Player 1 Wins")
			root.destroy()
		elif (win(panels, sign) and sign=='O'):
			msg.showinfo("Result", "Player 2 Wins")
			root.destroy()
	if digit==7 and digit in digits:
		digits.remove(digit)
		if count%2 == 0:
			mark = 'X'
			panels[digit]=mark
		elif count%2 != 0:
			mark = 'O'
			panels[digit]= mark
		button7.config(text=mark)
		count = count+1
		sign = mark
		if (win(panels, sign) and sign == 'X'):
			msg.showinfo("Result", "Player 1 Wins")
			root.destroy()
		elif (win(panels, sign) and sign=='O'):
			msg.showinfo("Result", "Player 2 Wins")
			root.destroy()
	if digit==8 and digit in digits:
		digits.remove(digit)
		if count%2 == 0:
			mark = 'X'
			panels[digit]=mark
		elif count%2 != 0:
			mark = 'O'
			panels[digit]= mark
		button8.config(text=mark)
		count = count+1
		sign = mark
		if (win(panels, sign) and sign == 'X'):
			msg.showinfo("Result", "Player 1 Wins")
			root.destroy()
		elif (win(panels, sign) and sign=='O'):
			msg.showinfo("Result", "Player 2 Wins")
			root.destroy()
	if digit==9 and digit in digits:
		digits.remove(digit)
		if count%2 == 0:
			mark = 'X'
			panels[digit]=mark
		elif count%2 != 0:
			mark = 'O'
			panels[digit]= mark
		button9.config(text=mark)
		count = count+1
		sign = mark
		if (win(panels, sign) and sign == 'X'):
			msg.showinfo("Result", "Player 1 Wins")
			root.destroy()
		elif (win(panels, sign) and sign=='O'):
			msg.showinfo("Result", "Player 2 Wins")
			root.destroy()
	if digit==6 and digit in digits:
		digits.remove(digit)
		if count%2 == 0:
			mark = 'X'
			panels[digit]=mark
		elif count%2 != 0:
			mark = 'O'
			panels[digit]= mark
		button6.config(text=mark)
		count = count+1
		sign = mark
		if (win(panels, sign) and sign == 'X'):
			msg.showinfo("Result", "Player 1 Wins")
			root.destroy()
		elif (win(panels, sign) and sign=='O'):
			msg.showinfo("Result", "Player 2 Wins")
			root.destroy()
	if (count>8 and win(panels, 'X')==False and win(panels, 'O') == False):
		msg.showinfo("Result", "Match Tied")
		root.destroy()
	

def win(panels, sign):
	return ((panels[1]==panels[2]==panels[3]==sign)
		or (panels[4]==panels[5]==panels[6]==sign)
		or (panels[7]==panels[8]==panels[9]==sign)
		or (panels[1]==panels[5]==panels[9]==sign)
		or (panels[3]==panels[5]==panels[7]==sign)
		or (panels[1]==panels[4]==panels[7]==sign)
		or (panels[2]==panels[5]==panels[8]==sign)
		or (panels[3]==panels[6]==panels[9]==sign)
		)

Label(root, text="Player 1 : X", font="times 15").grid(row=0, column=1)
Label(root, text="Player 2 : 0", font="times 15").grid(row=0, column=2)
button1 = Button(master=root, width=15, font=("Times 16 bold"), height=7, command=lambda:checker(1))
button1.grid(row=1, column=1)

button2 = Button(master=root, width=15, font=("Times 16 bold"), height=7, command=lambda:checker(2))
button2.grid(row=1, column=2)

button3 = Button(master=root, width=15, font=("Times 16 bold"), height=7, command=lambda:checker(3))
button3.grid(row=1, column=3)

button4 = Button(master=root, width=15, font=("Times 16 bold"), height=7, command=lambda:checker(4))
button4.grid(row=2, column=1)

button5 = Button(master=root, width=15, font=("Times 16 bold"), height=7, command=lambda:checker(5))
button5.grid(row=2, column=2)

button6 = Button(master=root, width=15, font=("Times 16 bold"), height=7, command=lambda:checker(6))
button6.grid(row=2, column=3)

button7 = Button(master=root, width=15, font=("Times 16 bold"), height=7, command=lambda:checker(7))
button7.grid(row=3, column=1)

button8 = Button(master=root, width=15, font=("Times 16 bold"), height=7, command=lambda:checker(8))
button8.grid(row=3, column=2)

button9 = Button(master=root, width=15, font=("Times 16 bold"), height=7, command=lambda:checker(9))
button9.grid(row=3, column=3)

root.mainloop()
