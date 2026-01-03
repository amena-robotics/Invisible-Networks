# Invisible Networks 🐟
Swarm robotics project showcasing emergent collective behaviour in biomimetic fish. 
<div style="display: flex; gap: 15px; justify-content: center;">
  <img width="450" height="167" alt="Fish Robot - Final Model" src="https://github.com/user-attachments/assets/1bab2ad0-1c5d-40d0-af79-d69f41979946" />
  <img width="450" height="177" alt="Fish Robot - CAD" src="https://github.com/user-attachments/assets/d2f63b78-6c5d-455f-8ae1-42efe2aaa785" />
</div>

---

## OVERVIEW
In a world of invisible forces, power no longer sits at the centre: it moves like a school of fish, fluid, responsive, uncatchable.

'Invisible Networks' uses biomimetic robotic fish to showcase the power of decentralised systems. Inspired by natural fish schools, each agent operates independently without central control yet responds in beautiful synchrony with its neighbours through local interactions. 
<div style="display: flex; gap: 15px; justify-content: center;">
  <img width="450" height="167" alt="Fish Robot - LED on" src="https://github.com/user-attachments/assets/5caf7497-39a3-477a-baf3-d30721c1110c" />
  <img width="450" height="177" alt="Fish Robot - Charging" src="https://github.com/user-attachments/assets/70ef3ed1-a64a-4884-80d3-2626a4605982" />
</div>

This project was accepted as an academic poster at the **2025 Ada Lovelace Colloquium**.

---

## QUICK START
```bash
git clone https://github.com/amena-robotics/invisible-networks.git
cd invisible-networks
pip3 install -r requirements.txt
python3 boid_control.py
```

**More detailed setup?** → See [Installation Guide](docs/INSTALLATION.md)

---

## Features and hardware specs

- **Decentralised swarm control** – No central contol, emergent behavior from local interactions
- **Real-Time computer vision** – HSV color-based detection of neighbuors and obstacles
- **Boid flocking algorithm** – Separation, alignment and cohesion behaviours
- **Custom electromagnetic actuators** – Hand-wound coils, PWM-driven motor for tail propulsion
- **Raspberry Pi Zero 2W** – Microcontroller with intergrated camera
- **3.2V LiFePO4 battery** – Safe, rechargeable power (alternative: 3.7V LiPO)
- **Intergrated sensors** - Water level sensor + real-time vision
- **L293D motor driver** – PWM-controlled electromagnetic actuation
- **Frame** – Silicone-casted waterproof body

**For detailed hardware & schematics** → See [Hardware Documentation](docs/HARDWARE.md)

---

## System Architecture

Our robot uses a real-time perception-decision-control loop that runs every 100ms:

<div style="display: flex; justify-content: center;">
  <img width="654" height="649" alt="System Architecture Flowchart" src="https://github.com/user-attachments/assets/6b991152-b9a7-4183-8394-8020b7a52b7b" />
</div>

---

**Good luck!** 🐟

Any problems? See the [Troubleshooting Guide](docs/TROUBLESHOOTING.md)
