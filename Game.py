from tkinter import *
import tkinter as tk
from tkinter import messagebox
import random
from pip._vendor.distlib.compat import raw_input

'''length = int(raw_input("How long do you want your frame"))
width = int(raw_input("How wide do you want your frame"))'''

length, width = 5, 5
charCount, buttons = [], []
start = False
textColors = ['red', 'blue', 'green']

for i in range(length):
    new = []
    for j in range(width):
        new.append("")
    charCount.append(new)

# print(charCount)

window = Tk()
window.title("MineSweeper")


def checker(btn, row, col):
    global start
    # print(str(row) + " " + str(col))
    if (btn["text"] == "" and not start):
        fillFrame(row, col)
        breakGround(row, col)
        start = True
        # showAllZeros()
    elif (start and isInt(charCount[row][col])):
        buttons[row][col]["text"] = charCount[row][col]
    elif (charCount[row][col] == "B"):
        endGame()
    disableButton(row, col, darken=False)


def endGame():
    for r in range(length):
        for c in range(width):
            if (charCount[r][c] == "B"):
                buttons[r][c].configure(bg="red")
    tk.messagebox.showinfo("Loss", "You just LOST")


def disableButton(row, col, darken=True):
    buttons[row][col].configure(state='disabled')
    if (darken):
        buttons[row][col].configure(bg="darkgray")


def createFrame():
    count = 1
    for i in range(length):
        new = []
        for j in range(width):
            print(str(i) + " " + str(j))
            newButton = Button(window, text="", font="Times 26 bold", height=2, width=4,
                               command=lambda i=i, j=j: checker(new[j], i, j))
            new.append(newButton)
            new[j].grid(column=j, row=i)
            count += 1
        buttons.append(new)
    print(buttons)


def optionmenu(count):
    print(count)


def fillFrame(row, col):
    '''
    assign mines, numbers and empties
    '''

    for g in range(int((length + width) / 2)):
        charCount[random.randint(0, length - 1)][random.randint(0, width - 1)] = "B"
        # print(charCount)

    for r in range(length):
        for c in range(width):
            count = 0
            if (charCount[r][c] != "B"):
                if (r > 0 and r < length - 1) and (c > 0 and c < width - 1):
                    count = aroundBox(r - 1, r + 2, c - 1, c + 2, r, c)

                elif r == 0 and c == 0:
                    count = aroundBox(r, r + 2, c, c + 2, r, c)
                elif r == 0 and (c > 0 and c < width - 1):
                    count = aroundBox(r, r + 2, c - 1, c + 2, r, c)
                elif r == 0 and c == width - 1:
                    count = aroundBox(r, r + 2, c - 1, c + 1, r, c)

                elif r == length - 1 and c == 0:
                    count = aroundBox(r - 1, r + 1, c, c + 2, r, c)
                elif r == length - 1 and c == width - 1:
                    count = aroundBox(r - 1, r + 1, c - 1, c + 1, r, c)
                elif r == length - 1 and (c > 0 and c < width - 1):
                    count = aroundBox(r-1, r + 1, c - 1, c + 2, r, c)

                elif c == 0 and (r > 0 and r < length - 1):
                    count = aroundBox(r - 1, r + 2, c, c + 2, r, c)
                elif c == width - 1 and (r > 0 and r < length - 1):
                    count = aroundBox(r - 1, r + 2, c - 1, c + 1, r, c)

                charCount[r][c] = count
    charCount[row][col] = "S"
    print(charCount)


def isInt(s):
    try:
        int(s)
        return True
    except ValueError or RecursionError:
        return False


def breakGround(row, col):
    while (row >= 0):
        while (col >= 0):
            stop = checkBox(row, col)
            if (charCount[row][col] == "B"):
                pass
            elif (stop):
                disableButton(row, col)
                break
            col -= 1
        while (col < width):
            stop = checkBox(row, col)
            if (charCount[row][col] == "B"):
                pass
            elif (stop):
                disableButton(row, col)
                break
            col += 1
        row -= 1
    while (row < length):
        while (col >= 0):
            stop = checkBox(row, col)
            if (charCount[row][col] == "B"):
                pass
            elif (stop):
                disableButton(row, col)
                break
            col -= 1
        while (col < width):
            stop = checkBox(row, col)
            if (charCount[row][col] == "B"):
                pass
            elif (stop):
                disableButton(row, col)
                break
            col += 1
        row += 1

    '''try:
        if (row < 0 or row >= length or col < 0 or col >= width):
            return
        if (charCount[row][col] == "B"):
            return
        if (isInt(charCount[row][col]) and charCount[row][col] != '0'):
            buttons[row][col]["text"] = charCount[row][col]
            return
    except IndexError:
        return

    rowBig = row + 1
    colBig = col + 1

    rowSmall = row - 1
    colSmall = col - 1

    breakGround(rowBig, col)
    breakGround(row, colBig)

    breakGround(rowSmall, col)
    breakGround(row, colSmall)

    breakGround(rowBig, colBig)
    breakGround(rowSmall, colSmall)'''


def checkBox(row, col):
    if (charCount[row][col] == "S"):
        return True
    elif (isInt(charCount[row][col]) and charCount[row][col] != '0'):
        buttons[row][col]["text"] = charCount[row][col]
        return True
    elif (charCount[row][col] == 0):
        return True
    else:
        return False


'''def showAllZeros():
    for r in range(length):
        for c in range(width):
            if(charCount[r][c] == "0"):
                print(charCount[r][c])
                disableButton(r, c)'''


def aroundBox(rowStart, rowEnd, colStart, colEnd, r, c):
    count = 0
    for j in range(rowStart, rowEnd):
        for k in range(colStart, colEnd):
            # print(str(j) + " " + str(k))
            if charCount[j][k] == charCount[r][c]:
                pass
            elif charCount[j][k] == "B":
                count += 1
    return count


createFrame()

window.mainloop()
