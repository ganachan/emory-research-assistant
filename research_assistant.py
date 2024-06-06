# Importing the function to load environment variables from a .env file
# Importing necessary libraries
from dotenv import load_dotenv
import openai, os, requests

# Setting the API type to Azure
# Setting the API version
openai.api_type = "azure"
openai.api_version = "2023-10-01-preview" # Version

# Load environment variables from a .env file
# Uncomment this line to load environment variables from a .env file
# load_dotenv()

# Azure OpenAI setup
# Setting the API base URL
# Setting the OpenAI API key (use os.getenv("OPENAI_API_KEY") to load from environment)
# Setting the deployment ID
openai.api_base = "https://xxxx.eastus2.openai.azure.com/" # Add your endpoint here
openai.api_key = '<insert your keys>' #os.getenv("OPENAI_API_KEY")
deployment_id = "gpt-35-turbo-16k" # Add your deployment ID here

# Azure AI Search setup
# Setting the Azure AI Search endpoint
# Setting the Azure AI Search admin key (use os.getenv("SEARCH_KEY") to load from environment)
# Setting the Azure AI Search index name
search_endpoint = "https://xxxx.search.windows.net"; # Add your Azure AI Search endpoint here
search_key = '<insert your keys>'; # os.getenv("SEARCH_KEY")
search_index_name = "emory-predive-grant-maching"; # Add your Azure AI Search index name here

# Printing the configuration details
print("OpenAI API Key:", openai.api_key)
print("Search Key:", search_key)
print("OpenAI API Base:", openai.api_base)
print("Deployment ID:", deployment_id)
print("Search Endpoint:", search_endpoint)
print("Search Index Name:", search_index_name)

# Function to set up BYOD with the specified deployment ID
def setup_byod(deployment_id: str) -> None:
    """Sets up the OpenAI Python SDK to use your own data for the chat endpoint.
    :param deployment_id: The deployment ID for the model to use with your own data.
    To remove this configuration, simply set openai.requestssession to None.
    """
    
    # Custom adapter for BYOD
    class BringYourOwnDataAdapter(requests.adapters.HTTPAdapter):
        def send(self, request, **kwargs):
            request.url = f"{openai.api_base}/openai/deployments/{deployment_id}/extensions/chat/completions?api-version={openai.api_version}"
            return super().send(request, **kwargs)
    
    # Creating a session for requests
    session = requests.Session()
    # Mount a custom adapter which will use the extensions endpoint for any call using the given `deployment_id`
    session.mount(
        prefix=f"{openai.api_base}/openai/deployments/{deployment_id}",
        adapter=BringYourOwnDataAdapter()
    )
    # Setting the session in the OpenAI SDK
    openai.requestssession = session

# Setting up BYOD with the specified deployment ID
setup_byod(deployment_id)

# Defining the message for the chat completion
message_text = [{"role": "user", "content": "What are the grants available for AI/ML researchers?"}]

# Creating the chat completion request
completion = openai.ChatCompletion.create(
    messages=message_text,
    deployment_id=deployment_id,
    dataSources=[
      {
      "type": "AzureCognitiveSearch",  # Specifying the data source type
      "parameters": {
        "endpoint": search_endpoint,  # Specifying the endpoint for the Azure Cognitive Search
        "index_name": search_index_name,  # Specifying the index name for the Azure Cognitive Search
        "semantic_configuration": "default",  # Using the default semantic configuration
        "query_type": "vectorSemanticHybrid",  # Using vectorSemanticHybrid query type
        "fields_mapping": {},  # Fields mapping (empty in this case)
        "in_scope": True,  # Indicating that the data source is in scope
        "role_information": "System: \"Welcome to the Grant Recommendation System! To provide you with personalized grant recommendations, I'll ask you a few quick questions.\"\n\nSystem: \"What is your main research area or field of interest?\"\n\nSystem: \"What is the approximate amount of grant funding you are seeking for your project?\"\n\nSystem: \"Could you please briefly describe your background or current position?\"\n\nRecommendation Generation:\n\nUse the user's responses to these questions to filter and search the RAG dataset for relevant grant opportunities.\nApply natural language processing techniques to match the user's research area, funding requirements, and profile with the grant opportunities in the dataset.\nPresent the top recommendations to the user based on their input in bullet points.",  # Providing role information for the system
        "filter": None,  # No filter applied
        "strictness": 3,  # Setting the strictness level
        "top_n_documents": 5,  # Specifying the number of top documents to retrieve
        "authentication": {
          "type": "api_key",  # Using API key for authentication
          "key": search_key  # The API key for authentication
        },
        "embedding_dependency": {
          "type": "deployment_name",  # Using deployment name for embedding dependency
          "deployment_name": "your_AI_indexer_name" # Your indexer name here
        },
        "key": search_key,  # The API key for the search
        "indexName": search_index_name  # The index name for the search
      }
    }],
    temperature=0,  # Setting the temperature for the completion
    top_p=1,  # Setting the top_p parameter for the completion
    max_tokens=800,  # Setting the maximum number of tokens for the completion
    stop=[],  # No stop sequences
    stream=False  # Not streaming the response
)

# Printing the completion result
print(completion)
