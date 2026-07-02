# FuzzyDistancePWM

FuzzyDistancePWM is an experimental MicroPython project that maps distance measurements to PWM duty cycle and frequency using fuzzy logic.

The project combines motion-gated distance sensing with a fuzzy controller. A PIR sensor is used as an activity gate, an ultrasonic sensor provides distance measurements, and the fuzzy controller computes PWM output values for a buzzer, LED, servo-style signal, or another PWM-driven device.

## Control flow

```text
PIR motion detection
        ↓
ultrasonic distance measurement
        ↓
fuzzy logic controller
        ↓
PWM frequency and duty-cycle output
```

When motion is active and a valid distance is available, the PWM output is updated. When there is no motion or no valid distance, the PWM output is turned off.

## Target runtime

This project is intended for MicroPython-compatible boards such as Raspberry Pi Pico, Pico W, ESP32, or similar boards.

The hardware-facing code uses MicroPython modules such as `machine`, so `main.py` is not expected to run directly with standard desktop Python.

## Project structure

```text
FuzzyDistancePWM/
├── main.py        # Main MicroPython control loop
├── fuzz/          # Fuzzy logic engine, membership functions, and rules
├── input/         # Sensor and interaction logic
├── output/        # PWM output abstraction
└── tests/         # Desktop-safe tests for fuzzy logic
```

## Fuzzy behavior

The fuzzy controller currently uses distance as the main input.

Example rule behavior:

```text
very close → high duty, high frequency
close      → medium duty, high frequency
medium     → low duty, medium frequency
far        → low duty, low frequency
```

The fuzzy logic is separated from the hardware code, so it can be tested on a normal computer without connected sensors.

## Run tests on desktop

```powershell
python -m pytest
```

## Run on MicroPython hardware

Copy the project files to the board and run:

```text
main.py
```

Default pins in `main.py`:

```text
PIR sensor:        GPIO 17
Ultrasonic trig:   GPIO 15
Ultrasonic echo:   GPIO 16
PWM output:        GPIO 14
```

Adjust the pins in `main.py` to match your wiring.

## Status

This is an experimental sandbox project for exploring fuzzy logic in simple sensor-driven embedded control.
