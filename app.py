from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QFileDialog, QLineEdit
from PyQt6.QtCore import Qt
from PIL import Image


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("ImgResizr")

        self.label = QLabel("Hello")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.width_input = QLineEdit()
        self.width_input.setPlaceholderText("Enter width")
        self.width_input.setText("800") # Set default width

        self.height_input = QLineEdit()
        self.height_input.setPlaceholderText("Enter height")
        self.height_input.setText("600")  # Set default height


        self.button = QPushButton("Resize Image")
        self.button.clicked.connect(self.resize_image)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.width_input)
        layout.addWidget(self.height_input)
        layout.addWidget(self.button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def resize_image(self):
        img_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.jpeg)")
        if img_path:
            new_width = int(self.width_input.text()) if self.width_input.text().isdigit() else 0
            new_height = int(self.height_input.text()) if self.height_input.text().isdigit() else 0
            if new_width > 0 and new_height > 0:
                output_path, _ = QFileDialog.getSaveFileName(self, "Save Resized Image", "", "Image Files (*.png *.jpg *.jpeg)")
                if output_path:
                    try:
                        image = Image.open(img_path)
                        resized_img = image.resize((new_width, new_height), Image.BICUBIC)
                        resized_img.save(output_path)
                        self.label.setText("Image resized and saved successfully!")
                    except Exception as e:
                        self.label.setText("Error resizing and saving image: " + str(e))
                else:
                    self.label.setText("No output path selected.")
            else:
                self.label.setText("Invalid width or height values.")
        else:
            self.label.setText("No image selected.")


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
