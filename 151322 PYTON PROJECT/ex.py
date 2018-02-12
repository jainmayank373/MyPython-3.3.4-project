from Tkinter import*
from PIL import Image,ImageTk
root=Tk()
display=ImageTk.PhotoImage(file='312704.png')
label = Label(root, image=display)
label.pack()
root.mainloop()
