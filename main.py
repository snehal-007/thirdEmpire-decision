import tkinter
import cv2 
import PIL.Image, PIL.ImageTk
from functools import partial
import threading
import imutils
import time

stream = cv2.VideoCapture("clip.mp4")
flag = True
def play(speed):
    global flag
    print(f"Play{speed}")
    
    #play video reverse
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1+speed)

    grabbed, frame = stream.read()
    if not grabbed:
        exit()

    frame = imutils.resize(frame,width=set_width,height=set_height)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame,anchor=tkinter.NW)
    if flag:
        canvas.create_text(136,26,fill = "yellow",font="Times 25 bold",text="Decision Pending")
    flag = not flag    


      


def out():
    thread = threading.Thread(target=pending,args=("out",))
    thread.daemon=1
    thread.start()
    print("Player out")

def not_out():
    thread = threading.Thread(target=pending,args=("not_out",))
    thread.daemon=1
    thread.start()
    print("Player notout")

def pending(decision):
    # 1.Display decision pending image
    frame = cv2.cvtColor(cv2.imread("pending.jpg"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,height=set_height,width=set_width)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    # 2. wait for 1.5 sec
    time.sleep(1.5)

    # 3. Display sponser image
    frame = cv2.cvtColor(cv2.imread("stark.jpg"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,height=set_height,width=set_width)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)

    # 4. wait for 1.5 sec
    time.sleep(1.5)

    # 5. Display out/notout image
    if decision == 'out':

        frame = cv2.cvtColor(cv2.imread("out.jpg"),cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame,height=set_height,width=set_width)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
        

    else:

        frame = cv2.cvtColor(cv2.imread("notout.jpg"),cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame,height=set_height,width=set_width)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
  

set_width = 500
set_height = 300

root = tkinter.Tk()
root.title("Stark Third Empire")
cv_img = cv2.cvtColor(cv2.imread("welcome.jpg"),cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(root,width=set_width,height=set_height)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0,ancho=tkinter.NW,image=photo)
canvas.pack()


# Button to control Playback
btn = tkinter.Button(root,text="<< Previous (fast)",bg="yellow",width=50,command=partial(play,-25))
btn.pack()

btn = tkinter.Button(root,text="<< Previous (slow)",bg="yellow",width=50,command=partial(play,-2))
btn.pack()

btn = tkinter.Button(root,text="Next (slow) >>",bg="yellow",width=50,command=partial(play,2))
btn.pack()

btn = tkinter.Button(root,text="Next (fast) >>",bg="yellow",width=50,command=partial(play,25))
btn.pack()

btn = tkinter.Button(root,text="Give Out",bg="yellow",width=50,command=out)
btn.pack()

btn = tkinter.Button(root,text="Give Not Out",bg="yellow",width=50,command=not_out)
btn.pack()




root.mainloop()