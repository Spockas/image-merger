import PIL
from tkinter import *
from tkinter import messagebox, font
from PIL import ImageTk, Image
from merger import merger as mg

class program_interface(Frame):
    def __init__(self):
            Frame.__init__(self)
            frame = Frame()
            Clothing = ''
            Designs = ''

            merger = mg.Merger()

            # Pavadinimas lango
            self.master.title('Image Combo Maker')

            # Dydis lango
            self.master.geometry("600x480+500+200")

            # Background spalva
            frame.configure(bg="#FF0066")

            #  Fonto aprasimas
            font11 = font.Font(family="Yu Gothic", size=11, weight='bold')
            #  Talpinimo budas
            frame.pack(fill="both", expand=True)
            # self.background = PhotoImage(file="Background.png")
            # self.background_label = Label(frame, image=self.background)
            # self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

            # Vieta ieskoti drabozio paveiksliukui
            self.pict_cloth_Entry = Entry(frame, width=39, bg="white")
            self.pict_cloth_Entry.place(x=300, y=23)

            def picture_in_GUI(Clothing):
                try:
                    self.img = PhotoImage(file=Clothing)
                    self.img = self.img.zoom(6)
                    self.img = self.img.subsample(32)
                    self.panel = Label(frame, image=self.img)
                    self.panel.place(x=15, y=130)
                    # frame.after(10000, picture_in_GUI)
                except:
                    messagebox.showerror("Error", "Mistake in directory to picture")


            #Kas atsitinka kai paspaudi Save prie Location of picture with clothing
            def click_pict_cloth(event):
                Clothing = str(self.pict_cloth_Entry.get())
                picture_in_GUI(Clothing)

            #Migtukas patvirtinti drabuzio paveiksliukui
            self.pict_cloth_Button = Button(frame, text="Save", font=font11)
            self.pict_cloth_Button.bind("<Button-1>", click_pict_cloth)
            self.pict_cloth_Button.place(x=540, y=17)

            #Kas atsitinka kai paspaudi Save prie Location of folder with designs:
            def click_fold_desi(event):
                try:
                    picture_in_GUI()

                except:
                    messagebox.showerror("Error", "Mistake in directory to folder with disigns")

            # Vieta pasirinkti dizainu folderi
            self.fold_desi_Entry = Entry(frame, width=39, bg="white")
            self.fold_desi_Entry.place(x=300, y=62)
            #Migtukas i6saugoti dizainu folderi
            self.fold_desi_Button = Button(frame, text="Save", font=font11)
            self.fold_desi_Button.bind("<Button-1>", click_fold_desi)
            self.fold_desi_Button.place(x=540, y=53)

            #Rodykles
            def click_left_arrow(event):
                try:
                    picture_in_GUI()

                except:
                    messagebox.showerror("Error", "Couldn't move design to the left")

            self.left_arrow_key = Button(frame, text="←", font=font11)
            self.left_arrow_key.bind("<Button-1>", click_left_arrow)
            self.left_arrow_key.place(x=395, y=300)

            def click_right_arrow(event):
                try:
                    picture_in_GUI()

                except:
                    messagebox.showerror("Error", "Couldn't move design to the right")

            self.right_arrow_key = Button(frame, text="→", font=font11)
            self.right_arrow_key.bind("<Button-1>", click_right_arrow)
            self.right_arrow_key.place(x=455, y=300)

            def click_up_arrow(event):
                try:
                    picture_in_GUI()

                except:
                    messagebox.showerror("Error", "Couldn't move design to the up")

            self.up_arrow_key = Button(frame, text="↑", font=font11)
            self.up_arrow_key.bind("<Button-1>", click_up_arrow)
            self.up_arrow_key.place(x=425, y=265)

            def click_down_arrow(event):
                try:
                    picture_in_GUI()

                except:
                    messagebox.showerror("Error", "Couldn't move design to the down")

            self.down_arrow_key = Button(frame, text="↓", font=font11)
            self.down_arrow_key.bind("<Button-1>", click_down_arrow)
            self.down_arrow_key.place(x=425, y=335)

            #Priartinimo/ tolinimo migtukai
            def click_plus(event):
                try:
                    picture_in_GUI()

                except:
                    messagebox.showerror("Error", "Couldn't increase design")

            self.plus_key = Button(frame, text="+", font=font11, width = 2)
            self.plus_key.bind("<Button-1>", click_plus)
            self.plus_key.place(x=400, y=180)

            def click_minus(event):
                try:
                    picture_in_GUI()

                except:
                    messagebox.showerror("Error", "Couldn't reduce design")

            self.minus_key = Button(frame, text="-", font=font11, width = 2)
            self.minus_key.bind("<Button-1>", click_minus)
            self.minus_key.place(x=450, y=180)

            # Drabuzio tekstas ir jo vieta
            self.pict_cloth = Label(frame, text="Location of picture with clothing:", bg="#FF0066", font=font11)
            self.pict_cloth.place(x=20, y=20)

            # Dizaino tekstas ir jo vieta
            self.fold_desi = Label(frame, text="Location of folder with designs:", bg="#FF0066", font=font11)
            self.fold_desi.place(x=20, y=60)

            # Tekstas
            self.Info1 = Label(frame, text="Increase/decrease design with +/-", bg="#FF0066", font=font11)
            self.Info1.place(x=330, y=215)

            # Tekstas
            self.Info = Label(frame, text="Move design with arrow keys", bg="#FF0066", font=font11)
            self.Info.place(x=330, y=375)

def Gui():
    program_interface().mainloop()


def main():
    Gui()


main()