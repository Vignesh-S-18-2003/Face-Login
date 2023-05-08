import numpy as np
from skimage.metrics import structural_similarity as ssim
from PIL import Image


def compare_images(image1_path, image2_path):
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)
    image1 = image1.resize(image2.size)
    # Convert images to grayscale
    image1_gray = image1.convert('L')
    image2_gray = image2.convert('L')

    # Convert images to numpy arrays
    image1_array = np.array(image1_gray)
    image2_array = np.array(image2_gray)

    # Calculate the structural similarity index (SSIM)
    similarity_score = ssim(image1_array, image2_array)

    if similarity_score >= 0.5:  # Adjust the threshold as per your requirement
        return True
    else:
        return False
