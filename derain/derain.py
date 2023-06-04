import cv2
import numpy as np

# open rain.mp4
cap = cv2.VideoCapture('rain.mp4')

# get all frames from the video
frames = []
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frames.append(frame)
    else:
        break
# close the video
cap.release()

print("Processing {} frames".format(len(frames)))

# dests = []
# for i, img in enumerate(frames):
#     index = np.ones((img.shape[0] // 3, img.shape[1] // 3), dtype=bool)
#
#     for j in range(2):
#         index &= (img[j::3, : ,:] - img[(j + 1)::3, :, :]) > 50
#
#     f = frames[i - 1][index]
#     img[index] = f
#
#     dests.append(img)
#     print("Processed {} / {} frames".format(i, len(frames)), end='\r')
#     cv2.imshow('frame', dests[-1])
#     cv2.waitKey(1)
#
# frames = dests

# cv2.imshow('frame', frames[0])
# cv2.waitKey(0)
#
# # run fastNlMeansDenoisingColoredMulti on all frames
for i in range(2, len(frames)-2):
    frames[i] = cv2.fastNlMeansDenoisingColoredMulti(frames, i, 5, None, 4, 7, 35)
    print("Processed {} / {} frames".format(i, len(frames)-2), end='\r')

# save all frames to a video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frames[0].shape[1], frames[0].shape[0]))
for frame in frames:
    out.write(frame)
out.release()
