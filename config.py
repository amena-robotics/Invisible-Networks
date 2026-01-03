# Configuration file for 'Invisible Networks'

import numpy as np

# Boid parameters
MAX_SPEED = 4 # maximum forward velocity
TURNING_FORCE = 2 # lateral steering force
MOTOR_DELAY = 0.8 # delay for motor movement (seconds)
VIEW_ANGLE = 150 # field of view (degrees)

# Vision parameters
# HSV color ranges (Hue: 0-179, Saturation: 0-255, Value: 0-255)
BLUE_HSV_LOWER = np.array([110, 100, 100])
BLUE_HSV_UPPER = np.array([130, 255, 255])

RED_HSV_LOWER1 = np.array([0, 150, 150])
RED_HSV_UPPER1 = np.array([10, 255, 255])

RED_HSV_LOWER2 = np.array([170, 150, 150])
RED_HSV_UPPER2 = np.array([180, 255, 255])

# Morph operations
KERNEL_SIZE = 5
KERNEL_ITERATIONS = 1
MIN_CONTOUR_AREA = 1000

# Camera settings
CAMERA_RESOLUTION = (320, 240)
CAMERA_STARTUP_DELAY = 1.0  # seconds

# GPIO pins
GPIO_PINS = {
    'MOTOR_PIN1': 10, # L293D input 1
    'MOTOR_PIN2': 12, # L293D input 2
    'ENABLE_PIN': 8, # L293D enable (PWM)
    'WATER_PIN': 22, # water sensor input
    'LED_PIN': 36, # status LED
}

# System settings
MAIN_LOOP_DELAY = 0.1 # seconds between iterations
