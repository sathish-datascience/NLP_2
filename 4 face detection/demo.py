import cv2

# Start video capture from the default camera (0)
video_capture = cv2.VideoCapture(0)

# Load the pre-trained face detector (Haar Cascade)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    # Capture each frame
    ret, frame = video_capture.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Convert the frame to grayscale for better detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Print the number of faces detected in the frame
    print("Found {0} faces".format(len(faces)))

    # Draw rectangles around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the frame with rectangles
    cv2.imshow("Face Detection", frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the window
video_capture.release()
cv2.destroyAllWindows()
