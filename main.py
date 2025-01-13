from google.api_core.client_options import ClientOptions
from google.cloud import documentai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configuration
project_id = "wtp-dockets-app"
location = "us"  # Processor location, e.g., 'us' or 'eu'
file_path = "./data/ams.pdf"
processor_id = os.getenv("PROCESSOR_ID") 

def quickstart(project_id: str, location: str, file_path: str, processor_id: str):
    if not processor_id:
        raise ValueError("Processor ID is not set. Please check your .env file.")

    # Set the API endpoint
    opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")

    # Initialize the Document AI client
    client = documentai.DocumentProcessorServiceClient(client_options=opts)

    # Define the processor resource name
    processor_name = f"projects/{project_id}/locations/{location}/processors/{processor_id}"

    # Read the file into memory
    with open(file_path, "rb") as image:
        image_content = image.read()

    # Load binary data
    raw_document = documentai.RawDocument(
        content=image_content,
        mime_type="application/pdf",  # Adjust MIME type as needed
    )

    # Configure the process request
    request = documentai.ProcessRequest(name=processor_name, raw_document=raw_document)

    # Process the document using the specified processor
    result = client.process_document(request=request)
    document = result.document

    # Extract and display key-value pairs
    print("Extracting key-value pairs:")
    key_value_pairs = extract_key_value_pairs(document)
    for key, value in key_value_pairs.items():
        print(f"{key}: {value}")

def extract_key_value_pairs(document):
    key_value_pairs = {}
    line_items = []  # To store line items as a list of dictionaries

    # Iterate over the entities in the document
    if document.entities:
        for entity in document.entities:
            # Handle line items specifically
            if entity.type == "line_item":
                line_item = {}  # Dictionary to store individual line item details
                
                # Iterate through properties of the line item
                for property in entity.properties:
                    key = (property.type or property.mention_text or "Unknown Key").replace("\n", " ").strip()
                    value = (
                        (property.normalized_value.text if property.normalized_value else property.mention_text or "Unknown Value")
                        .replace("\n", " ")
                        .strip()
                    )
                    line_item[key] = value  # Add key-value pair to the line item
                
                line_items.append(line_item)  # Add the line item to the list of line items
            
            else:
                # Extract general key-value pairs
                key = (entity.type or entity.mention_text or "Unknown Key").replace("\n", " ").strip()
                value = (
                    (entity.normalized_value.text if entity.normalized_value else entity.mention_text or "Unknown Value")
                    .replace("\n", " ")
                    .strip()
                )
                key_value_pairs[key] = value

    # Add line items to the key-value pairs under a 'line_items' key
    if line_items:
        key_value_pairs["line_items"] = line_items
    else:
        print("No line items found in the document.")

    return key_value_pairs


# Call the function
quickstart(project_id, location, file_path, processor_id)
