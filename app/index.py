import os

# imports
from camera import *
from layout import *


def close():
    app.quit()
    stop_camera()


if __name__ == "__main__":

    app = App()
    app.title("[Pi] X-PAN")

    app.after(10, lambda: app.wm_attributes("-fullscreen", "true"))

    app.columnconfigure(0, weight=1)
    app.rowconfigure(0, weight=1)

    app.bind("<Escape>", lambda e: close())

    app.mainloop()
