
# AquaIntel 🌊 – IoT-Based Flood Monitoring and Alert System

AquaIntel is a real-time flood monitoring and alert system that leverages IoT sensors and a Django-powered web dashboard to detect rising water levels, trigger alerts, and assist in disaster management and rescue planning.

---

## 📌 Project Overview

Floods are among the most destructive natural disasters. AquaIntel is designed to help monitor water levels in real-time, identify high-risk areas, and enable faster and smarter response through integrated IoT hardware and a powerful web dashboard.

---

## 🚀 Key Features

### 🔧 IoT System
- Real-time monitoring with **ultrasonic and water level sensors**
- **GPS & GSM integration** for tracking and alerts
- Sensor data collected using **NodeMCU ESP8266**

### 🖥️ Web Application (Django)
- Live monitoring of **water levels** from various locations
- **Admin portal** for staff, NGO, and rescue management
- **Alert control panel** to manage and send notifications
- Visual indicators (e.g., color zones: red/yellow/green)
- Track nearby **relief camps, rescue centers, and requirements**
- Historical data view with graphs and trends

---

## 🛠️ Technologies Used

### 📡 IoT:
- NodeMCU ESP8266
- Ultrasonic Sensor
- Water Level Sensor
- DHT11 (Temp/Humidity)
- GSM Module, GPS Module

### 🌐 Web App:
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap, JS
- **Database**: MySQL WorkBench
- **API Integration**: Live sensor data API to Django views/forms

---

## 🧩 Modules in Web Application

1. **Authentication**
   - Secure login for admins/staff

2. **Dashboard**
   - Overview of all monitoring stations
   - Live water level updates

3. **Location Management**
   - Add/update locations where sensors are deployed

4. **NGO & Relief Camp Module**
   - Register NGOs, available resources, relief centers

5. **Rescue Center Management**
   - Track teams and their active regions

6. **Alert System**
   - Auto-triggered and manual SMS/email alerts
   - Danger level indicators based on sensor input

7. **Requirements Management**
   - Basic needs (food, water, blankets) tracking in camps

---



