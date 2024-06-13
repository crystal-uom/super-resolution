from skimage import exposure as ex
from skimage.filters import threshold_otsu
from skimage.morphology import convex_hull_image
import numpy as np

def get_foreground_background(img, save_folder=None)-> tuple[np.array, np.array]:
    try:
        # Histogram equalization
        h = ex.equalize_hist(img[:,:]) * 255

        # Thresholding using Otsu's method on original image
        oi = np.zeros_like(img, dtype=np.uint16)
        oi[(img > threshold_otsu(img))] = 1

        # Thresholding using Otsu's method on histogram equalized image
        oh = np.zeros_like(img, dtype=np.uint16)
        oh[(h > threshold_otsu(h))] = 1

        # Calculate weights based on the percentage of pixels above Otsu's threshold
        nm = img.shape[0] * img.shape[1]
        w1 = np.sum(oi) / nm
        w2 = np.sum(oh) / nm

        # Combine images using weighted sum
        ots = np.zeros_like(img, dtype=np.uint16)
        new = (w1 * img) + (w2 * h)
        ots[(new > threshold_otsu(new))] = 1

        # Compute convex hull of the thresholded image
        conv_hull = convex_hull_image(ots)

        # Convert convex hull to binary (0 or 1)
        ch = np.multiply(conv_hull, 1)

        # Extract foreground and background images
        fore_image = ch * img
        back_image = (1 - ch) * img

    except Exception as e:
        print(e)
        fore_image = img.copy()
        back_image = np.zeros_like(img, dtype=np.uint16)

    return fore_image, back_image
  
def calculate_msr(data):
    """
    Calculate Mean-to-Standard Deviation Ratio (MSR) of a dataset.

    Parameters:
    - data: NumPy array or list, input dataset

    Returns:
    - msr: float, Mean-to-Standard Deviation Ratio
    """
    # Compute mean and standard deviation of the data
    mean_val = np.mean(data)
    std_dev = np.std(data)

    # Calculate MSR (mean-to-standard deviation ratio)
    if std_dev != 0:
        msr = mean_val / std_dev
    else:
        msr = float('inf')  # Handle division by zero case

    return msr
  
import numpy as np

def calculate_absolute_cnr(foreground, background):
    # Convert images to float arrays for numerical operations
    foreground = foreground.astype(np.float64)
    background = background.astype(np.float64)

    # Calculate mean intensities
    mean_foreground = np.mean(foreground)
    mean_background = np.mean(background)

    # Calculate standard deviations
    std_foreground = np.std(foreground)
    std_background = np.std(background)

    # Calculate contrast-to-noise ratio (CNR)
    numerator = np.abs(mean_foreground - mean_background)
    denominator = np.sqrt((std_foreground**2 + std_background**2) / 2)
    cnr = numerator / denominator

    return cnr
