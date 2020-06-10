# Author:        Janek Groß
# Created:       June 10th 2020

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

def matplotlib_figure_to_rgb(figure, grayscale = False):
    """
    Converts a matplotlib figure into a 3-channel numpy array.
    Figures are returned by
    gcf(), figure() or subplots() can be used as input.
    ---------------------------------------------------
    Arguments:
    figure:      matplotlib figure
    grayscale:   whether to return a grayscale image

    returns:
    color_array: a numpy integer array of shape 
               (height,width,3) or (height, width)
    """
    # calling this method ensures that the plot is rendered
    figure.canvas.draw()
    
    rgb_array = np.frombuffer(figure.canvas.tostring_rgb(), dtype='uint8').astype('int')
    color_array = rgb_array.reshape(figure.canvas.get_width_height()[::-1] + (3,))
    
    if grayscale:
        color_array = np.round(np.mean(color_array, axis = -1)).astype('int')
    return color_array
    
def gif_from_color_array(color_array, scale = 1,
                         filename = 'test.gif', fps = 2, frame_labels = False):
    """
    Creates an animated *.gif file from a tensor containing 3 channel rgb color images or
    1 channel or grayscale images.
    --------------------------------------------------------------------------
    Arguments:
    color_array:        numpy array of shape (number_of_frames, width, height, 3_color_channels) or
                        (number_of_frames, width, height) for grayscale images.
    scale:              int or float scaling factor determines the size of the image.
                        The number of pixels per inch is 100/scale.
    filename:           A string usually ending with '.gif'.
    fps:                int or float frames per second determine the speed of the animation. 
    frame_labels:       Boolean value determines whether to print a red frame number top left.
    """
    
    if len(color_array.shape) == 4 and color_array.shape[-1] == 3:
        cmap = None  
    elif len(color_array.shape) == 3:
        cmap = 'gray'
    else:
        raise Exception("wrong shape: expected color_array of shape (n,w,h,3) or (n,w,h)")
        
    n = color_array.shape[0]
    size = color_array.shape[1:3]
        
    fig = plt.figure(figsize = (size[0] / 100 * scale, size[1] / 100 * scale))
    ax = fig.add_axes([0, 0, 1, 1], frameon=False, aspect=1)
    ax.set_xticks([])
    ax.set_yticks([])
    
    artists = []
    
    for i in range(n):
        image = plt.imshow(color_array[i], cmap=cmap, vmin=0, vmax=255, animated=True)
        if frame_labels:
            label = str(i)
        else:
            label = ''        
        frame_number = plt.text(0.04*size[0], 0.08*size[0], label, color = 'red',
                                size = 0.0005*size[0]*size[1]*scale)
        artists += [[image, frame_number]]
        
    animation = anim.ArtistAnimation(fig, artists)
    animation.save(filename, writer='imagemagick', fps=fps)
