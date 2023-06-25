import json

# read file
def read_file(path: str) -> str:
    try:
        with open(path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f'File {path} not found')
        return ''

# read json data from dataset
def extract_data(path: str) -> list:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            
        # get the value of the key 'rows'
        return json_data['rows']
    except FileNotFoundError:
        print(f'File {path} not found')
        return []

def extract_text(data: list) -> list:
    try:
        texts = []
        for item in data:
            text = item['row']['text']
            texts.append(text)

        return texts
    except Exception as e:
        print(e)
        return []
    
def extract_output_text(data: list) -> list:
    try:
        texts = []
        for item in data:
            text = item['row']['prediction'][0]['text']
            texts.append(text)

        return texts
    except Exception as e:
        print(e)
        return []

if __name__ == "__main__":
    name = 'logic/dataset.json'
    data = extract_data(name)
    texts = extract_text(data)
    # print(texts[0])

    output_texts = extract_output_text(data)
    print(output_texts[0])