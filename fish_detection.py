import numpy as np
import cv2
from picamzero import Camera

from config import (
    BLUE_HSV_LOWER, BLUE_HSV_UPPER,
    RED_HSV_LOWER1, RED_HSV_UPPER1,
    RED_HSV_LOWER2, RED_HSV_UPPER2,
    KERNEL_SIZE, KERNEL_ITERATIONS, MIN_CONTOUR_AREA
)

def preprocess_mask(mask, kernel_size = KERNEL_SIZE, iterations = KERNEL_ITERATIONS):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=iterations) # Delete noise smalled than 5x5 kernel
    mask = cv2.dilate(mask, kernel, iterations=iterations) # Regrow object but do not include deleted noise
    return mask

def find_contours(mask, min_area = MIN_CONTOUR_AREA):
    # Convert binary mask into vectors
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    coordinates = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area >= min_area: # Don't react to tiny blips of colour
            x, y, w, h = cv2.boundingRect(contour) # Bound the detected colour
            coordinates.append((x, y, w, h))
    return coordinates

def calculate_positions(coordinates, image_width):
    # normalised positions of detected objects for steering
    positions = []
    for (x, y, w, h) in coordinates:
        # left = -10, centre = 0, right = 10
        centre_x = x + w // 2
        normalised_position = (centre_x - image_width // 2) / (image_width // 2) * 10
        position = int(round(normalised_position))
        positions.append(position)
    return positions

def find_fish(camera, min_area = MIN_CONTOUR_AREA, kernel_size = KERNEL_SIZE):
    #Detect blue fish and red obstacle
    try:
        image = camera.capture_array() # Capture image from the camera
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # RGB ---> HSV threshold inequalities
        img_width = image.shape[1]

        # Detecting neighbours
        blue_mask = cv2.inRange(hsv, BLUE_HSV_LOWER, BLUE_HSV_UPPER)
        blue_mask = preprocess_mask(blue_mask, kernel_size) # Cleans noise
        blue_coordinates = find_contours(blue_mask, min_area)
        blue_positions = calculate_positions(blue_coordinates, img_width)

        # Red obstacle detection
        red_mask1 = cv2.inRange(hsv, RED_HSV_LOWER1, RED_HSV_UPPER1)
        red_mask2 = cv2.inRange(hsv, RED_HSV_LOWER2, RED_HSV_UPPER2)
        red_mask = cv2.bitwise_or(red_mask1, red_mask2)
        red_mask = preprocess_mask(red_mask, kernel_size)
        red_coordinates = find_contours(red_mask, min_area)
        red_positions = calculate_positions(red_coordinates, img_width)

        return blue_positions, red_positions

    except:
        print("An error occurred")
        return [], []
