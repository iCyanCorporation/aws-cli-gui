import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QTextEdit
import subprocess

class AWSCLIGUI(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the layout
        layout = QVBoxLayout()

        # AWS Profile input
        self.profile_label = QLabel("AWS Profile:")
        self.profile_input = QLineEdit()
        layout.addWidget(self.profile_label)
        layout.addWidget(self.profile_input)

        # AWS Region input
        self.region_label = QLabel("AWS Region:")
        self.region_input = QLineEdit()
        layout.addWidget(self.region_label)
        layout.addWidget(self.region_input)

        # AWS Command input
        self.command_label = QLabel("AWS CLI Command:")
        self.command_input = QLineEdit()
        layout.addWidget(self.command_label)
        layout.addWidget(self.command_input)

        # Run button
        self.run_button = QPushButton("Run Command")
        self.run_button.clicked.connect(self.run_command)
        layout.addWidget(self.run_button)

        # Output display
        self.output_display = QTextEdit()
        layout.addWidget(self.output_display)

        # Set layout and window title
        self.setLayout(layout)
        self.setWindowTitle("AWS CLI GUI")

    def run_command(self):
        profile = self.profile_input.text()
        region = self.region_input.text()
        command = self.command_input.text()

        aws_command = f"aws {command} --profile {profile} --region {region}"

        try:
            result = subprocess.check_output(aws_command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
            self.output_display.setText(result)
        except subprocess.CalledProcessError as e:
            self.output_display.setText(f"Error: {e.output}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = AWSCLIGUI()
    gui.show()
    sys.exit(app.exec_())
