# Troubleshooting guide

Solutions for common issues with Invisible Networks.

## Camera sssues

 ```RuntimeError: Camera is not detected ```

**Solutions:**

1. Enable camera in `raspi-config`:

   ```bash
   sudo raspi-config
   
2. Verify camera works:

	```bash
   libcamera-hello

4. Check camera ribbon cable fully inserted in CSI port

---

Python & Dependencies

```ModuleNotFoundError: No module named 'picamzero'```

**Solutions:**

1. Reinstall dependencies:

	```bash
   pip3 install -r requirements.txt

2. Correct directory:

	```bash
   cd invisible-networks

3. Verify Python version (must be 3.7+):

	```bash
   python3 --version

---

GPIO & motor issues

```RuntimeError: No access to /dev/mem. Try running as root!```

**Solution:**

1. Run with sudo
   
```sudo python3 boid_control.py	```

---

Motor not spinning when script running

1. Verify GPIO pins in config.py match your wiring:

	```bash
	GPIO_PINS = {
	    'MOTOR_PIN1': 10,
	    'MOTOR_PIN2': 12,
	    'ENABLE_PIN': 8,
	}

2. Check L293D motor driver is powered (5V) 

3. Verify wiring matches [Hardware Documentation](HARDWARE.md)

4. Test motor with simple script:

	```bash
	import RPi.GPIO as GPIO
	from config import GPIO_PINS
	
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(GPIO_PINS['MOTOR_PIN1'], GPIO.OUT)
	GPIO.setup(GPIO_PINS['MOTOR_PIN2'], GPIO.OUT)
	GPIO.setup(GPIO_PINS['ENABLE_PIN'], GPIO.OUT)
	
	GPIO.output(GPIO_PINS['ENABLE_PIN'], GPIO.HIGH)
	GPIO.output(GPIO_PINS['MOTOR_PIN1'], GPIO.HIGH)
	GPIO.output(GPIO_PINS['MOTOR_PIN2'], GPIO.LOW)
	print("Motor should be turning...")
	
	import time
	time.sleep(2)
	GPIO.cleanup()

---

Fish not detected ([] every frame)

1. Check lighting conditions (HSV is sensitive to light)

2. Fish are actually visible in camera view

3. Fish colour matches HSV thresholds

Adjust HSV thresholds in config.py:

```bash
	BLUE_HSV_LOWER = np.array([110, 100, 100])
	BLUE_HSV_UPPER = np.array([130, 255, 255])
```

---

Water sensor issues

Test:

```bash
	import RPi.GPIO as GPIO
	from config import GPIO_PINS
	
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(GPIO_PINS['WATER_PIN'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
	for i in range(10):
	    state = GPIO.input(GPIO_PINS['WATER_PIN'])
	    print(f"Water sensor: {state}")
	    
	GPIO.cleanup()
```

- 0 = In water

- 1 = Out of water

---
