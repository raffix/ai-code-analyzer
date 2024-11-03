import os
import requests
from llama_index.core import SimpleDirectoryReader

# Set up paths and Llama API endpoint
project_directory = "/home/raffael/Projects/bike-ratio/"  # Update to your project's root directory
base_url = "localhost:11434/api/generate"  # Local Llama 3.2 API endpoint

# Initialize the reader and load data from the directory
reader = SimpleDirectoryReader(input_dir=project_directory)
docs = reader.load_data()

# Function to send file content and query to Llama 3.2
def send_to_llama(content, query):
    response = requests.post(base_url, json={"prompt": f"{content}\n\n{query}", "model": "llama3.2", "format": "json", "stream": False})
    if response.status_code == 200:
        return response.json().get("response", "No response from server")
    else:
        return f"Error: {response.status_code} - {response.text}"

# Function to analyze each file in the project with multiple queries
def analyze_project_files(docs, queries):
    results = {}
    for doc in docs:
        file_content = doc.get_text()  # Extract content of each file
        file_name = doc.metadata.get("file_name", "Unknown file")
        
        # Apply each query to the file content and store results
        results[file_name] = {}
        for query in queries:
            response = send_to_llama(file_content, query)
            results[file_name][query] = response

    return results

# Define your queries
queries = [
    "Suggest improvements for the project's architecture.",
    "Identify potential design patterns to optimize this code.",
    "List key components and recommend refactoring strategies."
]

# Run the analysis and print results
analysis_results = analyze_project_files(docs, queries)
for file, query_responses in analysis_results.items():
    print(f"File: {file}")
    for query, response in query_responses.items():
        print(f"  Query: {query}\n  Response: {response}\n")

