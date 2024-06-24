import os
import subprocess

project_root = r"D:\youtube_data_analysis"

structure = [
    ".github/workflows/ci-cd-pipeline.yml",
    "data/raw/",
    "data/processed/",
    "notebooks/research.ipynb",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_preprocessing.py",
    "src/components/model_training.py",
    "src/pipelines/__init__.py",
    "src/pipelines/training_pipeline.py",
    "src/pipelines/prediction_pipeline.py",
    "src/__init__.py",
    "src/exception.py",
    "src/logger.py",
    "src/utils.py",
    ".gitignore",
    "README.md",
    "requirements.txt",
    "setup.py",
    "LICENSE"
]

# Create project structure
for path in structure:
    full_path = os.path.join(project_root, path)
    if path.endswith("/"):
        os.makedirs(full_path, exist_ok=True)
    else:
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w') as f:
            pass

# Specify the path to the Python 3.9 executable
python_39_path = r"C:\Users\Admin\AppData\Local\Programs\Python\Python39\python.exe"  # Update with the correct path

# Create virtual environment with the name "youtube_data_analysis_env" using Python 3.9
venv_path = os.path.join(project_root, 'youtube_data_analysis_env')
subprocess.run([python_39_path, '-m', 'venv', venv_path])

# Install required packages
requirements = [
    "numpy",
    "pandas",
    "scikit-learn",
    "matplotlib",
    "seaborn",
    "jupyter"
]

with open(os.path.join(project_root, 'requirements.txt'), 'w') as f:
    f.write('\n'.join(requirements))

# Activate the virtual environment and install the requirements
pip_executable = os.path.join(venv_path, 'Scripts', 'pip.exe')

subprocess.run([pip_executable, 'install', '-r', os.path.join(project_root, 'requirements.txt')])

print("Project structure and virtual environment 'youtube_data_analysis_env' setup successfully.")

# Add default content to the LICENSE file
license_content = """MIT License

Copyright (c) 2024 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

with open(os.path.join(project_root, 'LICENSE'), 'w') as f:
    f.write(license_content)

# Add content to the README.md file
readme_content = """# YouTube Data Analysis#"""

