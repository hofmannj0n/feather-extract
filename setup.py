from setuptools import setup, find_packages

setup(
    name="feather_extract",
    version="0.1.15",
    description="A package for extracting handwritten data from PDF documents, and returning an Excel workbook output.",
    author="Jonathan Hofmann",
    author_email="awsjonathan99@gmail.com",
    url="https://www.featherdata.io/",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "feather_extract": ["data/*.pdf"],
    },
    install_requires=[
        "azure-ai-formrecognizer==3.3.3",
        "openpyxl==3.1.2",
    ],
)
