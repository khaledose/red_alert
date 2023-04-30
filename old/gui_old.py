import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class GeneralTab(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.columnconfigure(0, weight=1)

        # Create a frame for Set Cost option
        self.set_cost_frame = ttk.LabelFrame(self, text="Set Cost")
        self.set_cost_frame.grid(row=0, column=0, sticky="we", padx=10, pady=10)

        # Create a CustomSlider for Set Cost option
        self.set_cost_slider = CustomSlider(self.set_cost_frame, "Set Cost", 1, 10000, 1)
        self.set_cost_slider.pack(fill="x", padx=10, pady=10)

        # Create a frame for Ore Mining option
        self.ore_mining_frame = ttk.LabelFrame(self, text="Ore Mining")
        self.ore_mining_frame.grid(row=1, column=0, sticky="we", padx=10, pady=10)

        # Create CustomSliders for Ore Mining option
        self.growth_slider = CustomSlider(self.ore_mining_frame, "Growth", 1, 1000, 1)
        self.growth_slider.pack(fill="x", padx=10, pady=10)

        self.growth_percentage_slider = CustomSlider(self.ore_mining_frame, "Growth Percentage", 0.01, 1, 0.01, True)
        self.growth_percentage_slider.pack(fill="x", padx=10, pady=10)

        self.spread_slider = CustomSlider(self.ore_mining_frame, "Spread", 1, 1000, 1)
        self.spread_slider.pack(fill="x", padx=10, pady=10)

        self.spread_percentage_slider = CustomSlider(self.ore_mining_frame, "Spread Percentage", 0.01, 1, 0.01, True)
        self.spread_percentage_slider.pack(fill="x", padx=10, pady=10)

        self.income_slider = CustomSlider(self.ore_mining_frame, "Income", 1, 1000, 1)
        self.income_slider.pack(fill="x", padx=10, pady=10)

        # Create a frame for Set Building Speed option
        self.set_building_speed_frame = ttk.LabelFrame(self, text="Set Building Speed")
        self.set_building_speed_frame.grid(row=2, column=0, sticky="we", padx=10, pady=10)

        # Create a CustomSlider for Set Building Speed option
        self.set_building_speed_slider = CustomSlider(self.set_building_speed_frame, "Set Building Speed", 0.01, 5, 0.01, True)
        self.set_building_speed_slider.pack(fill="x", padx=10, pady=10)

class BuildingsTab(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.columnconfigure(0, weight=1)

        # Create a frame for Set Building Adjacency option
        self.set_building_adjacency_frame = ttk.LabelFrame(self, text="Set Building Adjacency")
        self.set_building_adjacency_frame.grid(row=0, column=0, sticky="we", padx=10, pady=10)

        # Create a CustomSlider for Set Building Adjacency option
        self.set_building_adjacency_slider = CustomSlider(self.set_building_adjacency_frame, "Set Building Adjacency", 1, 500, initial_value=1)
        self.set_building_adjacency_slider.pack(fill="x", padx=10, pady=10)

        # Create a frame for Allow Auto Repair option
        self.allow_auto_repair_frame = ttk.LabelFrame(self, text="Allow Auto Repair")
        self.allow_auto_repair_frame.grid(row=1, column=0, sticky="we", padx=10, pady=10)

        # Create a checkbox for Allow Auto Repair option
        # self.allow_auto_repair_checkbox = tb.Checkbutton(master=self.allow_auto_repair_frame, bootstyle="round-toggle", text="Enable")
        self.allow_auto_repair_checkbox = ttk.Checkbutton(self.allow_auto_repair_frame, text="Enable")
        self.allow_auto_repair_checkbox.pack(fill="x", padx=10, pady=10)

        # Create a frame for Allow All Bases For All option
        self.allow_all_bases_for_all_frame = ttk.LabelFrame(self, text="Allow All Bases For All")
        self.allow_all_bases_for_all_frame.grid(row=2, column=0, sticky="we", padx=10, pady=10)

        # Create a checkbox for Allow All Bases For All option
        self.allow_all_bases_for_all_checkbox = ttk.Checkbutton(self.allow_all_bases_for_all_frame, text="Enable")
        self.allow_all_bases_for_all_checkbox.pack(fill="x", padx=10, pady=10)

        # Create a frame for Allow All Bases For Country option
        self.allow_all_bases_for_country_frame = ttk.LabelFrame(self, text="Allow All Bases For Country")
        self.allow_all_bases_for_country_frame.grid(row=3, column=0, sticky="we", padx=10, pady=10)

        # Create a checkbox for Allow All Bases For Country option
        self.allow_all_bases_for_country_checkbox = ttk.Checkbutton(self.allow_all_bases_for_country_frame, text="Enable", command=self.toggle_country_dropdown)
        self.allow_all_bases_for_country_checkbox.pack(fill="x", padx=10, pady=10)

        # Create a dropdown list for Allow All Bases For Country option
        countries = ['c1', 'c2']
        self.country_dropdown = CustomDropdown(self.allow_all_bases_for_country_frame, 'Country', countries)
        self.country_dropdown.pack(fill="x", padx=10, pady=10)

    def toggle_country_dropdown(self):
        if self.allow_all_bases_for_country_checkbox.instate(["selected"]):
            self.country_dropdown.configure(state="readonly")
        else:
            self.country_dropdown.configure(state="disabled")

class UnitsTab(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.columnconfigure(0, weight=1)

        # Create a frame for Set Units Speed Multiplier option
        self.set_units_speed_multiplier_frame = ttk.LabelFrame(self, text="Set Units Speed Multiplier")
        self.set_units_speed_multiplier_frame.grid(row=0, column=0, sticky="we", padx=10, pady=10)

        # Create a slider for Set Units Speed Multiplier option
        self.set_units_speed_multiplier_slider = CustomSlider(self.set_units_speed_multiplier_frame,
                                                                name="Units Speed Multiplier",
                                                                minimum=1,
                                                                maximum=50,
                                                                initial_value=1)
        self.set_units_speed_multiplier_slider.pack(fill="x", padx=10, pady=10)

        # Create a frame for Set Veteran Ratio option
        self.set_veteran_ratio_frame = ttk.LabelFrame(self, text="Set Veteran Ratio")
        self.set_veteran_ratio_frame.grid(row=1, column=0, sticky="we", padx=10, pady=10)

        # Create a slider for Set Veteran Ratio option
        self.set_veteran_ratio_slider = CustomSlider(self.set_veteran_ratio_frame,
                                                        name="Veteran Ratio",
                                                        minimum=1,
                                                        maximum=1000,
                                                        initial_value=1)
        self.set_veteran_ratio_slider.pack(fill="x", padx=10, pady=10)

        # Create a frame for Set Chrono Delay option
        self.set_chrono_delay_frame = ttk.LabelFrame(self, text="Set Chrono Delay")
        self.set_chrono_delay_frame.grid(row=2, column=0, sticky="we", padx=10, pady=10)

        # Create a slider for Set Chrono Delay option
        self.set_chrono_delay_slider = CustomSlider(self.set_chrono_delay_frame,
                                                        name="Chrono Delay",
                                                        minimum=0,
                                                        maximum=50,
                                                        initial_value=0,
                                                        is_float=True)
        self.set_chrono_delay_slider.pack(fill="x", padx=10, pady=10)

        # Create a frame for Remove Required Houses option
        self.remove_required_houses_frame = ttk.LabelFrame(self, text="Remove Required Houses")
        self.remove_required_houses_frame.grid(row=3, column=0, sticky="we", padx=10, pady=10)

        # Create a checkbox for Remove Required Houses option
        self.remove_required_houses_checkbox = ttk.Checkbutton(self.remove_required_houses_frame, text="Enable")
        self.remove_required_houses_checkbox.pack(fill="x", padx=10, pady=10)

        # Create a frame for Allow Commando option
        self.allow_commando_frame = ttk.LabelFrame(self, text="Allow Commando")
        self.allow_commando_frame.grid(row=4, column=0, sticky="we", padx=10, pady=10)

        # Create a checkbox for Allow Commando option
        self.allow_commando_checkbox = ttk.Checkbutton(self.allow_commando_frame, text="Enable")
        self.allow_commando_checkbox.pack(fill="x", padx=10, pady=10)

class SupersTab(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create the Allied Paradrop labelframe
        self.allied_paradrop_frame = ttk.LabelFrame(self, text="Allied Paradrop")
        self.allied_paradrop_frame.pack(padx=10, pady=10, fill=tk.X)

        # Create the Enable checkbox
        self.allied_checkbox = ttk.Checkbutton(self.allied_paradrop_frame, text="Enable", command=self.allied_checkbox_callback)
        self.allied_checkbox.pack(padx=10, pady=10, fill=tk.X)

        # Create the Unit Type dropdown list
        options = ["Option 1", "Option 2", "Option 3"]
        self.allied_unit_type_dropdown = CustomDropdown(self.allied_paradrop_frame, "Unit Type", options=options)
        self.allied_unit_type_dropdown.pack(padx=10, pady=10, fill=tk.X)

        # Create the slider for the number of units
        self.allied_unit_count_slider = CustomSlider(self.allied_paradrop_frame, "Unit Count", 1, 50, 25)
        self.allied_unit_count_slider.pack(padx=10, pady=10, fill=tk.X)

        # Create the Soviet Paradrop labelframe
        self.soviet_paradrop_frame = ttk.LabelFrame(self, text="Soviet Paradrop")
        self.soviet_paradrop_frame.pack(padx=10, pady=10, fill=tk.X)

        # Create the Enable checkbox
        self.soviet_checkbox = ttk.Checkbutton(self.soviet_paradrop_frame, text="Enable", command=self.soviet_checkbox_callback)
        self.soviet_checkbox.pack(padx=10, pady=10, fill=tk.X)

        # Create the Unit Type dropdown list
        options = ["Option 1", "Option 2", "Option 3"]
        self.soviet_unit_type_dropdown = CustomDropdown(self.soviet_paradrop_frame, "Unit Type", options=options)
        self.soviet_unit_type_dropdown.pack(padx=10, pady=10, fill=tk.X)

        # Create the slider for the number of units
        self.soviet_unit_count_slider = CustomSlider(self.soviet_paradrop_frame, "Unit Count", 1, 50, 25)
        self.soviet_unit_count_slider.pack(padx=10, pady=10, fill=tk.X)

        # Create the Yuri Paradrop labelframe
        self.yuri_paradrop_frame = ttk.LabelFrame(self, text="Yuri Paradrop")
        self.yuri_paradrop_frame.pack(padx=10, pady=10, fill=tk.X)

        # Create the Enable checkbox
        self.yuri_checkbox = ttk.Checkbutton(self.yuri_paradrop_frame, text="Enable", command=self.yuri_checkbox_callback)
        self.yuri_checkbox.pack(padx=10, pady=10, fill=tk.X)

        # Create the Unit Type dropdown list
        options = ["Option 1", "Option 2", "Option 3"]
        self.yuri_unit_type_dropdown = CustomDropdown(self.yuri_paradrop_frame, "Unit Type", options=options)
        self.yuri_unit_type_dropdown.pack(padx=10, pady=10, fill=tk.X)

        # Create the slider for the number of units
        self.yuri_unit_count_slider = CustomSlider(self.yuri_paradrop_frame, "Unit Count", 1, 50, 25)
        self.yuri_unit_count_slider.pack(padx=10, pady=10, fill=tk.X)

        # Create the Paradrop Cooldown labelframe
        self.paradrop_cooldown_frame = ttk.LabelFrame(self, text="Paradrop Cooldown")
        self.paradrop_cooldown_frame.pack(padx=10, pady=10, fill=tk.X)

        # Create the slider for the cooldown time
        self.cooldown_slider = CustomSlider(self.paradrop_cooldown_frame, "Cooldown Time", 0.1, 10, 5, is_float=True)
        self.cooldown_slider.pack(padx=10, pady=10, fill=tk.X)

    def allied_checkbox_callback(self):
        if self.allied_checkbox.instate(['selected']):
            self.allied_unit_type_dropdown.configure(state="readonly")
            self.allied_unit_count_slider.configure(state="normal")
        else:
            self.allied_unit_type_dropdown.configure(state="disabled")
            self.allied_unit_count_slider.configure(state="disabled")
    
    def soviet_checkbox_callback(self):
        if self.soviet_checkbox.instate(['selected']):
            self.soviet_unit_type_dropdown.configure(state="readonly")
            self.soviet_unit_count_slider.configure(state="normal")
        else:
            self.soviet_unit_type_dropdown.configure(state="disabled")
            self.soviet_unit_count_slider.configure(state="disabled")

    def yuri_checkbox_callback(self):
        if self.yuri_checkbox.instate(['selected']):
            self.yuri_unit_type_dropdown.configure(state="readonly")
            self.yuri_unit_count_slider.configure(state="normal")
        else:
            self.yuri_unit_type_dropdown.configure(state="disabled")
            self.yuri_unit_count_slider.configure(state="disabled")

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("My App")
        self.geometry("600x850")
        self.minsize(width=600, height=850)
        self.resizable(True, True)
        self.columnconfigure(0, weight=1)

        # Create a notebook with tabs
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        # Create frames for each tab
        self.general_frame = GeneralTab(self.notebook)
        self.buildings_frame = BuildingsTab(self.notebook)
        self.units_frame = UnitsTab(self.notebook)
        self.supers_frame = SupersTab(self.notebook)

        # Add tabs to the notebook
        self.notebook.add(self.general_frame, text="General")
        self.notebook.add(self.buildings_frame, text="Buildings")
        self.notebook.add(self.units_frame, text="Units")
        self.notebook.add(self.supers_frame, text="Supers")

        # Create a frame for buttons
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(side="bottom", fill="x")

        # Create a button for selecting game location
        self.game_location_button = ttk.Button(self.button_frame, text="Game Location", command=self.select_game_location)
        self.game_location_button.pack(side="left")

        # Create a label to show the selected game location
        self.game_location_label = ttk.Label(self.button_frame, text="No location selected")
        self.game_location_label.pack(side="left", padx=10)

        # Create a button to launch the game
        self.launch_game_button = ttk.Button(self.button_frame, text="Launch Game")
        self.launch_game_button.pack(side="right")

        # Create a button to save rules
        self.save_rules_button = ttk.Button(self.button_frame, text="Save Rules")
        self.save_rules_button.pack(side="right", padx=10)

    def select_game_location(self):
        # Open a file dialog to select a game location
        game_location = filedialog.askdirectory()
        if game_location:
            self.game_location_label.configure(text=game_location)

class CustomSlider(ttk.Frame):
    def __init__(self, master, name, minimum, maximum, initial_value, is_float=False):
        super().__init__(master)
        self.name = name
        self.minimum = minimum
        self.maximum = maximum
        self.value = initial_value
        self.is_float = is_float
        
        # Create the label for the name of the slider
        self.name_label = ttk.Label(self, text=name, width=20)  # Set a fixed width of 10
        self.name_label.pack(side=tk.LEFT, padx=10, pady=5, anchor=tk.W)
        
        # Create the slider
        self.slider = ttk.Scale(self, from_=minimum, to=maximum, value=initial_value, orient=tk.HORIZONTAL, command=self.slider_callback)
        self.slider.pack(fill=tk.X, padx=10, pady=10)
        
        # Create the label for the minimum value
        self.min_label = ttk.Label(self, text=str(minimum))
        self.min_label.pack(side=tk.LEFT)
        
        # Create the label for the maximum value
        self.max_label = ttk.Label(self, text=str(maximum))
        self.max_label.pack(side=tk.RIGHT)
        
        # Create the label for the selected value
        self.value_label = ttk.Label(self, text=str(initial_value))
        self.value_label.pack(side=tk.BOTTOM)
        
    def slider_callback(self, value):
        self.value = float(value)
        if not self.is_float:
            self.value = int(self.value)
            self.value_label.configure(text=str(self.value))
        else:
            self.value_label.configure(text=f"{self.value:.2f}")
    
    def configure(self, state):
        self.name_label.configure(state=state)
        self.slider.configure(state=state)

class CustomDropdown(ttk.Frame):
    def __init__(self, master, label_text, options):
        super().__init__(master)
        
        # Create label
        self.label = ttk.Label(self, text=label_text, width=20)
        self.label.grid(column=0, row=0, padx=5, pady=5)

        # Create dropdown list
        self.combo = ttk.Combobox(self, values=options)
        self.combo.grid(column=1, row=0, padx=5, pady=5)

    def get_selection(self):
        return self.combo.get()
    
    def configure(self, state):
        self.label.configure(state=state)
        self.combo.configure(state=state)

if __name__ == "__main__":
    app = App()
    app.mainloop()