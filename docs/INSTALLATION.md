# Installation guide

Setup for 'Invisible Networks' on Raspberry Pi Zero 2W

## Prerequisites

- Raspberry Pi Zero 2W with Raspberry Pi OS installed
- Raspberry Pi camera module enabled
- Python 3.7+

## SETUP

### 1. Enable camera

```bash
sudo raspi-config
```
**Interface Options** → **Camera** → **Enable** → **Finish** → **Reboot**

Verify:

```bash
libcamera-hello
```

### 2. Clone repository

```bash
git clone https://github.com/amena-robotics/invisible-networks.git
cd invisible-networks
```

### 3. Install dependencies

```bash
pip3 install -r requirements.txt
```

### 4. Run

```bash
python3 boid_control.py
```

Press `Ctrl + C` to stop.

---

## Config

Edit `config.py` to tune parameters:

```python
MAX_SPEED = 4              # Forward velocity
TURNING_FORCE = 2          # Steering intensity
MOTOR_DELAY = 0.8          # Tail wag timing
```

Adjust HSV color thresholds if fish aren't detected properly
