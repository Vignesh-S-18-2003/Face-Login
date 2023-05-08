from flask import Flask, render_template
from compare_images import compare_images
from camera import Camera
app = Flask(__name__)
@app.route('/')
def index():
    camera = Camera()
    message = "Press 'q' to capture the image"
    print("Press 'q' to capture the image.")
    camera.start_capture()
    captured_image_path = 'captured_image.jpg'
    camera.stop_capture(captured_image_path)
    uploaded_image_path = 'sample1.jpg'
    if compare_images(captured_image_path, uploaded_image_path):
        message = "The images are similar."
        similar = True
    else:
        message = "The images are different."
        similar = False
    return render_template('index.html', message=message, similar=similar)
@app.route('/login')
def login():
    return "This is our Welcome Page"
if __name__ == '__main__':
    app.run(debug=True)
