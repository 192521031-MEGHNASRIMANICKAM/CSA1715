import cv2
import numpy as np

image = cv2.imread("image.jpg")

if image is None:
    print("Image not found")
else:
    image = cv2.resize(image, (300, 300))

    pixels = np.float32(image.reshape((-1, 3)))

    criteria = (
        cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,
        10, 1.0
    )

    _, labels, centers = cv2.kmeans(
        pixels, 3, None, criteria, 10,
        cv2.KMEANS_RANDOM_CENTERS
    )

    centers = np.uint8(centers)
    segmented = centers[labels.flatten()]
    segmented = segmented.reshape(image.shape)

    cv2.imshow("Original Image", image)
    cv2.imshow("Segmented Image", segmented)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
