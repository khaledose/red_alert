from ttkbootstrap.widgets import Frame, LabelFrame
from custom_widgets import CustomSlider, CustomCheckButton
from actions.actions import setSpeedMultiplier, setVeteranRatio, setChronoDelay, removeRequiredHousesFromUnits, AllowStolenTech
import tkinter as tk

class UnitsTab(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.columnconfigure(0, weight=1)

        # Create a frame for Set Units Speed Multiplier option
        self.set_units_speed_multiplier_frame = LabelFrame(self, text="Set Units Speed Multiplier")
        self.set_units_speed_multiplier_frame.grid(row=0, column=0, sticky="we", padx=10, pady=10)

        # Create a slider for Set Units Speed Multiplier option
        self.set_units_speed_multiplier_slider = CustomSlider(self.set_units_speed_multiplier_frame,
                                                                name="Units Speed Multiplier",
                                                                minimum=1,
                                                                maximum=50,
                                                                initial_value=1,
                                                                command=setSpeedMultiplier)
        self.set_units_speed_multiplier_slider.pack(fill=tk.X, padx=10, pady=10)

        # Create a frame for Set Veteran Ratio option
        self.set_veteran_ratio_frame = LabelFrame(self, text="Set Veteran Ratio")
        self.set_veteran_ratio_frame.grid(row=1, column=0, sticky="we", padx=10, pady=10)

        # Create a slider for Set Veteran Ratio option
        self.set_veteran_ratio_slider = CustomSlider(self.set_veteran_ratio_frame,
                                                        name="Veteran Ratio",
                                                        minimum=1,
                                                        maximum=1000,
                                                        initial_value=1,
                                                        command=setVeteranRatio)
        self.set_veteran_ratio_slider.pack(fill=tk.X, padx=10, pady=10)

        # Create a frame for Set Chrono Delay option
        self.set_chrono_delay_frame = LabelFrame(self, text="Set Chrono Delay")
        self.set_chrono_delay_frame.grid(row=2, column=0, sticky="we", padx=10, pady=10)

        # Create a slider for Set Chrono Delay option
        self.set_chrono_delay_slider = CustomSlider(self.set_chrono_delay_frame,
                                                        name="Chrono Delay",
                                                        minimum=0,
                                                        maximum=50,
                                                        initial_value=0,
                                                        command=setChronoDelay)
        self.set_chrono_delay_slider.pack(fill=tk.X, padx=10, pady=10)

        # Create a frame for Remove Required Houses option
        self.remove_required_houses_frame = LabelFrame(self, text="Remove Required Houses")
        self.remove_required_houses_frame.grid(row=3, column=0, sticky="we", padx=10, pady=10)

        # Create a checkbox for Remove Required Houses option
        self.remove_required_houses_checkbox = CustomCheckButton(self.remove_required_houses_frame, text="Enable", command=removeRequiredHousesFromUnits)
        self.remove_required_houses_checkbox.pack(fill=tk.X, padx=10, pady=10)

        # Create a frame for Allow Commando option
        self.allow_commando_frame = LabelFrame(self, text="Allow Stolen Tech")
        self.allow_commando_frame.grid(row=4, column=0, sticky="we", padx=10, pady=10)

        # Create a checkbox for Allow Commando option
        self.allow_commando_checkbox = CustomCheckButton(self.allow_commando_frame, text="Enable", command=AllowStolenTech)
        self.allow_commando_checkbox.pack(fill=tk.X, padx=10, pady=10)
