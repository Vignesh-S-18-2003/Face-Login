from compare_images import compare_images
from camera import Camera
def main():
    camera = Camera()
    print("Press 'q' to capture the image.")
    camera.start_capture()
    captured_image_path = 'captured_image.jpg'
    camera.stop_capture(captured_image_path)
    uploaded_image_path = 'sample1.jpg'
    if compare_images(captured_image_path, uploaded_image_path):
        print("The images are similar.")
    else:
        print("The images are different.")
if __name__ == '__main__':
    main()
