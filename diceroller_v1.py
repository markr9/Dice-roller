# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 10:15:14 2018

@author: MR
"""

#dice roller
#roll D6 dice grpahically

#modules
from tkinter import *
from tkinter import *
from random import random as rad
from time import *

class Gui:
    #initialistion
    def __init__(self,win):
        self.win=win
        
        #frames
        self.frametop=Frame(win)
        self.framemain=Frame(win)
        
        #static wigits
        self.numlab=Label(self.frametop,text='Number of dice')
        self.numentry=Entry(self.frametop)
        self.targetlab=Label(self.frametop,text='Target Value')
        self.modlab=Label(self.frametop,text='Modifier')
        self.d1=Label(self.frametop,text='1s')
        self.d2=Label(self.frametop,text='2s')
        self.d3=Label(self.frametop,text='3s')
        self.d4=Label(self.frametop,text='4s')
        self.d5=Label(self.frametop,text='5s')
        self.d6=Label(self.frametop,text='6s')
        self.dtotp=Label(self.frametop,text='Total pass')
        self.dtotf=Label(self.frametop,text='Total fail')
        self.d1v=Label(self.frametop,text=0)
        self.d2v=Label(self.frametop,text=0)
        self.d3v=Label(self.frametop,text=0)
        self.d4v=Label(self.frametop,text=0)
        self.d5v=Label(self.frametop,text=0)
        self.d6v=Label(self.frametop,text=0)
        self.dtotpv=Label(self.frametop,text=0)
        self.dtotfv=Label(self.frametop,text=0)
        self.d1c=Label(self.frametop,text=0)
        self.d2c=Label(self.frametop,text=0)
        self.d3c=Label(self.frametop,text=0)
        self.d4c=Label(self.frametop,text=0)
        self.d5c=Label(self.frametop,text=0)
        self.d6c=Label(self.frametop,text=0)
        self.d1cc=Label(self.frametop,text='1+')
        self.d2cc=Label(self.frametop,text='2+')
        self.d3cc=Label(self.frametop,text='3+')
        self.d4cc=Label(self.frametop,text='4+')
        self.d5cc=Label(self.frametop,text='5+')
        self.d6cc=Label(self.frametop,text='6+')
        self.high=Label(self.frametop,text='Highest Value')
        self.high2=Label(self.frametop,text='2nd Highest Value')
        self.totsum=Label(self.frametop,text='Sum')
        self.highv=Label(self.frametop,text=0)
        self.high2v=Label(self.frametop,text=0)
        self.totsumv=Label(self.frametop,text=0)
        self.rolllab=Label(self.frametop,text=' ')
        self.t1s=Label(self.frametop,text=0)
        self.t2s=Label(self.frametop,text=0)
        self.t3s=Label(self.frametop,text=0)
        self.t4s=Label(self.frametop,text=0)
        self.t5s=Label(self.frametop,text=0)
        self.t6s=Label(self.frametop,text=0)
        self.tot1s=Label(self.frametop,text=0)
        self.tot2s=Label(self.frametop,text=0)
        self.tot3s=Label(self.frametop,text=0)
        self.tot4s=Label(self.frametop,text=0)
        self.tot5s=Label(self.frametop,text=0)
        self.tot6s=Label(self.frametop,text=0)
        
        #dynamic wigits
        self.Btnroll=Button(self.frametop,text='Roll Dice')
        self.Btnrr=Button(self.frametop,text='Re-roll fails')
        self.Btnrr1=Button(self.frametop,text='Re-roll 1s')
        
    def posgui(self,win):
        #posistions
        #frames
        self.frametop.grid(row=1,column=1)
        self.framemain.grid(row=2,column=1)
        self.numlab.grid(row=1,column=1)
        self.numentry.grid(row=2,column=1)
        optarget.Btnup.grid(row=2,column=2)
        optarget.txvalue.grid(row=2,column=3,rowspan=2)
        optarget.Btndown.grid(row=3,column=2)
        self.targetlab.grid(row=1,column=2,columnspan=2)
        self.Btnroll.grid(row=1,column=6)
        self.Btnrr.grid(row=1,column=7)
        opmod.Btnup.grid(row=2,column=4)
        opmod.txvalue.grid(row=2,column=5,rowspan=2)
        opmod.Btndown.grid(row=3,column=4)
        self.modlab.grid(row=1,column=4,columnspan=2)
        self.Btnrr1.grid(row=2,column=7)
        self.d1.grid(row=1,column=8)
        self.d2.grid(row=1,column=9)
        self.d3.grid(row=1,column=10)
        self.d4.grid(row=1,column=11)
        self.d5.grid(row=1,column=12)
        self.d6.grid(row=1,column=13)
        self.dtotp.grid(row=1,column=14)
        self.dtotf.grid(row=1,column=15)
        self.d1v.grid(row=2,column=8)
        self.d2v.grid(row=2,column=9)
        self.d3v.grid(row=2,column=10)
        self.d4v.grid(row=2,column=11)
        self.d5v.grid(row=2,column=12)
        self.d6v.grid(row=2,column=13)
        self.dtotpv.grid(row=2,column=14)
        self.dtotfv.grid(row=2,column=15)
        self.d1c.grid(row=5,column=8)
        self.d2c.grid(row=5,column=9)
        self.d3c.grid(row=5,column=10)
        self.d4c.grid(row=5,column=11)
        self.d5c.grid(row=5,column=12)
        self.d6c.grid(row=5,column=13)
        self.d1cc.grid(row=4,column=8)
        self.d2cc.grid(row=4,column=9)
        self.d3cc.grid(row=4,column=10)
        self.d4cc.grid(row=4,column=11)
        self.d5cc.grid(row=4,column=12)
        self.d6cc.grid(row=4,column=13)
        self.high.grid(row=3,column=6)
        self.high2.grid(row=4,column=6)
        self.totsum.grid(row=4,column=14)
        self.highv.grid(row=3,column=7)
        self.high2v.grid(row=4,column=7)
        self.totsumv.grid(row=5,column=14)
        self.rolllab.grid(row=2,column=6)
        self.t1s.grid(row=3,column=8)
        self.t2s.grid(row=3,column=9)
        self.t3s.grid(row=3,column=10)
        self.t4s.grid(row=3,column=11)
        self.t5s.grid(row=3,column=12)
        self.t6s.grid(row=3,column=13)
        self.tot1s.grid(row=6,column=8)
        self.tot2s.grid(row=6,column=9)
        self.tot3s.grid(row=6,column=10)
        self.tot4s.grid(row=6,column=11)
        self.tot5s.grid(row=6,column=12)
        self.tot6s.grid(row=6,column=13)
        
    #destructor method
    def __del__(self):
        pass    
    
#class for buttons used in option frame
class Numop:
    opvalue=1 #displayed value of option
    maxvalue=25 #max value can be incremented to
    minvalue=1
    incvalue=1 #amount incremented per click
        
    #increases option value by incvalue on click of the + button
    def up(self,opvalue,maxvalue,incvalue):
        #stop increasing above maxvalue
        if self.opvalue >= self.maxvalue:
            return
        else:
            self.opvalue +=self.incvalue
            self.txvalue.configure(text=self.opvalue)
            return self.opvalue+self.incvalue
            
    #decreases option value by incvalue on click of the - button; only works as long as value>-1
    def down(self,opvalue,minvalue,incvalue):
        #stop decrementing below 0
        if self.opvalue <= self.minvalue:
            return
        else:
            self.opvalue -=self.incvalue
            self.txvalue.configure(text=self.opvalue)
            return self.opvalue-self.incvalue
        
    #definitions for buttons '+' and '-' and number label
    def __init__(self,opframe):
        self.opframe=opframe
        self.Btnup=Button(opframe,text='+',command=lambda:self.up(self.opvalue,self.maxvalue,self.incvalue),width=1)
        self.Btndown=Button(opframe,text='-',command=lambda:self.down(self.opvalue,self.minvalue,self.incvalue),width=1)
        self.txvalue=Label(opframe,text=1)
        
    #fn to disable all 3 parts of the option
    def Disable(self):
        self.Btnup.configure(state=DISABLED)
        self.Btndown.configure(state=DISABLED)
        
    #fn to enable all 3 parts of the option
    def Enable(self):
        self.Btnup.configure(state=NORMAL)
        self.Btndown.configure(state=NORMAL)
        
    #destructor method
    def __del__(self):
        pass

class Vars:
    target=0
    num=0
    tot=[0,0,0,0,0,0]
    reroll=0
    mod=0
    widthlim=10
    totpass=0
    totfail=0
    col=[]
    vec=[]
    rolls=0
    t1s=0
    t2s=0
    t3s=0
    t4s=0
    t5s=0
    t6s=0
    tot1s=0
    tot2s=0
    tot3s=0
    tot4s=0
    tot5s=0
    tot6s=0
    #rrs=0
    
    def __init__(self):
        self.dice=[]
        self.x=[]
    
    def roll(self):
        self.dice=[]
        self.x=[]
        try:
            self.num=int(gui.numentry.get())
        except Exception:
            pass
        i=0
        while i<self.num:
            a=rad()*6+1
            self.dice.append(int(a))
            self.x.append(int(a))
            i+=1
        self.count(0)
            
    def count(self,r):
        Vars.rolls=Vars.rolls+1
        gui.rolllab.configure(text=Vars.rolls)
        n=gui.framemain.grid_slaves()
        for m in n:
            m.destroy()
        self.vec=[]
        self.col=[]
        self.totpass=0
        self.totfail=0
        self.mod=int(opmod.txvalue.cget('text'))
        self.tot[0]=self.dice.count(1)
        self.tot[1]=self.dice.count(2)
        self.tot[2]=self.dice.count(3)
        self.tot[3]=self.dice.count(4)
        self.tot[4]=self.dice.count(5)
        self.tot[5]=self.dice.count(6)
        gui.d1v.configure(text=self.tot[0])
        gui.d2v.configure(text=self.tot[1])
        gui.d3v.configure(text=self.tot[2])
        gui.d4v.configure(text=self.tot[3])
        gui.d5v.configure(text=self.tot[4])
        gui.d6v.configure(text=self.tot[5])
        gui.d6c.configure(text=self.tot[5])
        gui.d5c.configure(text=self.tot[5]+self.tot[4])
        gui.d4c.configure(text=self.tot[5]+self.tot[4]+self.tot[3])
        gui.d3c.configure(text=self.tot[5]+self.tot[4]+self.tot[3]+self.tot[2])
        gui.d2c.configure(text=self.tot[5]+self.tot[4]+self.tot[3]+self.tot[2]+self.tot[1])
        gui.d1c.configure(text=self.tot[5]+self.tot[4]+self.tot[3]+self.tot[2]+self.tot[1]+self.tot[0])
        self.target=int(optarget.txvalue.cget('text'))
        j=5
        while j>=(self.target-1-self.mod):
            if j==0:
                break
            self.totpass+=self.tot[j]
            j-=1
        self.totfail=self.num-self.totpass
        gui.dtotpv.configure(text=self.totpass)
        gui.dtotfv.configure(text=self.totfail)
        self.place()
        if r==0:
            self.consect(0)
        
    def rr1(self):
        #self.rrs=1
        i=0
        while i<self.num:
            if self.dice[i]==1:
                a=rad()*6+1
                self.dice[i]=int(a)
                self.x[i]=int(a)
                self.consect(1,ix=i)
            i+=1
        self.count(1)
        
    def rr(self):
        #self.rrs=1
        i=0
        while i<self.num:
            if self.dice[i]<self.target:
                a=rad()*6+1
                self.dice[i]=int(a)
                self.x[i]=int(a)
                self.consect(1,ix=i)
            i+=1
        self.count(1)
        
    def place(self):
        sleep(1)
        j=0
        while j<self.num:
            a=str(j)
            b='v'+a
            self.vec.append(b)
            if self.dice[j]<(self.target-self.mod):
                self.col.append('red')
            else:
                self.col.append('green')
            j+=1
        i=0
        while i<self.num:
            self.vec[i]=Gui2(i,self.col[i])
            i+=1
        self.x.sort()
        self.x.reverse()
        gui.highv.configure(text=self.x[0])
        try:
            gui.high2v.configure(text=self.x[1])
            if self.x[1]>=(self.target-self.mod):
                gui.high2v.configure(bg='green')
            else:
                gui.high2v.configure(bg='red')
        except Exception:
            gui.high2v.configure(text=0)
        gui.totsumv.configure(text=sum(self.dice))
        if self.x[0]>=(self.target-self.mod):
            gui.highv.configure(bg='green')
        else:
            gui.highv.configure(bg='red')
        if sum(self.dice)>=(self.target-self.mod):
            gui.totsumv.configure(bg='green')
        else:
            gui.totsumv.configure(bg='red')
        
    def consect(self,ty,ix=0):
        if ty==0:
            gui.t1s.configure(text=self.tot[0]+self.t1s)
            gui.t2s.configure(text=self.tot[1]+self.t2s)
            gui.t3s.configure(text=self.tot[2]+self.t3s)
            gui.t4s.configure(text=self.tot[3]+self.t4s)
            gui.t5s.configure(text=self.tot[4]+self.t5s)
            gui.t6s.configure(text=self.tot[5]+self.t6s)
            gui.tot6s.configure(text=self.tot[5]+self.tot6s)
            gui.tot5s.configure(text=self.tot[5]+self.tot[4]+self.tot5s)
            gui.tot4s.configure(text=self.tot[5]+self.tot[4]+self.tot[3]+self.tot4s)
            gui.tot3s.configure(text=self.tot[5]+self.tot[4]+self.tot[3]+self.tot[2]+self.tot3s)
            gui.tot2s.configure(text=self.tot[5]+self.tot[4]+self.tot[3]+self.tot[2]+self.tot[1]+self.tot2s)
            gui.tot1s.configure(text=self.tot[5]+self.tot[4]+self.tot[3]+self.tot[2]+self.tot[1]+self.tot[0]+self.tot1s)
            self.t1s=self.t1s+self.tot[0]
            self.t2s=self.t2s+self.tot[1]
            self.t3s=self.t3s+self.tot[2]
            self.t4s=self.t4s+self.tot[3]
            self.t5s=self.t5s+self.tot[4]
            self.t6s=self.t6s+self.tot[5]
            self.tot1s=self.tot[0]+self.tot[1]+self.tot[2]+self.tot[3]+self.tot[4]+self.tot[5]+self.tot1s
            self.tot2s=self.tot[1]+self.tot[2]+self.tot[3]+self.tot[4]+self.tot[5]+self.tot2s
            self.tot3s=self.tot[2]+self.tot[3]+self.tot[4]+self.tot[4]+self.tot[5]+self.tot3s
            self.tot4s=self.tot[3]+self.tot[4]+self.tot[5]+self.tot4s
            self.tot5s=self.tot[4]+self.tot[5]+self.tot5s
            self.tot6s=self.tot[5]+self.tot6s
        else:
            if self.dice[ix]==1:
                gui.t1s.configure(text=1+self.t1s)
                gui.tot6s.configure(text=1+self.tot6s)
                gui.tot5s.configure(text=1+self.tot5s)
                gui.tot4s.configure(text=1+self.tot4s)
                gui.tot3s.configure(text=1+self.tot3s)
                gui.tot2s.configure(text=1+self.tot2s)
                gui.tot1s.configure(text=1+self.tot1s)
                self.t1s=self.t1s+1
                self.tot1s=1+self.tot1s
                self.tot2s=1+self.tot2s
                self.tot3s=1+self.tot3s
                self.tot4s=1+self.tot4s
                self.tot5s=1+self.tot5s
                self.tot6s=1+self.tot6s
            elif self.dice[ix]==2:
                gui.t2s.configure(text=1+self.t2s)
                gui.tot6s.configure(text=1+self.tot6s)
                gui.tot5s.configure(text=1+self.tot5s)
                gui.tot4s.configure(text=1+self.tot4s)
                gui.tot3s.configure(text=1+self.tot3s)
                gui.tot2s.configure(text=1+self.tot2s)
                self.t2s=self.t2s+1
                self.tot2s=1+self.tot2s
                self.tot3s=1+self.tot3s
                self.tot4s=1+self.tot4s
                self.tot5s=1+self.tot5s
                self.tot6s=1+self.tot6s
            elif self.dice[ix]==3:
                gui.t3s.configure(text=1+self.t3s)
                gui.tot6s.configure(text=1+self.tot6s)
                gui.tot5s.configure(text=1+self.tot5s)
                gui.tot4s.configure(text=1+self.tot4s)
                gui.tot3s.configure(text=1+self.tot3s)
                self.t3s=self.t3s+1
                self.tot3s=1+self.tot3s
                self.tot4s=1+self.tot4s
                self.tot5s=1+self.tot5s
                self.tot6s=1+self.tot6s
            elif self.dice[ix]==4:
                gui.t4s.configure(text=1+self.t4s)
                gui.tot6s.configure(text=1+self.tot6s)
                gui.tot5s.configure(text=1+self.tot5s)
                gui.tot4s.configure(text=1+self.tot4s)
                self.t4s=self.t4s+1
                self.tot4s=1+self.tot4s
                self.tot5s=1+self.tot5s
                self.tot6s=1+self.tot6s
            elif self.dice[ix]==5:
                gui.t5s.configure(text=1+self.t5s)
                gui.tot6s.configure(text=1+self.tot6s)
                gui.tot5s.configure(text=1+self.tot5s)
                self.t6s=self.t6s+1
                self.tot5s=1+self.tot5s
                self.tot6s=1+self.tot6s
            elif self.dice[ix]==6:
                gui.t6s.configure(text=1+self.t6s)
                gui.tot6s.configure(text=1+self.tot6s)
                self.t6s=self.t6s+1
                self.tot6s=1+self.tot6s
        
    #destructor method
    def __del__(self):
        pass
        
class Gui2:
    def __init__(self,i,col):
        dlab=Label(gui.framemain,text=vars0.dice[i],bg=col)
        a=int(i/50)
        b=i%50
        dlab.grid(row=a,column=b)
        
    #destructor method
    def __del__(self):
        pass

#main window, window title and getting image
win=Tk()
win.title('Dice Roller')

#instances
gui=Gui(win)
vars0=Vars()

#instances for up/down button sets
optarget=Numop(gui.frametop)
opmod=Numop(gui.frametop)

#mainfns
gui.posgui(win)

#set button range
opmod.maxvalue=20
opmod.minvalue=-20
opmod.txvalue.configure(text=0)
opmod.opvalue=0

#buttons commands
gui.Btnroll.configure(command=lambda:vars0.roll())
gui.Btnrr1.configure(command=lambda:vars0.rr1())
gui.Btnrr.configure(command=lambda:vars0.rr())

win.mainloop()
