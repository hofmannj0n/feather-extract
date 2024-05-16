# feather-extract

`feather-extract` is a Python package designed to extract handwritten data from PDF documents, format the extracted data, and save it as an Excel workbook. This package is particularly useful for businesses in the bar and restaurant industry that need to manage inventory.

## Installation

To install `feather-extract`, run the following command:
`pip install feather-extract`

## Usage

[tutorial/documentation](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

### Extracting Text from Documents

To extract text from a PDF document, use the `extract_text_from_document` function:

`from feather_extract import extract_text_from_document`

`extracted_text = extract_text_from_document('path/to/document.pdf')`

This function uses the Azure Form Recognizer service to extract text from the document. You'll need to provide your Azure Form Recognizer API key and endpoint when prompted.

### Formatting Extracted Text

The format_extracted_text function takes the extracted text and formats it into a list of rows, each containing an item, quantity, and bar designation:
`from feather_extract import format_extracted_text`

`formatted_data = format_extracted_text(extracted_text)`

The formatted_data variable will contain a list of lists, where each inner list represents a row with the following format: [item, quantity, bar_designation].
Saving Data to Excel

To save the formatted data to an Excel workbook, use the save_to_excel function:

`from feather_extract import save_to_excel`

`save_to_excel(headers, formatted_data, 'output.xlsx')`

This function creates a new Excel workbook, writes the headers and formatted data rows to the active worksheet, and saves the workbook to the specified file name ('output.xlsx' in this example).

### Dependencies

feather_extract relies on the following dependencies:

azure-ai-formrecognizer: For extracting text from PDF documents using the Azure Form Recognizer service.
openpyxl: For creating and writing data to Excel workbooks.

These dependencies will be automatically installed when you install feather_extract using pip.

### Contributing
Contributions to feather_extract are welcome! If you encounter any issues or have suggestions for improvements, please open an issue on the GitHub repository.
To contribute code changes, follow these steps:

Fork the repository
Create a new branch for your changes
Make your changes and commit them with descriptive commit messages
Push your changes to your forked repository
Open a pull request against the main repository

License
feather_extract is released under the MIT License.
