# Document AI Python Project

This project demonstrates how to use Google Document AI with Python to process documents, extract key-value pairs, and save the extracted data into a structured JSON file.

## Features

- Utilizes a custom Document AI processor for detailed data extraction.

- Supports PDF and other document formats.

- Extracts general key-value pairs and line items from documents.

- Outputs the extracted data into a JSON file for further use.

## Prerequisites

To run this project, ensure you have the following:

1.  **Python 3.8 or higher** installed.

2.  **Google Cloud SDK** configured with your project.

3.  A **Google Document AI processor** set up in your Google Cloud project.

4.  A `.env` file with the following variables:

    ```
    PROCESSOR_ID=your-processor-id
    PROJECT_ID=your-project-id
    ```

## Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/Calvinphuah/DocumentAI.git
    cd DocumentAI
    ```

2.  Install the required Python libraries:

    ```
    pip install google-cloud-documentai python-dotenv
    ```

3.  Create a `.env` file in the root directory and configure the required variables as shown above.

## Configuration

- **Project and Location**: Update the `project_id` and `location` variables in the script:

  ```
  project_id = "your-google-cloud-project-id"
  location = "your-processor-location"  # e.g., "us"
  ```

- **File Path**: Place the document you want to process in the `./data/` directory and update the `file_path` variable:

  ```
  file_path = "./data/your-document.pdf"
  ```

- **Processor ID**: Ensure your `.env` file contains the correct `PROCESSOR_ID`.

## Usage

1.  Run the script:

    ```
    python main.py
    ```

2.  The script will process the document and output the extracted data into a file named `extracted_data.json` in the project root directory.

## Key Functions

### `quickstart`

This is the main function that processes the document using the specified processor and extracts data.

### `extract_key_value_pairs`

This function extracts key-value pairs and line items from the processed document.

## Example Output

Here is an example of the JSON file generated:

```json
{
  "invoice_id": "2767",
  "net_amount": "4669.77",
  "invoice_date": "2021-12-06",
  "total_tax_amount": "126.08",
  "total_amount": "4795.85",
  "receiver_name": "Martin Colby",
  "invoice_type": "invoice_statement",
  "supplier_email": "sales@amnoshsuppliers.com",
  "supplier_address": "9291 Proin Road Lake Charles, ME-11292",
  "ship_to_address": "45 Lightning Road, Arizona, AZ 88776",
  "currency": "USD",
  "ship_to_name": "Johnny Patel Abcxyz Traders",
  "supplier_name": "AMNOSH",
  "supplier_phone": "123-456-7890",
  "supplier_website": "www.amnoshsuppliers.com",
  "receiver_address": "45 Lightning Road, Arizona, AZ 88776",
  "line_items": [
    {
      "line_item/quantity": "1",
      "line_item/description": "Hitachi Trans Fluid - Quart",
      "line_item/unit_price": "876",
      "line_item/amount": "876"
    },
    {
      "line_item/quantity": "1",
      "line_item/description": "4X189 Powerlink Belt",
      "line_item/unit_price": "567.87",
      "line_item/amount": "567.87"
    },
    {
      "line_item/quantity": "3",
      "line_item/description": "3-Planetary Gear System",
      "line_item/unit_price": "456.82",
      "line_item/amount": "1370.46"
    },
    {
      "line_item/quantity": "3",
      "line_item/description": "D2 Heavy Duty Fluid",
      "line_item/unit_price": "345.06",
      "line_item/amount": "1035.18"
    },
    {
      "line_item/quantity": "2",
      "line_item/description": "Hydraullic Press-25 Tons",
      "line_item/unit_price": "56.09",
      "line_item/amount": "112.18"
    },
    {
      "line_item/quantity": "2",
      "line_item/unit_price": "354.04",
      "line_item/amount": "708.08",
      "line_item/description": "Optional: HMT Machine"
    }
  ]
}
```

## Error Handling

- **Processor ID Missing**: The script will raise an error if the `PROCESSOR_ID` is not set in the `.env` file.

- **No Line Items Found**: The script will notify you if no line items are detected in the document.
