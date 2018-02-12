from Tkinter import*
from sqlite3 import*
import Tix

import tkMessageBox
root=Tk()
root.config(bg="white")
conn=connect('My.db')

cursor=conn.cursor()


po=PhotoImage(file="Untitled-3.gif")

def main():
    var=0
    def buy(item,txt):
        def bill():
            def go():
                tkMessageBox.showinfo("Window Title","Please Connect To Internet")

            labe=Toplevel()
            labe.config(bg="white")
            pin=Label(labe,text="Enter Your PIN",bg="white")
            pin.grid(row=0,column=0)
            Entry(labe).grid(row=0,column=1)
            passw=Label(labe,text="Enter Your PIN",bg="white")
            passw.grid(row=1,column=0)
            Entry(labe).grid(row=1,column=1)
            Button(labe,text="Buy",command=go).grid(row=2,column=1,sticky="WE")
        root3=Toplevel()
        root3.geometry("600x300")
        root3.config(bg="white")
        Label(root3,image=item).grid(row=0,column=0,sticky="W")
        Label(root3,text=txt,font="Time 14 bold",bg="white",fg="#256372").grid(row=0,column=1,sticky="N")
        
        byn=Button(root3,text="BUY NOW",bg="#71cee8",command=bill)
        byn.grid(row=1,column=1,sticky="S",padx=20,pady=5,ipadx=15,ipady=5)
        cart=Button(root3,text="Add To Cart",bg="#f9951f")
        
        cart.grid(row=1,column=2,sticky="S",ipady=5,ipadx=10,pady=5)
      

        
        
        
    root2=Tix.Tk()
    
    root2.geometry("1200x1000")
    root2.config(bg="white")
    label1=Label(root2,bg="white")
    label1.pack()

    p1=PhotoImage(file="running.gif")
    
    label2=Label(label1,bg="#2a2e31")
    label2.grid(row=0,column=0,ipadx=700,ipady=5)
    new1=Label(label2,text="Shop in your Way >>>",font="Times 20 bold",bg="#2a2e31" ,fg="#3bab9d")
    new1.pack()
    
    sw = Tix.ScrolledWindow(root2, bg="white",scrollbar=Tix.AUTO)
    sw.pack(side=LEFT,fill="both",expand="yes")
    canvas=Canvas(sw.window,bg="white")
    canvas.grid(row=1,column=0,ipadx=80,ipady=10)
    label3=Label(sw.window,image=p1,bg="white")
    label3.grid(row=0,column=0,sticky="WE",ipady=10)
    def shoes():
            
            img0=PhotoImage(file="img1.gif")

            
            img1=PhotoImage(file="img1.gif")
            
        
            img2=PhotoImage(file="img2.gif")
            img3=PhotoImage(file="img6.gif")
            img4=PhotoImage(file="formal.gif")
            img5=PhotoImage(file="flip.gif")
            img6=PhotoImage(file="Adidas.gif")

            
            Label(canvas,text="Shoes",font="Times 20 bold",bg="white",fg="#3bab9d").grid(row=0,column=0)
            
            btn1=Button(canvas,text="NIKE SHOES \n Fitness expert\n\n MRP:1500",fg="#252b48",image=img2,relief="flat",activebackground="#2a2e31",compound="top",bg="white",bd=4,font="Helvetica  11 bold")
            btn1.grid(row=1,column=0,padx=25,pady=25)
            btn1.bind("<Button-1>",lambda img4,img=img2:buy(img,"NIKE SHOES \n\n Fitness expert\n\n MRP:1500"))     
            btn2=Button(canvas,text="Puma \nSports In light\nMRP:2500",image=img1,relief="flat",fg="#252b48",activebackground="#2a2e31",compound="top",bg="white",font="Helvetica 11 bold")
            btn2.bind("<Button-1>",lambda img4,img=img1:buy(img,"Puma \n\nSports In light\n\nMRP:2500"))
            btn2.grid(row=1,column=1,padx=25)
                
            btn3=Button(canvas,text="NEW Puma Shoes \nLIVE THE SPIRIT\nMRP:2999",image=img3,compound="top",fg="#252b48",activebackground="#2a2e31",relief="flat",bg="white",font="Helvetica 11 bold")
            btn3.bind("<Button-1>",lambda img4,img=img3:buy(img,"NEW Puma Shoes \n\nLIVE THE SPIRIT\n\nMRP:2999"))
            btn3.grid(row=1,column=2,sticky="W",padx=25)
            btn4=Button(canvas,text="Red Tep\nFormal Shoes\nMRP:1999\-",image=img4,compound="top",fg="#252b48",activebackground="#2a2e31",relief="flat",bg="white",font="Helvetica 11 bold")
            btn4.bind("<Button-1>",lambda img4,img=img4:buy(img,"Red Tep\nFormal Shoes\nMRP:1999\-"))
            btn4.grid(row=1,column=3,sticky="W",padx=35)
            btn5=Button(canvas,text="Puma \nFlip-Flop Slipper\nMRP:950",image=img5,compound="top",fg="#252b48",activebackground="#2a2e31",relief="flat",bg="white",font="Helvetica 11 bold")
            btn5.bind("<Button-1>",lambda img4,img=img5:buy(img,"Puma \n\nFlip-Flop Slipper\n\nMRP:950"))
            btn5.grid(row=1,column=4,sticky="W",padx=35)
            
            btn6=Button(canvas,text="Adidas\n CSF Mens Shoes\nMRP:2855\-",image=img6,compound="top",fg="#252b48",activebackground="#2a2e31",relief="flat",bg="white",font="Helvetica 11 bold")
            btn6.bind("<Button-1>",lambda img4,img=img6:buy(img,"Adidas\n CSF Mens Shoes\nMRP:2855\-"))
            btn6.grid(row=1,column=4,sticky="W",padx=35)
            Label(canvas,text="Shirt",font="Times 20 bold",bg="white",fg="#3bab9d").grid(row=2,column=0)
    
    def shirt():
            s1=PhotoImage(file="s1.gif")
            s2=PhotoImage(file="s6.gif")
            s3=PhotoImage(file="s3.gif")
            s4=PhotoImage(file="s4.gif")
            s5=PhotoImage(file="s5.gif")
            
            
            btn7=Button(canvas,image=s1,relief="flat",bg="white",fg="#252b48",activebackground="#2a2e31",text="Men Black Shirt\nMRP:450",compound="top",font="Helvet 11 bold")
            btn7.bind("<Button-1>",lambda img4,img=s1:buy(img,"Men Black Shirt\n\nLatest In Design\n\n MRP:450"))
            btn7.grid(row=3,column=0,sticky="W",padx=15)
           
            btn8=Button(canvas,image=s2,bg="white",fg="#252b48",activebackground="#2a2e31",compound="top",text="Blue Printed Shirt\nTrendy Look\nMRP:499",relief="flat",font="Helvet 11 bold")
            btn8.bind("<Button-1>",lambda img4,img=s2:buy(img,"Blue Printed Shirt\n\nTrendy Look\n\nMRP:499"))
            btn8.grid(row=3,column=1,sticky="W",padx=15)
            
            btn9=Button(canvas,image=s3,bg="white",fg="#252b48",activebackground="#2a2e31",compound="top",text="ETHER-NAVY-ANIT Microbial\nCasual Shirt\nMRP:700",relief="flat",font="Helvet 11 bold")
            btn9.bind("<Button-1>",lambda img4,img=s3:buy(img,"ETHER-NAVY-ANIT Microbial\n\nCasual Shirt\n\nMRP:700"))
            btn9.grid(row=3,column=2,sticky="W",padx=25)

            btn10=Button(canvas,image=s4,bg="white",fg="#252b48",activebackground="#2a2e31",compound="top",text="ETHER BLUE\nAnti Microbial\nCasual Shirt\nMRP:799",relief="flat",font="Helvet 11 bold")
            btn10.bind("<Button-1>",lambda img4,img=s4:buy(img,"ETHER BLUE\n\nAnti Microbial\n\nCasual Shirt\n\nMRP:799"))
            btn10.grid(row=3,column=3,sticky="W",padx=25)
            
            btn11=Button(canvas,image=s5,bg="white",fg="#252b48",activebackground="#2a2e31",compound="top",text="Ether WHITE\nMen Casual Shirt\nMRP:899",relief="flat",font="Helvet 11 bold")
            btn11.bind("<Button-1>",lambda img4,img=s5:buy(img,"Ether WHITE\n\nMen Casual Shirt\n\nMRP:899"))
            btn11.grid(row=3,column=4,sticky="W",padx=15)
    def jeans():
            j1=PhotoImage(file="j1.gif")
            j2=PhotoImage(file="j2.gif")
            j3=PhotoImage(file="j3.gif")
            j4=PhotoImage(file="j4.gif")
            j5=PhotoImage(file="j5.gif")
            Label(canvas,text="Jeans",font="Times 20 bold",bg="white",fg="#3bab9d").grid(row=4,column=0)
            btn12=Button(canvas,image=j1,bg="white",fg="#252b48",activebackground="#2a2e31",compound="top",text="ROADSTER\nMen Blue Skinny Fit\nMRP:1599",relief="flat",font="Helvet 11 bold")
            btn12.bind("<Button-1>",lambda img4,img=j1:buy(img,"ROADSTER\n\nMen Blue Skinny Fit\n\nMRP:1599"))
            btn12.grid(row=5,column=0,sticky="W",padx=15)

            btn13=Button(canvas,image=j2,bg="white",fg="#252b48",activebackground="#2a2e31",compound="top",text="MID Rise\nMen Jeans\nMRP:1999",relief="flat",font="Helvet 11 bold")
            btn13.bind("<Button-1>",lambda img4,img=j2:buy(img,"MID Rise\n\nMen Jeans\n\nMRP:1999"))
            btn13.grid(row=5,column=1,sticky="W",padx=15)
            
            btn14=Button(canvas,image=j3,bg="white",fg="#252b48",activebackground="#2a2e31",compound="top",text="Rise Clean\nWomen Slim Fit\nMRP:1299",relief="flat",font="Helvet 11 bold")
            btn14.bind("<Button-1>",lambda img4,img=j3:buy(img,"Rise Clean\n\nWomen Slim Fit\n\nMRP:1299"))
            btn14.grid(row=5,column=2,sticky="W",padx=15)
            btn15=Button(canvas,image=j4,bg="white",fg="#252b48",activebackground="#2a2e31",compound="top",text="Roadster\nWomen Regular Fit\nMRP:1499",relief="flat",font="Helvet 11 bold")
            btn15.bind("<Button-1>",lambda img4,img=j4:buy(img,"Roadster\n\nWomen Regular Fit\n\nMRP:1499"))
            btn15.grid(row=5,column=3,sticky="W",padx=15)
            
            btn16=Button(canvas,image=j5,bg="white",fg="#252b48",activebackground="#2a2e31",compound="top",text="Ether \nMen Jeans\nMRP:899",relief="flat",font="Helvet 11 bold")
            btn16.bind("<Button-1>",lambda img4,img=j5:buy(img,"Ether \n\nMen Jeans\n\nMRP:899"))
            btn16.grid(row=5,column=4,sticky="W",padx=15)

    def women():   
            Label(canvas,text="Women   Suit & Kurta",font="Times 20 bold",bg="white",fg="#3bab9d").grid(row=6,column=0)
            suit1=PhotoImage(file="su1.gif")
            suit2=PhotoImage(file="su2.gif")
            suit3=PhotoImage(file="su3.gif")
            suit4=PhotoImage(file="su4.gif")
            suit5=PhotoImage(file="su5.gif")
            btn17=Button(canvas,image=suit1,bg="white",fg="#252b48",activebackground="#2a2e31",compound="top",text="Aujjessa Black \nFornt Slit\nMRP:1299",relief="flat",font="Helvet 11 bold")
            btn17.bind("<Button-1>",lambda img4,img=suit1:buy(img,"Aujjessa Black \n\nFornt Slit\n\nMRP:1299"))
            btn17.grid(row=7,column=0,sticky="W",padx=15)
                
            btn18=Button(canvas,image=suit2,bg="white",fg="#252b48",activebackground="#2a2e31",compound="top",text="La Firangi\nGreen Printed\nMRP:1350",relief="flat",font="Helvet 11 bold")
            btn18.bind("<Button-1>",lambda img4,img=suit2:buy(img,"La Firangi\n\nGreen Printed\n\nMRP:1350"))
            btn18.grid(row=7,column=1,sticky="W",padx=15)
                
            btn16=Button(canvas,image=suit3,bg="white",fg="#252b48",activebackground="#2a2e31",compound="top",text="Tissu \nWhite Printed\nMRP:899",relief="flat",font="Helvet 11 bold")
            btn16.bind("<Button-1>",lambda img4,img=suit3:buy(img,"Tissu \n\nWhite Printed\n\nMRP:899"))
            btn16.grid(row=7,column=2,sticky="W",padx=15)

                
            btn16=Button(canvas,image=suit4,bg="white",fg="#252b48",activebackground="#2a2e31",compound="top",text="Libas Orignal \nOriginal\nMRP:899",relief="flat",font="Helvet 11 bold")
            btn16.bind("<Button-1>",lambda img4,img=suit4:buy(img,"Libas Orignal \n\nOriginal\n\nMRP:899"))
            btn16.grid(row=7,column=3,sticky="W",padx=15)


                
            btn17=Button(canvas,image=suit5,bg="white",fg="#252b48",activebackground="#2a2e31",compound="top",text="Parom a art\nOriginal\nMRP:1399",relief="flat",font="Helvet 11 bold")
            btn17.bind("<Button-1>",lambda img4,img=suit5:buy(img,"Parom a art\n\nOriginal\n\nMRP:1399"))
            btn17.grid(row=7,column=4,sticky="W",padx=15)
    def ec():

            Label(canvas,text="Electronics",font="Times 20 bold",bg="white",fg="#3bab9d").grid(row=8,column=0)
            ec1=PhotoImage(file="ec1.gif")
            ec2=PhotoImage(file="ec2.gif")
            ec3=PhotoImage(file="ec3.gif")
            ec4=PhotoImage(file="ec4.gif")
            ec5=PhotoImage(file="ec5.gif")
            btn18=Button(canvas,image=ec1,bg="white",fg="#252b48",activebackground="#2a2e31",compound="top",text="Aujjessa Black \nFornt Slit\nMRP:5555",relief="flat",font="Helvet 11 bold")
            btn18.bind("<Button-1>",lambda img4,img=ec1:buy(img,"Aujjessa Black \n\nFornt Slit\n\nMRP:1299"))
            btn18.grid(row=9,column=0,sticky="W",padx=15)
            
            btn19=Button(canvas,image=ec2,bg="white",fg="#252b48",activebackground="#2a2e31",compound="top",text="Samsung Galaxy\n\nSamsmg Galxy S6\nMRP:11000",relief="flat",font="Helvet 11 bold")
            btn19.bind("<Button-1>",lambda img4,img=ec2:buy(img,"Karbon\n\nKarbon Desert With Lolipop\n\nMRP:6000"))
            btn19.grid(row=9,column=1,sticky="W",padx=15)
                
            btn20=Button(canvas,image=ec3,bg="white",fg="#252b48",activebackground="#2a2e31",compound="top",text="HTC Desire \nNew Model Camera Expert\nMRP:18999",relief="flat",font="Helvet 11 bold")
            btn20.bind("<Button-1>",lambda img4,img=ec3:buy(img,"HTC Desire \nNew Model Camera Expert\nMRP:18999"))
            btn20.grid(row=9,column=2,sticky="W",padx=15)

                
            btn21=Button(canvas,image=ec4,bg="white",fg="#252b48",activebackground="#2a2e31",compound="top",text="Intex \n\n Intex Hometheter \n \n With Five Wireless spekar \n\nMRP:2500",relief="flat",font="Helvet 11 bold")
            btn21.bind("<Button-1>",lambda img4,img=ec4:buy(img,"Intex \n\nIntex Hometheter\n\n With Five Wireless spekar \n\nMRP:899"))
            btn21.grid(row=9,column=3,sticky="W",padx=15)


                
            btn22=Button(canvas,image=ec5,bg="white",fg="#252b48",activebackground="#2a2e31",compound="top",text="Sony\nSony New Wireless Headpone \nMRP:1200",relief="flat",font="Helvet 11 bold")
            btn22.bind("<Button-1>",lambda img4,img=ec5:buy(img,"Sony\nSony New Wireless Headpone\nMRP:1200 "))
            btn22.grid(row=9,column=4,sticky="W",padx=15)
    shoes()
    shirt()
    jeans()
    women()
    ec()
    root2.mainloop()

    
    
