# AWS CLI GUI

The **AWS CLI GUI** is a graphical interface built to simplify the use of AWS Command Line Interface (CLI). Users can manage their AWS resources without manually typing commands. This project contains two versions of the AWS CLI GUI: one built using **Tkinter** (lightweight and simple) and the other using **PyQt5** (more advanced, feature-rich).

## Features

- **Two GUI Versions**:
  - **Tkinter**: Lightweight and simple, perfect for small applications.
  - **PyQt5**: Modern and feature-rich, suited for more complex interfaces.
- **Environment Switching**: Seamlessly switch between AWS environments (e.g., dev, staging, prod) with profile support.
- **Real-time AWS Interaction**: Execute AWS CLI commands via a user-friendly graphical interface.

## Prerequisites

Before running the AWS CLI GUI, ensure you have the following installed:

- **AWS CLI**: Install the AWS CLI and configure it with profiles. Refer to the [AWS CLI installation guide](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) for setup instructions.
- **Python 3.x**: Required to run the GUI applications.
- **Node.js** (optional for development purposes).

For **PyQt5 Version**:
- **PyQt5**: Install via `pip install pyqt5`.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/aws-cli-gui.git
   cd aws-cli-gui
   ```

2. **Choose your preferred version**:
   - For the Tkinter version, navigate to the `Tkinter` folder:
     ```bash
     cd Tkinter
     ```
   - For the PyQt5 version, navigate to the `PyQt5` folder:
     ```bash
     cd PyQt5
     ```

3. **Install dependencies**:
   - For Tkinter, no additional installation is required since it's included with Python.
   - For PyQt5, install the required packages:
     ```bash
     pip install pyqt5
     ```

4. **Run the application**:
   - For Tkinter:
     ```bash
     python aws_cli_gui_tkinter.py
     ```
   - For PyQt5:
     ```bash
     python aws_cli_gui_pyqt5.py
     ```

## Usage

1. **AWS Profile**: Enter your AWS profile name (e.g., `dev`, `prod`) to switch between different environments.
2. **AWS Region**: Specify the AWS region (e.g., `us-east-1`) in which you want to execute commands.
3. **CLI Command**: Enter the AWS CLI command you want to run (e.g., `s3 ls`, `ec2 describe-instances`).
4. **Execute**: Click the "Run Command" button to execute the command and view the results in the output window.

### Switching Between Environments

To switch between environments, ensure you have configured multiple AWS profiles via the AWS CLI:

```bash
aws configure --profile dev
aws configure --profile prod
```

You can select the appropriate profile in the AWS CLI GUI to run commands in that specific environment.

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix (`git checkout -b feature-branch`).
3. Make your changes.
4. Submit a pull request.

## Issues

If you encounter any problems or have suggestions, please [open an issue](https://github.com/yourusername/aws-cli-gui/issues).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
