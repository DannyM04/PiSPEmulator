PiSP Emulator UI

A Python Tkinter-based UI for a Raspberry Pi CM4 handheld emulator.
The UI currently allows users to browse through different emulators (PSP, N64, PC). All optimised for fullscreen usage.

Current Features:
- Fullscreen Tkinter GUI tailored for Raspberry Pi CM4
- Home screen with buttons to select emulator platforms (PSP, N64, PC)
- A functional UI that provides users with the time and battery percentage of their device (if the device has a battery)
- Consistent UI style
- Navigation buttons including a "Home" button on emulator screens
- Escape key binding to exit application
- Settings menu with system diagnostics (CPU Temp only available for Linux systems)
- A customisable dark/light mode


Future Goals (In no particular order):
- Allow the system to access Emulator files and run games from application
- Create settings menu for resolution, Bluetooth headphones, and a dev mode option for future updates
- Create a sleek, and maybe customisable, opening animation for the application (on startup)
- Implement home menu music for application
- Implement animations for selecting different emulators
- Display a warning for when the emulator's battery is low
- Further optimisations to make the application more accessable
- An .ini file to save user preferences/connections (dark/light mode, Bluetooth connected devices, saved Wi-Fi connections)

Prerequisites:
Python 3.11
Tkinter 
psutil (you can install psutil with(pip install psutil))

Notes:
- Next update should be a more complete version, including emulators and  Thank you for following the development of the PiSP.
- Placeholder assets are used to prevent copyright infringement
