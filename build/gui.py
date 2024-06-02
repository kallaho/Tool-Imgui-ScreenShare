import tkinter as tk
from tkinter import Canvas, Entry, PhotoImage
from tkinter.messagebox import showinfo
from pathlib import Path
import math

# Paths configuration
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Kallaho\Desktop\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Function to center the window on the screen
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

# Function to allow window dragging
def on_press(event):
    window.x = event.x
    window.y = event.y

def on_drag(event):
    x = window.winfo_pointerx() - window.x
    y = window.winfo_pointery() - window.y
    window.geometry(f'+{x}+{y}')

# Function to handle Enter key press on the entry field
def on_enter(event):
    pin = entry_1.get()
    if pin == "your_pin_here":  # Put your pin validation logic here
        window.destroy()  # Close the first form
        open_second_form()
    else:
        showinfo("Invalid Pin", "Please enter a valid PIN.")

# Placeholder function to search for strings/APIs
def perform_search():
    print("Searching...")  # Replace this with your search logic

# Function to open the second form
def open_second_form():
    second_window = tk.Tk()
    second_window_width = 559
    second_window_height = 300
    center_window(second_window, second_window_width, second_window_height)
    second_window.configure(bg="#243253")  # Set background color
    second_window.overrideredirect(True)  # Hide the title bar
    
    # Load background image for the second form
    bg_image = PhotoImage(file=relative_to_assets("image_11.png"))

    # Create a canvas for the second form
    second_canvas = Canvas(
        second_window,
        bg="#243253",
        height=300,
        width=559,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    second_canvas.place(x=0, y=0)
    
    # Add background image to the canvas
    second_canvas.create_image(0, 0, anchor="nw", image=bg_image)
    
    # Function to allow window dragging for the second form
    def on_press_second(event):
        second_window.x = event.x
        second_window.y = event.y

    def on_drag_second(event):
        x = second_window.winfo_pointerx() - second_window.x
        y = second_window.winfo_pointery() - second_window.y
        second_window.geometry(f'+{x}+{y}')
    
    # Bind mouse events for dragging to the canvas of the second form
    second_canvas.bind("<ButtonPress-1>", on_press_second)
    second_canvas.bind("<B1-Motion>", on_drag_second)

    # Loading animation
    def create_loading_animation(canvas, x, y, radius, num_dots, dot_radius):
        angle = 360 / num_dots
        dots = []
        for i in range(num_dots):
            dot_x = x + radius * math.cos(math.radians(i * angle))
            dot_y = y + radius * math.sin(math.radians(i * angle))
            dot = canvas.create_oval(
                dot_x - dot_radius, dot_y - dot_radius, dot_x + dot_radius, dot_y + dot_radius, fill="white"
            )
            dots.append(dot)
        return dots

    def rotate_dots(canvas, dots, angle_step):
        for dot in dots:
            coords = canvas.coords(dot)
            x_center = (coords[0] + coords[2]) / 2
            y_center = (coords[1] + coords[3]) / 2

            x = x_center - 279.5  # Center of the canvas
            y = y_center - 150  # Center of the canvas

            new_x = x * math.cos(math.radians(angle_step)) - y * math.sin(math.radians(angle_step)) + 279.5
            new_y = x * math.sin(math.radians(angle_step)) + y * math.cos(math.radians(angle_step)) + 150

            canvas.move(dot, new_x - x_center, new_y - y_center)

    loading_dots = create_loading_animation(second_canvas, 279.5, 150, 50, 12, 5)
    angle_step = 5

    def animate_loading():
        rotate_dots(second_canvas, loading_dots, angle_step)
        second_window.after(50, animate_loading)

    # Start the loading animation
    animate_loading()

    # Add label for changing text
    status_label = tk.Label(second_window, text="Searching...", font=("Helvetica", 14), bg="#243253", fg="white")
    status_label.place(x=second_window_width/2 + 2, y=250, anchor="center")

    # Function to update the status label
    def update_status_label():
        current_text = status_label.cget("text")
        if current_text == "Searching...":
            new_text = "Scanning..."
        else:
            new_text = "Searching..."
        status_label.config(text=new_text)
        second_window.after(2000, update_status_label)  # Change text every 2 seconds

    # Start updating the status label
    update_status_label()

    # Perform the search after showing the animation and status label update
    second_window.after(2000, perform_search)  # Simulate search delay

    second_window.mainloop()

# Create the main window (first form)
window = tk.Tk()
window_width = 559
window_height = 300
center_window(window, window_width, window_height)
window.configure(bg="#243253")  # Change window background color
window.overrideredirect(True)  # Hide the title bar

# Bind mouse events for dragging
window.bind("<ButtonPress-1>", on_press)
window.bind("<B1-Motion>", on_drag)

# Create a canvas for the first form
canvas = Canvas(
    window,
    bg="#243253",
    height=300,
    width=559,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Add elements to the first form canvas
canvas.create_rectangle(
    0.0,
    0.0,
    559.0,
    19.0,
    fill="#111222",
    outline=""
)

canvas.create_rectangle(
    0.0,
    293.0,
    559.0,
    300.0,
    fill="#C2C5CD",
    outline=""
)

canvas.create_text(
    3.0,
    276.0,
    anchor="nw",
    text="v2.6",
    fill="#FFFFFF",
    font=("Inter SemiBold", 12)
)

entry_1 = Entry(
    bd=0,
    bg="#2B395D",
    fg="#FFFFFF",
    highlightthickness=0
)
entry_1.place(
    x=130.0,
    y=204.0,
    width=202.0,
    height=40.0
)

canvas.create_text(
    161.0,
    183.0,
    anchor="nw",
    text="Enter The pin.",
    fill="#FFFFFF",
    font=("JosefinSansRoman SemiBold", 11)
)

image_image_10 = PhotoImage(file=relative_to_assets("image_10.png"))
canvas.create_image(280.0, 150.0, image=image_image_10)

# Bind Enter key press event to the entry field
entry_1.bind("<Return>", on_enter)

window.resizable(False, False)
window.mainloop()
