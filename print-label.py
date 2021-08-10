import tkinter as tk
import win32print
import win32api
import time

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='PrintStop Label Print')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Order Number:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

def win_print(filename):
	 win32api.ShellExecute(0, "print", filename, None,  ".",  0)

def printLabelInvoice (event):
    
    x1 = entry1.get()
    
    # all_printers = [printer[2] for printer in win32print.EnumPrinters(2)]
    pdf_path = "\\\\psnas1\\W2P\\hot_folder\\orders\\invoice\\"+ x1 +".pdf"
    #pdf_path = "E:/printstop/img/invoice/"+ x1 +".pdf"	
    win32print.SetDefaultPrinter("HP LaserJet 1020")
    default_printer = win32print.GetDefaultPrinter()
    pHandle = win32print.OpenPrinter(default_printer, None)
    properties = win32print.GetPrinter(pHandle, 1)
    win32api.ShellExecute(0, "print", pdf_path, None,  ".",  0)
    time.sleep(2)
    win32print.ClosePrinter(pHandle)
    label4 = tk.Label(root, text= properties,font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 210, window=label4)

    label_path = "\\\\psnas1\\W2P\\hot_folder\\orders\\label\\" + x1 + ".pdf"
    #label_path = "E:/printstop/img/labels/" + x1 + ".pdf"	
    win32print.SetDefaultPrinter("Citizen CL-S621 #2")
    default2_printer = win32print.GetDefaultPrinter()
    p2Handle = win32print.OpenPrinter(default2_printer , None)
    properties = win32print.GetPrinter(p2Handle, 2)
    win32api.ShellExecute(0, "print", label_path, None,  ".",  0)
    win32print.ClosePrinter(p2Handle)

    label5 = tk.Label(root, text= win32print.GetDefaultPrinter(),font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 230, window=label5)
    entry1.delete(0, 'end')
    entry1.focus()
    
# button1 = tk.Button(text='Print', command=printLabelInvoice, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
# canvas1.create_window(200, 180, window=button1)
root.bind('<Return>', printLabelInvoice)

root.mainloop()