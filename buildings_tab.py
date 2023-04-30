from custom_widgets import CustomSlider, CustomDropdown, CustomCheckButton
from ttkbootstrap.widgets import Frame, LabelFrame
from actions.actions import setBuildingAdjacency, toggleAutoRepair, allowAllBases, allowAllBasesForCountry
from actions.readers import getAllCountries
import tkinter as tk


class BuildingsTab(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.columnconfigure(0, weight=1)

        # Create a frame for Set Building Adjacency option
        self.set_building_adjacency_frame = LabelFrame(self, text="Set Building Adjacency")
        self.set_building_adjacency_frame.grid(row=0, column=0, sticky="we", padx=10, pady=10)

        # Create a CustomSlider for Set Building Adjacency option
        self.set_building_adjacency_slider = CustomSlider(self.set_building_adjacency_frame, "Set Building Adjacency", 1, 500, initial_value=1, command=setBuildingAdjacency)
        self.set_building_adjacency_slider.pack(fill=tk.X, padx=10, pady=10)

        # Create a frame for Allow Auto Repair option
        self.allow_auto_repair_frame = LabelFrame(self, text="Allow Auto Repair")
        self.allow_auto_repair_frame.grid(row=1, column=0, sticky="we", padx=10, pady=10)

        # Create a checkbox for Allow Auto Repair option
        self.allow_auto_repair_checkbox = CustomCheckButton(self.allow_auto_repair_frame, text="Enable", command=toggleAutoRepair)
        self.allow_auto_repair_checkbox.pack(fill=tk.X, padx=10, pady=10)

        # Create a frame for Allow All Bases For All option
        self.allow_all_bases_for_all_frame = LabelFrame(self, text="Allow All Bases For All")
        self.allow_all_bases_for_all_frame.grid(row=2, column=0, sticky="we", padx=10, pady=10)

        # Create a checkbox for Allow All Bases For All option
        self.allow_all_bases_for_all_checkbox = CustomCheckButton(self.allow_all_bases_for_all_frame, text="Enable", command=allowAllBases)
        self.allow_all_bases_for_all_checkbox.pack(fill=tk.X, padx=10, pady=10)

        # Create a frame for Allow All Bases For Country option
        self.allow_all_bases_for_country_frame = LabelFrame(self, text="Allow All Bases For Country")
        self.allow_all_bases_for_country_frame.grid(row=3, column=0, sticky="we", padx=10, pady=10)

        # Create a checkbox for Allow All Bases For Country option
        self.allow_all_bases_for_country_checkbox = CustomCheckButton(self.allow_all_bases_for_country_frame, text="Enable")
        self.allow_all_bases_for_country_checkbox.pack(fill=tk.X, padx=10, pady=10)

        # Create a dropdown list for Allow All Bases For Country option
        countries = getAllSides()
        self.country_dropdown = CustomDropdown(self.allow_all_bases_for_country_frame, 'Country', countries, state="disabled", command=allowAllBasesForCountry)
        self.country_dropdown.pack(fill=tk.X, padx=10, pady=10)

        self.allow_all_bases_for_country_checkbox.add_dep(self.country_dropdown)
