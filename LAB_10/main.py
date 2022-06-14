from tkinter import *

root = Tk()
root.title("LAB10")
root.geometry("600x600")


def read():
    file = open("~/Desktop/somedir/Marvel.txt", "r")
    read_file = file.read()
    myTextBox.delete(1.0, END)
    myTextBox.insert(END, read_file)
    file.close()


def calculate():
    myTextBox.delete(1.0, END)
    file = open("~/Desktop/somedir/Marvel.txt", "r")
    x = file.read().split()
    frequents_list = []
    for i in x:
        if i not in frequents_list:
            frequents_list.append(i)

    for i in range(0, len(frequents_list)):
        text = 'Frequency of {} is : {}\n'.format(frequents_list[i], x.count(frequents_list[i]))
        myTextBox.insert(END, text)


myTextBox = Text(root, width=70, height=25)
myTextBox.pack()

readButton = Button(master=root, text="READ", width=40, command=read)
readButton.pack()
calculateButton = Button(master=root, text='CALCULATE', width=40, command=calculate)
calculateButton.pack()

root.mainloop()
