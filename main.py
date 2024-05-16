import fitz # PyMuPDF
from tkinter import *
from tkinter import filedialog
 
 
def open_pdf():
    file_path = filedialog.askopenfilename(initialdir="/",    title="Select a PDF file",
filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*")))
 
 
    if file_path:
        pdf_viewer = fitz.open(file_path)
        page = pdf_viewer.load_page(0) # Load the first page
 
 
        img = page.get_pixmap()
        img.save("temp.png") # Convert the page to a temporary image file
 
 
        img_data = PhotoImage(file="temp.png")
        img_label = Label(canvas, image=img_data)
        img_label.image = img_data # Keep a reference
 
 
        # Delete the temporary image file when a new PDF is opened
        root.protocol("WM_DELETE_WINDOW",
                      lambda: [img_data.blank(), img_data, img_label, pdf_viewer.close(), root.destroy()])
 
 
        # Add a canvas for scrolling and center it
        canvas.create_window((0, 0), window=img_label, anchor="center")
        canvas.config(scrollregion=canvas.bbox("all"))
 
 
# Create the main tkinter window
root = Tk()
root.title("Simple PDF Viewer - The Pycodes")
root.geometry("620x600")
 
 
# Create an "Open PDF" button
open_button = Button(root, text="Open PDF", command=open_pdf, width=20, font="Arial 16", bd=4, relief=RAISED)
open_button.pack(pady=10)
 
 
# Create a canvas and scrollbar for scrolling
canvas = Canvas(root)
canvas.pack(fill=BOTH, expand=True)
 
 
scrollbar = Scrollbar(canvas, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)
 
 
canvas.config(yscrollcommand=scrollbar.set)
 
 
# Start the tkinter main loop
root.mainloop()
