import traceback
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
        # GUi title
        self.master.title('Design applier')
        # Gui size
        self.master.geometry("610x540+500+200")
        #Gui always-on-top
        self.master.wm_attributes("-topmost", 1)
        self.master.resizable(0, 0)
        # Background color
        frame.configure(bg="#D0D0D0")
        #  Font description
        font11 = font.Font(family="Yu Gothic", size=11, weight='bold')
        #  Packing decision
        frame.pack(fill="both", expand=True)

        # Entry for cloth.png
        self.pict_cloth_Entry = Entry(frame, width=34, bg="white")
        self.pict_cloth_Entry.place(x=266, y=23)

        def picture_in_GUI():
            try:
                self.img = ImageTk.PhotoImage(image=merger.get_display())
                self.panel = Label(frame, image=self.img)
                self.panel.place(x=25, y=110)
            except:
                messagebox.showerror("Error", "Mistake in directory to picture")

        # Function for clicking Save cloth
        def click_pict_cloth(event):
            try:
                hoodie_path = str(self.pict_cloth_Entry.get())
                merger.open_main_image_folder(hoodie_path) # return
            except:
                messagebox.showerror("Error", "Mistake in directory to clothing png")

        # Button to confirm cloth.png
        self.pict_cloth_Button = Button(frame, text="Save", font=font11)
        self.pict_cloth_Button.bind("<ButtonRelease-1>", click_pict_cloth)
        self.pict_cloth_Button.place(x=540, y=17)

        # Function for button allowing to use OS selection for file
        def select_file_location(event):
            pic_file_name = filedialog.askdirectory(title="Select folder with pictures of clothing")
            # self.pict_cloth_Entry.config(text=pic_file_name)
            self.pict_cloth_Entry.delete(0, len(str(self.pict_cloth_Entry.get())))
            self.pict_cloth_Entry.insert(0, pic_file_name)

        # Button to select file location
        self.pict_cloth_file = Button(frame, text="Select", font=font11)
        self.pict_cloth_file.bind("<ButtonRelease-1>", select_file_location)
        self.pict_cloth_file.place(x=476, y=17)

        # Function which happens after clicking save design folder
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

        # Entry for design folder
        self.fold_desi_Entry = Entry(frame, width=34, bg="white")
        self.fold_desi_Entry.place(x=265, y=64)

        # Button to save design folder
        self.fold_desi_Button = Button(frame, text="Save", font=font11)
        self.fold_desi_Button.bind("<ButtonRelease-1>", click_fold_desi)
        self.fold_desi_Button.place(x=540, y=53)

        # Function on button "Set"
        def opacity_set(event):
            try:
                merger.change_opacity(opacity=int(self.opacity_Entry.get()))
                picture_in_GUI()
            except Exception as ex:
                print(ex)
                messagebox.showerror("Error", "Mistake in setting opacity")

        # Button for setting opacity
        self.opacity_Button = Button(frame, text="Set", font=font11)
        self.opacity_Button.bind("<ButtonRelease-1>", opacity_set)
        self.opacity_Button.place(x=445, y=122)

        # Opacity entry
        self.opacity_Entry = Entry(frame, width=3, bg="white")
        self.opacity_Entry.insert(END, str(merger.opacity))
        self.opacity_Entry.place(x=415, y=130)

        # Button to select designs folder location
        self.pict_cloth_file = Button(frame, text="Select", font=font11)
        self.pict_cloth_file.bind("<ButtonRelease-1>", select_folder_location)
        self.pict_cloth_file.place(x=476, y=53)

        # Arrows to move design on cloth
        def click_left_arrow(event):
            try:
                merger.move_left(int(self.Pix_move_Entry.get()))
                picture_in_GUI()
            except:
                messagebox.showerror("Error", "Couldn't move design to the left")

        self.left_arrow_key = Button(frame, text="←", font=font11)
        self.left_arrow_key.bind("<ButtonRelease-1>", click_left_arrow)
        self.left_arrow_key.place(x=405, y=310)

        def click_right_arrow(event):
            try:
                merger.move_right(int(self.Pix_move_Entry.get()))
                picture_in_GUI()
            except:
                messagebox.showerror("Error", "Couldn't move design to the right")

        self.right_arrow_key = Button(frame, text="→", font=font11)
        self.right_arrow_key.bind("<ButtonRelease-1>", click_right_arrow)
        self.right_arrow_key.place(x=465, y=310)

        def click_up_arrow(event):
            try:
                merger.move_up(int(self.Pix_move_Entry.get()))
                picture_in_GUI()
            except:
                messagebox.showerror("Error", "Couldn't move design to the up")

        self.up_arrow_key = Button(frame, text="↑", font=font11)
        self.up_arrow_key.bind("<ButtonRelease-1>", click_up_arrow)
        self.up_arrow_key.place(x=435, y=275)

        def click_down_arrow(event):
            try:
                merger.move_down(int(self.Pix_move_Entry.get()))
                picture_in_GUI()
            except:
                messagebox.showerror("Error", "Couldn't move design to the down")

        self.down_arrow_key = Button(frame, text="↓", font=font11)
        self.down_arrow_key.bind("<ButtonRelease-1>", click_down_arrow)
        self.down_arrow_key.place(x=435, y=345)

        # Buttons to increase/decrease design size
        def click_plus(event):
            try:
                merger.increase_size(size=int(self.Design_size_Entry.get()))
                picture_in_GUI()
            except:
                messagebox.showerror("Error", "Couldn't increase design")

        self.plus_key = Button(frame, text="+", font=font11, width=2)
        self.plus_key.bind("<ButtonRelease-1>", click_plus)
        self.plus_key.place(x=400, y=190)

        def click_minus(event):
            try:
                merger.decrease_size(size=int(self.Design_size_Entry.get()))
                picture_in_GUI()
            except:
                messagebox.showerror("Error", "Couldn't reduce design")

        self.minus_key = Button(frame, text="-", font=font11, width=2)
        self.minus_key.bind("<ButtonRelease-1>", click_minus)
        self.minus_key.place(x=470, y=190)

        def Start(event):
            try:
                start = time.time()
                print((time.time() - start))
                print("Merging all starts")
                start = time.time()
                merger.merge_all(opacity=int(self.opacity_Entry.get()), maxi=0)
                print("{:.1f}".format(time.time() - start), "Seconds")
                picture_in_GUI()
            except:
                messagebox.showerror("Error", "Couldn't start script (All)")

        self.up_arrow_key = Button(frame, text="Merge all", font=font11)
        self.up_arrow_key.bind("<ButtonRelease-1>", Start)
        self.up_arrow_key.place(x=490, y=440)

        def Amount(event):
            try:
                start = time.time()
                print((time.time() - start))
                print("Testing some starts")
                start = time.time()
                merger.merge_all(opacity=int(self.opacity_Entry.get()), maxi=int(self.Set_amount.get()))
                print("{:.1f}".format(time.time() - start), "Seconds")
            except Exception as e:
                messagebox.showerror("Error", "Couldn't start script (Set amount)")

        self.Set_amount = Entry(frame, width=3, bg="white")
        self.Set_amount.insert(END, '0')
        self.Set_amount.place(x=330, y=445)

        self.Button_amount = Button(frame, text="Set amount", font=font11)
        self.Button_amount.bind("<ButtonRelease-1>", Amount)
        self.Button_amount.place(x=360, y=440)

        # Default amount of pixels to move design
        self.Pix_move_Entry = Entry(frame, width=4, bg="white")
        self.Pix_move_Entry.insert(END, '100')
        self.Pix_move_Entry.place(x=435, y=315)

        # Default amount of pixels to increase/decrease design size
        self.Design_size_Entry = Entry(frame, width=4, bg="white")
        self.Design_size_Entry.insert(END, '100')
        self.Design_size_Entry.place(x=435, y=197)

        # Text label for cloth
        self.pict_cloth = Label(frame, text="Location of folder with clothing:", bg="#D0D0D0", font=font11)
        self.pict_cloth.place(x=20, y=20)

        # Text label for design
        self.fold_desi = Label(frame, text="Location of folder with designs:", bg="#D0D0D0", font=font11)
        self.fold_desi.place(x=20, y=60)

        # Text label for increase/decrease design
        self.Info1 = Label(frame, text="Increase/decrease design with +/-", bg="#D0D0D0", font=font11)
        self.Info1.place(x=330, y=225)

        # Text label for moving design
        self.Info = Label(frame, text="Move design with arrow keys", bg="#D0D0D0", font=font11)
        self.Info.place(x=340, y=385)

        # Text label for setting opacity
        self.Info1 = Label(frame, text="Set opacity", bg="#D0D0D0", font=font11)
        self.Info1.place(x=405, y=155)


def Gui():
    ProgramInterface().mainloop()


def main():
    Gui()


main()
