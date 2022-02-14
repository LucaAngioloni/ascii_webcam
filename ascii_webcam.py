import cv2
import os

# from rich import print
# from rich.traceback import install
# install(show_locals=True)

# gray scale level values from:
# http://paulbourke.net/dataformats/asciiart/

# 70 levels of gray
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

# 10 levels of gray
gscale2 = '@%#*+=-:. '

gscale = gscale2[::-1]

if __name__ == "__main__":
    w, h = os.get_terminal_size().columns, os.get_terminal_size().lines

    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, (w, h))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ascii_string = "\n".join(["".join([gscale[int((gray[i, j]*(len(gscale)-1))/255)]
                                           for j in range(w)]) for i in range(h)])

        os.system('clear')
        # os.system('cls') # On Windows?

        print(ascii_string)
