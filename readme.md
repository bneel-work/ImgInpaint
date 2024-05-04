# ImgInpaint: AI-Powered Image Inpainting Web App

This project offers a user-friendly web application for image inpainting, allowing you to restore damaged images using AI and machine learning techniques.

This code snippet handles the core functionality of image inpainting:

1. **Loading Images:**
    - OpenCV's `cv2.imread` function reads the damaged image and the mask (grayscale) from their respective paths.

2. **Image Inpainting:**
    - OpenCV's `cv2.inpaint` function performs the inpainting:
        - Takes the damaged image, mask, a radius for context, and the Navier-Stokes algorithm as arguments.
        - Fills in the missing areas based on the surrounding image content and the mask information.
        - Stores the result in a separate NumPy array representing the inpainted image.

3. **Saving the Result:**
    - A unique filename is generated using the current date/time and random characters.
    - The path to save the inpainted image is constructed within the project's static directory.
    - OpenCV's `cv2.imwrite` function saves the inpainted image data to the specified path.


## Features

* **Image Upload:** Upload your damaged images and corresponding masks for seamless inpainting.
* **AI-Powered Restoration:** Leverage the power of OpenCV to automatically fill in missing regions, creating visually cohesive results.
* **Task History:** Keep track of your completed inpainting tasks for easy reference.

## Technologies

* **Backend:** Django (Python web framework)
* **Image Processing:** OpenCV (Python library)
* **Database:** Django Models (SQLite by default)

## Installation

**Prerequisites:**

* Python 3.10

**Steps:**

1. **Clone or Download the Project:** Obtain the project files (consider using Git for version control).
2. **Navigate to Project Directory:** Open a terminal or command prompt and navigate to the project directory using `cd ImgInpaint`.
3. **Create a Virtual Environment (Recommended):** Create a virtual environment to isolate project dependencies and avoid conflicts (instructions vary based on your operating system).
4. **Install Dependencies:** Within the virtual environment, activate it and install the required packages using `pip install -r requirements.txt`.
5. **Run the Development Server:** Start the Django development server using `python manage.py runserver`.

## Usage

1. **Access the App:** Open http://localhost:8000/ in your web browser.
2. **Create a New Task:** Go to the main page and click "Create New".
3. **Provide Task Name:** Enter a descriptive name for your image inpainting task.
4. **Upload Images:** Upload both the damaged image and the corresponding mask image that defines the missing regions.
5. **Process the Image:** Click the "Process Image" button.
6. **View the Result:** The application will automatically process the images and display the restored image.

**Note:** This is a foundational implementation with potential for further development to enhance accuracy and functionality.