def login():
    def data():
        l=0
        p=0
    
        name=e.get()
        password=e1.get()
        cursor.execute("select Id from info")
        row=cursor.fetchall()
      
        
        for rows in row:
            for i in rows:
               if name==i:
                    break

                 
        cursor.execute("select password from info")
        col=cursor.fetchall()
        
        for cols in col:
            for j in cols:
                if password==j and name==i:
                    p=1
                    
                    try:
                        root1.destroy()
                        root.destroy()
                        
                    except:
                        break
                    main()
                else :
                    l=1
                   
                    
                
                    
                    
            
        if p==0:
           
            tkMessageBox.showinfo("Window Title","Password Doesn't match")
        
            
    
    cursor.execute("create table if not exists info(Id varchar2(16),password varchar2(16))")
    
    root1=Toplevel()
    root1.geometry("700x500")
    root1.title("Login")
    
    
    
    la=Label(root1,image=po)
    la.pack(fill="both",expand="yes")
    
    l2=Label(la,text="Name/Email: ",bg="black",fg="#31948f",font="Times 14 bold")
    l2.grid(row=0,column=0,pady=80,padx=60,ipady=5)
    
    e=Entry(la,width=30,bg="white",fg="#31948f",font=90)
    e.grid(row=0,column=1,ipady=6)
    
    l3=Label(la,text="Password: ",bg="black",fg="#31948f",font="Times 14 bold")
    l3.grid(row=1,column=0,ipadx=14,ipady=5)
    
    e1=Entry(la,show="*",font=90,bg="white",fg="#31948f",width=30)
    e1.grid(row=1,column=1,ipady=6)
    
    lgin=Button(la,text="Login",bg="#130D19",fg="#31948f",padx=20,pady=8,font="Times 16 bold",command=data)
    lgin.grid(row=3,column=1,padx=10,pady=10)
    
    
