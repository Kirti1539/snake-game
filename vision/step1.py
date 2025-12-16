import time
import cv2  # assuming you're using OpenCV
# other imports you have in step1.py

# Initialize variables
prev_time = time.time()
fps = 0

# Example video capture (if applicable)
cap = cv2.VideoCapture(0)  # or your source

while True:
    ret, frame = cap.read()
    if not ret:
        break

    current_time = time.time()
    time_diff = current_time - prev_time

    # Calculate FPS safely
    if time_diff > 0:
        fps = 1 / time_diff
    else:
        fps = 0  # first iteration or extremely fast loop

    # Optional: cap FPS to 60 for realistic display
    if fps > 60:
        fps = 60
        time.sleep(1 / 60)  # maintain ~60 FPS

    prev_time = current_time

    # Display FPS on the frame (optional)
    cv2.putText(frame, f'FPS: {int(fps)}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Step1", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
