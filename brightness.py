import cv2 as cv
from PIL import Image

# Automatic brightness and contrast optimization with optional histogram clipping
def automatic_brightness_and_contrast(image, clip_hist_percent=1):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    
    # Calculate grayscale histogram
    hist = cv.calcHist([gray], [0], None, [256], [0, 256])
    hist_size = len(hist)
    
    # Calculate cumulative distribution from the histogram
    accumulator = []
    accumulator.append(float(hist[0].item()))  # Use item() to extract scalar
    for index in range(1, hist_size):
        accumulator.append(accumulator[index - 1] + float(hist[index].item()))  # Use item() here too
    
    # Locate points to clip
    maximum = accumulator[-1]
    clip_hist_percent *= (maximum / 100.0)
    clip_hist_percent /= 2.0
    
    # Locate left cut
    minimum_gray = 0
    while accumulator[minimum_gray] < clip_hist_percent:
        minimum_gray += 1
    
    # Locate right cut
    maximum_gray = hist_size - 1
    while accumulator[maximum_gray] >= (maximum - clip_hist_percent):
        maximum_gray -= 1
    
    # Calculate alpha and beta values
    alpha = 255 / (maximum_gray - minimum_gray)
    beta = -minimum_gray * alpha

    auto_result = cv.convertScaleAbs(image, alpha=alpha, beta=beta)
    return auto_result

# Load the image
image = cv.imread('kino.jpg')
if image is None:
    print("Error: Could not read the image.")
else:
    auto_result = automatic_brightness_and_contrast(image)
    cv.imwrite('output_kino.jpg', auto_result)
