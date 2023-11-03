# Semantic Seach REST

Welcome to my semantic search REST API! This is a brief guide to help you get started.

## Getting Started

### Setup

To get started with this project, clone the repository, set up your virtual environment, and create a config.json file

   ```bash
   git clone https://github.com/B0RDERS/semantic_search.git
   cd semantic_search
   python -m venv env
   source env/bin/activate
   pip install flask pymongo openai
   cp config.json.template config.json
   ```
   Then fill in the config.json file with your information

### Usage

Now that you have set up the project, you can run it with the following command:

```bash
python server.py
```
