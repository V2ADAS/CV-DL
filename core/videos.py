import cv2

# Accepts Camera index, or video filename
cap = cv2.VideoCapture(0)

# If not openned, open
if not cap.isOpened():
    cap.open(0)

# scale video by 0.5 factor
cap.set(3, cap.get(3) / 2)  # width
cap.set(4, cap.get(4) / 2)  # height

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('tmp.avi', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

# Capture loop
while(True):
    # read next frame
    isRead, frame = cap.read()

    if not isRead:
        break

    # convert to grascale
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # write frame to file
    out.write(frame)

    # display frame
    cv2.imshow('frame', frame_gray)

    # if 'q' is pressed, quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release capture object
cap.release()

# release output file
out.release()

# close windows
cv2.destroyAllWindows()
