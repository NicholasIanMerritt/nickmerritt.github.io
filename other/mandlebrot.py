import numpy as np
import matplotlib.pyplot as plt

# Define the function to generate the Mandelbrot set
def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

# Function to generate a grid of Mandelbrot set
def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return np.array([[mandelbrot(complex(r, i), max_iter) for r in r1] for i in r2])

# Initial parameters
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
width, height = 800, 800
max_iter = 256

# Generate the Mandelbrot set image
mandelbrot_img = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)

# Plot the Mandelbrot set
fig, ax = plt.subplots(figsize=(10, 10))
mandelbrot_plot = ax.imshow(mandelbrot_img, extent=(xmin, xmax, ymin, ymax), cmap='inferno')

# Function to update the plot based on zoom
def on_zoom(event):
    if event.inaxes != ax:
        return

    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    
    xmid = (xlim[0] + xlim[1]) / 2
    ymid = (ylim[0] + ylim[1]) / 2
    
    zoom_factor = 0.5
    dx = (xlim[1] - xlim[0]) * zoom_factor / 2
    dy = (ylim[1] - ylim[0]) * zoom_factor / 2
    
    xmin_new, xmax_new = xmid - dx, xmid + dx
    ymin_new, ymax_new = ymid - dy, ymid + dy
    
    mandelbrot_img_new = mandelbrot_set(xmin_new, xmax_new, ymin_new, ymax_new, width, height, max_iter)
    mandelbrot_plot.set_data(mandelbrot_img_new)
    mandelbrot_plot.set_extent([xmin_new, xmax_new, ymin_new, ymax_new])
    
    ax.set_xlim([xmin_new, xmax_new])
    ax.set_ylim([ymin_new, ymax_new])
    
    plt.draw()

# Connect the zoom event
fig.canvas.mpl_connect('button_press_event', on_zoom)

plt.show()
