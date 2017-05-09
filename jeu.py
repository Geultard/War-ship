from tkinter import*
from random import*
from math import*
global k
k=0
player=0

def val(): #Taille de la grille
  global k
  k=int(entry.get())
  if 7<k<9 :
    draw()
    draw2()
    adversaire()    
  else :
    entry.slaves()
                                                
def draw(): #Grille1 
    for i in range(k):
        canvas.create_text(100+i*50,100,text=chr(i+65))
        canvas.create_text(50,150+i*50,text=str(i+1))
    for i in range (k+1):
        canvas.create_line(75+i*50,75,75+i*50,75+(k+1)*50)
        canvas.create_line(25,75+(i+1)*50,75+k*50,125+i*50)
    canvas.bind("<Button-1>",click)
    canvas.bind("<Motion>",prev)
    entry.destroy()
    bou1.destroy()

def draw2(): #Grille2
  for i in range (k):
    canvas.create_text(600+i*50,100,text=chr(i+65))
    canvas.create_text(550,150+i*50,text=str(i+1))
  for i in range (k+1):
    canvas.create_line(575+i*50,75,575+i*50,75+(k+1)*50)
    canvas.create_line(525,75+(i+1)*50,575+k*50,125+i*50)

                                                
def tourne(event): #fonction permettant de tourner les bateaux
    global turn
    turn=not turn
    if turn:
        tex1["text"]="Horizontal"
        tex1["fg"]="purple"
    else:
        tex1["text"]="Vertical"
        tex1["fg"]="blue"
       
    
def adversaire():#Bateau adverse
  canvas.create_rectangle (825,125,875,175,)
  canvas.create_rectangle (675,175,725,275,)
  canvas.create_rectangle (825,225,975,275,)
  canvas.create_rectangle (575,325,625,525,)
  canvas.create_rectangle (725,425,975,475,)

i=0
turn= False
def click(event): # Fonction permettant de poser les bateaux
    global X
    global Y
    X = event.x
    Y = event.y
    global i
    if 75 <= X <= 75 + 50*(k) and 125 <= Y <= 125+50*(k):
      X = floor((X+25)/50)*50
      Y = floor((Y+25)/50)*50
      if turn:
        canvas.create_rectangle(X-25, Y-25, X+25+50*i, Y+25, fill="grey")
      else:
        canvas.create_rectangle(X-25,Y-25,X+25,Y+25+50*i, fill= "grey")
      if i<5:
        if i==0:# enregistrements des bateaux alliés dans une liste
          chip.append([X,Y])
        if i==1:
          if turn:
            chip.append([X,Y])
            chip.append([X+50,Y])
          else:
            chip.append([X,Y+50])
            chip.append([X,Y])
        if i==2:
          if turn:
            chip.append([X,Y])
            chip.append([X+50,Y])
            chip.append([X+100,Y])
          else:
            chip.append([X,Y])
            chip.append([X,Y+50])
            chip.append([X,Y+100])
        if i==3 :
          if turn:
            chip.append([X,Y])
            chip.append([X+50,Y])
            chip.append([X+100,Y])
            chip.append([X+150,Y])
          else :
            chip.append([X,Y])
            chip.append([X,Y+50])
            chip.append([X,Y+100])
            chip.append([X,Y+150])
        if i==4:
          if turn:
            chip.append([X,Y])
            chip.append([X+50,Y])
            chip.append([X+100,Y])
            chip.append([X+150,Y])
            chip.append([X+200,Y])
          else :
            chip.append([X,Y])
            chip.append([X,Y+50])
            chip.append([X,Y+100])
            chip.append([X,Y+150])
            chip.append([X,Y+200])
            
          
        i+=1  
      if i >= 5: # PrÃ©visualisation des bateaux
        canvas.unbind("<Button-1>")
        canvas.coords(Prevc, 0,0,0,0)
        canvas.unbind("<Motion>")
        canvas.bind("<Button-1>",click2)
        canvas.bind("<Button-2>",tir)
  
o=0
def click2(event):# Fonction permettant de tirer
  
  X=event.x
  Y=event.y
  global o
  if 575 <= X <= 575 + 50*(k) and 125 <= Y <= 125+50*(k):
    X = floor((X+25)/50)*50-25
    Y = floor((Y+25)/50)*50-25
    for s in ship:
      if s[0]==X and s[1]==Y:
        canvas.create_rectangle(X,Y,X+50,Y+50,fill='black')
        o=o+1
        if o==15 :
          tex1["text"]="VICTOIRE"
          tex1["fg"]="red"
          tex1["font"]="42"
          canvas.unbind("<Button-1>")

        break
      else :
        canvas.create_rectangle(X,Y,X+50,Y+50,fill='lightblue')
  
    tir()

    



def prev(event): # fonction centrer dans les cases 
    X = event.x
    Y = event.y
    global Prevc
    global i
    if 75 <= X <= 75 + 50*(k) and 125 <= Y <= 125+50*(k):
      X = floor((X+25)/50)*50
      Y = floor((Y+25)/50)*50
      if turn:
        canvas.coords(Prevc, X-25, Y-25, X+25+50*i, Y+25)
      else:
        canvas.coords(Prevc, X-25,Y-25,X+25,Y+25+50*i)

def tir():#tir adverse
  
  x = (randint(1,8) * 50) + 25
  y = (randint(1,8) * 50) + 75
   
  for c in chip:
    if c[0]==x+25 and c[1]==y+25:
      canvas.create_rectangle(x,y,x+50,y+50,fill='red')
      break
    else :
      canvas.create_rectangle(x,y,x+50,y+50,fill='lightblue')
  
  
     


  
ship=[] # Bateau adverse
ship.append([825,125])
ship.append([675,175])
ship.append([675,225])
ship.append([825,225])
ship.append([875,225])
ship.append([925,225])
ship.append([575,325])
ship.append([575,375])
ship.append([575,425])
ship.append([575,475])
ship.append([725,425])
ship.append([775,425])
ship.append([825,425])
ship.append([875,425])
ship.append([925,425])

chip=[] # Bateau allié



# Mise en page de la fenetre
fen1=Tk()
fen1.title("Bataille Navale")
tex1=Label(fen1,text="Quelle est la taille de votre grille ?", fg="red")
bou1=Button(fen1, text='Valider', command=val)
tex1.pack()
entry=Entry(fen1)
entry.pack()
bou1.pack()
canvas=Canvas (fen1, width = 1000, height=1000, bg="white")
fen1.bind("<space>",tourne)
Prevc = canvas.create_rectangle(0, 0, 0, 0, outline="red", width=5)


canvas.pack()
fen1.mainloop()
