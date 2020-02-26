import cv2
import numpy as np

def process_frame(image):
    image = cv2.resize(image, (1920//2, 1080//2))
    cv2.imshow('Frame', image)
    print(image.shape)

def play(file):
    cap = cv2.VideoCapture(file)

    if(cap.isOpened() == False):
        print("Error opening video")

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            process_frame(frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()

    cv2.destroyAllWindows()

if __name__ == "__main__":
    play('videos/test_countryroad.mp4')