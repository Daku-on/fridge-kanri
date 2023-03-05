# the codes following are written by 

#write a code such that
# - get good's name by using Yahoo API from JAN code
import requests
import json

# Enter your Yahoo API key
yahoo_api_key = 'YOUR_API_KEY_HERE'

# Enter the JAN code of the product you want to search for
jan_code = '4901777333152'

# Make a request to the Yahoo Product Search API
url = 'https://shopping.yahooapis.jp/ShoppingWebService/V1/json/itemSearch'
params = {
    'appid': yahoo_api_key,
    'jan': jan_code,
    'hits': '1',
    'availability': '1'
}
response = requests.get(url, params=params)

# Parse the JSON response
data = json.loads(response.text)

# Extract the name of the product
product_name = data['ResultSet']['0']['Result']['0']['Name']

# Print the name of the product
print(product_name)

# - get jan code from stdin by barcode scanner as  an external device

import sys
import usb.core
import usb.util

# Find the USB device corresponding to the barcode scanner
dev = usb.core.find(idVendor=0xXXXX, idProduct=0xXXXX)

if dev is None:
    raise ValueError('Device not found')

# Detach the device from the kernel driver if it is attached
if dev.is_kernel_driver_active(0):
    dev.detach_kernel_driver(0)

# Set the configuration of the device
dev.set_configuration()

# Read input from the device
jan_code = ''
while True:
    try:
        data = dev.read(0x81, 64, timeout=100)
        jan_code += data.decode('utf-8').strip()
    except usb.core.USBError as e:
        if e.args == ('Operation timed out',):
            break

# Print the JAN code
print(jan_code)


# - make GUI window to enter JAN code without using package tkinter
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class JanCodeWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set the window properties
        self.setGeometry(100, 100, 300, 150)
        self.setWindowTitle('Enter JAN Code')

        # Create the JAN code label and input field
        self.jan_label = QLabel('JAN Code:')
        self.jan_input = QLineEdit()

        # Create the OK button
        self.ok_button = QPushButton('OK')
        self.ok_button.clicked.connect(self.on_ok_clicked)

        # Create the layout
        layout = QVBoxLayout()
        layout.addWidget(self.jan_label)
        layout.addWidget(self.jan_input)
        layout.addWidget(self.ok_button)
        self.setLayout(layout)

    def on_ok_clicked(self):
        jan_code = self.jan_input.text()
        print(jan_code)
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = JanCodeWindow()
    window.show()
    sys.exit(app.exec_())
