# Bulk-Image-Editor
This project aims to enable bulk editing of images. The program allows you to import an image from your computer, adjust parameters such as brightness and contrast, and save these settings for reuse. You can then apply the same settings to an entire folder of photos. The resulting images are saved within the original folder.


# Description

While browsing the internet, I realized that there are many high-quality photo editors, but none that combine this quality with the ability to edit large quantities of images.  

This project has exactly that purpose: to create a simple program, based on image manipulation libraries such as **Pillow** and **OpenCV**, that allows you to edit a sample photo by adjusting parameters such as brightness or contrast, save those settings, and then automatically apply them to dozens or hundreds of other images within a folder.  

The processed photos are saved in the original folder with new names, preserving the existing files.  


# Features

1. Import an image as an example and edit parameters such as brightness and contrast.
2. Save the same settings applied to the sample image.
3. Select an entire folder from the computer's memory and apply the same settings.
4. Create a folder inside the original folder with all the edited photos!

# Libraries Used

Pillow - (https://pypi.org/project/pillow/) 

Open CV - (https://pypi.org/project/opencv-python/)

Tkinter - (https://pypi.org/project/tkinter-page/)

Pathlib - (https://pypi.org/project/pathlib/)
