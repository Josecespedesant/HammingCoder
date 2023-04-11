### Libraries ###

# imported libraries ------------------------------------------------------------------------------------------------------------------------------------------
from conversor import converter
from NRZI_v2 import draw_NRZI
from tkinter import *
from tkinter import messagebox
import sys # to increase the recursion limit
sys.setrecursionlimit(10**9)



### Main Window ###
    
MainWindow = Tk() # Create the Main window (menu) 
MainWindow.title("Project 1") 
MainWindow.minsize(991,425) # Size
MainWindow.resizable(width=NO,height=NO) # The window cannot be enlarged or made smaller 


binText = StringVar()
octText = StringVar()
decText = StringVar()
canvas = Canvas(MainWindow, width=320, height=150, bg='white')
canvas.place(x=42,y=189)

    
def CheckNum(num):
    nonAllowed = ["8","9","A","B","C","D","E","F"]
    Allowed = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    fails = []
    cont = 0
    if len(num)==3:
        if num[0] in Allowed:
            if num[0] not in nonAllowed:
                for c in num:
                    if c in Allowed:
                        print (c)
                        cont+=1
                        if cont == 3:
                            return SetNum(converter(num)[0],converter(num)[1],converter(num)[2])
                        # Convert
                        # return SetNum("10110101110","1234","78")
                    else:
                        messagebox.showerror("Numero no permitido", "Caracter \""+c+ "\" no pertenece \nal sistema hexadecimal.")
                        print ("Numero no permitido, el caracter \""+c+ "\" no pertenece al sistema hexadecimal.")
                        break
            else:
                messagebox.showerror("Numero no permitido", "El numero sobrepasa el rango \nestablecido (000 a 7FF).")
                print ("Numero no permitido, el numero sobrepasa el rango establecido.")
        else:
            messagebox.showerror("Numero no permitido", "Caracter \""+num[0]+ "\" no pertenece \nal sistema hexadecimal.")
            print ("Numero no permitido, el caracter \""+num[0]+ "\" no pertenece al sistema hexadecimal.")
    else:
        messagebox.showerror("Numero no permitido", "El numero debe ser exactamente de 3\ndigitos hexadecimales.")
        print ("Numero no permitido, el numero debe ser exactamente de 3 digitos hexadecimales.")
    
 
    

LabelFondo=Label(MainWindow) # 
LabelFondo.place (x=0, y=0) # 

NumLabel=Label(MainWindow,width=58,height=2,text="1. Ingrese un numero hexadecimal entre 000 y 7FF",font=("Consolas", 10),bg="black",fg="yellow")#texto
NumLabel.place(x=0,y=10)#
num=Entry(MainWindow,width=8,font=("Consolas", 12),bg="white",fg="black", justify=CENTER)
num.place(x=124,y=55) #
ConvertButton=Button(MainWindow,text="Convertir",font=("Consolas", 10),bg="#31416D",fg="#8DA9F3", activebackground="black",
                        activeforeground="yellow", relief=RAISED, command= lambda:CheckNum(num.get()))# boton de aceTime2ar7291E4
ConvertButton.place(x=204,y=54)

NumLabel2=Label(MainWindow,width=58,height=1,text="   Binario          Octal          Decimal   ",font=("Consolas", 10),bg="black",fg="yellow")#texto
NumLabel2.place(x=0,y=90)#
blackLabel=Label(MainWindow,width=58,height=2,bg="black")
blackLabel.place(x=0,y=110)#


binText = StringVar()

def selectParity():
    if parity.get() == 1:
        binText.set("Utilizar: Par")
    elif parity.get() == 2:
        binText.set("Utilizar: Impar")

BinLabel=Label(MainWindow,width=12,height=1,textvariable=binText, font=("Consolas", 10),bg="white",fg="black",justify=CENTER)#texto
BinLabel.place(x=46,y=118)#
OctLabel=Label(MainWindow,width=12,height=1,textvariable=octText,font=("Consolas", 10),bg="white",fg="black",justify=CENTER)#texto
OctLabel.place(x=160,y=118)#
DecLabel=Label(MainWindow,width=12,height=1,textvariable=decText,font=("Consolas", 10),bg="white",fg="black",justify=CENTER)#texto
DecLabel.place(x=274,y=118)#

nrziLabel=Label(MainWindow,width=58,height=1,text="2. Observe la codificación NRZI",font=("Consolas", 10),bg="black",fg="yellow")#texto
nrziLabel.place(x=0,y=148)#123

parityLabel=Label(MainWindow,width=58,height=1,text="3. Seleccione la paridad",font=("Consolas", 10),bg="black",fg="yellow")#texto
parityLabel.place(x=0,y=360)#123





parity = IntVar()
print(parity.get())
btn_text = StringVar()
btn_text.set("Utilizar:  -")
def selectParity():
    if parity.get() == 1:
        btn_text.set("Utilizar: Par")
    elif parity.get() == 2:
        btn_text.set("Utilizar: Impar")
evenRButton=Radiobutton(MainWindow,width = 8,text='Par', font=("Consolas", 10),bg="black",fg="yellow" ,activebackground="#31416D",
                        activeforeground="#8DA9F3",variable=parity, relief=RAISED, value=1, command = selectParity)
evenRButton.place(x=52,y=390)#148

oddRButton=Radiobutton(MainWindow,width = 8, text='Impar', font=("Consolas", 10),bg="black",fg="yellow",activebackground="#31416D",
                       activeforeground="#8DA9F3", variable=parity, relief=RAISED, value=2, command = selectParity)
oddRButton.place(x=137,y=390)#        


