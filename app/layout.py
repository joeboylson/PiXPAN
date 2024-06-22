import customtkinter
from camera import *

################################################################################
# PREVIEW FRAME
################################################################################


class PreviewFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        start_camera()

        # render children
        self.label = customtkinter.CTkLabel(self, text="[preview]")
        self.label.grid(row=0, column=0, padx=0)
        self.label.after(10, self.start_stream)

    def start_stream(self):
        if camera_is_online():
            image = capture_camera_image()
            self.label.configure(image=image)
            self.label.after(10, self.start_stream)


################################################################################
# RESULT FRAME
################################################################################


class ResultFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # render children
        self.label = customtkinter.CTkLabel(self, text="[result]")
        self.label.grid(row=0, column=0, padx=0)

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
        self.PreviewFrame = PreviewFrame(master=self)
        self.PreviewFrame.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
        self.ResultFrame = ResultFrame(master=self)
        self.ResultFrame.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        # show preview frame
        self.show_preview_frame = True
        self.show_frame()

        # bind space to switch frames
        self.bind("<space>", lambda e: self.switch_frames())

    def show_frame(self):
        if self.show_preview_frame:
            self.PreviewFrame.lift()
        else:
            self.ResultFrame.lift()
            self.ResultFrame.on_render()

    def switch_frames(self):
        self.show_preview_frame = not self.show_preview_frame
        self.show_frame()
