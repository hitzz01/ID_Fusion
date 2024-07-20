# ID_Fusion

##Views
home: Renders the homepage.
preprocess_image: Converts an image to grayscale and applies binary thresholding.
extract_info: Extracts text from the processed image using PyTesseract and parses the text to extract relevant information.
parse_text: Parses the extracted text to find name, birth date, PAN number, and Aadhaar number.
create_connection: Establishes a connection to the MySQL database.
create_table: Creates a table in the MySQL database to store extracted data.
insert_data: Inserts extracted data into the MySQL database.
process_image: Orchestrates the extraction, processing, and storing of data from the uploaded image.
create_qr_code: Generates a QR code with the extracted data and expiration time.
upload_image: Handles image upload and processing.
download_pdf: Generates and serves a PDF of the visitor pass.
##Models
ExtractedData: Defines the structure of the data stored in the MySQL database.
##Templates
home.html: The main template for the homepage.
pdf_template.html: Template for generating the PDF of the visitor pass.
##URLs
Maps URLs to corresponding views.
##Logging
The application uses the Python logging module to log debug and error messages to the console. Ensure logging is configured appropriately for your production environment.

##License
This project is licensed under the MIT License. See the LICENSE file for details.
