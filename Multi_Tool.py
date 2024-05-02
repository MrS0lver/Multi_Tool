from tkinter import *
import threading
from tkinter import filedialog,font
import speech_recognition as sr
import pyttsx3 as pt
import webbrowser as wb
import qrcode as qr
from PIL import Image, ImageTk








class Main:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x500")
        self.root.title("Multi - Tool")



        self.qrcode_button = Button(self.root, text="Qrcode", font="Dungeon 16", command=self.open_qrcode)
        self.qrcode_button.pack(fill=BOTH, side=TOP, pady=10)

        self.notepad_button = Button(self.root, text="Smart Notepad", font="Dungeon 16", command=self.open_notepad)
        self.notepad_button.pack(fill=BOTH, side = TOP, pady = 10)

        self.spell = Button(self.root, text="Spell Corrector",font="Dungeon 16",command=self.open_spell)
        self.spell.pack(fill=BOTH, side=TOP,pady=10)
    
    def open_notepad(self):
        self.root.destroy()
        notepad_window = Notepad()
        notepad_window.open()

    def open_qrcode(self):
        self.root.destroy()
        qrcode_window = Qrcode()
        qrcode_window.open()

    def open_spell(self):
        self.root.destroy()
        spell = Spell()
        spell.open()


class Spell:
    def __init__(self):
        self.spell = Tk()
        self.spell.geometry("500x500")
        self.spell.title("Spell Corrector")

        self.label = Label(self.spell, text="Type your sentence/spelling here: ",font="Dungeon 17")
        self.label.pack(pady=5,fill=BOTH,side=TOP)
        self.text = Entry(self.spell, font = "consolas 20",bd=0)
        self.text.pack()
        self.button = Button(self.spell, text="Correct", font = "sonsolas 20")
        self.button.pack()
        self.label2 = Label(self.spell, font = "Dungeon 17")
        self.label2.pack(pady=5,fill=BOTH)


        def correction(self):
            pass









        self.spell.protocol("WM_DELETE_WINDOW",self.reopen)

    
    def open(self):
        self.spell.mainloop()
    
    def reopen(self):
        self.root = Tk()
        self.root.geometry("500x500")
        self.spell.destroy()
        obj = Main(self.root)


class Qrcode:
    def __init__(self):
        self.qrcode = Tk() # Create a Toplevel window for QR code
        self.qrcode.title("Qrcode Generator")
        self.qrcode.geometry("500x500")

        self.see = Label(self.qrcode, text="Paste Your Text or Link Here:", font = "Dungeon 20")
        self.see.pack(fill= BOTH, side = TOP, pady = 10)

        self.link = Entry(self.qrcode, font="consolas 16")
        self.link.pack(fill = BOTH)

        self.generate = Button(self.qrcode , text="Generate", font="Dungeon 16", command=self.generate)
        self.generate.pack()

        self.show = Label(self.qrcode)
        self.show.pack(pady=10)

        self.last = Label(self.qrcode)
        self.last.pack()
        self.qrcode.protocol("WM_DELETE_WINDOW",self.reopen)


    def generate(self):
        qro = qr.make(self.link.get())
        image_path = "CustomQR.png"
        qro.save(image_path)
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        self.show.config(image=photo)
        self.show.image = photo  #avoid garbage collection
        self.last.config(text="QRcode is Generated Sucessfully !\n Your Generated Image is Saved in your Working Directory with the name CustomQR.png")

    def open(self):
        self.qrcode.mainloop()
    def reopen(self):
        self.root = Tk()
        self.root.geometry("500x500")
        self.qrcode.destroy()
        obj = Main(self.root)
        #Re_Intilize



