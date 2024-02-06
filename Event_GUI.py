from tkinter import *

def himansh(event):
    print(f"you can do at{event.x},{event.y}")

root=Tk()
root.title("Sobhasaria Events")
root.geometry("600x500")
'''
ye program hume btata h ki user isko kis jgh pr lejakr click ya is pr work kr rha h
ye me ek trh  iski location btata h dimentions ki form me
for enample agr hum ise top left me rkkr click kr windows ko jo humne create ki h to ye hume uski  dimentions 
dega x,y ki form me like  top left ki dimentions h as pr my pc is 67,18
or isse thoda niche sehu64,19   
<ButtonPress event state=Mod1 num=1 x=67 y=15>
ye line double press krne pr deta h ye uske puri location hoti h

'''
H = Button(root, text= "please click on me")
H.pack()

#tkinter k events aapko all events of tkinter pr mil jayengeor vo ky krte h unka bhi bta chl jayega
H.bind("<Button-1>",himansh)
H.bind("<Double-1>",quit)#isse agr hum double click krenge to exit ho jayega


root.mainloop()