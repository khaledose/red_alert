from ttkbootstrap.widgets import Frame, LabelFrame
from .custom_widgets import CustomSlider, CustomCheckbutton
from src.actions.actions import setSpeedMultiplier, setVeteranRatio, removeChronoDelay, removeRequiredHousesFromUnits, AllowStolenTech
import tkinter as tk

class UnitsTab(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.columnconfigure(0, weight=1)

        # Create a frame for Set Units Speed Multiplier option
        self.set_units_speed_multiplier_frame = LabelFrame(self, text="Speed Multiplier")
        self.set_units_speed_multiplier_frame.grid(row=0, column=0, sticky="we", padx=10, pady=10)

        # Create a slider for Set Units Speed Multiplier option
        self.set_units_speed_multiplier_slider = CustomSlider(self.set_units_speed_multiplier_frame,
                                                                name="Set Speed Multiplier",
                                                                minimum=1,
                                                                maximum=50,
                                                                initial_value=1,
                                                                command=setSpeedMultiplier)
        self.set_units_speed_multiplier_slider.pack(fill=tk.X, padx=10, pady=10)

        # Create a frame for Set Veteran Ratio option
        self.set_veteran_ratio_frame = LabelFrame(self, text="Veteran Ratio")
        self.set_veteran_ratio_frame.grid(row=1, column=0, sticky="we", padx=10, pady=10)

        # Create a slider for Set Veteran Ratio option
        self.set_veteran_ratio_slider = CustomSlider(self.set_veteran_ratio_frame,
                                                        name="Set Veteran Ratio",
                                                        minimum=1,
                                                        maximum=1000,
                                                        initial_value=1,
                                                        command=setVeteranRatio)
        self.set_veteran_ratio_slider.pack(fill=tk.X, padx=10, pady=10)

        # Create a frame for Set Chrono Delay option
        self.set_chrono_delay_frame = LabelFrame(self, text="Chrono Delay")
        self.set_chrono_delay_frame.grid(row=2, column=0, sticky="we", padx=10, pady=10)

        # Create a slider for Set Chrono Delay option
        self.set_chrono_delay_checkbox = CustomCheckbutton(self.set_chrono_delay_frame,
                                                        text="Remove",
                                                        command=removeChronoDelay)
        self.set_chrono_delay_checkbox.pack(fill=tk.X, padx=10, pady=10)

        # Create a frame for Remove Required Houses option
        self.remove_required_houses_frame = LabelFrame(self, text="Required Houses")
        self.remove_required_houses_frame.grid(row=3, column=0, sticky="we", padx=10, pady=10)

        # Create a checkbox for Remove Required Houses option
        self.remove_required_houses_checkbox = CustomCheckbutton(self.remove_required_houses_frame, text="Remove", command=removeRequiredHousesFromUnits)
        self.remove_required_houses_checkbox.pack(fill=tk.X, padx=10, pady=10)

        # Create a frame for Allow Commando option
        self.allow_commando_frame = LabelFrame(self, text="Stolen Tech")
        self.allow_commando_frame.grid(row=4, column=0, sticky="we", padx=10, pady=10)

        # Create a checkbox for Allow Commando option
        self.allow_commando_checkbox = CustomCheckbutton(self.allow_commando_frame, text="Enable", command=AllowStolenTech)
        self.allow_commando_checkbox.pack(fill=tk.X, padx=10, pady=10)
