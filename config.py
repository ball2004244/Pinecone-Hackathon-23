import dotenv
import os

dotenv.load_dotenv()
GCP_API_KEY = str(os.getenv('GCP_API_KEY'))
PINECONE_API_KEY = str(os.getenv('PINECONE_API_KEY'))
PINECONE_ENVIRONMENT = str(os.getenv('PINECONE_ENVIRONMENT'))