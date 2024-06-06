Grant Allocation Assistant
This project uses sample grant allocation data from grants.gov to create an assistant that helps users find information about available grants for AI/ML researchers. The assistant utilizes the Azure OpenAI service and Azure Cognitive Search to provide personalized grant recommendations based on user input.

Introduction
The Grant Allocation Assistant is designed to assist researchers in finding relevant grant opportunities by leveraging AI and machine learning. By integrating Azure OpenAI and Azure Cognitive Search, this assistant can process user queries and provide tailored recommendations for grants.

The data used in this project is sourced from grants.gov, a reliable resource for finding and applying for federal grants. The assistant uses this data to offer accurate and up-to-date grant information.

Setup Instructions
To set up the Grant Allocation Assistant, follow these steps:


1. Clone the Repository
git clone [https://github.com/yourusername/grant-allocation-assistant.git]
cd grant-allocation-assistant

2. Create a Virtual Environment and Install Dependencies
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
pip install -r requirements.txt

3. Create a .env File
Create a .env file in the root directory of the project to provide your API keys and endpoints. The .env file should have the following format:

OPENAI_API_KEY=your_openai_api_key
SEARCH_KEY=your_search_key

4. Update Configuration
Update the configuration in app.py to use your specific endpoints and deployment IDs.

5. Run the Application
python research_assistant.py

Usage
Once the application is set up and running, you can interact with the assistant by providing your research area, the amount of funding you are seeking, and a brief description of your background. The assistant will use this information to search the grant data and provide personalized recommendations.

Contributing
We welcome contributions to enhance the functionality of the Grant Allocation Assistant. Feel free to open issues or submit pull requests.


License
This project is licensed under the MIT License. See the LICENSE file for details.