def account():
    
    
    
    def insert():
            l=0
            name=e.get()
            password=e1.get()
            cpassword=e2.get()
            cursor.execute("select Id from info")
            row=cursor.fetchall()
        
        
            for rows in row:
                for i in rows:
                   if name==i:
                        l=1
                        tkMessageBox.showinfo("Window Title","User Alredy Exists")
                        
            if l==0:
                   
                   if (password =="" or name == "" or cpassword == ""):
                         tkMessageBox.showinfo("Window Title","Please Fill All Entry")
                
            
                   else:
                            
                            if password==cpassword:
                                          
                                          a=[(name,password)]
                                          
                                          cursor.executemany("insert into info values(?,?)",a)
                                          
                                          e1.destroy()
                                          e.destroy()
                                          e2.destroy()
                                          l2.destroy()
                                          l3.destroy()
                                          l4.destroy()
                                          lgin.destroy()
                                          tkMessageBox.showinfo("Window Title","User has Created")
                                          root1.destroy()
                                                
                            else:
                                    tkMessageBox.showinfo("Window Title","Password doesnot match")

    cursor.execute("create table if not exists info(Id varchar2(16),password varchar2(16))")
    detail=cursor.execute("select * from info")
    new=cursor.fetchall()
    
                
    str1=StringVar()
    str2=StringVar()
    str3=StringVar()
    str4=StringVar()
    root1=Toplevel()
    root1.geometry("800x560")
    root1.title("Create Account")               
    la=Label(root1,image=po)
    la.pack(fill="both",expand="yes")

    l2=Label(la,text="Id: ",bg="black",fg="#31948f",font="Times 14 bold")
    l2.grid(row=1,column=0,padx=60,ipady=5,ipadx=60,pady=20)
    
    e=Entry(la,width=30,text=str1,bg="white",fg="#31948f",font=90)
    e.grid(row=1,column=1,ipady=6)
    
    l3=Label(la,text="Password: ",bg="black",fg="#31948f",font="Times 14 bold")
    l3.grid(row=2,column=0,padx=60,ipady=5,ipadx=35)
    
    e1=Entry(la,font=90,show="*",text=str2,bg="white",fg="#31948f",width=30)
    e1.grid(row=2,column=1,ipady=6)
    l4=Label(la,text="Confirm Password: ",bg="black",fg="#31948f",font="Times 14 bold")
    l4.grid(row=3,column=0,pady=80,padx=60,ipady=5)
    
    e2=Entry(la,font=90,text=str3,show="*",bg="white",fg="#31948f",width=30)
    e2.grid(row=3,column=1,ipady=6)
    
    lgin=Button(la,text="Login",bg="#130D19",fg="#31948f",padx=20,pady=8,font="Times 16 bold",command=insert)
    lgin.grid(row=4,column=1,padx=10,pady=10)
   
root.title("Account")
root.geometry("870x500")
poto=PhotoImage(file="pyimg.gif")
l=Label(root,image=poto)
l.pack(fill="both",expand="yes")
b1=Button(l,text="Login",activebackground="white",bg="#130D19",fg="#31948f",font="Times 16 bold",relief="sunken",padx=60,pady=20,command=login)
b1.grid(row=0,column=0,pady=50,padx=30)
b2=Button(l,text="Create Account",fg="#31948f",bg="#130D19",font="Times 16 bold",padx=80,pady=20,relief="sunken",command=account)
b2.grid(row=2,column=0,padx=300)
information=Toplevel()
information.config(bg="white")
lab=Label(information,text="NAME:MAYANK JAIN\n\nEnroll: 151322\n\nBatch:B4",bg="white",fg="#31948f",font="Times 14 bold")
lab.grid(row=3,column=0,padx=300,pady=50)
root.mainloop()
