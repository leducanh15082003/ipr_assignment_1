import cv2

def resize_image(image, width, height):
    resized_image = cv2.resize(image, (width, height))
    return resized_image

def binary_threshold(image, threshold_value):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)
    return binary_image

def main():
    # Ask user for input image path
    input_image_path = input("Enter the input image path: ")

    # Read input image
    input_image = cv2.imread(input_image_path)

    # Ask user for desired width and height
    width = int(input("Enter the desired width for resizing: "))
    height = int(input("Enter the desired height for resizing: "))

    # Apply binary thresholding
    threshold_str = input("Enter the threshold value for binary thresholding (press Enter to skip): ")

    if threshold_str:  # If user entered a threshold value
        threshold_value = int(threshold_str)
        # Resize image
        resized_image = resize_image(input_image, width, height)
        # Apply binary thresholding
        thresholded_image = binary_threshold(resized_image, threshold_value)
        # Display output image
        cv2.imshow("Thresholded Image", thresholded_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:  # If user didn't enter a threshold value
        # Resize image only
        resized_image = resize_image(input_image, width, height)
        # Display output image
        cv2.imshow("Resized Image", resized_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
