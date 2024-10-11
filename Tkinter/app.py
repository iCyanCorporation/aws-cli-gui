import tkinter as tk
from tkinter import messagebox
import subprocess

# Function to execute AWS CLI command
def run_aws_command():
    profile = profile_entry.get()
    region = region_entry.get()
    command = command_entry.get()
    
    # Construct AWS CLI command with profile and region
    aws_command = f"aws {command} --profile {profile} --region {region}"
    
    try:
        result = subprocess.check_output(aws_command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        output_textbox.delete(1.0, tk.END)
        output_textbox.insert(tk.END, result)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Command failed: {e.output}")

# GUI setup
root = tk.Tk()
root.title("AWS CLI GUI")

# Profile label and entry
profile_label = tk.Label(root, text="AWS Profile:")
profile_label.grid(row=0, column=0, padx=10, pady=5)
profile_entry = tk.Entry(root)
profile_entry.grid(row=0, column=1, padx=10, pady=5)

# Region label and entry
region_label = tk.Label(root, text="AWS Region:")
region_label.grid(row=1, column=0, padx=10, pady=5)
region_entry = tk.Entry(root)
region_entry.grid(row=1, column=1, padx=10, pady=5)

# Command label and entry
command_label = tk.Label(root, text="AWS CLI Command:")
command_label.grid(row=2, column=0, padx=10, pady=5)
command_entry = tk.Entry(root, width=50)
command_entry.grid(row=2, column=1, padx=10, pady=5)

# Button to execute the command
run_button = tk.Button(root, text="Run Command", command=run_aws_command)
run_button.grid(row=3, column=1, padx=10, pady=5)

# Textbox to display output
output_textbox = tk.Text(root, height=10, width=60)
output_textbox.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI
root.mainloop()
