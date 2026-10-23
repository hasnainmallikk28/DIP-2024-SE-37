Exercise 1:- Variables and Data Types
width  = 640
height = 480
image_name ="sample.png"
is_color =True

print("Width :",width,"\nType :",type(width))
print("Height :",height,"\nType :",type(height))
print("Image Name :",image_name,"\n Image Type :",type(image_name))
print("Image Color :",is_color,"\n Is color :",type(is_color))

total_pixels = height*width
print("Total Pixels :",total_pixels)



Exercise 2:- if, elif, and else

test_values =[-1, 0, 127, 128, 255, 256]
for value in test_values:
    if value < 0 or value > 255:
        label ="Invalid"
    elif value >= 128:
        label = "Bright Pixel"
    else:
        label = "Dark"

    print(f"Intensity {value}: {label}")

Exercise 3:- for and while loop
print("For loop")
intensities = [20, 130, 255]
for value in intensities:
    if value >= 128:
        print(f"Value {value} : Bright Pixel")
    else:
        print(f"Value {value} : Dark Pixel")

        ---While Loop---
print("While Loop")
counter = 0
while counter<3:
    print(counter)
    counter+=1

Exercise 4:- Functions

print("\n Exercise 4 Outputs ")

def is_bright(pixel, threshold=128):
    if pixel >= threshold:
        return True
    else:
        return False

print("is_bright(127):", is_bright(127))
print("is_bright(128):", is_bright(128))
print("is_bright(200, 210):", is_bright(200, 210))



Exercise 5: Lists and Tuples
print("\n Exercise 5 Outputs")

pixels = [0, 128, 255]
print("First item:", pixels[0])

pixels[1] = 150       # it Replaces middle item
pixels.append(64)     # it Appends 64 at the end

print("Updated list:", pixels)
print("Length of list:", len(pixels))
# Tuples operations and unpacking
size = (640, 480)
width, height = size
print(f"Unpacked Tuple -> Width: {width}, Height: {height}")

Comment explaining Mutability
Explanation: List items are mutable (they can be modified, added, or replaced after creation), 
whereas tuple items are immutable (their values cannot be changed once the tuple is created).

# Exercise 6: Dictionaries and Sets
print("\n--- Exercise 6 Outputs ---")

#1. Dictionary operations
image = {"width": 640, "height": 480}
image["mode"] = "RGB"  # Adding mode: RGB
print(f"Width: {image['width']}, Mode: {image['mode']}")

# 2. Set operations (unique labels)
labels = ["cat", "dog", "cat", "bird"]
unique_labels = set(labels)
print("Unique labels set:", unique_labels)
print("Number of unique labels (Length):", len(unique_labels))
