import sys
import re
import tkMessageBox as mbox
import urllib2
from Tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, END, INSERT
from ttk import Frame, Label, Entry
if sys.version_info < (3, 0):
    # Python 2
    import Tkinter as tk
else:
    # Python 3
    import tkinter as tk


def get_page_text(url):
    response = urllib2.urlopen(url)
    html = response.read()
    return html


def get_keywords(url):
    html = get_page_text(url)
    regex = r"<a[^>]*data-track=\"click.assetDetails.keywordSelected-[^>]*>([a-zA-Z0-9]+)<"
    keywords = []
    for match in re.findall(regex, html):
        keywords.append(match)
    return keywords


def init_ui(root):
    root.geometry("500x500+500+500")

    f = Frame(root)
    f.pack(fill=BOTH, expand=True)

    frame1 = Frame(f)
    frame1.pack(fill=X)
    
    lbl1 = Label(frame1, text="Enter url here", width=6)
    lbl1.pack(side=LEFT, padx=5, pady=5)
       
    entry1 = Entry(frame1)
    entry1.pack(fill=X, padx=5, expand=True)
        
    frame3 = Frame(f)
    frame3.pack(fill=X)
        
    lbl3 = Label(frame3, text="Keywords", width=6)
    lbl3.pack(side=LEFT, anchor=N, padx=5, pady=5)        

    txt = Text(frame3)
    txt.pack(fill=BOTH, pady=5, padx=5, expand=True)

    def on_click():
        url = entry1.get()
        print url

        keywords = get_keywords(url)
        res = ", ".join(keywords)
        print res
        
        txt.delete("1.0", END)
        txt.insert("1.0", res)

    def on_click2():
        entry1.delete(0,END)
    
    frame2 = Frame(f)
    frame2.pack(fill=X)
    
    tk.Button(frame2, text="Get keywords", command=on_click).pack()
    tk.Button(frame2, text="Clear", command=on_click2).pack()

root = tk.Tk()
root.title("Shutterstock keywords")
init_ui(root)
tk.mainloop()
