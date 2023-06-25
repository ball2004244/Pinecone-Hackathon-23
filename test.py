from logic.ai_training import PineconeTrainer
from config import GCP_API_KEY, PINECONE_API_KEY, PINECONE_ENVIRONMENT

pinecone_trainer = PineconeTrainer(
    gcp_api_key=GCP_API_KEY,
    pinecone_api_key=PINECONE_API_KEY,
    pinecone_environment=PINECONE_ENVIRONMENT,
)

def create_index():
    input_file = 'logic/dataset.json'
    data = pinecone_trainer.extract_input_text(input_file)
    pinecone_trainer.add_data(data)

def get_info():
    info = pinecone_trainer.get_index_info()
    print(info)

def main():
    _input = 'Russia'
    output = pinecone_trainer.query(query=_input)

    print(output)

if __name__ == '__main__':
    main()


