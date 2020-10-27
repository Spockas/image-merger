from tkinter import *
from tkinter import messagebox, font, filedialog
from PIL import ImageTk
import merger as mg
import time


class Kintamieji:
    def __init__(self):
        sides = 0
        vertically = 0
        bigger = 0
        smaller = 0
        size = 600


K = Kintamieji()
merger = mg.Merger()


class ProgramInterface(Frame):
    def __init__(self):
        Frame.__init__(self)
        frame = Frame()
        sides = 80
        vertically = 80
        merger.move_down(vertically)
        merger.move_right(sides)
        # Pavadinimas lango
        self.master.title('Design applier')
        # Dydis lango
        self.master.geometry("600x480+500+200")
        # Background spalva
        frame.configure(bg="#D0D0D0")
        #  Fonto aprasimas
        font11 = font.Font(family="Yu Gothic", size=11, weight='bold')
        #  Talpinimo budas
        frame.pack(fill="both", expand=True)

        # Vieta ieskoti drabozio paveiksliukui
        self.pict_cloth_Entry = Entry(frame, width=34, bg="white")
        self.pict_cloth_Entry.place(x=266, y=23)

        def picture_in_GUI():
            try:
                self.img = ImageTk.PhotoImage(image=merger.get_display())
                self.panel = Label(frame, image=self.img)
                self.panel.place(x=25, y=110)
            except:
                messagebox.showerror("Error", "Mistake in directory to picture")

        # Kas atsitinka kai paspaudi Save prie Location of picture with clothing
        def click_pict_cloth(event):
            try:
                hoodie_path = str(self.pict_cloth_Entry.get())
                if not merger.set_main_image(hoodie_path):
                    messagebox.showerror("Error", "Can't read this file. Is directory right?")
            except:
                messagebox.showerror("Error", "Mistake in directory to clothing png")

        # Migtukas patvirtinti drabuzio paveiksliukui
        self.pict_cloth_Button = Button(frame, text="Save", font=font11)
        self.pict_cloth_Button.bind("<ButtonRelease-1>", click_pict_cloth)
        self.pict_cloth_Button.place(x=540, y=17)

        # Function for button allowing to use OS selection for file
        def select_file_location(event):
            pic_file_name = filedialog.askopenfilename(title="Select picture of clothing")
            # self.pict_cloth_Entry.config(text=pic_file_name)
            self.pict_cloth_Entry.delete(0, len(str(self.pict_cloth_Entry.get())))
            self.pict_cloth_Entry.insert(0, pic_file_name)

        # Button to select file location
        self.pict_cloth_file = Button(frame, text="Select", font=font11)
        self.pict_cloth_file.bind("<ButtonRelease-1>", select_file_location)
        self.pict_cloth_file.place(x=476, y=17)

        # Kas atsitinka kai paspaudi Save prie Location of folder with designs:
        def click_fold_desi(event):
            try:
                design_path = str(self.fold_desi_Entry.get())
                merger.set_design_folder(design_path)
                merger.resize_to_set_size(quality=True)
                picture_in_GUI()
            except Exception as ex:
                print(ex)
                messagebox.showerror("Error", "Mistake in directory to folder with designs")

        def select_folder_location(event):
            pic_file_name = filedialog.askdirectory(title="Select folder with designs")
            self.fold_desi_Entry.delete(0, len(str(self.fold_desi_Entry.get())))
            self.fold_desi_Entry.insert(0, pic_file_name)

        # Vieta pasirinkti dizainu folderi
        self.fold_desi_Entry = Entry(frame, width=34, bg="white")
        self.fold_desi_Entry.place(x=265, y=64)

        # Mygtukas issaugoti dizainu folderi
        self.fold_desi_Button = Button(frame, text="Save", font=font11)
        self.fold_desi_Button.bind("<ButtonRelease-1>", click_fold_desi)
        self.fold_desi_Button.place(x=540, y=53)

        self.opacity_Entry = Entry(frame, width=3, bg="white")
        self.opacity_Entry.insert(END, '220')
        self.opacity_Entry.place(x=425, y=124)

        # Button to select designs folder location
        self.pict_cloth_file = Button(frame, text="Select", font=font11)
        self.pict_cloth_file.bind("<ButtonRelease-1>", select_folder_location)
        self.pict_cloth_file.place(x=476, y=53)

        # Rodykles
        def click_left_arrow(event):
            try:
                merger.move_left(int(self.Pix_move_Entry.get()))
                picture_in_GUI()
            except:
                messagebox.showerror("Error", "Couldn't move design to the left")

        self.left_arrow_key = Button(frame, text="←", font=font11)
        self.left_arrow_key.bind("<ButtonRelease-1>", click_left_arrow)
        self.left_arrow_key.place(x=395, y=300)

        def click_right_arrow(event):
            try:
                merger.move_right(int(self.Pix_move_Entry.get()))
                picture_in_GUI()
            except:
                messagebox.showerror("Error", "Couldn't move design to the right")

        self.right_arrow_key = Button(frame, text="→", font=font11)
        self.right_arrow_key.bind("<ButtonRelease-1>", click_right_arrow)
        self.right_arrow_key.place(x=455, y=300)

        def click_up_arrow(event):
            try:
                merger.move_up(int(self.Pix_move_Entry.get()))
                picture_in_GUI()
            except:
                messagebox.showerror("Error", "Couldn't move design to the up")

        self.up_arrow_key = Button(frame, text="↑", font=font11)
        self.up_arrow_key.bind("<ButtonRelease-1>", click_up_arrow)
        self.up_arrow_key.place(x=425, y=265)

        def click_down_arrow(event):
            try:
                merger.move_down(int(self.Pix_move_Entry.get()))
                picture_in_GUI()
            except:
                messagebox.showerror("Error", "Couldn't move design to the down")

        self.down_arrow_key = Button(frame, text="↓", font=font11)
        self.down_arrow_key.bind("<ButtonRelease-1>", click_down_arrow)
        self.down_arrow_key.place(x=425, y=335)

        # Priartinimo/ tolinimo migtukai
        def click_plus(event):
            try:
                merger.increase_size(size=int(self.Design_size_Entry.get()))
                picture_in_GUI()
            except:
                messagebox.showerror("Error", "Couldn't increase design")

        self.plus_key = Button(frame, text="+", font=font11, width=2)
        self.plus_key.bind("<ButtonRelease-1>", click_plus)
        self.plus_key.place(x=390, y=180)

        def click_minus(event):
            try:
                merger.decrease_size(size=int(self.Design_size_Entry.get()))
                picture_in_GUI()
            except:
                messagebox.showerror("Error", "Couldn't reduce design")

        self.minus_key = Button(frame, text="-", font=font11, width=2)
        self.minus_key.bind("<ButtonRelease-1>", click_minus)
        self.minus_key.place(x=460, y=180)

        def Start(event):
            try:
                start = time.time()
                print((time.time() - start))
                print("Merging all starts")
                start = time.time()
                merger.merge_all(opacity=int(self.opacity_Entry.get()))
                print("{:.1f}".format(time.time() - start), "Seconds")
            except:
                messagebox.showerror("Error", "Couldn't start script (All)")

        self.up_arrow_key = Button(frame, text="Merge all", font=font11)
        self.up_arrow_key.bind("<ButtonRelease-1>", Start)
        self.up_arrow_key.place(x=480, y=430)

        def Amount(event):
            try:
                start = time.time()
                print((time.time() - start))
                print("Testing some starts")
                start = time.time()
                merger.merge_all(opacity=int(self.opacity_Entry.get()), maxi=int(self.Set_amount.get()))
                print("{:.1f}".format(time.time() - start), "Seconds")
            except:
                messagebox.showerror("Error", "Couldn't start script (Set amount)")

        self.Set_amount = Entry(frame, width=3, bg="white")
        self.Set_amount.insert(END, '2')
        self.Set_amount.place(x=320, y=435)

        self.Button_amount = Button(frame, text="Set amount", font=font11)
        self.Button_amount.bind("<ButtonRelease-1>", Amount)
        self.Button_amount.place(x=350, y=430)

        # Kiek pixelių pajudinti
        self.Pix_move_Entry = Entry(frame, width=4, bg="white")
        self.Pix_move_Entry.insert(END, '100')
        self.Pix_move_Entry.place(x=425, y=305)

        # Kiek pixelių padidės/sumažės
        self.Design_size_Entry = Entry(frame, width=4, bg="white")
        self.Design_size_Entry.insert(END, '100')
        self.Design_size_Entry.place(x=425, y=187)

        # Drabuzio tekstas ir jo vieta
        self.pict_cloth = Label(frame, text="Location of picture with clothing:", bg="#D0D0D0", font=font11)
        self.pict_cloth.place(x=20, y=20)

        # Dizaino tekstas ir jo vieta
        self.fold_desi = Label(frame, text="Location of folder with designs:", bg="#D0D0D0", font=font11)
        self.fold_desi.place(x=20, y=60)

        # Tekstas
        self.Info1 = Label(frame, text="Increase/decrease design with +/-", bg="#D0D0D0", font=font11)
        self.Info1.place(x=330, y=215)

        # Tekstas
        self.Info = Label(frame, text="Move design with arrow keys", bg="#D0D0D0", font=font11)
        self.Info.place(x=330, y=375)

        self.Info1 = Label(frame, text="Set opacity", bg="#D0D0D0", font=font11)
        self.Info1.place(x=395, y=145)


def Gui():
    ProgramInterface().mainloop()


def main():
    Gui()


main()
