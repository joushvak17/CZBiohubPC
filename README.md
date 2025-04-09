# CZBiohubPC
## How to run the program
Run the following commands in order to run the program:
```
git clone https://github.com/joushvak17/CZBiohubPC.git
cd CZBiohubPC
pip install -r requirements.txt
python interface.py
```
Prior to running these commands, you would need to activate an env that has Python=>3.9 and pip.
## LLM Usage
The use of large language models as a coding assistant was mainly used to help identify certain bugs/issues that became apparent when testing the interface. The following shows the prompts that were given and a short form response the LLM gave, along with the generated lines of code:

First Question: When I select different functions like sine and power, the frames keep resizing. I am sure it is the plot frame, since when I select the sine function, the entry frame is larger, but then I select the power function and then the plot frame is larger?

Response: Use pack_propagate(False): You're already using this for the plot frame, but you should also apply it to the entry frame to prevent it from resizing based on its contents.  
```
# Entry frame
entry_frame = ctk.CTkFrame(
    app_frame,
    fg_color="#222831",
    border_color="#FFFFFF",
    border_width=1,
    corner_radius=0,
    width=300  # Set a fixed width
)
entry_frame.pack(side="left", fill="y", padx=5, pady=5)  # Use fill="y" instead of fill="both"
entry_frame.pack_propagate(False)  # Prevent resizing based on contents
```

Second Question: How can I set the user interface so the first function along with the default parameters are initially set?    

Response: Set the default function in the function_var StringVar during initialization.  
```
class Interface(tk.Tk):
    """Main interface for the CZ Biohub Function Graph Viewer."""

    def __init__(self):
        super().__init__()

        # [Previous initialization code remains the same until function_dict creation...]

        # Dictionary of the current functions
        self.function_dict = {
            func().name: func
            for func in (
                SineFunction,
                PowerFunction,
            )
        }

        # Set the default function to the first one in the dictionary
        first_function_name = list(self.function_dict.keys())[0]
        self.function_var = tk.StringVar(value=first_function_name)
        
        # [Rest of your initialization code remains the same until before the update_function call...]

        # Initialize with the first function
        self.update_function(first_function_name)
```
The source files, specifically the interface.py file, should have comments that state which lines use the LLM generated codes as an example for dealing with the bugs/issues that I faced.