import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox

"""Author ALI BDEIR : Masters in Robotics and Control"""



def select_roi(image):
    cv2.imshow('Select ROI', image)
    roi = cv2.selectROI('Select ROI', image, fromCenter=False, showCrosshair=True)
    cv2.destroyWindow('Select ROI')
    return roi


def crop_image(image, roi, save_path):
    cropped_image = image[int(roi[1]):int(roi[1] + roi[3]), int(roi[0]):int(roi[0] + roi[2])]
    cv2.imwrite(save_path, cropped_image)


def select_images_and_crop():
    root = tk.Tk()
    root.withdraw()

    file_paths = filedialog.askopenfilenames()
    if file_paths:
        if not messagebox.askokcancel("Confirm Image Selection", "Are you sure you want to proceed with these images?"):
            return

        image_paths = list(file_paths)
        first_image = cv2.imread(image_paths[0])
        if first_image is None:
            print("Error: Unable to open image.")
            return

        roi = select_roi(first_image)
        save_dir = filedialog.askdirectory(title="Select Directory to Save Cropped Images")
        if not save_dir:
            return

        if not messagebox.askokcancel("Save Cropped Images", "Save images with the selected ROI?"):
            return

        for image_path in image_paths:
            image = cv2.imread(image_path)
            filename = os.path.basename(image_path)
            cropped_filename = "cropped_" + filename
            save_path = os.path.join(save_dir, cropped_filename)
            crop_image(image, roi, save_path)
            print(f"Cropped image saved successfully: {save_path}")

        messagebox.showinfo("Cropped Images Saved", "Cropped images saved successfully.")

        cv2.destroyAllWindows()


if __name__ == "__main__":
    select_images_and_crop()
