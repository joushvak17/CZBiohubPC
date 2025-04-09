import tkinter as tk
import customtkinter as ctk
import matplotlib.pyplot as plt
import numpy as np
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from features import SineFunction, PowerFunction, SawtoothFunction


class Interface(tk.Tk):
    """Main interface for the CZ Biohub Function Graph Viewer.

    Args:
        tk (_type_): _description_
    """

    def __init__(self):
        super().__init__()

        # NOTE: Application main window properties
        self.title("CZ Biohub Function Graph Viewer")
        self.geometry("1100x600")
        self.resizable(False, False)
        self.configure(bg="#0F0F0F")

        # NOTE: Dictionary of the current functions
        self.function_dict = {
            func().name: func
            for func in (SineFunction, PowerFunction, SawtoothFunction)
        }

        # NOTE: Initial parameters
        self.param_a: float = 1.0
        self.param_b: float = 1.0
        self.x_min: float = -25.0
        self.x_max: float = 25.0
        self.x_res: int = 500
        self.current_function = None

        # NOTE: Application main frame
        app_frame = tk.Frame(self, bg="#0F0F0F")
        app_frame.pack(fill="both", expand=True, padx=5, pady=5)

        # NOTE: Entry frame
        entry_frame = ctk.CTkFrame(
            app_frame,
            fg_color="#222831",
            border_color="#FFFFFF",
            border_width=1,
            corner_radius=0,
        )
        
        # NOTE: Use pack propagate to prevent the frame from resizing and use fill="y"
        # This line was added through LLM usage, first entry in the LLM Usage section of the README.md
        entry_frame.pack(side="left", fill="y", padx=5, pady=5)
        entry_frame.pack_propagate(False)
        
        entry_label = ctk.CTkLabel(
            entry_frame,
            text="Entry Fields",
            text_color="#00ADB5",
            fg_color="#222831",
        )
        entry_label.pack(pady=1)

        entry_sep = ttk.Separator(entry_frame, orient="horizontal")
        entry_sep.pack(
            fill="x",
        )

        # NOTE: Function selection
        ctk.CTkLabel(
            entry_frame,
            text="Select Function:",
            text_color="#FFFFFF",
            fg_color="#222831",
        ).pack(anchor="w", padx=10, pady=1)

        # NOTE: Set the default function to the first one in the dictionary
        # This line was added through LLM usage, second entry in the LLM Usage section of the README.md
        self.function_var = tk.StringVar(value=list(self.function_dict.keys())[0])

        function_option = ctk.CTkOptionMenu(
            entry_frame,
            corner_radius=0,
            fg_color="#27548A",
            variable=self.function_var,
            values=list(self.function_dict.keys()),
            command=self.update_function,
        )
        function_option.pack(fill="x", padx=10, pady=(1, 5))

        top_sep = ttk.Separator(entry_frame, orient="horizontal")
        top_sep.pack(fill="x", pady=5)

        # NOTE: X min, X max, and X resolution entries
        x_min_frame = ctk.CTkFrame(
            entry_frame,
            fg_color="#222831",
            corner_radius=0,
        )
        x_min_frame.pack(fill="x", padx=5, pady=5)
        ctk.CTkLabel(
            x_min_frame,
            text="X Min:",
            text_color="#FFFFFF",
            fg_color="#222831",
        ).pack(side="left", padx=(10, 0), pady=1)
        self.x_min_var = tk.StringVar(value=self.x_min)
        x_min_entry = ctk.CTkEntry(
            x_min_frame,
            textvariable=self.x_min_var,
            corner_radius=0,
            border_color="#FFFFFF",
            text_color="#FFFFFF",
            border_width=1,
            width=50,
            fg_color="#27548A",
        )
        x_min_entry.pack(side="right", padx=(0, 10), pady=1)
        x_min_entry.bind("<Return>", lambda event: self.update_x_values())
        x_min_entry.bind("<FocusOut>", lambda event: self.update_x_values())

        x_max_frame = ctk.CTkFrame(
            entry_frame,
            fg_color="#222831",
            corner_radius=0,
        )
        x_max_frame.pack(fill="x", padx=5, pady=5)
        ctk.CTkLabel(
            x_max_frame,
            text="X Max:",
            text_color="#FFFFFF",
            fg_color="#222831",
        ).pack(side="left", padx=(10, 0), pady=1)
        self.x_max_var = tk.StringVar(value=self.x_max)
        x_max_entry = ctk.CTkEntry(
            x_max_frame,
            textvariable=self.x_max_var,
            corner_radius=0,
            border_color="#FFFFFF",
            text_color="#FFFFFF",
            border_width=1,
            width=50,
            fg_color="#27548A",
        )
        x_max_entry.pack(side="right", padx=(0, 10), pady=1)
        x_max_entry.bind("<Return>", lambda event: self.update_x_values())
        x_max_entry.bind("<FocusOut>", lambda event: self.update_x_values())

        x_res_frame = ctk.CTkFrame(
            entry_frame,
            fg_color="#222831",
            corner_radius=0,
        )
        x_res_frame.pack(fill="x", padx=5, pady=5)
        ctk.CTkLabel(
            x_res_frame,
            text="X Resolution:",
            text_color="#FFFFFF",
            fg_color="#222831",
        ).pack(side="left", padx=(10, 0), pady=1)
        self.x_res_var = tk.StringVar(value=self.x_res)
        x_res_entry = ctk.CTkEntry(
            x_res_frame,
            textvariable=self.x_res_var,
            corner_radius=0,
            border_color="#FFFFFF",
            text_color="#FFFFFF",
            border_width=1,
            width=50,
            fg_color="#27548A",
        )
        x_res_entry.pack(side="right", padx=(0, 10), pady=1)
        x_res_entry.bind("<Return>", lambda event: self.update_x_values())
        x_res_entry.bind("<FocusOut>", lambda event: self.update_x_values())

        mid_sep = ttk.Separator(entry_frame, orient="horizontal")
        mid_sep.pack(fill="x", pady=5)

        # NOTE: Parameter A and B entries
        param_a_frame = ctk.CTkFrame(
            entry_frame,
            fg_color="#222831",
            corner_radius=0,
        )
        param_a_frame.pack(fill="x", padx=5, pady=5)
        self.param_a_label = ctk.CTkLabel(
            param_a_frame,
            text="Parameter A:",
            text_color="#FFFFFF",
            fg_color="#222831",
        )
        self.param_a_label.pack(side="left", padx=(10, 0), pady=1)
        self.param_a_var = tk.StringVar(value=self.param_a)
        param_a_entry = ctk.CTkEntry(
            param_a_frame,
            textvariable=self.param_a_var,
            corner_radius=0,
            border_color="#FFFFFF",
            text_color="#FFFFFF",
            border_width=1,
            width=50,
            fg_color="#27548A",
        )
        param_a_entry.pack(side="right", padx=(0, 10), pady=1)
        param_a_entry.bind("<Return>", lambda event: self.update_parameters())
        param_a_entry.bind("<FocusOut>", lambda event: self.update_parameters())

        param_b_frame = ctk.CTkFrame(
            entry_frame,
            fg_color="#222831",
            corner_radius=0,
        )
        param_b_frame.pack(fill="x", padx=5, pady=5)
        self.param_b_label = ctk.CTkLabel(
            param_b_frame,
            text="Parameter B:",
            text_color="#FFFFFF",
            fg_color="#222831",
        )
        self.param_b_label.pack(side="left", padx=(10, 0), pady=1)
        self.param_b_var = tk.StringVar(value=self.param_b)
        param_b_entry = ctk.CTkEntry(
            param_b_frame,
            textvariable=self.param_b_var,
            corner_radius=0,
            border_color="#FFFFFF",
            text_color="#FFFFFF",
            border_width=1,
            width=50,
            fg_color="#27548A",
        )
        param_b_entry.pack(side="right", padx=(0, 10), pady=1)
        param_b_entry.bind("<Return>", lambda event: self.update_parameters())
        param_b_entry.bind("<FocusOut>", lambda event: self.update_parameters())

        bottom_sep = ttk.Separator(entry_frame, orient="horizontal")
        bottom_sep.pack(fill="x", pady=5)

        # NOTE: Plot frame
        plot_frame = ctk.CTkFrame(
            app_frame,
            fg_color="#222831",
            border_color="#FFFFFF",
            border_width=1,
            corner_radius=0,
            width=700,
            height=500,
        )
        plot_frame.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        plot_frame.pack_propagate(False)
        plot_label = ctk.CTkLabel(
            plot_frame,
            text="Function Plot",
            text_color="#00ADB5",
            fg_color="#222831",
        )
        plot_label.pack(pady=1)

        plot_sep = ttk.Separator(plot_frame, orient="horizontal")
        plot_sep.pack(
            fill="x",
        )

        # NOTE: Figure and canvas plotting
        plt.style.use("bmh")
        self.figure = plt.Figure(figsize=(6, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, plot_frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)

        # NOTE: Call the function update to set the initial function and plot
        self.update_function(self.function_var.get())

    def update_function(self, function):
        """Update and plot the current function based on the selected option.

        Args:
            function (_type_): _description_
        """
        if function not in self.function_dict:
            messagebox.showerror("Invalid Selection", "Please select a valid function.")
            return
        else:
            self.current_function = self.function_dict[function]()
            self.function_var.set(function)

            self.param_a_label.configure(text=self.current_function.param_a_desc + ":")
            self.param_b_label.configure(text=self.current_function.param_b_desc + ":")

            # NOTE: Reset the values for each function change
            self.x_min: float = -25.0
            self.x_max: float = 25.0
            self.x_res: float = 500
            self.x_min_var.set(str(self.x_min))
            self.x_max_var.set(str(self.x_max))
            self.x_res_var.set(str(self.x_res))

            self.param_a = self.current_function.default_param_a
            self.param_b = self.current_function.default_param_b
            self.param_a_var.set(str(self.param_a))
            self.param_b_var.set(str(self.param_b))

            self.plot_function()

    def update_parameters(self):
        """Update the parameters, A and B, based on the entry fields."""
        try:
            updated_param_a = float(self.param_a_var.get())
            updated_param_b = float(self.param_b_var.get())
            self.param_a = updated_param_a
            self.param_b = updated_param_b

            self.plot_function()
        except ValueError:
            messagebox.showerror(
                "Invalid Input", "Please enter valid numbers for parameters A and B."
            )

            self.param_a_var.set(str(self.param_a))
            self.param_b_var.set(str(self.param_b))

    def update_x_values(self):
        """Update the X min, X max, and X resolution based on the entry fields."""
        try:
            updated_x_min = float(self.x_min_var.get())
            updated_x_max = float(self.x_max_var.get())
            updated_x_res = int(self.x_res_var.get())

            if updated_x_min >= updated_x_max:
                raise ValueError("X Min must be less than X Max.")
            if updated_x_res <= 0:
                raise ValueError("X Resolution must be a positive integer.")

            self.x_min = updated_x_min
            self.x_max = updated_x_max
            self.x_res = updated_x_res

            self.plot_function()
        except ValueError as e:
            messagebox.showerror(
                "Invalid Input", f"Please enter valid values for X range: {e}"
            )

            self.x_min_var.set(str(self.x_min))
            self.x_max_var.set(str(self.x_max))
            self.x_res_var.set(str(self.x_res))

    def plot_function(self):
        """Plot the selected function with the given parameters."""
        if self.current_function is None:
            return
        else:
            self.figure.clear()

            x_values = np.linspace(self.x_min, self.x_max, self.x_res)
            y_values = self.current_function.calculate(
                x_values, self.param_a, self.param_b
            )

            self.ax = self.figure.add_subplot(111)
            self.ax.plot(x_values, y_values, color="#00ADB5")

            self.ax.set_title(f"{self.current_function.name}")
            self.ax.set_xlabel("X")
            self.ax.set_ylabel("Y")
            self.ax.legend([f"(A={self.param_a}, B={self.param_b})"])
            self.ax.grid(True)

            self.canvas.draw()


if __name__ == "__main__":
    app = Interface()
    app.mainloop()
