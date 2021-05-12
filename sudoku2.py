import sys

print("This is sudoku puzzle.\nThe empty boxes in the puzzle represents the places need to be filled the player\n\n")
a=input("Do you know how to Solve a sudoku?(Yes or No)\n")
if a.upper()=='YES':
    print("You have chosen 'Yes'.\nEnjoy solving the Sudoku puzzle below")
    print("IMPORTANT : THE PLAYER CAN ONLY AFFORD TO MAKE 3 MISTAKES. IF MORE THAN 3 MISTAKES ARE COMMITTED,THE PLAYER WILL BE DECLARED AS LOST\n\n")
    print("The sudoku is in the format - \n|square 1 |square 2 |square 3 |")
    print("-------------------------------")
    print("|square 4 |square 5 |square 6 |")
    print("-------------------------------")
    print("|square 7 |square 8 |square 9 |\n\n")
else:
    f=open("rules.txt",'r')
    r=f.read()
    f.close()
    print(r)



from tkinter import *
root=Tk()


#row 1
bt1=Button(root,text='9',padx=40,pady=20)
bt2=Button(root,text='8',padx=40,pady=20)
bt3=Button(root,text='4',padx=40,pady=20)
e4=Entry(root,width=14)
bt5=Button(root,text='3',padx=40,pady=20)
bt6=Button(root,text='1',padx=40,pady=20)
e7=Entry(root,width=14)
bt8=Button(root,text='7',padx=40,pady=20)
bt9=Button(root,text='2',padx=40,pady=20)

#row 2
bt10=Button(root,text='6',padx=40,pady=20)
bt11=Button(root,text='1',padx=40,pady=20)
e12=Entry(root,width=14)
e13=Entry(root,width=14)
e14=Entry(root,width=14)
bt15=Button(root,text='7',padx=40,pady=20)
e16=Entry(root,width=14)
e17=Entry(root,width=14)
e18=Entry(root,width=14)

#row 3
bt19=Button(root,text='2',padx=40,pady=20)
bt20=Button(root,text='5',padx=40,pady=20)
bt21=Button(root,text='7',padx=40,pady=20)
e22=Entry(root,width=14)
e23=Entry(root,width=14)
bt24=Button(root,text='9',padx=40,pady=20)
bt25=Button(root,text='8',padx=40,pady=20)
e26=Entry(root,width=14)
e27=Entry(root,width=14)

#row4
bt28=Button(root,text='3',padx=40,pady=20)
bt29=Button(root,text='7',padx=40,pady=20)
e30=Entry(root,width=14)
e31=Entry(root,width=14)
bt32=Button(root,text='6',padx=40,pady=20)
e33=Entry(root,width=14)
e34=Entry(root,width=14)
bt35=Button(root,text='1',padx=40,pady=20)
e36=Entry(root,width=14)

#row5
e37=Entry(root,width=14)
e38=Entry(root,width=14)
e39=Entry(root,width=14)
bt40=Button(root,text='3',padx=40,pady=20)
bt41=Button(root,text='7',padx=40,pady=20)
e42=Entry(root,width=14)
bt43=Button(root,text='9',padx=40,pady=20)
bt44=Button(root,text='2',padx=40,pady=20)
e45=Entry(root,width=14)

#row6
e46=Entry(root,width=14)
e47=Entry(root,width=14)
bt48=Button(root,text='9',padx=40,pady=20)
bt49=Button(root,text='1',padx=40,pady=20)
e50=Entry(root,width=14)
bt51=Button(root,text='5',padx=40,pady=20)
e52=Entry(root,width=14)
e53=Entry(root,width=14)
e54=Entry(root,width=14)

#row7
e55=Entry(root,width=14)
bt56=Button(root,text='3',padx=40,pady=20)
e57=Entry(root,width=14)
e58=Entry(root,width=14)
e59=Entry(root,width=14)
bt60=Button(root,text='6',padx=40,pady=20)
e61=Entry(root,width=14)
e62=Entry(root,width=14)
e63=Entry(root,width=14)

#row8
e64=Entry(root,width=14)
bt65=Button(root,text='4',padx=40,pady=20)
bt66=Button(root,text='5',padx=40,pady=20)
e67=Entry(root,width=14)
bt68=Button(root,text='1',padx=40,pady=20)
bt69=Button(root,text='8',padx=40,pady=20)
e70=Entry(root,width=14)
bt71=Button(root,text='9',padx=40,pady=20)
bt72=Button(root,text='6',padx=40,pady=20)

#row 9
bt73=Button(root,text='1',padx=40,pady=20)
bt74=Button(root,text='9',padx=40,pady=20)
bt75=Button(root,text='6',padx=40,pady=20)
bt76=Button(root,text='7',padx=40,pady=20)
e77=Entry(root,width=14)
e78=Entry(root,width=14)
bt79=Button(root,text='2',padx=40,pady=20)
bt80=Button(root,text='8',padx=40,pady=20)
e81=Entry(root,width=14)

#gridding of row 1
bt1.grid(row=0,column=0)
bt2.grid(row=0,column=1)
bt3.grid(row=0,column=2)
e4.grid(row=0,column=4,ipady=20)
bt5.grid(row=0,column=5)
bt6.grid(row=0,column=6)
e7.grid(row=0,column=8,ipady=20)
bt8.grid(row=0,column=9)
bt9.grid(row=0,column=10)

#Gridiing of row 2
bt10.grid(row=1,column=0)
bt11.grid(row=1,column=1)
e12.grid(row=1,column=2,ipady=20)
e13.grid(row=1,column=4,ipady=20)
e14.grid(row=1,column=5,ipady=20)
bt15.grid(row=1,column=6)
e16.grid(row=1,column=8,ipady=20)
e17.grid(row=1,column=9,ipady=20)
e18.grid(row=1,column=10,ipady=20)

