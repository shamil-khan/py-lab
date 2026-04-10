from langchain_community.document_loaders import TextLoader, WebBaseLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language
from langchain_openai import OpenAIEmbeddings

def print_section(title="", section=""):
    print("\n" + "="*40 + title + "="*40 + "\n")
    print(section)


def main():
    loader = TextLoader("docs/sample.txt")
    documents = loader.load()
    # print_section(" Original Document ", documents[0].page_content[:1000])
    print_section(" Original Document ", documents[0])
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    splitted_documents =text_splitter.split_documents(documents)
    print_section(" Splitted Documents ", splitted_documents)
    
    model = OpenAIEmbeddings(
        openai_api_base="http://localhost:1234/v1", 
        openai_api_key="lm-studio", # Key is usually ignored by local servers but required
        check_embedding_ctx_length=False, 
        model="nomic-embed-text-v1.5" 
    )
    embeddings = model.embed_documents([
        chunk.page_content for chunk in splitted_documents
    ])
    print_section(" Embeddings ", embeddings)

if __name__ == "__main__":
    main()
