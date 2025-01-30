Llama 3.2 Code Analyzer

This Python script analyzes a project's source code using Llama 3.2 API. It extracts key insights, suggests architectural improvements, identifies design patterns, and provides refactoring recommendations.

Features

Scans all files in the project directory.

Runs multiple queries for architectural insights and code optimization.

Saves analysis results in a timestamped folder for better organization.

Installation

Install Python & Dependencies

Ensure you have Python 3.8+ installed. Then, install required dependencies:

pip install requests llama-index

Set Up Llama 3.2 API

Run your local Llama 3.2 server. Update base_url in the script if needed:

base_url = "http://localhost:11434/api/generate"

Usage

Configure Project Path

Update the project directory path in the script:

project_directory = "<your_project_path>"

Run the Analysis

Execute the script:

python analyze.py

View Results

Analysis reports are saved in:

<your_output_path>/YYYYMMDD_HHMMSS_project-name/

Example:

<your_output_path>/20250129_153045_project-name/
  ├── gpt_output_file1.txt
  ├── gpt_output_file2.txt

Each file contains:

The queries asked

The AI-generated suggestions

Example Output

A generated file (gpt_output_main.py.txt) might look like this:

Query: Analyze the project's architecture and suggest improvements.
Response: The project follows a monolithic structure but can benefit from modularization...

Troubleshooting

Error: ModuleNotFoundError → Run:

pip install requests llama-index

Llama API Not Responding?
Check if the server is running at http://localhost:11434.

Contributing

Feel free to submit issues or improve the script!