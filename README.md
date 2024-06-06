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




Results 

Hello! My name is Gana,, I'm a Ph.D. student in Environmental Science at Stanford University. I'm looking for grants in the range of $50,000 to $100,000.My research focuses on the impact of climate change on marine biodiversity in coastal regions


Hello Gana! Based on the retrieved documents and your specified criteria, here is a grant opportunity that might align with your research interests in Environmental Science, specifically focusing on the impact of climate change on marine biodiversity in coastal regions:

Grant ID: G002
Research Area: Environmental Science
Project Proposal: Study on the impact of climate change on marine biodiversity in the Arctic region
Grant Amount: $150,000
Deadline: 2024-09-30
Eligibility Criteria: Open to researchers with expertise in Environmental Science 1 .
While the grant amount for G002 is above your specified range, it is the most relevant to your research focus as listed in the documents. If you can adjust your budget requirements or find additional funding sources to cover the difference, this could be a potential option to explore.

Hello! My name is Alex,, I'm a Ph.D. student in Environmental Science at Stanford University. I'm looking for grants in the range of $50,000 to $100,000.My research focuses on the impact of climate change on marine biodiversity in coastal regions



Hello Gana! Based on the information you've provided and the retrieved documents, here are a couple of grant opportunities that might align with your research interests and funding requirements:

Grant ID: G002
Research Area: Environmental Science
Project Proposal: Study on the impact of climate change on marine biodiversity in the Arctic region
Grant Amount: $150,000
Deadline: 2024-09-30
Eligibility Criteria: Open to researchers with expertise in Environmental Science 1 .
Although the grant amount for G002 is slightly above your specified range, it closely matches your research focus. It might be worth considering if you can adjust your budget requirements.

Grant ID: G031
Research Area: Environmental Engineering
Project Proposal: Designing wastewater treatment systems for remote communities
Grant Amount: $200,000
Deadline: 2024-10-31
Eligibility Criteria: Environmental engineers with expertise in water treatment and sanitation 2 .
While G031 is not directly related to marine biodiversity, it falls within the broader scope of environmental science and could be relevant if your research extends to environmental engineering and the impact of climate change on water treatment in coastal regions.

Please note that both of these grants exceed your funding range, but they are the closest matches to your research area in the provided documents. If you are flexible with the grant amount, these could be potential options to explore. If you require grants strictly within the $50,000 to $100,000 range, I would recommend looking for additional opportunities that may not be listed in the current dataset.



License
This project is licensed under the MIT License. See the LICENSE file for details.

