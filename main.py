import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog
from PIL import Image, ImageTk
from capture import take_picture
from upload import upload_image
from convert import convert_image_to_text
from docx import Document  

class OCRApp:
    def __init__(self, master):
        self.master = master
        master.title("Optical Character Recognission Project")
        master.geometry("1300x700")  

        # Left Frame for Buttons
        self.left_frame = tk.Frame(master, bg='#bcd1c4')
        self.left_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.Y)

        # Define button width
        button_width = 20

        # Button for Taking Picture
        self.take_picture_button = tk.Button(self.left_frame, text="Take Picture", command=self.take_picture, 
                                             bg='#4CAF50', fg='white', font=('Arial', 12), width=button_width)
        self.take_picture_button.pack(pady=5)

        # Button for Uploading Image
        self.upload_button = tk.Button(self.left_frame, text="Upload", command=self.upload, 
                                       bg='#2196F3', fg='white', font=('Arial', 12), width=button_width)
        self.upload_button.pack(pady=5)

        # Button for Converting Image
        self.convert_button = tk.Button(self.left_frame, text="Convert", command=self.convert, 
                                         bg='#FF9800', fg='white', font=('Arial', 12), width=button_width)
        self.convert_button.pack(pady=5)

        # Button for Saving Extracted Text
        self.save_button = tk.Button(self.left_frame, text="Save Text", command=self.save_text, 
                                      bg='#9C27B0', fg='white', font=('Arial', 12), width=button_width)
        self.save_button.pack(pady=5)

        # Left Panel for Image Display
        self.image_label = tk.Label(master, text="Your image will appear here", bg='#f0f0f0', fg='#777', font=('Arial', 16))
        self.image_label.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Middle Panel for Tex Area
        self.text_area = tk.Text(master, wrap=tk.WORD, width=50, height=50, font=('Arial', 12), bg='#f9f9f9', fg='#333')
        self.text_area.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

    def take_picture(self):
        image = take_picture()
        if image is not None:
            self.display_image(image)

    def upload(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            image = upload_image(file_path)
            self.display_image(image)

    def convert(self):
        if hasattr(self, 'current_image'):
            text = convert_image_to_text(self.current_image)
            self.text_area.delete(1.0, tk.END)  
            self.text_area.insert(tk.END, text)  
        else:
            messagebox.showerror("Error", "No image to convert.")

    def save_text(self):
        if self.text_area.get(1.0, tk.END).strip():
            file_name = simpledialog.askstring("Save Text", "Enter the file name (without extension):")
            if file_name:
                file_path = filedialog.asksaveasfilename(defaultextension=".docx", initialfile=file_name, 
                                                           filetypes=[("Word files", "*.docx"), ("All files", "*.*")])
                if file_path:
                    doc = Document()
                    doc.add_paragraph(self.text_area.get(1.0, tk.END).strip())  
                    doc.save(file_path)  # Save the document
                    messagebox.showinfo("Success", "Text saved successfully!")
        else:
            messagebox.showerror("Error", "No text to save.")

    def display_image(self, image):
        self.current_image = image 
        img = Image.fromarray(image)
        img = img.resize((300, 300))  # Adjust size as needed
        img_tk = ImageTk.PhotoImage(img)
        self.image_label.configure(image=img_tk)
        self.image_label.image = img_tk 

if __name__ == "__main__":
    root = tk.Tk()
    app = OCRApp(root)
    root.mainloop()
