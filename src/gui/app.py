from ttkbootstrap.widgets import Frame, Button, Label, Notebook
from buildings_tab import BuildingsTab
from general_tab import GeneralTab
from supers_tab import SupersTab
from units_tab import UnitsTab
from trainer_tab import TrainerTab
from tkinter import filedialog
from ttkbootstrap import Style
import tkinter as tk
from kink import di

class CustomWindowBar(Frame):
    def __init__(self, master, icon_path, title, max_icon_size=(20, 20)):
        super().__init__(master, height=30)

        # Load the icon image
        icon = tk.PhotoImage(file=icon_path)

        # Resize the image if it exceeds the maximum size
        if icon.width() > max_icon_size[0] or icon.height() > max_icon_size[1]:
            icon = icon.subsample(
                max(1, icon.width() // max_icon_size[0]), 
                max(1, icon.height() // max_icon_size[1])
            )

        # Create the icon label
        icon_label = Label(self, image=icon)
        icon_label.image = icon
        icon_label.pack(side='left', padx=5)

        # Create the title label
        title_label = Label(self, text=title, style='Title.TLabel')
        title_label.pack(side='left', padx=10, pady=5)

        # Create the exit button
        exit_button = Button(self, text='X', style='TButton', command=master.destroy)
        exit_button.pack(side='right', padx=5)

        # Create the expand button
        expand_button = Button(self, text='[]', style='TButton', command=self.toggle_expand)
        expand_button.pack(side='right', padx=5)

        # Create the minimize button
        min_button = Button(self, text='-', style='TButton', command=self.minimize_window)
        min_button.pack(side='right', padx=5)

        # Bind the window bar to the drag event
        self.bind('<B1-Motion>', self.drag_window)

        # Initialize the expand state
        self.expand_state = False

    def toggle_expand(self):
        if not self.expand_state:
            self.master.state('zoomed')
            self.expand_state = True
        else:
            self.master.state('normal')
            self.expand_state = False

        self.update_expand_button()

    def update_expand_button(self):
        if self.expand_state:
            self.children['!button2']['text'] = '[]'
        else:
            self.children['!button2']['text'] = '[]'

    def drag_window(self, event):
        self.after(10, self._drag_window, event)

    def _drag_window(self, event):
        self.master.update_idletasks()
        self.master.overrideredirect(True)
        self.master.geometry(f'+{event.x_root - self.winfo_rootx()}+{event.y_root - self.winfo_rooty()}')
        self.master.overrideredirect(False)

    def minimize_window(self):
        self.master.wm_state('iconic')

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("My App")
        self.geometry("600x750")
        self.minsize(width=600, height=750)
        self.resizable(True, True)
        self.columnconfigure(0, weight=1)
        # self.overrideredirect(True)

        # Create a ttkbootstrap style object
        style = Style(theme='darkly')
        style.theme_use()

        # window_bar = CustomWindowBar(self, 'icon.png', 'Custom Window Bar')
        # window_bar.pack(fill='x', side='top')

        # Create a notebook with tabs
        self.notebook = Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        # Create frames for each tab
        self.general_frame = GeneralTab(self.notebook)
        self.buildings_frame = BuildingsTab(self.notebook)
        self.units_frame = UnitsTab(self.notebook)
        self.supers_frame = SupersTab(self.notebook)
        self.trainer_frame = TrainerTab(self.notebook)

        # Add tabs to the notebook
        self.notebook.add(self.general_frame, text="General")
        self.notebook.add(self.buildings_frame, text="Buildings")
        self.notebook.add(self.units_frame, text="Units")
        self.notebook.add(self.supers_frame, text="Supers")
        self.notebook.add(self.trainer_frame, text="Trainer")

        # Create a frame for buttons
        self.button_frame = Frame(self)
        self.button_frame.pack(side="bottom", fill="x", padx=10, pady=10)

        # Create a button for selecting game location
        self.game_location_button = Button(self.button_frame, text="Game Location", command=self.select_game_location)
        self.game_location_button.pack(side="left", padx=(0, 10))

        # Create a label to show the selected game location
        self.game_location_label = Label(self.button_frame, text="No location selected")
        self.game_location_label.pack(side="left")

        # Create a button to launch the game
        self.launch_game_button = Button(self.button_frame, text="Launch Game", command=di['config'].launchGame)
        self.launch_game_button.pack(side="right", padx=(10, 0))

        # Create a button to save rules
        self.save_rules_button = Button(self.button_frame, text="Save Rules", command=di['config'].saveConfig)
        self.save_rules_button.pack(side="right", padx=(0, 10))

    def select_game_location(self):
        # Open a file dialog to select a game location
        game_location = filedialog.askdirectory()
        if game_location:
            di['config'].setGameDir(game_location)
            self.game_location_label.configure(text=game_location)