
from ttkbootstrap.widgets import Frame, Label, Scale, Combobox, Checkbutton
import tkinter as tk

class CustomSlider(Frame):
    def __init__(self, master, name, minimum, maximum, initial_value, command=None, is_float=False):
        super().__init__(master)
        self.name = name
        self.minimum = minimum
        self.maximum = maximum
        self.value = initial_value
        self.is_float = is_float
        
        # Create the label for the name of the slider
        self.name_label = Label(self, text=name, width=20)  # Set a fixed width of 10
        self.name_label.pack(side=tk.LEFT, padx=10, pady=5, anchor=tk.W)
        
        # Create the slider
        self.slider = Scale(self, from_=minimum, to=maximum, value=initial_value, orient=tk.HORIZONTAL, command=self.slider_callback)
        self.slider.pack(fill=tk.X, padx=10, pady=10)
        
        # Create the label for the minimum value
        self.min_label = Label(self, text=str(minimum))
        self.min_label.pack(side=tk.LEFT)
        
        # Create the label for the maximum value
        self.max_label = Label(self, text=str(maximum))
        self.max_label.pack(side=tk.RIGHT)
        
        # Create the label for the selected value
        self.value_label = Label(self, text=str(initial_value))
        self.value_label.pack(side=tk.BOTTOM)

        self.action = command
        
    def slider_callback(self, value):
        self.value = float(value)
        if not self.is_float:
            self.value = int(self.value)
            self.value_label.configure(text=str(self.value))
        else:
            self.value_label.configure(text=f"{self.value:.2f}")
        if self.action is not None:
            self.action(self.value)
    
    def set_state(self, state):
        self.name_label.configure(state=state)
        self.slider.configure(state=state)

class CustomDropdown(Frame):
    def __init__(self, master, label_text, options, state="readonly", command=None):
        super().__init__(master)
        
        # Create label
        self.label = Label(self, text=label_text, width=20)
        self.label.pack(side=tk.LEFT, padx=10, pady=5, anchor=tk.W)

        # Create dropdown list
        self.combo = Combobox(self, values=options, state=state)
        self.combo.pack(fill=tk.X, padx=10, pady=10, anchor=tk.E)

        self.combo.bind("<<ComboboxSelected>>", self.dropdown_callback)

        self.action = command

    def get_selection(self):
        return self.combo.get()
    
    def set_state(self, state):
        self.label.configure(state=state)
        self.combo.configure(state=state)

    def dropdown_callback(self, event):
        if self.action is not None:
            self.action(self.get_selection())

class CustomCheckButton(Frame):
    def __init__(self, master, text="Text", command=None):
        super().__init__(master)
        
        # Create label
        self.label = Label(self, text=text, width=20)
        self.label.pack(side=tk.LEFT, padx=10, pady=5, anchor=tk.W)

        self.var = tk.BooleanVar()
        self.action = command

        # Create dropdown list
        self.check = Checkbutton(self, bootstyle="round-toggle", variable=self.var, command=self.checkbutton_callback)
        self.check.pack(fill=tk.X, padx=10, pady=10, anchor=tk.E, side=tk.RIGHT)

        self.deps = []
    
    def checkbutton_callback(self):
        for widget in self.deps:
            if self.var.get():
                widget.set_state(state="readonly")
            else:
                widget.set_state(state="disabled")

        if self.action is not None:
            self.action(self.var.get())
    
    def add_dep(self, widget):
        self.deps.append(widget)
