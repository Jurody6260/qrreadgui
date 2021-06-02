import cv2
import pyzbar.pyzbar as pyzbar
import jwt
def show_webcam(mirror=False):
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_PLAIN
    while True:
        ret_val, img = cam.read()
        decodedObjects = pyzbar.decode(img)
        for obj in decodedObjects:
            print("Data", obj.data.decode("utf-8"))
            decoded_jwt = jwt.decode(obj.data.decode("utf-8"), "secret", algorithms="HS256")
            print(decoded_jwt)
            cv2.putText(img, str(obj.data), (50, 50), font, 2,
                        (255, 0, 0), 3)
        if mirror: 
            img = cv2.flip(img, 1)
        cv2.imshow('my webcam', img)
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    cv2.destroyAllWindows()


def main():
    show_webcam(mirror=True)


if __name__ == '__main__':
    main()

