import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

my_font = customtkinter.CTkFont(family="Roboto", size=24)
my_font.configure(family="Name")

label = customtkinter.CTkLabel(master=frame, text="MURCURY", font=my_font)
label.pack(pady=12, padx=1)

# textbox = customtkinter.CTkTextbox()

root.mainloop()
