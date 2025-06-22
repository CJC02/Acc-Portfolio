import cv2
import matplotlib.pyplot as plt

# Load color image, then convert to grayscale
img = cv2.imread('coin.jpg')              # Load image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

# Apply histogram equalization to improve contrast
eqhist = cv2.equalizeHist(gray)

# Set up the plot size and resolution
plt.figure(figsize=(10, 4), dpi=80)

# Plot the equalized grayscale image
plt.subplot(1, 2, 1)
plt.imshow(eqhist, cmap='gray')
plt.title("Equalized Image")
plt.axis('off')

# Plot the histogram of the equalized image
plt.subplot(1, 2, 2)
plt.hist(eqhist.flatten(), bins=256, color='gray')
plt.title("Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()
