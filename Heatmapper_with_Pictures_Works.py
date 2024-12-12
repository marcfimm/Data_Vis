import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


def generate_heatmap_with_images(csv_file_path, heatmap_title, images):
    """
    Generates a heatmap with images placed in the upper-right corner of each cell.

    Args:
        csv_file_path (str): Path to the CSV file containing heatmap data.
        heatmap_title (str): Title of the heatmap.
        images (list): List of dictionaries with image paths and their corresponding row/col positions.
    """
    # Read data from the CSV file
    with open(csv_file_path, 'r') as file:
        content = file.read().strip().split('\n\n')
        color_data = pd.read_csv(pd.io.common.StringIO(content[0]), index_col=0)
        annotation_data = pd.read_csv(pd.io.common.StringIO(content[1]), index_col=0)

    if color_data.shape != annotation_data.shape:
        raise ValueError("Color data and annotation data must have the same dimensions")

    # Set the color bar range from 0 to 100
    vmin, vmax = 0, 100
    
    # Define the custom colormap (cut off the top 25% of 'viridis')
    original_cmap = plt.cm.viridis
    n_colors = original_cmap.N
    cutoff = int(n_colors * 0.75)  # 75% of the colormap
    colors = original_cmap(np.linspace(0, 0.75, cutoff))  # Extract first 75%
    custom_cmap = ListedColormap(colors)

    

        # Plot the heatmap with fixed vmin and vmax
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(
        color_data,
        annot=annotation_data,
        fmt="d",
        cmap=custom_cmap,
        annot_kws={"size": 10},
        vmin=vmin,
        vmax=vmax,
        cbar_kws={"ticks": np.linspace(vmin, vmax, num=6)}  # Fixed color bar ticks from 0 to 100
    )
    plt.title(heatmap_title, fontsize=16)

    # Remove ticks on the left and bottom
    ax.tick_params(left=False, bottom=False)
    
    # Remove ticks and labels from x-axis and y-axis
    ax.set_xticks([])
    ax.set_yticks([])

    # Get the size of each cell in the heatmap (in figure pixels)
    ax.figure.canvas.draw()
    cell_width, cell_height = ax.get_window_extent().width / color_data.shape[1], ax.get_window_extent().height / color_data.shape[0]

    # Place images in the upper-right corner of each cell without resizing
    for image_info in images:
        image_path = image_info["path"]
        row = image_info["row"]
        col = image_info["col"]

        # Open the image and flip it upside down
        img = Image.open(image_path)
        img = img.transpose(Image.FLIP_TOP_BOTTOM)

        # Get the original image size
        img_width, img_height = img.size

        # Get the position of the image (upper-right corner of the cell)
        x_pos = col + 1 -0.1 - (img_width / cell_width)  # x position relative to the cell
        y_pos = row + 0.1  # y position is the top of the cell

        # Add the flipped image using imshow to correctly align it with the cells
        ax.imshow(np.array(img), aspect='auto', extent=[x_pos, x_pos + img_width / cell_width, y_pos, y_pos + img_height / cell_height], zorder=10)

    plt.tight_layout()
    plt.show()
# Example usage
csv_file_path = "Substrate_Scope_Thermal_Borylation_TFA.csv"  # Replace with your CSV file path
heatmap_title = ""
images = [
    {"path": "1_DMP_Boryl.png", "row": 0, "col": 0},  # Image in the top-left cell
    {"path": "2_2_6_Lutidine_Boryl.png", "row": 0, "col": 1},  # Image in the second row, second column
    {"path": "3_Nicotinate_Boryl.png", "row": 0, "col": 2},  # Image in the second row, second column
    {"path": "4_AminoPyrimi_Boryl.png", "row": 1, "col": 0},  # Image in the second row, second column
    {"path": "5_Phtalazine_Boryl.png", "row": 1, "col": 1},  # Image in the second row, second column
    {"path": "6_Thiazole_Boryl.png", "row": 1, "col": 2},  # Image in the second row, second column
]

generate_heatmap_with_images(csv_file_path, heatmap_title, images)
