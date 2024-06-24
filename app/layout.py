import customtkinter
from camera import *

################################################################################
# PREVIEW FRAME
################################################################################


class PreviewFrame(customtkinter.CTkFrame):
    def __init__(self, master, button_click, **kwargs):
        super().__init__(master, **kwargs)
        start_camera()

        # render children
        self.label = customtkinter.CTkLabel(self, text="")
        self.label.grid(row=0, column=0, padx=0)
        self.label.after(10, self.start_stream)

        self.button = customtkinter.CTkButton(
            self, command=button_click, text="TAKE IMAGE"
        )
        self.button.grid(row=1, column=0, padx=4, pady=4)

    def start_stream(self):
        image = capture_camera_image()
        self.label.configure(image=image)

        if camera_is_online():
            self.label.after(10, self.start_stream)


################################################################################
# RESULT FRAME
################################################################################


class ResultFrame(customtkinter.CTkFrame):
    def __init__(self, master, button_click, **kwargs):
        super().__init__(master, **kwargs)

        # render children
        self.label = customtkinter.CTkLabel(self, text="")
        self.label.grid(row=0, column=0, padx=0)

        self.button = customtkinter.CTkButton(self, command=button_click, text="RETURN")
        self.button.grid(row=1, column=0, padx=4, pady=4)

    def on_render(self):
        image = take_camera_image()
        self.label.configure(image=image)


################################################################################
# APP
################################################################################


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # self.geometry("800x400")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # render children (render both frames)
        self.PreviewFrame = PreviewFrame(master=self, button_click=self.switch_frames)
        self.PreviewFrame.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
        self.ResultFrame = ResultFrame(master=self, button_click=self.switch_frames)
        self.ResultFrame.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        # show preview frame
        self.show_preview_frame = True
        self.show_frame()

    def show_frame(self):
        if self.show_preview_frame:
            self.PreviewFrame.lift()
        else:
            self.ResultFrame.lift()
            self.ResultFrame.on_render()

    def switch_frames(self):
        self.show_preview_frame = not self.show_preview_frame
        self.show_frame()
