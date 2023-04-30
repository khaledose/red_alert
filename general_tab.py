from ttkbootstrap.widgets import Frame, LabelFrame
from custom_widgets import CustomSlider, CustomCheckButton
from actions.actions import setCostMultiplier, setBuildSpeed, setOreGrowthRate, setOreIncome, removeBuildLimit, removeRequirements
import tkinter as tk

class GeneralTab(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.columnconfigure(0, weight=1)

        # Create a frame for Set Cost option
        self.set_cost_frame = LabelFrame(self, text="Cost")
        self.set_cost_frame.pack(fill=tk.X, padx=10, pady=5)

        # Create a CustomSlider for Set Cost option
        self.set_cost_slider = CustomSlider(self.set_cost_frame, "Set Cost", 0.01, 10.0, 1.0, is_float=True, command=setCostMultiplier)
        self.set_cost_slider.pack(fill=tk.X, padx=10, pady=5)

        # Create a frame for Ore Mining option
        self.ore_mining_frame = LabelFrame(self, text="Ore Mining")
        self.ore_mining_frame.pack(fill=tk.X, padx=10, pady=5)

        # Create CustomSliders for Ore Mining option
        self.growth_slider = CustomSlider(self.ore_mining_frame, "Growth Rate", 0.01, 1, 0.01, is_float=True, command=setOreGrowthRate)
        self.growth_slider.pack(fill=tk.X, padx=10, pady=5)

        self.income_slider = CustomSlider(self.ore_mining_frame, "Income", 1, 1000, 1, command=setOreIncome)
        self.income_slider.pack(fill=tk.X, padx=10, pady=5)

        # Create a frame for Set Building Speed option
        self.set_building_speed_frame = LabelFrame(self, text="Building Speed")
        self.set_building_speed_frame.pack(fill=tk.X, padx=10, pady=5)

        # Create a CustomSlider for Set Building Speed option
        self.set_building_speed_slider = CustomSlider(self.set_building_speed_frame, "Set Building Speed", 0.01, 5, 0.01, is_float=True, command=setBuildSpeed)
        self.set_building_speed_slider.pack(fill=tk.X, padx=10, pady=5)

        # Create a frame for Set Building Speed option
        self.set_building_speed_frame = LabelFrame(self, text="Remove Build Limit")
        self.set_building_speed_frame.pack(fill=tk.X, padx=10, pady=5)

        # Create a CustomSlider for Set Building Speed option
        self.set_building_speed_slider = CustomCheckButton(self.set_building_speed_frame, "Enable", command=removeBuildLimit)
        self.set_building_speed_slider.pack(fill=tk.X, padx=10, pady=5)

        # Create a frame for Set Building Speed option
        self.set_building_speed_frame = LabelFrame(self, text="Remove Requirements")
        self.set_building_speed_frame.pack(fill=tk.X, padx=10, pady=5)

        # Create a CustomSlider for Set Building Speed option
        self.set_building_speed_slider = CustomCheckButton(self.set_building_speed_frame, "Enable", command=removeRequirements)
        self.set_building_speed_slider.pack(fill=tk.X, padx=10, pady=5)