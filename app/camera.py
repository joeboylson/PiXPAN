import customtkinter
from PIL import Image
from picamera2 import Picamera2
from datetime import datetime

W = 800
H = 295

camera = None


def camera_is_online():
    if camera is None:
        print(">>> NO CAMERA FOUND")
        return False
    return True


def setup_camera():
    if not camera_is_online():
        camera = Picamera2()
        camera_config = camera.create_still_configuration(
            main={"size": (W, H)},
            lores={"size": (W, H)},
            display="lores",
        )
        camera.configure(camera_config)


def start_camera():
    if camera_is_online():
        camera.start()


def stop_camera():
    if camera_is_online():
        camera.stop()


def capture_camera_image():
    if camera_is_online():
        image = camera.capture_image()

        return customtkinter.CTkImage(
            light_image=image,
            dark_image=image,
            size=(W, H),
        )


def take_camera_image():
    if camera_is_online():
        timestamp = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
        filename = f"images/piXPAN_{timestamp}.jpg"
        camera.capture_file(filename)
        image = Image.open(filename)

        return customtkinter.CTkImage(
            light_image=image,
            dark_image=image,
            size=(W, H),
        )
