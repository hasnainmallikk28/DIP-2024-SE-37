import os
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# Defining path to image
image_path = "image.png"

# Checking if image file exists in the directory
if not os.path.exists(image_path):
  raise FileNotFoundError(
      f"Image file '{image_path}' not found! Please check the file name and"
      " location."
  )
# Loading image using OpenCV
image = cv.imread(image_path)

# Print the shape (dimensions and channels) and data type of the image
print("Image Shape (Height, Width, Channels):", image.shape)
print("Image Data Type (dtype):", image.dtype)

 
# 1. Height, Width, and Channels (Inspection)
height, width, channels = image.shape
print(f"Height: {height}, Width: {width}, Channels: {channels}")

# 2. Top-left and Center Pixels
top_left_pixel = image[0, 0]
center_y, center_x = height // 2, width // 2
center_pixel = image[center_y, center_x]

print(f"Top-Left Pixel [0, 0] (BGR): {top_left_pixel}")
print(f"Center Pixel [{center_y}, {center_x}] (BGR): {center_pixel}")

# 3. Global and Per-Channel Min/Max values
global_min = np.min(image)
global_max = np.max(image)
print(f"Global Minimum: {global_min}, Global Maximum: {global_max}")

for i, color in enumerate(["Blue", "Green", "Red"]):
  channel_min = np.min(image[:, :, i])
  channel_max = np.max(image[:, :, i])
  print(f"{color} Channel Min: {channel_min}, Max: {channel_max}")

  
print("\n--- Step 4: Color Conversion and Channels ---")

# 1. Convert BGR to RGB (OpenCV loads in BGR, Matplotlib expects RGB)
image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)

# 2. Convert to Grayscale
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# 3. Split BGR channels
b_channel, g_channel, r_channel = cv.split(image)

# 4. Convert center pixel BGR to HEX format
# Note: OpenCV uses BGR, so we extract R, G, B accordingly for HEX
cb, cg, cr = center_pixel
center_hex = f"#{cr:02x}{cg:02x}{cb:02x}"
print(f"Center Pixel HEX Color: {center_hex}")

# 5. Plotting 2x3 subplot grid
plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.imshow(image_rgb)
plt.title("Original RGB")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(gray_image, cmap="gray")
plt.title("Grayscale")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(r_channel, cmap="Reds")
plt.title("Red Channel")
plt.axis("off")

plt.subplot(2, 3, 4)
plt.imshow(g_channel, cmap="Greens")
plt.title("Green Channel")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(b_channel, cmap="Blues")
plt.title("Blue Channel")
plt.axis("off")

plt.subplot(2, 3, 6)
plt.imshow(image)  # Unconverted BGR
plt.title("Unconverted BGR (OpenCV Default)")
plt.axis("off")

plt.tight_layout()
plt.show()


# --- Step 5: Crop, Resize, and Save ---
print("\n--- Step 5: Crop, Resize, and Save ---")

# 1. Crop a 100x100 region from the center of the image
h, w, _ = image.shape
start_y, start_x = h // 2 - 50, w // 2 - 50
cropped_region = image[start_y : start_y + 100, start_x : start_x + 100]

# 2. Resize the cropped region to 200x200 pixels using bilinear interpolation
resized_crop = cv.resize(
    cropped_region, (200, 200), interpolation=cv.INTER_LINEAR
)

# 3. Save the processed image to disk
output_filename = "resized_crop.png"
cv.imwrite(output_filename, resized_crop)
print(f"Cropped and resized image successfully saved as '{output_filename}'")

# 4. Display original, cropped, and resized images side-by-side using Matplotlib
plt.figure(figsize=(10, 4))

plt.subplot(1, 3, 1)
plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(cv.cvtColor(cropped_region, cv.COLOR_BGR2RGB))
plt.title("Cropped (100x100)")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(cv.cvtColor(resized_crop, cv.COLOR_BGR2RGB))
plt.title("Resized (200x200)")
plt.axis("off")

plt.tight_layout()
plt.show()


# --- Step 6: Histogram Creation ---
print("\n--- Step 6: Histogram Creation ---")

# 1. Calculate 256-bin histogram for the grayscale image
hist = cv.calcHist([gray_image], [0], None, [256], [0, 256])

# 2. Plot the histogram
plt.figure(figsize=(8, 4))
plt.plot(hist, color="black")
plt.title("Grayscale Intensity Histogram")
plt.xlabel("Pixel Intensity (0 - 255)")
plt.ylabel("Pixel Count")
plt.xlim([0, 256])
plt.grid(True, linestyle="--", alpha=0.6)

# 3. Save histogram plot to disk
hist_filename = "grayscale_histogram.png"
plt.savefig(hist_filename, dpi=300, bbox_inches="tight")
print(f"Histogram plot successfully saved as '{hist_filename}'")

plt.show()

print("\n--- Step 7: Bit Depth Demonstration ---")

# 1. Create an 8-bit horizontal grayscale gradient (width: 256, height: 50)
gradient = np.tile(np.linspace(0, 255, 256, dtype=np.uint8), (50, 1))

# Helper function for quantization
def quantize_image(img, bits):
  levels = 2**bits
  # Reduce levels and scale back up to 0-255 range
  factor = 256 // levels
  quantized = (img // factor) * factor
  return quantized, len(np.unique(quantized))

# 2. Quantize to different bit depths
grad_1bit, unique_1bit = quantize_image(gradient, 1)
grad_2bit, unique_2bit = quantize_image(gradient, 2)
grad_4bit, unique_4bit = quantize_image(gradient, 4)

print(f"1-bit Unique Intensity Values: {unique_1bit}")
print(f"2-bit Unique Intensity Values: {unique_2bit}")
print(f"4-bit Unique Intensity Values: {unique_4bit}")
print(f"8-bit Unique Intensity Values: {len(np.unique(gradient))}")

# 3. Plot the bit depth comparison
plt.figure(figsize=(8, 6))

plt.subplot(4, 1, 1)
plt.imshow(gradient, cmap="gray", vmin=0, vmax=255)
plt.title("Original 8-bit Gradient (256 values)")
plt.axis("off")

plt.subplot(4, 1, 2)
plt.imshow(grad_4bit, cmap="gray", vmin=0, vmax=255)
plt.title("4-bit Quantized (16 values)")
plt.axis("off")

plt.subplot(4, 1, 3)
plt.imshow(grad_2bit, cmap="gray", vmin=0, vmax=255)
plt.title("2-bit Quantized (4 values)")
plt.axis("off")

plt.subplot(4, 1, 4)
plt.imshow(grad_1bit, cmap="gray", vmin=0, vmax=255)
plt.title("1-bit Quantized (2 values)")
plt.axis("off")

plt.tight_layout()
plt.show()