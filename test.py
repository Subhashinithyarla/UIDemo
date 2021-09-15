try:
    import tkinter as tk
    import tkinter.ttk as ttk
    from tkinter import filedialog
except ImportError:
    import Tkinter as tk
    import ttk
    import tkFileDialog as filedialog
from tkinter import *
import tkinter
from tkcalendar import Calendar
import sqlite3
import os
import tkinter as tk
from ttkthemes import ThemedStyle
import time
import tkinter.font as font
from datetime import date
from datetime import datetime, timedelta
from datetime import datetime
from tkinter import ttk
import time
# Import Module
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("ROS Documentation tool")
# Set geometry (widthxheight)
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

global ticketno1
ticketno1 = ""

global fromdate
fromdate = [];
def f_calender():
    # def print_sel(selection):
    # print(selection.widget.get_date())
    fromcalenderframe = Tk()
    fromcalenderframe.title('select the from Date')
    fromcalenderframe.geometry('250x180+250+120')
    cal = Calendar(fromcalenderframe, selectmode='day', date_pattern='MM/dd/yyyy', year=date.today().year,
                   month=date.today().month, day=date.today().day, maxdate=date.today())
    cal.place(x=0, y=0)
    cal.bind('<<CalendarSelected>>', from_entrydate)

    # destroy function
    def afterclick(evt):
        w = fromcalenderframe
        w.destroy()

    fromcalenderframe.bind('<<CalendarSelected>>', afterclick)


def from_entrydate(selection):
    comp_date_ros.delete(0, END)
    date = selection.widget.get_date()
    final_date = datetime.strptime(date, "%m/%d/%Y").strftime('%d %B %Y')
    comp_date_ros.insert(0, final_date)
    fdate = comp_date_ros.get()
    fromdate.insert(0, comp_date_ros.get())
    #print(fromdate)

def check1(event):
    ticketno1 = ticket_ros.get()


fram2 = Frame(root, width=950, height=700, relief=SUNKEN, background="LightSkyBlue3")
fram2.pack(side=TOP, fill='both', expand=True)
root.state('zoomed')
style = ThemedStyle()
style.set_theme("aquativo")
style.configure("Kim.TButton", font=('ARIAL', 9, 'bold'), anchor='CENTER', relief='raised')
ros = ttk.Label(fram2, text='ROS DOCUMENTATION TOOL',font=('ARIAL', 10, 'bold'),anchor='center', width=45)
ros.place(x=480, y=20, height=26)
lbf = tk.LabelFrame(fram2, text="Documentation tool", relief="groove", font=('ARIAL', 13, 'bold'),
                            bg='LightSkyBlue3', fg="navy")
lbf.place(x=40, y=60, width=1200, height=560)

reset = ttk.Button(lbf, text='RESET', style="Kim.TButton")
reset.place(x=20, y=20, width=80, height=25)


ticket = ttk.Label(lbf, text='TICKET NO', anchor='center', width=30, font=('ARIAL', 10, 'bold'))
ticket.place(x=140, y=20, height=26)
ticket_ros = ttk.Entry(lbf,  justify='center', width=36)
ticket_ros.place(x=380, y=20, height=26)
ticket_ros.bind('<KeyRelease>', check1)


assigned = ttk.Label(lbf, text='ASSIGNED TO', anchor='center', width=30, font=('ARIAL', 10, 'bold'))
assigned.place(x=660, y=20, height=26)
assigned_ros = ttk.Entry(lbf,  justify='center', width=36)
assigned_ros.place(x=900, y=20, height=26)

firewall = ttk.Label(lbf, text='Firewall Involved', anchor='center', width=30, font=('ARIAL', 10, 'bold'))
firewall.place(x=140, y=125, height=26)
firewall_ros = ttk.Entry(lbf,  justify='center', width=60)
firewall_ros.place(x=380, y=110, height=50)


current_status = ttk.Label(lbf, text='Current Status', anchor='center', width=30, font=('ARIAL', 10, 'bold'))
current_status.place(x=140, y=185, height=30)
current_status_ros = ttk.Entry(lbf,  justify='center', width=60)
current_status_ros.place(x=380, y=185, height=30)

# comp_date = ttk.Label(lbf, text='current Status', anchor='center', width=30, font=('ARIAL', 10, 'bold'))
# comp_date.place(x=140, y=235, height=30)
comp_date = ttk.Button(lbf, text='Compilation Date', style="Kim.TButton", command = f_calender)
comp_date.place(x=140, y=235, width=210, height=30)
comp_date_ros = ttk.Entry(lbf,  justify='center', width=60)
comp_date_ros.place(x=380, y=235, height=30)

childcare = ttk.Label(lbf, text='Child Care', anchor='center', width=30, font=('ARIAL', 10, 'bold'))
childcare.place(x=140, y=285, height=30)
childcare_ros = ttk.Entry(lbf,  justify='center', width=60)
childcare_ros.place(x=380, y=285, height=30)

copyall = ttk.Button(lbf, text='COPY ALL', style="Kim.TButton")
copyall.place(x=700, y=360, width=80, height=25)
# all widgets will be here
# Execute Tkinter
root.mainloop()
