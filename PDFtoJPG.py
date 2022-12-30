import fitz
import os
import tkinter as tk
from tkinter import filedialog


def browse_file():
    file_path = filedialog.askopenfilename()
    if os.path.exists("Output"):
        os.chdir("Output")
        for file in os.listdir():
            if os.path.isfile(file) and os.path.exists(file):
                os.unlink(file)
        os.chdir("..")

    doc = fitz.open(
        file_path)
    for page in doc:
        pix = page.get_pixmap(matrix=fitz.Identity, dpi=None,
                              colorspace=fitz.csRGB, clip=None, alpha=False, annots=True)
        if not os.path.exists("Output"):
            os.makedirs("Output")

        pix.save("Output/Page-%i.jpg" % page.number)  # save file
    root.destroy()


root = tk.Tk()
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack()
label = tk.Label(root)
label.pack()
root.mainloop()
