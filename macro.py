import pyautogui  # type: ignore
import time
import threading
from PIL import ImageGrab
import keyboard  # type: ignore
import tkinter as tk
from tkinter import ttk

# Define the main application
class App:
    def __init__(self, root):
        self.root = root
        self.running = False
        self.selected_property = tk.StringVar(value='Giant.png')

        # Set up the GUI
        self.root.title("Fisch Appraisals")
        self.root.geometry("300x200")

        # Dropdown menu to select the property
        ttk.Label(self.root, text="Select Property:").pack(pady=5)
        self.property_dropdown = ttk.Combobox(self.root, textvariable=self.selected_property)
        self.property_dropdown['values'] = (
            'Giant.png', 'Shiny.png', 'Sparkling.png', 'Hexed.png',
            'Mythical.png', 'Big.png', 'Abyssal.png'
        )
        self.property_dropdown.pack(pady=5)

        # Start button
        self.start_button = ttk.Button(self.root, text="Start", command=self.start_macro)
        self.start_button.pack(pady=5)

        # Stop button
        self.stop_button = ttk.Button(self.root, text="Stop", command=self.stop_macro)
        self.stop_button.pack(pady=5)

        # Status label
        self.status_label = ttk.Label(self.root, text="Status: Idle")
        self.status_label.pack(pady=10)

    def locate_and_move(self):
        while self.running:
            try:
                # Look for the specified property on the screen
                button_location = pyautogui.locateOnScreen(
                    self.selected_property.get(),
                    confidence=0.80,
                    region=(858, 957, 62, 62)
                )
                if button_location:
                    print(f"Found: {button_location}")
                    pyautogui.moveTo(button_location)
                    self.status_label.config(text="Status: Found Mutation")
                    self.running = False
            except Exception as e:
                print("Button not found, performing alternate actions.")
                self.status_label.config(text="Status: Button Not Found")
                pyautogui.click()
                time.sleep(1)
                keyboard.press('3')
                keyboard.release('3')
                time.sleep(.2)
                keyboard.press('4')
                keyboard.release('4')

    def start_macro(self):
        if not self.running:
            time.sleep(1.5)
            self.running = True
            self.status_label.config(text="Status: Running")
            # Start the macro thread
            self.macro_thread = threading.Thread(target=self.locate_and_move, daemon=True)
            self.macro_thread.start()

    def stop_macro(self):
        if self.running:
            self.running = False
            self.status_label.config(text="Status: Stopped")

# Create the main window and run the app
root = tk.Tk()
app = App(root)
root.mainloop()



