# Import necessary libraries
import cv2                    # For video processing and computer vision
import matplotlib.pyplot as plt  # For displaying images and drawing circles

# Load the video file of falling coins
video = cv2.VideoCapture("samples-teaching/coins.mp4")

# Read through the first 150 frames to reach a later point in the video
# This is useful if the coins fall later in the video, and we want a clear frame
for i in range(150):
    ret, frame = video.read()  # 'ret' tells if the frame was read successfully

# Define a function to detect circular objects (coins) in the frame
def find_circles(frame):
    # Convert the color image to grayscale (easier to process)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply a simple brightness threshold to isolate bright objects
    _, thresh = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)

    # Try to find circles using the Hough Circle Transform
    circles = cv2.HoughCircles(
        thresh,                 # Image input: thresholded grayscale
        cv2.HOUGH_GRADIENT,     # Detection method
        dp=1,                   # Inverse ratio of resolution
        minDist=40,             # Minimum distance between detected centers
        param1=10,              # High threshold for internal edge detector
        param2=10,              # Threshold for circle detection
        minRadius=1,            # Smallest coin radius expected
        maxRadius=20            # Largest coin radius expected
    )

    # Return the detected circles (if any), stored as a list of x, y, radius
    return circles[0]

# Call the function to detect coins (circles) in the selected frame
circles = find_circles(frame)

# Display the result with matplotlib
fig, ax = plt.subplots()

# Show the thresholded (black and white) image used for detection
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)
ax.imshow(thresh, cmap='gray')

# If no circles were found, notify the user
if circles is None:
    print("No circles found!")
else:
    # Otherwise, draw a red circle around each detected coin
    for circ in circles:
        x, y, r = circ
        ax.add_artist(plt.Circle((x, y), r, fill=False, color="red", linewidth=2))

# Show the final figure
plt.title("Detected Coins")
plt.axis("off")
plt.show()
