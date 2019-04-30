import cv2
import os
import sys

input_path = sys.argv[1]
frame_interval = int(sys.argv[2])
filenames = os.listdir(input_path)[1:]
video_prefix = input_path.split(os.sep)[-1]
frame_path = '{}_frames'.format(input_path)

if not os.path.exists(frame_path):
    os.mkdir(frame_path)

cap = cv2.VideoCapture()
for filename in filenames:
    filepath = os.sep.join([input_path, filename])
    cap.open(filepath)

    n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    for i in range(n_frames):
        ret, frame = cap.read()
        if i % frame_interval == 0:
            imagename = '{}_{}_{:0>6d}.jpg'.format(video_prefix, filename.split('.')[0], i)
            imagepath = os.sep.join([frame_path, imagename])
            cv2.imwrite(imagepath, frame)
cap.release()
