from tkinter import *
from sympy import Matrix
from math import floor

root = Tk()
root.title('Periodic Points')
#root.geometry("800x1080")
root.state('zoomed') #maximize the window


w = 1250
h = 500
x = w//2
y = h//2

my_canvas = Canvas(root,width=w,height=h,bg="white")
my_canvas.pack(pady=20)


#A=Matrix([[2,1],\
#          [1,1]])
#B=A-Matrix.eye(2)

B=Matrix([[1,1],[1,0]])
B_inv=B.inv()


(x1,y1)=(250,250)
(x2,y2)=(950,250)
unit=50
N=4.5 #how far we go away from origin, both vertically and horizontally


#draw x-axis in plane 1
my_canvas.create_line(x1-N*unit,y1, x1+N*unit,y1, arrow=LAST,width=1.5)

#draw y-axis in plane 1
my_canvas.create_line(x1,y1+N*unit, x1,y1-N*unit, arrow=LAST,width=1.5)

#draw vertical coordinate grid lines in plane 1
for i in range(-floor(N),floor(N)+1):
    my_canvas.create_line(x1+i*unit,y1+N*unit, x1+i*unit,y1-N*unit,fill="gray")

#draw horizontal coordinate grid lines in plane 1
for j in range(-floor(N),floor(N)+1):
    my_canvas.create_line(x1-N*unit,y1-j*unit, x1+N*unit,y1-j*unit,fill="gray")

#draw x-axis in plane 2
my_canvas.create_line(x2-N*unit,y2, x2+N*unit,y2, arrow=LAST,width=1.5)

#draw y-axis in plane 2
my_canvas.create_line(x2,y2+N*unit, x2,y2-N*unit, arrow=LAST,width=1.5)

#draw vertical coordinate grid lines in plane 2
for i in range(-floor(N),floor(N)+1):
    my_canvas.create_line(x2+i*unit,y2+N*unit, x2+i*unit,y2-N*unit,fill="gray")

#draw horizontal coordinate grid lines in plane 2
for j in range(-floor(N),floor(N)+1):
    my_canvas.create_line(x2-N*unit,y2-j*unit, x2+N*unit,y2-j*unit,fill="gray")

#draw e_x in plane 1
my_canvas.create_line(x1,y1, x1+unit,y1, arrow=LAST,arrowshape=(8,10,6),\
                      fill="red",width=3)
#draw e_y in plane 1
my_canvas.create_line(x1,y1, x1,y1-unit, arrow=LAST,arrowshape=(8,10,6),\
                      fill="blue",width=3)

#draw Be_x in plane 2
my_canvas.create_line(x2,y2, x2+unit*B[0,0],y2-unit*B[1,0], arrow=LAST,arrowshape=(8,10,6),\
                      fill="red",width=3)

#draw Be_y in plane 2
my_canvas.create_line(x2,y2, x2+unit*B[0,1],y2-unit*B[1,1], arrow=LAST,arrowshape=(8,10,6),\
                      fill="blue",width=3)

#create the point v
img1=PhotoImage(file="v_trans.png")
my_image=my_canvas.create_image(x1,y1,image=img1)

#create the point Bv
img2=PhotoImage(file="Bv_trans.png")
my_image2=my_canvas.create_image(x2,y2,image=img2)

def get_v_coord():
    pass

def move_v(e):
    #e.x
    #e.y

    #my_circle = my_canvas.create_oval(e.x,e.y,e.x+10,e.y+10,fill="red")

    global img1
    img1=PhotoImage(file="v_trans.png")
    my_image=my_canvas.create_image(e.x,e.y,image=img1)

    global img2
    img2=PhotoImage(file="Bv_trans.png")
    my_image2=my_canvas.create_image(x2+B[0,0]*(e.x-x1)+B[0,1]*(-e.y+y1),\
                                     y2-B[1,0]*(e.x-x1)-B[1,1]*(-e.y+y1),image=img2)


    my_label.config(text="Coordinates: ("+str(e.x)+","+str(e.y)+")")

def move_Bv(e):
    #e.x
    #e.y

    #my_circle = my_canvas.create_oval(e.x,e.y,e.x+10,e.y+10,fill="red")

    global img2
    img2=PhotoImage(file="Bv_trans.png")
    my_image=my_canvas.create_image(e.x,e.y,image=img2)

    global img1
    img1=PhotoImage(file="v_trans.png")
    
    my_image2=my_canvas.create_image(int(x1+B_inv[0,0]*(e.x-x2)+B_inv[0,1]*(-e.y+y2)),\
                                     int(y1-B_inv[1,0]*(e.x-x2)-B_inv[1,1]*(-e.y+y2)),\
                                     image=img1)


    my_label.config(text="Coordinates: ("+str(e.x)+","+str(e.y)+")")

def move(e):
    if e.x>w//2:
        move_Bv(e)
    else:
        move_v(e)

def show_coord(e):
    my_label.config(text="Coordinates: ("+str(e.x)+","+str(e.y)+")")
    
    
my_label = Label(root,text="")
my_label.pack(pady=20)


my_canvas.bind("<B1-Motion>",move)
my_canvas.bind("<Motion>",show_coord)

root.mainloop()
