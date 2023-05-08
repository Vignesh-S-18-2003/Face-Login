import cv2


class Camera:
    def __init__(self):
        self.capture = cv2.VideoCapture(0)
        self.current_frame = None
        self.is_capturing = False

    def start_capture(self):
        self.is_capturing = True
        while self.is_capturing:
            ret, frame = self.capture.read()
            self.current_frame = frame
            cv2.imshow("Camera Feed", frame)
            if cv2.waitKey(1) == ord('q'):
                break

        cv2.destroyAllWindows()

    def stop_capture(self, output_path):
        self.is_capturing = False
        if self.current_frame is not None:
            cv2.imwrite(output_path, self.current_frame)
        self.capture.release()
