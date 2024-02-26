import tkinter as tk

win=tk.Tk()
win.geometry("500x500")
win.title("student managrment system")

def quit():
    win.destory()

def aboutpage():
    abt=tk.Tk()
    abt.title("about us")
    abt.geometry("300x300")

    message="""welcome to parent window
    created on : 23-02-2024
    by Hajeera sithika
    """
menubar=tk.Menu(win)
filemenu=tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File",menu=filemenu,underline=0)
filemenu.add_command(label="New", underline=0, accelerator="Alt+F")
filemenu.add_command(label="New window", underline=4, accelerator="Alt+F")
filemenu.add_command(label="Open", underline=0, accelerator="Alt+F")
filemenu.add_command(label="Save", underline=0, accelerator="Alt+F")
filemenu.add_command(label="SaveAs", underline=4, accelerator="Alt+F")
filemenu.add_separator()
filemenu.add_command(label="PageSetup", underline=7, accelerator="Alt+F")
filemenu.add_command(label="Print", underline=0, accelerator="Alt+F")
filemenu.add_separator()
filemenu.add_command(label="Exit", underline=1, command=quit, accelerator="Ctrl+2")


editmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editmenu, underline=0)
editmenu.add_separator()
editmenu.add_command(label="Cut", underline=0,accelerator="Ctrl+F")
editmenu.add_command(label="Copy", underline=0,accelerator="Ctrl+C")
editmenu.add_command(label="Paste", underline=0,accelerator="Ctrl+V")
editmenu.add_command(label="Delete", underline=0,accelerator="Del")
editmenu.add_separator()
editmenu.add_command(label="Find...", underline=0, accelerator="Ctrl+F")
editmenu.add_command(label="Find Next", underline=0, accelerator="F3")
editmenu.add_command(label="Find Previous", underline=0, accelerator="Shift+F3")
editmenu.add_command(label="Replace...", underline=0,accelerator="Ctrl+H")
editmenu.add_command(label="Go To...", underline=0,accelerator="Ctrl+G")
editmenu.add_separator()
editmenu.add_command(label="Select All", underline=0,accelerator="Ctrl+A")
editmenu.add_command(label="Time/Date", underline=0,accelerator="F5")

formatmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Format",menu=formatmenu, underline=0)
formatmenu.add_command(label="Word Wrap", underline=0, accelerator="Alt+F")
formatmenu.add_command(label="Font...", underline=0, accelerator="Alt+F")

viewmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="View",menu=viewmenu, underline=0)
viewmenu.add_command(label="Zoom", underline=0, accelerator="Alt+F")
viewmenu.add_command(label="Status Bar", underline=0, accelerator="Alt+F")

helpmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=helpmenu, underline=0)
helpmenu.add_command(label="View Help", underline=5,accelerator="Alt+F",command=aboutpage)
helpmenu.add_command(label="Send Feedback", underline=5,accelerator="Alt+F")
helpmenu.add_command(label="About Notepad", underline=0,accelerator="Alt+F")
                     

win.config(menu=menubar)

win.mainloop()