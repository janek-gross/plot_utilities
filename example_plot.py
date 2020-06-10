# Author:        Janek Groß
# Created:       June 10th 2020

# This program demonstrates the plot utilities functionality by
# recursively plotting axis image and creating an animated gif.

from plot_utilities import *

depth = 10
fig = plt.figure(figsize=(4,4))

plt.imshow(np.ones((400,400))*255, cmap = 'gray', vmin=0, vmax=255)
image_shape = matplotlib_figure_to_rgb(fig, grayscale=True).shape
grayscale_array = np.zeros((depth, *image_shape))

for i in range(depth):
    fig = plt.gcf()
    grayscale_array[i] = matplotlib_figure_to_rgb(fig, grayscale=True)
    plt.imshow(grayscale_array[i], cmap = 'gray')
    
gif_from_color_array(grayscale_array, scale = 3)
