from langchain_community.document_loaders import TextLoader, WebBaseLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language
from langchain_openai import OpenAIEmbeddings

def line(title=""):
    print("\n" + "="*40 + title + "="*40 + "\n")

def text_sample():
    loader = TextLoader("docs/sample.txt")
    return loader.load()

def pdf_sample():
    loader = PyPDFLoader("docs/sample.pdf")
    return loader.load()

def web_sample():
    # loader = WebBaseLoader("https://en.wikipedia.org/wiki/Artificial_intelligence")
    loader = WebBaseLoader("https://www.langchain.com/")
    return loader.load()

def python_sample():
    PYTHON_CODE = """
    def hello_world():
        print("Hello, World!")

    # Call the function
    hello_world()
    """
    python_splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.PYTHON, chunk_size=50, chunk_overlap=0
    )
    python_docs = python_splitter.create_documents([PYTHON_CODE])    
    return python_docs

def embed_sample():
    model = OpenAIEmbeddings(
        openai_api_base="http://localhost:1234/v1", 
        openai_api_key="lm-studio", # Key is usually ignored by local servers but required
        check_embedding_ctx_length=False, 
        model="nomic-embed-text-v1.5" 
    )
    embeddings = model.embed_documents([
        "Hi there!",
        "Oh, hello!",
        "What's your name?",
        "My friends call me World",
        "Hello World!"
    ])
    return embeddings

def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return text_splitter.split_documents(documents)

if __name__ == "__main__":
    # This is a sample text file for testing RAG. It contains multiple lines of text to simulate a larger document. The purpose of this file is to provide content for retrieval and generation tasks
    
    line(" Text sample ")
    documents = text_sample()
    splitted = split_documents(documents)
    print(splitted)

    # line(" PDF sample ")
    # documents = pdf_sample()
    # splitted = split_documents(documents)
    # print(splitted)


    # line(" Python Code sample ")
    # documents = python_sample()
    # splitted = split_documents(documents)
    # print(splitted)

    # line(" Web sample ")
    # documents = web_sample()
    # splitted = split_documents(documents)
    # print(splitted)

    # line(" Embedding sample ")
    # embeddings = embed_sample()
    # print(embeddings)
