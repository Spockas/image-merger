import traceback
from tkinter import *
from tkinter import messagebox, font, filedialog
from PIL import ImageTk
import merger as mg
import time


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
        self.master.geometry("910x685+500+200")
        # Gui always-on-top
        self.master.wm_attributes("-topmost", 1)
        self.master.resizable(0, 0)
        # Background color
        frame.configure(bg="#D0D0D0")
        #  Font description
        font11 = font.Font(family="Yu Gothic", size=11, weight='bold')
        #  Packing decision
        frame.pack(fill="both", expand=True)

        # Select cloths folder section:
        # Text label for cloth
        self.pict_cloth = Label(frame, text="Location of folder with clothing:", bg="#D0D0D0", font=font11)
        self.pict_cloth.place(x=20, y=20)

        # Entry for cloths folder
        self.pict_cloth_Entry = Entry(frame, width=34, bg="white")
        self.pict_cloth_Entry.place(x=266, y=23)

        # Function for clicking Save cloth
        def click_pict_cloth(event):
            try:
                hoodie_path = str(self.pict_cloth_Entry.get())
                merger.open_main_image_folder(hoodie_path)  # return
            except:
                messagebox.showerror("Error", "Mistake in directory to clothing png")

        # Button to confirm cloths folder
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

        # End of select cloths folder section
        # --------------------=--------------------

        # Select designs folder section:
        # Text label for design
        self.fold_desi = Label(frame, text="Location of folder with designs:", bg="#D0D0D0", font=font11)
        self.fold_desi.place(x=20, y=58)

        # Entry for design folder
        self.fold_desi_Entry = Entry(frame, width=34, bg="white")
        self.fold_desi_Entry.place(x=265, y=61)

        # Function which displays cloth and design on GUI
        def picture_in_GUI():
            try:
                self.img = ImageTk.PhotoImage(image=merger.get_display())
                self.panel = Label(frame, image=self.img)
                self.panel.place(x=25, y=110)
            except:
                messagebox.showerror("Error", "Mistake in directory to picture")

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

        # Button to save design folder
        self.fold_desi_Button = Button(frame, text="Save", font=font11)
        self.fold_desi_Button.bind("<ButtonRelease-1>", click_fold_desi)
        self.fold_desi_Button.place(x=540, y=53)

        # Function which happens after clicking select design folder
        def select_folder_location(event):
            pic_file_name = filedialog.askdirectory(title="Select folder with designs")
            self.fold_desi_Entry.delete(0, len(str(self.fold_desi_Entry.get())))
            self.fold_desi_Entry.insert(0, pic_file_name)

        # Button to select designs folder location
        self.pict_cloth_file = Button(frame, text="Select", font=font11)
        self.pict_cloth_file.bind("<ButtonRelease-1>", select_folder_location)
        self.pict_cloth_file.place(x=476, y=53)

        # End of select designs folder section
        # --------------------=--------------------

        # Set opacity section:
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
        self.opacity_Button.place(x=160, y=525)

        # Opacity entry
        self.opacity_Entry = Entry(frame, width=3, bg="white")
        self.opacity_Entry.insert(END, str(merger.opacity))
        self.opacity_Entry.place(x=130, y=531)

        # Text label for setting opacity
        self.Info1 = Label(frame, text="Set opacity", bg="#D0D0D0", font=font11)
        self.Info1.place(x=120, y=557)

        # End of set opacity section
        # --------------------=--------------------

        # Move design section:
        # Arrows to move design on cloth
        def click_left_arrow(event):
            try:
                merger.move_left(int(self.Pix_move_Entry.get()))
                picture_in_GUI()
            except:
                messagebox.showerror("Error", "Couldn't move design to the left")

        self.left_arrow_key = Button(frame, text="←", font=font11)
        self.left_arrow_key.bind("<ButtonRelease-1>", click_left_arrow)
        self.left_arrow_key.place(x=405, y=150)

        def click_right_arrow(event):
            try:
                merger.move_right(int(self.Pix_move_Entry.get()))
                picture_in_GUI()
            except:
                messagebox.showerror("Error", "Couldn't move design to the right")

        self.right_arrow_key = Button(frame, text="→", font=font11)
        self.right_arrow_key.bind("<ButtonRelease-1>", click_right_arrow)
        self.right_arrow_key.place(x=465, y=150)

        def click_up_arrow(event):
            try:
                merger.move_up(int(self.Pix_move_Entry.get()))
                picture_in_GUI()
            except:
                messagebox.showerror("Error", "Couldn't move design to the up")

        self.up_arrow_key = Button(frame, text="↑", font=font11)
        self.up_arrow_key.bind("<ButtonRelease-1>", click_up_arrow)
        self.up_arrow_key.place(x=435, y=115)

        def click_down_arrow(event):
            try:
                merger.move_down(int(self.Pix_move_Entry.get()))
                picture_in_GUI()
            except:
                messagebox.showerror("Error", "Couldn't move design to the down")

        self.down_arrow_key = Button(frame, text="↓", font=font11)
        self.down_arrow_key.bind("<ButtonRelease-1>", click_down_arrow)
        self.down_arrow_key.place(x=435, y=185)

        # Default amount of pixels to move design
        self.Pix_move_Entry = Entry(frame, width=4, bg="white")
        self.Pix_move_Entry.insert(END, '100')
        self.Pix_move_Entry.place(x=435, y=157)

        # Text label for moving design
        self.Info = Label(frame, text="Move design with arrow keys", bg="#D0D0D0", font=font11)
        self.Info.place(x=340, y=225)

        # End of move design section
        # --------------------=--------------------

        # Design size section:
        # Buttons to increase/decrease design size
        def click_plus(event):
            try:
                merger.increase_size(size=int(self.Design_size_Entry.get()))
                picture_in_GUI()
            except:
                messagebox.showerror("Error", "Couldn't increase design")

        self.plus_key = Button(frame, text="+", font=font11, width=2)
        self.plus_key.bind("<ButtonRelease-1>", click_plus)
        self.plus_key.place(x=115, y=595)

        def click_minus(event):
            try:
                merger.decrease_size(size=int(self.Design_size_Entry.get()))
                picture_in_GUI()
            except:
                messagebox.showerror("Error", "Couldn't reduce design")

        self.minus_key = Button(frame, text="-", font=font11, width=2)
        self.minus_key.bind("<ButtonRelease-1>", click_minus)
        self.minus_key.place(x=185, y=595)

        # Default amount of pixels to increase/decrease design size
        self.Design_size_Entry = Entry(frame, width=4, bg="white")
        self.Design_size_Entry.insert(END, '100')
        self.Design_size_Entry.place(x=150, y=602)

        # Text label for increase/decrease design
        self.Info1 = Label(frame, text="Increase/decrease design with +/-", bg="#D0D0D0", font=font11)
        self.Info1.place(x=50, y=630)

        # End of design size section
        # --------------------=--------------------

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
        self.up_arrow_key.place(x=800, y=595)

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
        self.Set_amount.place(x=630, y=600)

        self.Button_amount = Button(frame, text="Set amount", font=font11)
        self.Button_amount.bind("<ButtonRelease-1>", Amount)
        self.Button_amount.place(x=660, y=595)

        # Excel doc entries:
        #Excel Maker label
        # Text label for product type
        self.excel_maker = Label(frame, text="Excel Maker", bg="#D0D0D0", font=font11)
        self.excel_maker.place(x=410, y=260)

        # Text label for product type
        self.product_type = Label(frame, text="(A)Product type:", bg="#D0D0D0", font=font11)
        self.product_type.place(x=330, y=285)

        # Entry for product type
        self.product_type_Entry = Entry(frame, width=20, bg="white")
        self.product_type_Entry.place(x=455, y=289)

        # Text label for seller SKU
        self.seller_SKU = Label(frame, text="(B)Seller SKU:", bg="#D0D0D0", font=font11)
        self.seller_SKU.place(x=330, y=310)

        # Entry for seller SKU
        self.seller_SKU_Entry = Entry(frame, width=20, bg="white")
        self.seller_SKU_Entry.place(x=455, y=314)

        # Text label for brand name
        self.brand_name = Label(frame, text="(C)Brand name:", bg="#D0D0D0", font=font11)
        self.brand_name.place(x=330, y=335)

        # Entry for brand name
        self.brand_name_Entry = Entry(frame, width=20, bg="white")
        self.brand_name_Entry.place(x=455, y=339)

        # Text label for product name UK
        self.product_name_UK = Label(frame, text="(F)Prod. name UK:", bg="#D0D0D0", font=font11)
        self.product_name_UK.place(x=329, y=370)

        # Entry for product name UK
        self.product_name_UK_Entry = Entry(frame, width=20, bg="white")
        self.product_name_UK_Entry.place(x=475, y=374)

        # Text label for product name DE
        self.product_name_DE = Label(frame, text="(F)Prod. name DE:", bg="#D0D0D0", font=font11)
        self.product_name_DE.place(x=329, y=395)

        # Entry for product name DE
        self.product_name_DE_Entry = Entry(frame, width=20, bg="white")
        self.product_name_DE_Entry.place(x=475, y=399)

        # Text label for product name FR
        self.product_name_FR = Label(frame, text="(F)Prod. name FR:", bg="#D0D0D0", font=font11)
        self.product_name_FR.place(x=329, y=420)

        # Entry for product name FR
        self.product_name_FR_Entry = Entry(frame, width=20, bg="white")
        self.product_name_FR_Entry.place(x=475, y=424)

        # Text label for product name IT
        self.product_name_IT = Label(frame, text="(F)Prod. name IT:", bg="#D0D0D0", font=font11)
        self.product_name_IT.place(x=329, y=445)

        # Entry for product name IT
        self.product_name_IT_Entry = Entry(frame, width=20, bg="white")
        self.product_name_IT_Entry.place(x=475, y=449)

        # Text label for product name ES
        self.product_name_ES = Label(frame, text="(F)Prod. name ES:", bg="#D0D0D0", font=font11)
        self.product_name_ES.place(x=329, y=470)

        # Entry for product name ES
        self.product_name_ES_Entry = Entry(frame, width=20, bg="white")
        self.product_name_ES_Entry.place(x=475, y=474)

        # Text label for recommended browse node UK
        self.recommended_browse_node_UK = Label(frame, text="(G)Rec. BN UK:", bg="#D0D0D0", font=font11)
        self.recommended_browse_node_UK.place(x=329, y=503)

        # Entry for recommended browse node UK
        self.recommended_browse_node_UK_Entry = Entry(frame, width=20, bg="white")
        self.recommended_browse_node_UK_Entry.place(x=450, y=507)

        # Text label for recommended browse node DE
        self.recommended_browse_node_DE = Label(frame, text="(G)Rec. BN DE:", bg="#D0D0D0", font=font11)
        self.recommended_browse_node_DE.place(x=329, y=528)

        # Entry for recommended browse node DE
        self.recommended_browse_node_DE_Entry = Entry(frame, width=20, bg="white")
        self.recommended_browse_node_DE_Entry.place(x=450, y=532)

        # Text label for recommended browse node FR
        self.recommended_browse_node_FR = Label(frame, text="(G)Rec. BN FR:", bg="#D0D0D0", font=font11)
        self.recommended_browse_node_FR.place(x=329, y=553)

        # Entry for recommended browse node FR
        self.recommended_browse_node_FR_Entry = Entry(frame, width=20, bg="white")
        self.recommended_browse_node_FR_Entry.place(x=450, y=557)

        # Text label for recommended browse node IT
        self.recommended_browse_node_IT = Label(frame, text="(G)Rec. BN IT:", bg="#D0D0D0", font=font11)
        self.recommended_browse_node_IT.place(x=329, y=578)

        # Entry for recommended browse node FR
        self.recommended_browse_node_IT_Entry = Entry(frame, width=20, bg="white")
        self.recommended_browse_node_IT_Entry.place(x=450, y=582)

        # Text label for recommended browse node ES
        self.recommended_browse_node_ES = Label(frame, text="(G)Rec. BN ES:", bg="#D0D0D0", font=font11)
        self.recommended_browse_node_ES.place(x=329, y=602)

        # Entry for recommended browse node ES
        self.recommended_browse_node_ES_Entry = Entry(frame, width=20, bg="white")
        self.recommended_browse_node_ES_Entry.place(x=450, y=606)

        # Text label for material composition
        self.material_composition = Label(frame, text="(I)Mat comp.:", bg="#D0D0D0", font=font11)
        self.material_composition.place(x=620, y=20)

        # Entry for material composition
        self.material_composition_Entry = Entry(frame, width=20, bg="white")
        self.material_composition_Entry.place(x=750, y=23)

        # Text label for color map
        self.color_map = Label(frame, text="(J)Color map:", bg="#D0D0D0", font=font11)
        self.color_map.place(x=620, y=45)

        # Entry for color map
        self.color_map_Entry = Entry(frame, width=20, bg="white")
        self.color_map_Entry.place(x=750, y=49)

        # Text label for department
        self.color_map = Label(frame, text="(M)Department:", bg="#D0D0D0", font=font11)
        self.color_map.place(x=620, y=70)

        # Entry for department
        self.color_map_Entry = Entry(frame, width=20, bg="white")
        self.color_map_Entry.place(x=750, y=74)

        # Text label for standard price
        self.standard_price = Label(frame, text="(P)Stan. price:", bg="#D0D0D0", font=font11)
        self.standard_price.place(x=620, y=95)

        # Entry for standard price
        self.standard_price_Entry = Entry(frame, width=20, bg="white")
        self.standard_price_Entry.place(x=750, y=99)

        # Text label for other image url
        self.other_image_url = Label(frame, text="(S)Other img. url:", bg="#D0D0D0", font=font11)
        self.other_image_url.place(x=620, y=120)

        # Entry for other image url
        self.other_image_url_Entry = Entry(frame, width=20, bg="white")
        self.other_image_url_Entry.place(x=750, y=124)

        # Text label for bullet points UK 1
        self.bullet_points_UK_1 = Label(frame, text="1.", bg="#D0D0D0", font=font11)
        self.bullet_points_UK_1.place(x=620, y=177)

        # Entry for bullet points UK 1
        self.bullet_points_UK_Entry_1 = Entry(frame, width=19, bg="white")
        self.bullet_points_UK_Entry_1.place(x=640, y=180)

        # Text label for bullet points UK 2
        self.bullet_points_UK_2 = Label(frame, text="2.", bg="#D0D0D0", font=font11)
        self.bullet_points_UK_2.place(x=620, y=202)

        # Entry for bullet points UK 2
        self.bullet_points_UK_Entry_2 = Entry(frame, width=19, bg="white")
        self.bullet_points_UK_Entry_2.place(x=640, y=205)

        # Text label for bullet points UK 3
        self.bullet_points_UK_3 = Label(frame, text="(AR-AV)BPs UK:     3.", bg="#D0D0D0", font=font11)
        self.bullet_points_UK_3.place(x=620, y=152)

        # Entry for bullet points UK 3
        self.bullet_points_UK_Entry_3 = Entry(frame, width=19, bg="white")
        self.bullet_points_UK_Entry_3.place(x=778, y=155)

        # Text label for bullet points UK 4
        self.bullet_points_UK_4 = Label(frame, text="4.", bg="#D0D0D0", font=font11)
        self.bullet_points_UK_4.place(x=758, y=177)

        # Entry for bullet points UK 4
        self.bullet_points_UK_Entry_4 = Entry(frame, width=19, bg="white")
        self.bullet_points_UK_Entry_4.place(x=778, y=180)

        # Text label for bullet points UK 5
        self.bullet_points_UK_5 = Label(frame, text="5.", bg="#D0D0D0", font=font11)
        self.bullet_points_UK_5.place(x=758, y=202)

        # Entry for bullet points UK 5
        self.bullet_points_UK_Entry_5 = Entry(frame, width=19, bg="white")
        self.bullet_points_UK_Entry_5.place(x=778, y=205)

        # Text label for bullet points DE 1
        self.bullet_points_DE_1 = Label(frame, text="1.", bg="#D0D0D0", font=font11)
        self.bullet_points_DE_1.place(x=620, y=255)

        # Entry for bullet points DE 1
        self.bullet_points_DE_Entry_1 = Entry(frame, width=19, bg="white")
        self.bullet_points_DE_Entry_1.place(x=640, y=258)

        # Text label for bullet points DE 2
        self.bullet_points_DE_2 = Label(frame, text="2.", bg="#D0D0D0", font=font11)
        self.bullet_points_DE_2.place(x=620, y=280)

        # Entry for bullet points DE 2
        self.bullet_points_DE_Entry_2 = Entry(frame, width=19, bg="white")
        self.bullet_points_DE_Entry_2.place(x=640, y=283)

        # Text label for bullet points DE 3
        self.bullet_points_DE_3 = Label(frame, text="(AR-AV)BPs DE:     3.", bg="#D0D0D0", font=font11)
        self.bullet_points_DE_3.place(x=620, y=230)

        # Entry for bullet points DE 3
        self.bullet_points_DE_Entry_3 = Entry(frame, width=19, bg="white")
        self.bullet_points_DE_Entry_3.place(x=778, y=233)

        # Text label for bullet points DE 4
        self.bullet_points_DE_4 = Label(frame, text="4.", bg="#D0D0D0", font=font11)
        self.bullet_points_DE_4.place(x=758, y=255)

        # Entry for bullet points DE 4
        self.bullet_points_DE_Entry_4 = Entry(frame, width=19, bg="white")
        self.bullet_points_DE_Entry_4.place(x=778, y=258)

        # Text label for bullet points DE 5
        self.bullet_points_DE_5 = Label(frame, text="5.", bg="#D0D0D0", font=font11)
        self.bullet_points_DE_5.place(x=758, y=360)

        # Entry for bullet points DE 5
        self.bullet_points_DE_Entry_5 = Entry(frame, width=19, bg="white")
        self.bullet_points_DE_Entry_5.place(x=778, y=283)

        # Text label for bullet points FR 1
        self.bullet_points_FR_1 = Label(frame, text="1.", bg="#D0D0D0", font=font11)
        self.bullet_points_FR_1.place(x=620, y=330)

        # Entry for bullet points FR 1
        self.bullet_points_FR_Entry_1 = Entry(frame, width=19, bg="white")
        self.bullet_points_FR_Entry_1.place(x=640, y=336)

        # Text label for bullet points FR 2
        self.bullet_points_FR_2 = Label(frame, text="2.", bg="#D0D0D0", font=font11)
        self.bullet_points_FR_2.place(x=620, y=358)

        # Entry for bullet points FR 2
        self.bullet_points_FR_Entry_2 = Entry(frame, width=19, bg="white")
        self.bullet_points_FR_Entry_2.place(x=640, y=361)

        # Text label for bullet points FR 3
        self.bullet_points_FR_3 = Label(frame, text="(AR-AV)BPs FR:     3.", bg="#D0D0D0", font=font11)
        self.bullet_points_FR_3.place(x=620, y=308)

        # Entry for bullet points FR 3
        self.bullet_points_FR_Entry_3 = Entry(frame, width=19, bg="white")
        self.bullet_points_FR_Entry_3.place(x=778, y=311)

        # Text label for bullet points FR 4
        self.bullet_points_FR_4 = Label(frame, text="4.", bg="#D0D0D0", font=font11)
        self.bullet_points_FR_4.place(x=758, y=333)

        # Entry for bullet points FR 4
        self.bullet_points_FR_Entry_4 = Entry(frame, width=19, bg="white")
        self.bullet_points_FR_Entry_4.place(x=778, y=336)

        # Text label for bullet points FR 5
        self.bullet_points_FR_5 = Label(frame, text="5.", bg="#D0D0D0", font=font11)
        self.bullet_points_FR_5.place(x=758, y=358)

        # Entry for bullet points FR 5
        self.bullet_points_FR_Entry_5 = Entry(frame, width=19, bg="white")
        self.bullet_points_FR_Entry_5.place(x=778, y=361)

        # Text label for bullet points IT 1
        self.bullet_points_IT_1 = Label(frame, text="1.", bg="#D0D0D0", font=font11)
        self.bullet_points_IT_1.place(x=620, y=413)

        # Entry for bullet points IT 1
        self.bullet_points_IT_Entry_1 = Entry(frame, width=19, bg="white")
        self.bullet_points_IT_Entry_1.place(x=640, y=416)

        # Text label for bullet points IT 2
        self.bullet_points_IT_2 = Label(frame, text="2.", bg="#D0D0D0", font=font11)
        self.bullet_points_IT_2.place(x=620, y=438)

        # Entry for bullet points IT 2
        self.bullet_points_IT_Entry_2 = Entry(frame, width=19, bg="white")
        self.bullet_points_IT_Entry_2.place(x=640, y=441)

        # Text label for bullet points IT 3
        self.bullet_points_IT_3 = Label(frame, text="(AR-AV)BPs IT:      3.", bg="#D0D0D0", font=font11)
        self.bullet_points_IT_3.place(x=620, y=387)

        # Entry for bullet points IT 3
        self.bullet_points_IT_Entry_3 = Entry(frame, width=19, bg="white")
        self.bullet_points_IT_Entry_3.place(x=778, y=390)

        # Text label for bullet points IT 4
        self.bullet_points_IT_4 = Label(frame, text="4.", bg="#D0D0D0", font=font11)
        self.bullet_points_IT_4.place(x=758, y=413)

        # Entry for bullet points IT 4
        self.bullet_points_IT_Entry_4 = Entry(frame, width=19, bg="white")
        self.bullet_points_IT_Entry_4.place(x=778, y=416)

        # Text label for bullet points IT 5
        self.bullet_points_IT_5 = Label(frame, text="5.", bg="#D0D0D0", font=font11)
        self.bullet_points_IT_5.place(x=758, y=438)

        # Entry for bullet points IT 5
        self.bullet_points_IT_Entry_5 = Entry(frame, width=19, bg="white")
        self.bullet_points_IT_Entry_5.place(x=778, y=441)

        # Text label for bullet points ES 1
        self.bullet_points_ES_1 = Label(frame, text="1.", bg="#D0D0D0", font=font11)
        self.bullet_points_ES_1.place(x=620, y=494)

        # Entry for bullet points ES 1
        self.bullet_points_ES_Entry_1 = Entry(frame, width=19, bg="white")
        self.bullet_points_ES_Entry_1.place(x=640, y=497)

        # Text label for bullet points ES 2
        self.bullet_points_ES_2 = Label(frame, text="2.", bg="#D0D0D0", font=font11)
        self.bullet_points_ES_2.place(x=620, y=519)

        # Entry for bullet points ES 2
        self.bullet_points_ES_Entry_2 = Entry(frame, width=19, bg="white")
        self.bullet_points_ES_Entry_2.place(x=640, y=522)

        # Text label for bullet points ES 3
        self.bullet_points_ES_3 = Label(frame, text="(AR-AV)BPs ES:     3.", bg="#D0D0D0", font=font11)
        self.bullet_points_ES_3.place(x=620, y=469)

        # Entry for bullet points ES 3
        self.bullet_points_ES_Entry_3 = Entry(frame, width=19, bg="white")
        self.bullet_points_ES_Entry_3.place(x=778, y=472)

        # Text label for bullet points ES 4
        self.bullet_points_ES_4 = Label(frame, text="4.", bg="#D0D0D0", font=font11)
        self.bullet_points_ES_4.place(x=758, y=494)

        # Entry for bullet points ES 4
        self.bullet_points_ES_Entry_4 = Entry(frame, width=19, bg="white")
        self.bullet_points_ES_Entry_4.place(x=778, y=497)

        # Text label for bullet points ES 5
        self.bullet_points_ES_5 = Label(frame, text="5.", bg="#D0D0D0", font=font11)
        self.bullet_points_ES_5.place(x=758, y=519)

        # Entry for bullet points ES 5
        self.bullet_points_ES_Entry_5 = Entry(frame, width=19, bg="white")
        self.bullet_points_ES_Entry_5.place(x=778, y=522)

def Gui():
    ProgramInterface().mainloop()


def main():
    Gui()


main()