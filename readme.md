# DediDuplicator

DediDuplicator is a user-friendly application designed to help you quickly and effectively identify and manage duplicate files on your computer. Built with Python and utilizing the PySide6 framework for the user interface, this application provides a seamless experience for users looking to clean up their file systems.

## Features

- **Add Folders:** Easily add folders to search for duplicate files.
- **Remove Folders:** Remove any added folder from the search list.
- **Reset:** Clear all added folders with a single click.
- **Info:** Access information about the application and its developer.
- **Scan:** Scan selected folders for duplicate files and display results in a user-friendly table.
- **File Information:** View details such as file name, size, path, creation time, and a selection option for deletion.
- **Automatic Selection:** Automatically mark newly created or older files based on your preference.
- **Delete Operation:** Remove selected duplicate files with ease.

## Screenshots

![Main Interface](image\main_window.png)
*Main interface of DediDuplicator showing the folder selection.*

![Scan Results](image\scan_window.png)
*Scan results displaying duplicate files.*

![Selection By Time Results](image\select_window.png)
*When selecting by time, identical files are marked for deletion according to the selected time.*

## Installation

To run DediDuplicator, you need to have Python 3.12.2 installed on your system. Follow these steps to get started:

1. Clone the repository:

   ```bash
   git clone https://github.com/mhats99/DediDuplicator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd DediDuplicator
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python __main__.py
   ```

### Windows Users

- An executable (EXE) format of the application will be provided in the future for easier installation on Windows.

### Linux Users

- You can run the application using the command provided above.

## Testing

Tests are conducted using `pytest`. To run the tests, ensure that the `config.py` file in the `tests` directory is configured correctly. You can run the tests as follows:

1. Navigate to the tests directory:

   ```bash
   cd tests
   ```

2. Run the tests:

   ```bash
   pytest
   ```

   - Only the logger test in the module tests and the worker tests in the `ui_tool` module should be executed in sequence.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## Acknowledgments

Special thanks to the following libraries that made this project possible:

- [PySide6](https://pyside.org/)
- [pytest](https://pytest.org/)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please reach out to Melih Ates at <devix.soft@gmail.com>.
