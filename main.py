import tkinter

# create a window 
window = tkinter.Tk()

window.title('My First GUI Program')
window.minsize(width=500, height=300)

#label
my_label = tkinter.Label(text='I am a Label', font=("Arial", 24, "bold"))
my_label.pack(side='left') #needed to have the label appear




# keep the window open; must be at end of code
window.mainloop()



