import customtkinter
from PIL import Image
from datetime import datetime

W = 800
H = 295

camera = None


def get_blank_image():
    BLANK_IMAGE_URL = "assets/no-camera-detected.jpg"
    return Image.open(BLANK_IMAGE_URL)


def camera_is_online():
    if camera is None:
        print(">>> NO CAMERA FOUND")
        return False
    return True


def capture_and_save_image():
    if camera_is_online():
        timestamp = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
        filename = f"images/piXPAN_{timestamp}.jpg"
        camera.capture_file(filename)
        return Image.open(filename)

    return get_blank_image()


def setup_camera():
    from picamera2 import Picamera2

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
    image = camera.capture_image() if camera_is_online() else get_blank_image()

    return customtkinter.CTkImage(
        light_image=image,
        dark_image=image,
        size=(W, H),
    )


def take_camera_image():
    image = capture_and_save_image()
    return customtkinter.CTkImage(
        light_image=image,
        dark_image=image,
        size=(W, H),
    )
