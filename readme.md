# Aliquot Freezer Assignment Automation

[![GitHub](https://img.shields.io/badge/GitHub-thussenthanwalter--angelo-blue?style=flat&logo=github)](https://github.com/thussenthanwalter-angelo)


## Purpose
This script automates the Aliquot Freezer Assignment process in the Freezerworks software. It was originally developed for the Sholler Lab at Penn State College of Medicine to streamline the management of aliquot locations within the freezer system. Written by Thussenthan Walter-Angelo.

## Features
- Authenticates with the Freezerworks API using JWT (JSON Web Token)
- Reads aliquot assignment data from a CSV file
- Updates aliquot locations in the Freezerworks system
- Demonstrates how to retrieve sample information and verify aliquot actions

## Prerequisites
- Python 3.x
- `requests` library (install via `pip install requests`)
- Access to the Freezerworks API (your URL, username, and password)

## Setup
1. Clone this repository or download the script files.
2. Install the required Python library:
   ```
   pip install requests
   ```
3. Update the following variables in the script:
   - `username` and `password` with your Freezerworks API credentials
   - Update the API URL in the `update_aliquot` function
   - Ensure the CSV file path is correct (`csv_file_path` variable)

## Usage
1. Prepare your CSV file named "Aliquot Freezer Assignment.csv" with the following columns:
   - Aliquot ID
   - Rack
   - Box
   - Position

2. Run the script:
   ```
   python aliquot_freezer_assignment.py
   ```

3. The script will process each row in the CSV file and update the corresponding aliquot's location in Freezerworks.

## Script Components
1. **Authentication**: The script first authenticates with the Freezerworks API to obtain a JWT token.

2. **Update Aliquot Function**: `update_aliquot()` sends a POST request to update each aliquot's location.

3. **CSV Processing**: The script reads the CSV file and calls `update_aliquot()` for each row.

4. **Sample Aliquot Retrieval**: Demonstrates how to retrieve all aliquots for a specific sample (commented out by default).

5. **Aliquot Verification**: Shows how to verify if aliquots are available for requisition (commented out by default).

## Notes
- Ensure that your Freezerworks API is accessible and that you have the necessary permissions.
- The script includes error handling, but additional logging and error management may be necessary for production use.
- Always test the script with a small dataset before running it on your entire inventory.

## Support
For questions or issues, please contact the code and readme author Thussenthan Walter-Angelo, Sholler Lab IT support, or the current script maintainer.

## Disclaimer
This script interacts with your Freezerworks database. Always ensure you have a backup of your data and an understanding of the Freezerworks API calls before running automated updates on your data.

Created by [@thussenthanwalter-angelo](https://github.com/thussenthanwalter-angelo)

(Email: t.walterangelo@gmail.com)


