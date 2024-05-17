# feather_extract

`feather-extract` is a Python package designed to extract handwritten data from PDF documents, format the extracted data, and save it as an Excel workbook. This package is particularly useful for businesses in the bar and restaurant industry that need to manage inventory.

[documentation](https://pypi.org/project/feather-extract/0.1.16/)

[video tutorial](https://www.youtube.com/watch?v=s1YWwMr3lRk)

## Installation

To install `feather-extract`, run the following command:
`pip install feather-extract`

## Extracting Text from Documents

feather_extract is trained on a standarized form, to download this form simply run the `get_form()` function

by setting `get_form(filled_out=True)` you can also download an already filled out form for testing and practice.

`from feather_extract import get_form`

`form = get_form()`

To extract text from a document, use the `extract_text_from_document` function:

`from feather_extract import extract_text_from_document`

`extracted_text = extract_text_from_document('path/to/document.pdf')`

This function uses the Azure Form Recognizer service to extract text from the document. You'll need to provide your Azure Form Recognizer API key and endpoint when prompted.

## Formatting Extracted Text

The format_extracted_text function takes the extracted text and formats it into a list of rows, each containing an item, quantity, and bar designation:
`from feather_extract import format_extracted_text`

`formatted_data = format_extracted_text(extracted_text)`

The formatted_data variable will contain a list of lists, where each inner list represents a row with the following format: [item, quantity, bar_designation].
Saving Data to Excel

To save the formatted data to an Excel workbook, use the save_to_excel function:

`from feather_extract import save_to_excel`

`save_to_excel(headers, formatted_data, 'output.xlsx')`

This function creates a new Excel workbook, writes the headers and formatted data rows to the active worksheet, and saves the workbook to the specified file name ('output.xlsx' in this example).

## Dependencies

`feather-extract` relies on the following dependencies:

`azure-ai-formrecognizer` - For extracting text from PDF documents using the Azure Form Recognizer service.

`openpyxl` - For creating and writing data to Excel workbooks.

These dependencies will be automatically installed when you install feather-extract using pip.

## Contributing
Contributions to feather_extract are welcome! 

If you encounter any issues or have suggestions for improvements, please open an issue on the [GitHub repository.](https://github.com/hofmannj0n/feather-extract)

To contribute code changes, follow these steps:

- Fork the repository

- Create a new branch for your changes

- Make your changes and commit them with descriptive commit messages

- Push your changes to your forked repository

- Open a pull request against the main repository

## License
feather-extract is released under the MIT License. 
