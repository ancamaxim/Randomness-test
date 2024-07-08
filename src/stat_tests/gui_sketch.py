# a file to help with the design of the gui
# use it and adapt it to your own taste
# serves as an implementation for the main menu module

import tkinter
import tkinter.messagebox
import customtkinter
import monobit
import mbit
import autocorrelation
import serial
import runs

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("gui_sketch.py")
        self.geometry(f"{1000}x{800}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=10)
        self.sidebar_frame.grid(row=0, column=0, rowspan=11, sticky="nsew")
        
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Interactive Randomness Test", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.monobit_event, text = "Monobit Test")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.mbit_event, text = "M-bit Test")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.autocorr_event, text = "Autocorrelation Test")
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=self.runs_event, text = "Runs Test")
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=self.serial_event, text = "Serial Test")
        self.sidebar_button_4.grid(row=5, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        # the next line brings about that annoying space in the menu 
        self.sidebar_frame.grid_rowconfigure(6, weight=1)
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 20))

        # should be created a new frame for the right hand of the gui 
        # to be implemented...
        
        self.main_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, rowspan=10, columnspan=3, sticky="nsew")
        self.main_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.main_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), weight=1)
        
        # create textbox
        self.main_label = customtkinter.CTkLabel(self.main_frame,
        font=customtkinter.CTkFont(size=17, weight="normal"),
        text = "Select the desired Randomness Test")
        self.main_label.grid(row=6, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # set default values
        self.appearance_mode_optionemenu.set("Dark")
        self.change_appearance_mode_event("Dark")
        self.scaling_optionemenu.set("100%")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def monobit_event(self):
        self.main_label.destroy()
        monobit.monobit(self)
    def mbit_event(self):
        pass
    def autocorr_event(self):
        self.main_label.destroy()
        
        input_frame = customtkinter.CTkFrame(self.main_frame, corner_radius=0, fg_color="transparent")
        input_frame.grid(row=0, column=0, rowspan=2, columnspan=3, pady=20,  sticky="nsew")
        input_frame.grid_columnconfigure((1, 2, 3, 4, 5), weight=1)
        # input_frame.grid_columnconfigure(3, weight=0)
        
        # sequence label
        self.bitSeqLabel = customtkinter.CTkLabel(input_frame,
                                        text="Bit Sequence")
        self.bitSeqLabel.grid(row=1, column=0, padx=20, pady=5,sticky="w")

        # sequence entry field
        self.bitSeqEntry = customtkinter.CTkEntry(input_frame)
        self.bitSeqEntry.grid(row=1, column=1, columnspan=4, padx=10, pady=5, sticky="ew")
        
        # alpha label
        self.bitSeqLabel = customtkinter.CTkLabel(input_frame,
                                        text="Sensitivity coefficient")
        self.bitSeqLabel.grid(row=2, column=0, padx=20, pady=5,sticky="w")

        # alpha entry field
        self.bitSeqEntry = customtkinter.CTkEntry(input_frame)
        self.bitSeqEntry.grid(row=2, column=1, columnspan=1, padx=10, pady=5, sticky="ew")
        
        # d param label
        self.bitSeqLabel = customtkinter.CTkLabel(input_frame,
                                        text="Bit Sequence")
        self.bitSeqLabel.grid(row=3, column=0, padx=20, pady=5,sticky="w")

        # d param entry field
        self.bitSeqEntry = customtkinter.CTkEntry(input_frame)
        self.bitSeqEntry.grid(row=3, column=1, columnspan=1, padx=10, pady=5, sticky="ew")

        # Generate Button
        self.generateResultsButton = customtkinter.CTkButton(input_frame,
                                            text="Generate Results")
        self.generateResultsButton.grid(row=4, column=3,
                                        columnspan=1,
                                        padx=20, pady=15,
                                        sticky="ew")
        
        # call the function for the sequence
        autocorrelation.autocorrelation("", 0, 0)
        
    def serial_event(self):
        pass
    def runs_event(self):
        pass
if __name__ == "__main__":
    app = App()
    app.mainloop()