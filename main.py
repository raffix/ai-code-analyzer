import os
import datetime
import requests
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader

load_dotenv()

project_directory = os.getenv('PROJECT_DIRECTORY')
base_url = os.getenv('AI_BASE_URL')
output_directory = os.getenv('OUTPUT_DIRECTORY')

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
project_name = os.path.basename(os.path.normpath(project_directory))
run_output_folder = os.path.join(output_directory, f"{timestamp}_{project_name}")

os.makedirs(run_output_folder, exist_ok=True)

reader = SimpleDirectoryReader(input_dir=project_directory)
docs = reader.load_data()

def send_to_llama(content, query):
    response = requests.post(
        base_url,
        json={"prompt": f"{content}\n{query}", "model": "llama3.2", "format": "json", "stream": False},
        timeout=5000
    )
    if response.status_code == 200:
        return response.json().get("response", "No response from server")
    else:
        return f"Error: {response.status_code} - {response.text}"

def analyze_project_files(docs, queries):
    print(f"Starting analyze files {project_directory}")
    for doc in docs:
        file_content = doc.get_text()  # Extract content of each file
        file_name = doc.metadata.get("file_name", "Unknown_file")
        print(f"processing {file_name}")
        # Prepare output filename
        output_filename = os.path.join(run_output_folder, f"gpt_output_{file_name}")

        # Collect responses for each query
        with open(output_filename, "w", encoding="utf-8") as output_file:
            for query in queries:
                response = send_to_llama(file_content, query)
                output_file.write(f"Query: {query}\nResponse: {response}\n\n")
    print("Process complete.")

# Define your queries
queries = [ 
    "Analyze the project's architecture and suggest improvements to enhance scalability, maintainability, and performance.",
    "Identify suitable design patterns that can optimize this code, explaining their benefits and implementation strategy.",
    "Break down the key components of this project and provide specific refactoring recommendations to improve code readability, modularity, and efficiency."
]

# Run the analysis
analyze_project_files(docs, queries)
