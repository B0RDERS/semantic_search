# Semantic Seach REST

Welcome to my semantic search REST API! This is a brief guide to help you get started.

## Getting Started

### Installation

To get started with this project, you'll need to clone the repository and set up your environment. You can do this using the following steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/B0RDERS/semantic_search.git
   ```

2. Change to the project directory:

   ```bash
   cd semantic_search
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

5. Install project dependencies:

   ```bash
   pip install flask pymongo openai
   ```

6. Create config.json:

    ```bash
   cp config.json.template config.json
   ```
   Then fill in the config.json file with your information

### Usage

Now that you have set up the project, you can run it with the following command:

```bash
python server.py
```