parityButton=Button(MainWindow,width =16 ,textvariable=btn_text,font=("Consolas", 10),bg="#31416D",fg="#8DA9F3", activebackground="black",
                        activeforeground="yellow", relief=RAISED, command=selectParity)# boton de aceTime2ar7291E4
parityButton.place(x=222,y=390)


divLabel=Label(MainWindow,width=2,height=100,font=("Consolas", 10),bg="black",fg="yellow")#texto
divLabel.place(x=410,y=10)#

table1Label=Label(MainWindow,width=80,height=2,text="4. Observe el calculo de los bits de paridad en el codigo Hamming.",font=("Consolas", 10),bg="black",fg="yellow")#texto
table1Label.place(x=425,y=10)#

# take the data
lst = ["","p1","p2","d1","p3","d2","d3","d4","p4","d5","d6","d7","d8","d9","d10","d11"]
lst2 = ["","Datos sin paridad","p1","p2","p3","p4","Datos con paridad"]
lstE = []
lstAUX = []
matrixE = []


    
# find total number of rows and
# columns in list
total_rows = 7
total_columns = 16


u  = 476
o = 53


  
for i in range(total_rows):
    for j in range(total_columns):
        if u==476:
            e = Entry(MainWindow, width=15, fg='black',font=('Console',10), justify= CENTER)
            e.place(x=u,y=o)
            e.insert(END, lst2[i])
            u+=107
            lstE.append(e)
            lstAUX.append(e)
            #print(e.get())

        else:
            e = Entry(MainWindow, width=3, fg='black',font=('Console',10), justify= CENTER) 
            e.place(x=u,y=o)
            if o==53:
                e.insert(END, lst[j])
            u+=24
            lstE.append(e)
            lstAUX.append(e)
            #print(e.get())
    matrixE.append(lstAUX)
    lstAUX=[]
    u = 476    
    o+=20




table2Label=Label(MainWindow,width=80,height=1,text="5. Cambie un bit de la hilera original para forzar un error.",font=("Consolas", 10),bg="black",fg="yellow")#texto
table2Label.place(x=425,y=200)#
# take the data
lst3 = ["","p1","p2","d1","p3","d2","d3","d4","p4","d5","d6","d7","d8","d9","d10","d11","Prueba","Bit paridad"]
lst4 = ["","Datos","p1","p2","p3","p4"]
lstE2 = []
lstAUX2 = []
matrixE2 = []

# find total number of rows and
# columns in list
total_rows2 = 6
total_columns2 = 18
u2  = 440
o2 = 230
for i in range(total_rows2):
    for j in range(total_columns2):
        if u2==440:
            e2 = Entry(MainWindow, width=5, fg='black',font=('Console',10), justify= CENTER)
            e2.place(x=u2,y=o2)
            e2.insert(END, lst4[i])
            u2+=37
            lstE2.append(e2)
            lstAUX2.append(e2)
        elif u2 ==(440+(24*15)+37) or u2 ==(440+(24*15)+37+67):
            
            e2 = Entry(MainWindow, width=10, fg='black',font=('Console',10), justify= CENTER)
            e2.place(x=u2,y=o2)
        
            #print(j)
            if o2==230:
                e2.insert(END, lst3[j])
            u2+=67
            lstE2.append(e2)
            lstAUX2.append(e2)
        else:
            e2 = Entry(MainWindow, width=3, fg='black',font=('Console',10), justify= CENTER) 
            e2.place(x=u2,y=o2)
            
            if o2==230:
                e2.insert(END, lst3[j])
            u2+=24
            lstE2.append(e2)
            lstAUX2.append(e2)
    matrixE2.append(lstAUX2)
    lstAUX2=[]
    u2 = 440    
    o2+=20



def getBin(binNum):
    cont = 0
    for e in range(len(lstE)):
        
        
        if e == 19:
            lstE[e].delete(0)
            lstE[e].insert(END,binNum[cont])
            cont+=1
        elif e>20 and e<24:
            lstE[e].delete(0)
            lstE[e].insert(END,binNum[cont])
            cont+=1
        elif e>24 and e<32:
            lstE[e].delete(0)
            lstE[e].insert(END,binNum[cont])
            cont+=1

def getBinP2(binNumP):
    print(len(matrixE))
    print(len(matrixE[0]))
    print(len(matrixE2))
    print(len(matrixE2[0]))
    print(len(lstE2))
    cont2=0
    for e2 in range(len(lstE2)):
        if e2>18 and e2<34:
            lstE2[e2].delete(0)
            lstE2[e2].insert(END,binNumP[cont2])
            cont2+=1

def insert(matrix, row, column, char):
    if matrix==1:
        matrixE[row][column].delete(0)
        matrixE[row][column].insert(END,char)
    else:
        matrixE2[row][column].delete(0)
        matrixE2[row][column].insert(END,char)
    print(1)

getBinP2("000010101010101")

insert(2, 5, 5, "17")
    
def SetNum(num2,num8,num10):
    binText.set(num2)
    octText.set(num8)
    decText.set(num10)
    getBin(num2)
    canvas2 = Canvas(MainWindow, width=320, height=150, bg='white')
    canvas2.place(x=42,y=189)
    return draw_NRZI(canvas2, num2)
#getBin("10101010101")

testLabel=Label(MainWindow,width=80,height=1,text="6. Realice la prueba y observe el número de bit en donde ocurre la falla.",font=("Consolas", 10),bg="black",fg="yellow")#texto
testLabel.place(x=425,y=360)#
testButton=Button(MainWindow,width =16 ,text= "Realizar prueba",font=("Consolas", 10),bg="#31416D",fg="#8DA9F3", activebackground="black",
                        activeforeground="yellow", relief=RAISED, command=selectParity)
testButton.place(x=649,y=390)

MainWindow.mainloop()  
