from .custom_widgets import CustomSlider, CustomDropdown, CustomCheckbutton
from ttkbootstrap.widgets import Frame, LabelFrame
from src.actions.actions import allowAlliedParaDrop, allowSovietParaDrop, allowYuriParaDrop, setParaDropCooldown, setAlliedParaDropUnit, setAlliedParaDropCount, setSovietParaDropUnit, setSovietParaDropCount, setYuriParaDropUnit, setYuriParaDropCount
from src.actions.readers import getAllInfantries
import tkinter as tk

class SupersTab(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        infantries = getAllInfantries()

        # Create the Allied Paradrop labelframe
        self.allied_paradrop_frame = LabelFrame(self, text="Allied Paradrop")
        self.allied_paradrop_frame.pack(padx=10, pady=5, fill=tk.X)

        # Create the Enable checkbox
        self.allied_checkbox = CustomCheckbutton(self.allied_paradrop_frame, text="Enable", command=allowAlliedParaDrop)
        self.allied_checkbox.pack(padx=10, pady=5, fill=tk.X)

        # Create the Unit Type dropdown list
        self.allied_unit_type_dropdown = CustomDropdown(self.allied_paradrop_frame, "Unit Type", options=infantries, state="disabled", command=setAlliedParaDropUnit)
        self.allied_unit_type_dropdown.pack(padx=10, pady=5, fill=tk.X)

        # Create the slider for the number of units
        self.allied_unit_count_slider = CustomSlider(self.allied_paradrop_frame, "Unit Count", 1, 50, 25, command=setAlliedParaDropCount)
        self.allied_unit_count_slider.pack(padx=10, pady=5, fill=tk.X)

        self.allied_checkbox.add_dep(self.allied_unit_type_dropdown)
        self.allied_checkbox.add_dep(self.allied_unit_count_slider)

        # Create the Soviet Paradrop labelframe
        self.soviet_paradrop_frame = LabelFrame(self, text="Soviet Paradrop")
        self.soviet_paradrop_frame.pack(padx=10, pady=5, fill=tk.X)

        # Create the Enable checkbox
        self.soviet_checkbox = CustomCheckbutton(self.soviet_paradrop_frame, text="Enable", command=allowSovietParaDrop)
        self.soviet_checkbox.pack(padx=10, pady=5, fill=tk.X)

        # Create the Unit Type dropdown list
        self.soviet_unit_type_dropdown = CustomDropdown(self.soviet_paradrop_frame, "Unit Type", options=infantries, state="disabled", command=setSovietParaDropUnit)
        self.soviet_unit_type_dropdown.pack(padx=10, pady=5, fill=tk.X)

        # Create the slider for the number of units
        self.soviet_unit_count_slider = CustomSlider(self.soviet_paradrop_frame, "Unit Count", 1, 50, 25, command=setSovietParaDropCount)
        self.soviet_unit_count_slider.pack(padx=10, pady=5, fill=tk.X)

        self.soviet_checkbox.add_dep(self.soviet_unit_type_dropdown)
        self.soviet_checkbox.add_dep(self.soviet_unit_count_slider)

        # Create the Yuri Paradrop labelframe
        self.yuri_paradrop_frame = LabelFrame(self, text="Yuri Paradrop")
        self.yuri_paradrop_frame.pack(padx=10, pady=5, fill=tk.X)

        # Create the Enable checkbox
        self.yuri_checkbox = CustomCheckbutton(self.yuri_paradrop_frame, text="Enable", command=allowYuriParaDrop)
        self.yuri_checkbox.pack(padx=10, pady=5, fill=tk.X)

        # Create the Unit Type dropdown list
        self.yuri_unit_type_dropdown = CustomDropdown(self.yuri_paradrop_frame, "Unit Type", options=infantries, state="disabled", command=setYuriParaDropUnit)
        self.yuri_unit_type_dropdown.pack(padx=10, pady=5, fill=tk.X)

        # Create the slider for the number of units
        self.yuri_unit_count_slider = CustomSlider(self.yuri_paradrop_frame, "Unit Count", 1, 50, 25, command=setYuriParaDropCount)
        self.yuri_unit_count_slider.pack(padx=10, pady=5, fill=tk.X)

        self.yuri_checkbox.add_dep(self.yuri_unit_type_dropdown)
        self.yuri_checkbox.add_dep(self.yuri_unit_count_slider)

        # Create the Paradrop Cooldown labelframe
        self.paradrop_cooldown_frame = LabelFrame(self, text="Paradrop Cooldown")
        self.paradrop_cooldown_frame.pack(padx=10, pady=5, fill=tk.X)

        # Create the slider for the cooldown time
        self.cooldown_slider = CustomSlider(self.paradrop_cooldown_frame, "Cooldown Time", 0.1, 10, 5, is_float=True, command=setParaDropCooldown)
        self.cooldown_slider.pack(padx=10, pady=5, fill=tk.X)
