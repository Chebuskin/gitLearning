from tkinter import *
# bg '#282C34'
# light dark bg "#1d2025"
# dark bg '#121417'
#borders #0F1011

#listcolors =  ["#528BFF", "#ABB2BF", "#282C34", "#121417", "#1d2025", "#828997", "#5C6370", "#56B6C2", "#61AFEF", "#C678DD", "#98C379", "#E06C75", "#BE5046", "#D19A66", "#E5C07B", "#3E4451", "#AAAAAA", "#0F1011"]
root = Tk()
root.geometry("500x500")
frame = Frame(root, bg='#121417')
frame.pack(fill="both", expand=True)

inside = Frame(frame, bg='#282C34', bd = 0,relief = 'solid')
inside.config( highlightbackground="#000000",  highlightthickness=1)
inside.pack(fill="both", expand=True, padx=(150,30), pady=30)

ins = Frame(inside, bg='#ABB2BF', bd = 0,relief = 'solid')
ins.config( highlightbackground="#000000",  highlightthickness=1)
ins.pack(fill="both", expand=True, padx=(150,30), pady=30)

mainLabel = 

root.mainloop()