class Notepad:
    def __init__(self):
        self.root = Tk()
        self.root.title("SM Notepad")
        self.root.geometry("600x400")
        # self.root.iconbitmap("notepad.ico")
        self.root.protocol("WM_DELETE_WINDOW",self.reopen)

        self.text_area = Text(self.root, font=("Arial", 12))
        self.text_area.pack(fill=BOTH, expand=True)

        self.text_area.bind("<MouseWheel>", self.change_font_size)
        
        # self.text_area = tk.Text(self.root)
        # self.text_area.pack(fill=tk.BOTH, expand=True)

        #Files
        self.menu_bar = Menu(self.root)
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        #Edit
        self.edit_menu = Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Paste", command=self.paste_text)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        #Font :)
        self.Font_menu = Menu(self.edit_menu, tearoff=0)
        self.Font_menu.add_command(label="Consolas", command=self.consolas)
        self.Font_menu.add_command(label="Candara", command=self.candara)
        self.Font_menu.add_command(label="Castellar", command=self.castellar)
        self.Font_menu.add_command(label="Chiller", command=self.chiller)
        self.Font_menu.add_command(label="Harrington", command=self.harrington)
        
        
        self.menu_bar.add_cascade(label="Fonts", menu=self.Font_menu)
        #Task (Speak & Read)
        self.voice_menu = Menu(self.edit_menu, tearoff=0)
        self.voice_menu.add_command(label="Speak & Write", command=self.voice_writing)
        self.voice_menu.add_separator()
        self.voice_menu.add_command(label="Read", command=self.read)
        self.menu_bar.add_cascade(label="Task", menu=self.voice_menu)
        #Contact us 
        self.contact_menu = Menu(self.edit_menu, tearoff=0)
        self.contact_menu.add_command(label="Twitter", command=self.Instagram)
        self.contact_menu.add_command(label="GitHub", command=self.github)
        self.menu_bar.add_cascade(label="Contact", menu=self.contact_menu)

        self.root.config(menu=self.menu_bar)
    def harrington(self):
        self.text_area.config(font=("Harrington"))
    def chiller(self):
        self.text_area.config(font=("Chiller"))
    def castellar(self):
        self.text_area.config(font=("castellar"))
    def candara(self):
        self.text_area.config(font=("Candara"))
    def consolas(self):
        self.text_area.config(font=("consolas"))
    def change_font_size(self, event):
        current_font = font.Font(font=self.text_area["font"])
        size = current_font.actual()["size"]
        if event.delta > 0:
            size += 2
        else:
            size -= 2
        if size < 8:
            size = 8
        self.text_area.configure(font=("Arial", size))
    def Instagram(self):
        wb.open_new("https://twitter.com/Mrs0lver")
    def github(self):
        wb.open_new("https://github.com/MrS0lver")
    
    def read(self):
        threading.Thread(target=self.read_func,daemon=True).start()
    def read_func(self):
        eng = pt.init()
        eng.getProperty('rate')
        eng.setProperty('rate',145)
        eng.say(self.text_area.get('1.0','end-1c'))
        eng.runAndWait()
    
    def voice_writing(self):
        threading.Thread(target=self.voice_write,daemon=True).start()

    def voice_write(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(text)
            self.text_area.insert(END, text + " ")
        except sr.UnknownValueError:
            self.text_area.insert(END, "Could not understand audio")
        except sr.RequestError:
            self.text_area.insert(END, "Could not request results from Google Speech Recognition")

    def new_file(self):
        self.text_area.delete("1.0", END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete("1.0", END)
                self.text_area.insert(END, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get("1.0", END))

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get("1.0", END))

    def cut_text(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.text_area.get("sel.first", "sel.last"))
        self.text_area.delete("sel.first", "sel.last")

    def copy_text(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.text_area.get("sel.first", "sel.last"))

    def paste_text(self):
        self.text_area.insert(INSERT, self.root.clipboard_get())
    def open(self):
        self.root.mainloop()
    def reopen(self):
        self.new = Tk()
        self.root.destroy()
        obj = Main(self.new)

if __name__ == "__main__":
    win = Tk()
    obj = Main(win)
    win.mainloop()
