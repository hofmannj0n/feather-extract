import os

def get_form(filled_out=False, output_path=None):
    package_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(package_dir, 'data')

    if filled_out:
        form_file = 'standard-form-filled-out.pdf'
    else:
        form_file = 'standard_form.pdf'

    pdf_file = os.path.join(data_dir, form_file)

    # Print the absolute paths
    print(f"Package directory: {package_dir}")
    print(f"Data directory: {data_dir}")
    print(f"PDF file path: {pdf_file}")

    if output_path is None:
        output_path = os.path.join(os.getcwd(), form_file)
    else:
        output_path = os.path.join(output_path, form_file)

    with open(pdf_file, 'rb') as src, open(output_path, 'wb') as dst:
        dst.write(src.read())

    return output_path