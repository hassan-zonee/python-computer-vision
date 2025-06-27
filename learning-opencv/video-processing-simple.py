import cv2


cap = cv2.VideoCapture('../testvid.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000/fps)

h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) * 0.5)
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) * 0.5)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter('1.mp4', fourcc, fps, (w, h))

while True:
    ret, frame = cap.read()

    if not ret:
        break

    resized = cv2.resize(frame, (w, h), interpolation=cv2.INTER_AREA) 
    output.write(resized)
    cv2.imshow('Video', resized)

    if(cv2.waitKey(delay) & 0xff==ord('q')):
        break

cap.release()
output.release()
cv2.destroyAllWindows()