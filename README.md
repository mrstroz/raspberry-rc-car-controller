# Raspberry PI RC Car Controller

## Introduction

This project is a Python-based controller for an RC Car raspberry project. It uses Flask and SocketIO to handle
real-time communication between the web-based controller application and the vehicle (via Raspberry GPIO). The
application receives simple joystick data and processes it
to control the vehicle's movement.

## Features

- Real-time vehicle control
- Easy-to-use web interface
- Lightweight Flask server
- SocketIO for efficient client-server communication

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- Pip for Python package management

## Installation

1. Clone the repository: `git clone https://github.com/mrstroz/raspberry-rc-car-controller.git`
2. Navigate to the project directory: `cd raspberry-rc-car-controller`
3. Install the required Python packages: `pip install flask python-socketio python-dotenv`
4. Copy .env.example file into .env `cp .env.example .env`

## Usage

To run the server, use the following command:

```bash
python main.py
```

Once the server is running, open a web browser and navigate to http://127.0.0.1:5000 to access the control interface.