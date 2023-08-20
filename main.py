import os
import PySimpleGUI as sg
from PIL import Image
from pdf2image import convert_from_path
import img2pdf


def jpg_to_pdf(jpg_path, pdf_path):
    image = Image.open(jpg_path)
    pdf_bytes = img2pdf.convert(image.filename)

    with open(pdf_path, "wb") as file:
        file.write(pdf_bytes)


def pdf_to_jpg(pdf_path, saving_folder, image_format):
    # Get the directory of the Python executable
    python_executable_path = os.path.dirname(os.path.abspath(__file__))
    # Construct the full path to the poppler bin directory
    poppler_path = os.path.join(python_executable_path, "poppler-23.08.0", "Library", "bin")

    pages = convert_from_path(pdf_path=pdf_path, poppler_path=poppler_path)

    c = 1
    for page in pages:
        img_name = f"img-{c}.{image_format}"
        page.save(os.path.join(saving_folder, img_name), "JPEG")
        c += 1


# Create UI layout
layout = [
    [sg.Text("Select Conversion Direction:")],
    [sg.Radio("JPG to PDF", "conversion_direction", default=True, key="jpg_to_pdf"),
     sg.Radio("PDF to JPG", "conversion_direction", key="pdf_to_jpg")],
    [sg.Text("Select File:"), sg.InputText(key="file_path"), sg.FileBrowse()],
    [sg.Text("Select Saving Path:"), sg.InputText(key="saving_path"), sg.FolderBrowse()],
    [sg.Text("Select Image Format:"), sg.Combo(["jpg", "png"], key="image_format", enable_events=True, visible=False)],
    [sg.Button("Convert")]
]

# Create the window
window = sg.Window("File Converter", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Convert":
        if values["jpg_to_pdf"]:
            if values["file_path"] and values["saving_path"]:
                pdf_path = os.path.join(values["saving_path"], "converted.pdf")
                jpg_to_pdf(values["file_path"], pdf_path)
                sg.popup("Conversion completed!", title="Success")
            else:
                sg.popup("Please provide all required fields.", title="Input Error")

        if values["pdf_to_jpg"]:
            if values["file_path"] and values["saving_path"]:
                if values["image_format"]:
                    pdf_to_jpg(values["file_path"], values["saving_path"], values["image_format"])
                    sg.popup("Conversion completed!", title="Success")
                else:
                    sg.popup("Please select an image format.", title="Input Error")
            else:
                sg.popup("Please provide all required fields.", title="Input Error")

        # Show/hide the image format selection based on the chosen conversion direction
        window["image_format"].update(visible=values["pdf_to_jpg"])

window.close()
