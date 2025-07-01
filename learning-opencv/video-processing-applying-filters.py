import cv2

cap = cv2.VideoCapture('testvid.mp4')
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) * 0.4)
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) * 0.4)
fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000/fps)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.resize(frame, (w, h), interpolation=cv2.INTER_AREA)
    cv2.imshow('Simple', frame)

    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    cv2.imshow('Grayscaled', grayscale)

    edges = cv2.Canny(frame, 300, 500)
    canny = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    cv2.imshow('Canny Edges', canny)

    gaussianBlur = cv2.GaussianBlur(frame, (9, 9), 0)
    cv2.putText(gaussianBlur, 'testing', (100, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow('Gaussian Blur', gaussianBlur)


    if(cv2.waitKey(delay) & 0xff == ord('q')):
        break


cap.release()
cv2.destroyAllWindows()