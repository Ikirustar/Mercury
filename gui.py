import customtkinter
import main

class App(customtkinter.CTk):
    WIDTH = 680
    HEIGHT = 480

    def __init__(self):
        super().__init__()

        self.title("Mercury")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")

        self.checkbox_frame = customtkinter.CTkFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx=0, pady=0, sticky="nsw")

        #* OS-Bot frames

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(
            master=self,
            corner_radius=0,
        )
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        #* Buttons
        self.terminal_button = self.create_button(self, main.mercury_terminal(), "Mercury Terminal")
        self.terminal_button.grid(row=0, column=0, sticky="nswe", padx=20, pady=20)

    def create_button(self, button_event, text):
        button = customtkinter.CTkButton(app, text=text, command=button_event)

        return button

app = App()
app.mainloop()