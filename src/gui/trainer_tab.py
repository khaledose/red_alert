from .custom_widgets import CustomSlider, CustomDropdown, CustomCheckbutton
from ttkbootstrap.widgets import Frame, LabelFrame
from src.actions.readers import getAllInfantries
from src.actions.trainer import instant_build, unlimited_energy, set_money, set_tech_level, train_elites, reveal_map, allied_stolen_tech, soviet_stolen_tech, yuri_stolen_tech, foehn_stolen_tech, build_anywhere
import tkinter as tk

class TrainerTab(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create the Allied Paradrop labelframe
        self.general_frame = LabelFrame(self, text="General")
        self.general_frame.pack(padx=10, pady=5, fill=tk.X)

        # Create the Enable checkbox
        self.reveal_map_checkbox = CustomCheckbutton(self.general_frame, text="Reveal Map", command=reveal_map)
        self.reveal_map_checkbox.pack(padx=10, pady=5, fill=tk.X)

        self.money_slider = CustomSlider(self.general_frame, "Money", 0, 100000, 0, command=set_money)
        self.money_slider.pack(padx=10, pady=5, fill=tk.X)

        # Create the Allied Paradrop labelframe
        self.build_frame = LabelFrame(self, text="Building")
        self.build_frame.pack(padx=10, pady=5, fill=tk.X)

        # Create the Enable checkbox
        self.instant_build_checkbox = CustomCheckbutton(self.build_frame, text="Instant Build", command=instant_build)
        self.instant_build_checkbox.pack(padx=10, pady=5, fill=tk.X)

        self.build_anywhere_checkbox = CustomCheckbutton(self.build_frame, text="Build Anywhere", command=build_anywhere)
        self.build_anywhere_checkbox.pack(padx=10, pady=5, fill=tk.X)

        self.elites_checkbox = CustomCheckbutton(self.build_frame, text="Elites", command=train_elites)
        self.elites_checkbox.pack(padx=10, pady=5, fill=tk.X)

        self.tech_level_slider = CustomSlider(self.build_frame, "Tech Level", 1, 10, 0, command=set_tech_level)
        self.tech_level_slider.pack(padx=10, pady=5, fill=tk.X)

        # Create the Allied Paradrop labelframe
        self.energy_frame = LabelFrame(self, text="Energy")
        self.energy_frame.pack(padx=10, pady=5, fill=tk.X)

        # Create the Enable checkbox
        self.unlimited_energy_checkbox = CustomCheckbutton(self.energy_frame, text="Unlimited Energy", command=unlimited_energy)
        self.unlimited_energy_checkbox.pack(padx=10, pady=5, fill=tk.X)

        # Create the Allied Paradrop labelframe
        self.stolen_tech_frame = LabelFrame(self, text="Stolen Tech")
        self.stolen_tech_frame.pack(padx=10, pady=5, fill=tk.X)

        # Create the Enable checkbox
        self.allied_tech_checkbox = CustomCheckbutton(self.stolen_tech_frame, text="Allied", command=allied_stolen_tech)
        self.allied_tech_checkbox.pack(padx=10, pady=5, fill=tk.X)

        self.soviet_tech_checkbox = CustomCheckbutton(self.stolen_tech_frame, text="Soviet", command=soviet_stolen_tech)
        self.soviet_tech_checkbox.pack(padx=10, pady=5, fill=tk.X)

        self.yuri_tech_checkbox = CustomCheckbutton(self.stolen_tech_frame, text="Yuri", command=yuri_stolen_tech)
        self.yuri_tech_checkbox.pack(padx=10, pady=5, fill=tk.X)

        self.foehn_tech_checkbox = CustomCheckbutton(self.stolen_tech_frame, text="Foehn", command=foehn_stolen_tech)
        self.foehn_tech_checkbox.pack(padx=10, pady=5, fill=tk.X)

        # # Create the Unit Type dropdown list
        # self.allied_unit_type_dropdown = CustomDropdown(self.allied_paradrop_frame, "Unit Type", options=infantries, state="disabled", command=setAlliedParaDropUnit)
        # self.allied_unit_type_dropdown.pack(padx=10, pady=5, fill=tk.X)

        # # Create the slider for the number of units
        # self.allied_unit_count_slider = CustomSlider(self.allied_paradrop_frame, "Unit Count", 1, 50, 25, command=setAlliedParaDropCount)
        # self.allied_unit_count_slider.pack(padx=10, pady=5, fill=tk.X)

        # self.allied_checkbox.add_dep(self.allied_unit_type_dropdown)
        # self.allied_checkbox.add_dep(self.allied_unit_count_slider)

        # # Create the Soviet Paradrop labelframe
        # self.soviet_paradrop_frame = LabelFrame(self, text="Soviet Paradrop")
        # self.soviet_paradrop_frame.pack(padx=10, pady=5, fill=tk.X)

        # # Create the Enable checkbox
        # self.soviet_checkbox = CustomCheckbutton(self.soviet_paradrop_frame, text="Enable", command=allowSovietParaDrop)
        # self.soviet_checkbox.pack(padx=10, pady=5, fill=tk.X)

        # # Create the Unit Type dropdown list
        # self.soviet_unit_type_dropdown = CustomDropdown(self.soviet_paradrop_frame, "Unit Type", options=infantries, state="disabled", command=setSovietParaDropUnit)
        # self.soviet_unit_type_dropdown.pack(padx=10, pady=5, fill=tk.X)

        # # Create the slider for the number of units
        # self.soviet_unit_count_slider = CustomSlider(self.soviet_paradrop_frame, "Unit Count", 1, 50, 25, command=setSovietParaDropCount)
        # self.soviet_unit_count_slider.pack(padx=10, pady=5, fill=tk.X)

        # self.soviet_checkbox.add_dep(self.soviet_unit_type_dropdown)
        # self.soviet_checkbox.add_dep(self.soviet_unit_count_slider)

        # # Create the Yuri Paradrop labelframe
        # self.yuri_paradrop_frame = LabelFrame(self, text="Yuri Paradrop")
        # self.yuri_paradrop_frame.pack(padx=10, pady=5, fill=tk.X)

        # # Create the Enable checkbox
        # self.yuri_checkbox = CustomCheckbutton(self.yuri_paradrop_frame, text="Enable", command=allowYuriParaDrop)
        # self.yuri_checkbox.pack(padx=10, pady=5, fill=tk.X)

        # # Create the Unit Type dropdown list
        # self.yuri_unit_type_dropdown = CustomDropdown(self.yuri_paradrop_frame, "Unit Type", options=infantries, state="disabled", command=setYuriParaDropUnit)
        # self.yuri_unit_type_dropdown.pack(padx=10, pady=5, fill=tk.X)

        # # Create the slider for the number of units
        # self.yuri_unit_count_slider = CustomSlider(self.yuri_paradrop_frame, "Unit Count", 1, 50, 25, command=setYuriParaDropCount)
        # self.yuri_unit_count_slider.pack(padx=10, pady=5, fill=tk.X)

        # self.yuri_checkbox.add_dep(self.yuri_unit_type_dropdown)
        # self.yuri_checkbox.add_dep(self.yuri_unit_count_slider)

        # # Create the Paradrop Cooldown labelframe
        # self.paradrop_cooldown_frame = LabelFrame(self, text="Paradrop Cooldown")
        # self.paradrop_cooldown_frame.pack(padx=10, pady=5, fill=tk.X)

        # # Create the slider for the cooldown time
        # self.cooldown_slider = CustomSlider(self.paradrop_cooldown_frame, "Cooldown Time", 0.1, 10, 5, is_float=True, command=setParaDropCooldown)
        # self.cooldown_slider.pack(padx=10, pady=5, fill=tk.X)