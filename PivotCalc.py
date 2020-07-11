# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 09:34:34 2018

@author: Corkidi
"""

import tkinter as tk
import matplotlib.pyplot as plt
import fix_yahoo_finance as yf  

import arrow
#from matplotlib.figure import Figure 
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key='EJ69MPM068NGTJ30', output_format='pandas')



#yf.pdr_override() 



        
class Win1:
    def __init__(self, win, title, geo):

        self.win = win
        self.win.title('PivotGo')
        self.win.geometry(geo)
        self.lbl = tk.Label(win, text = title)
        self.lbl.grid(column = 1, row = 0)
        self.stocklbl = tk.Label(win, text = 'Stock Ticker')
        self.stocklbl.grid(column = 0, row = 1)
        self.enter_ticker = tk.Entry(self.win, width = 10)
        self.enter_ticker.grid(column = 0, row = 2)        
        self.enter_tik_but = tk.Button(win, text = 'Enter', command = self.getStock)
        self.enter_tik_but.grid(column = 0, row = 3)
        self.temp_lbl_list = []
        self.now = arrow.now().format('YYYY-MM-DD')
        self.yesterday = arrow.now().shift(days=-2).date()
        self.getDow()
#        self.matplotCanvas()
        
    def getDow(self):
        self.data = yf.download('DJI', self.yesterday, self.now)
        self.data1, self.meta_data = ts.get_intraday(symbol= 'DJI', interval='5min', outputsize='compact')
        a, b, c, d, e = self.now, self.yesterday, self.data, self.data1, 3
        self.dow = tk.Label(self.win, text = 'Dow Jone Ind.')
        self.dow.grid(column = 3, row = 3)
        self.buildPP(a, b, c, d, e) 
   
    def getStock(self):
        
        for i in self.temp_lbl_list:
            i.destroy()
        
        self.data = yf.download(self.enter_ticker.get(), self.yesterday, self.now)
        self.data1, self.meta_data = ts.get_intraday(symbol= self.enter_ticker.get(), interval='5min', outputsize='compact')

        a, b, c, d, e = self.now, self.yesterday, self.data, self.data1, 0 
        self.buildPP(a, b, c, d, e)  
        self.getDow()
         
    
    def buildPP(self, now, yesterday, data, data1, e):        
        self.r = 4
        self.high = self.data.loc[self.yesterday, 'High']
        self.low = self.data.loc[self.yesterday, 'Low']
        self.close = self.data.loc[self.yesterday, 'Close']
        self.pp = (self.high + self.low + self.close)/3
        self.r1 = (self.pp * 2) - self.low
        self.s1 = (self.pp * 2) - self.high
        self.r2 = self.pp + (self.high - self.low)
        self.s2 = self.pp - (self.high - self.low) 
        self.lblr = tk.Label(self.win, text = 'Resistance')
        self.lblr.grid(column = e, row = self.r)
        self.r += 1
        self.temp_lbl_list.append(self.lblr)
        self.lblr2 = tk.Label(self.win, text = round(self.r2, 2))
        self.lblr2.grid(column = e, row = self.r)
        self.r += 1
        self.temp_lbl_list.append(self.lblr2)
        self.lblr1 = tk.Label(self.win, text = round(self.r1, 2))
        self.lblr1.grid(column = e, row = self.r)
        self.r += 1
        self.temp_lbl_list.append(self.lblr1)
        self.lblpp = tk.Label(self.win, text = 'Pivot Point')
        self.lblpp.grid(column = e, row = self.r)
        self.r += 1
        self.temp_lbl_list.append(self.lblpp)
        self.lblpp1 = tk.Label(self.win, text = round(self.pp, 2))
        self.lblpp1.grid(column = e, row = self.r)
        self.r += 1
        self.temp_lbl_list.append(self.lblpp1)
        self.lbls = tk.Label(self.win, text = 'Support')
        self.lbls.grid(column = e, row = self.r)
        self.r += 1
        self.temp_lbl_list.append(self.lbls)
        self.lbls1 = tk.Label(self.win, text = round(self.s1, 2))
        self.lbls1.grid(column = e, row = self.r)
        self.r += 1
        self.temp_lbl_list.append(self.lbls1)
        self.lbls2 = tk.Label(self.win, text = round(self.s2, 2))
        self.lbls2.grid(column = e, row = self.r)
        self.r += 1
        self.temp_lbl_list.append(self.lbls2)
        
        self.cp = self.data1.loc[str(self.data1.tail(1).index.item()), '1. open']
        self.lblcp = tk.Label(self.win, text = 'Current Price')
        self.lblcp.grid(column = e, row = self.r)
        self.r += 1
        self.temp_lbl_list.append(self.lblcp)
        self.lblcp1 = tk.Label(self.win, text = self.cp)
        self.lblcp1.grid(column = e, row = self.r)
        self.r += 1
        self.temp_lbl_list.append(self.lblcp1)
        
        self.data1['2. high'].plot()
#        plt.savefig('output.png')
        plt.show()
        
#    def matplotCanvas(self):
#        f = Figure(figsize = (5,5), dpi = 100)
#        a = f.add_subplot(111)
#        a.plot([1,2,3,4,5], [5,6,7,8,9])
#        
#        canvas  = FigureCanvasTkAgg(f, self)
#        canvas.show()
#        canvas.grid(column=2, row=4)
#        
#        toolbar = NavigationToolbar2TkAgg(canvas, self)
#        canvas._tkcanvas.grig(column=2, row=5)
        
        
        
        
temp =[]
def start(): 
    
    main = tk.Tk()
    app = Win1(main, '_______________________Pivot Point Calculator______________________', '600x500')
    temp.append(app)
    main.mainloop()

if __name__ == '__main__':
    start()












