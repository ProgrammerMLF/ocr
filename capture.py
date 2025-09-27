import cv2

def take_picture():
    cap = cv2.VideoCapture(0) 

    if not cap.isOpened():
        print("Cannot open camera")
        return None

    while True:
        ret, frame = cap.read()  

        if not ret:
            print("Failed to capture image")
            break

        cv2.imshow("Press space button to capture", frame)  # Display the current frame

        # Check for key presses
        key = cv2.waitKey(1) 
        if key == ord(' '):  
            break

    cap.release()  
    cv2.destroyAllWindows()  

    return frame  # Return the captured frame
