import customtkinter # type: ignore

customtkinter.set_appearance_mode("Dark") 
customtkinter.set_default_color_theme("green")  

class ButonAPP(customtkinter.CTk):
   
    def __init__(self):
        super().__init__()
        self.title("Mon application #1")
        self.geometry(f"{1100}x{580}")
        
        self.grid_columnconfigure(0, weight=1 )
        self.grid_rowconfigure(0, weight=1 )
        
        self.principal_frame = customtkinter.CTkFrame(self, width=200, corner_radius=0) 
        self.principal_frame.grid(row=0, column=0, sticky="nsew")
        self.principal_frame.grid_columnconfigure(0, weight=1)
        # self.principal_frame.grid_rowconfigure(0, weight=1)
        
        self.button = customtkinter.CTkButton(master=self.principal_frame, text="Cliquez ici", command=self.say_hello)
        self.button.grid(row=0, column=0, sticky="nsew")
       
    def say_hello(self):
        print("Hello World")


if __name__ == "__main__":
    mon_instance = ButonAPP()    
    mon_instance.mainloop()