#gridiing of row 3
bt19.grid(row=2,column=0)
bt20.grid(row=2,column=1)
bt21.grid(row=2,column=2)
e22.grid(row=2,column=4,ipady=20)
e23.grid(row=2,column=5,ipady=20)
bt24.grid(row=2,column=6)
bt25.grid(row=2,column=8)
e26.grid(row=2,column=9,ipady=20)
e27.grid(row=2,column=10,ipady=20)

#gridiing of row 4
bt28.grid(row=4,column=0)
bt29.grid(row=4,column=1)
e30.grid(row=4,column=2,ipady=20)
e31.grid(row=4,column=4,ipady=20)
bt32.grid(row=4,column=5)
e33.grid(row=4,column=6,ipady=20)
e34.grid(row=4,column=8,ipady=20)
bt35.grid(row=4,column=9)
e36.grid(row=4,column=10,ipady=20)

#gridding of row 5
e37.grid(row=5,column=0,ipady=20)
e38.grid(row=5,column=1,ipady=20)
e39.grid(row=5,column=2,ipady=20)
bt40.grid(row=5,column=4)
bt41.grid(row=5,column=5)
e42.grid(row=5,column=6,ipady=20)
bt43.grid(row=5,column=8)
bt44.grid(row=5,column=9)
e45.grid(row=5,column=10,ipady=20)

#gridiing of row 6
e46.grid(row=6,column=0,ipady=20)
e47.grid(row=6,column=1,ipady=20)
bt48.grid(row=6,column=2)
bt49.grid(row=6,column=4)
e50.grid(row=6,column=5,ipady=20)
bt51.grid(row=6,column=6)
e52.grid(row=6,column=8,ipady=20)
e53.grid(row=6,column=9,ipady=20)
e54.grid(row=6,column=10,ipady=20)

#gridding of row 7
e55.grid(row=8,column=0,ipady=20)
bt56.grid(row=8,column=1)
e57.grid(row=8,column=2,ipady=20)
e58.grid(row=8,column=4,ipady=20)
e59.grid(row=8,column=5,ipady=20)
bt60.grid(row=8,column=6)
e61.grid(row=8,column=8,ipady=20)
e62.grid(row=8,column=9,ipady=20)
e63.grid(row=8,column=10,ipady=20)

#gridiing of row 8
e64.grid(row=9,column=0,ipady=20)
bt65.grid(row=9,column=1)
bt66.grid(row=9,column=2)
e67.grid(row=9,column=4,ipady=20)
bt68.grid(row=9,column=5)
bt69.grid(row=9,column=6)
e70.grid(row=9,column=8,ipady=20)
bt71.grid(row=9,column=9)
bt72.grid(row=9,column=10)

#gridiing of row 9
bt73.grid(row=10,column=0)
bt74.grid(row=10,column=1)
bt75.grid(row=10,column=2)
bt76.grid(row=10,column=4)
e77.grid(row=10,column=5,ipady=20)
e78.grid(row=10,column=6,ipady=20)
bt79.grid(row=10,column=8)
bt80.grid(row=10,column=9)
e81.grid(row=10,column=10,ipady=20)

l1=Canvas(root,width=20,height=20)
l1.grid(row=0,column=3)

l2=Canvas(root,width=20,height=20)
l2.grid(row=0,column=7)

l3=Canvas(root,width=20,height=20)
l3.grid(row=3,column=0)

l4=Canvas(root,width=20,height=20)
l4.grid(row=7,column=0)



def fun():
    count = 0
    if e4 != 5:
        count+=1
    elif e7 != 6:
        count+=1
    elif e12 != 3:
        count+=1
    elif e13 != 8:
        count+=1
    elif e14 != 2:
        count+=1
    elif e16 != 5:
        count+=1
    elif e17 != 4:
        count+=1
    elif e18 != 9:
        count+=1
    elif e22 != 6:
        count+=1
    elif e23 != 4:
        count+=1
    elif e26 != 3:
        count+=1
    elif e27 != 1:
        count+=1
    elif e30 != 8:
        count+=1
    elif e31 != 9:
        count+=1
    elif e33 != 2:
        count+=1    
    elif e34 != 4:
        count+=1
    elif e36 != 5:
        count+=1
    elif e37 != 5:
        count+=1
    elif e38 != 6:
        count+=1
    elif e39 != 1:
        count+=1
    elif e42 != 4:
        count+=1
    elif e45 != 8:
        count+=1
    elif e46 != 4:
        count+=1
    elif e47 != 2:
        count+=1
    elif e50 != 8:
        count+=1 
    elif e52 != 7:
        count+=1
    elif e53 != 6:
        count+=1
    elif e54 != 3:
        count+=1
    elif e55 != 8:
        count+=1
    elif e57 != 2:
        count+=1
    elif e58 != 4:
        count+=1
    elif e59 != 9:
        count+=1
    elif e61 != 1:
        count+=1
    elif e62 != 5:
        count+=1
    elif e63 != 7:
        count+=1
    elif e64 != 7:
        count+=1
    elif e67 != 2:
        count+=1
    elif e70 != 3:
        count+=1
    elif e77 != 5:
        count+=1
    elif e78 != 3:
        count+=1
    elif e81 != 4:
        count+=1

    if count>=3:
        def showMsg():  
            messagebox.showinfo('Message', 'You lost')
    else:
        def showMsg():  
            messagebox.showinfo('Message', 'You won')
fun()

root.mainloop()


