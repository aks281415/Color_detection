import cv2
import numpy as np

colors = {
    'yellow': ((20, 100, 100), (30, 255, 255)),
    'red': ((0, 100, 100), (10, 255, 255)),
    'white': ((0, 0, 200), (180, 20, 255))
}


cap = cv2.VideoCapture(0)


mask = np.zeros((480, 640), dtype=np.uint8)

while True:
    ret, frame = cap.read() 
    if not ret:
        break

    
    print("Available colors:")
    for idx, color_name in enumerate(colors.keys()):
        print(f"{idx + 1}: {color_name}")

    choice = int(input("Select a color (1-10), or 0 to quit: "))

    if choice == 0:
        break

    color_name = list(colors.keys())[choice - 1]

    
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

   
    lower_limit, upper_limit = colors[color_name]
    mask = cv2.inRange(hsvImage, lower_limit, upper_limit)

    
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, color_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

   
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
