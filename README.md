
# NewsBot: News Research Chatbot 📈

NewsBot is an intelligent chatbot designed to process news articles from user-provided URLs and answer user queries based on those articles. By leveraging advanced Natural Language Processing (NLP) techniques and embedding-based similarity search, RockyBot delivers precise answers along with source references.

---

## Features

- **Load URLs**: Input article URLs to fetch their content.
- **Process Articles**: Utilize LangChain’s tools to clean and split article content.
- **Generate Embeddings**: Convert text into vector embeddings using OpenAI's embedding model.
- **Efficient Retrieval**: Use FAISS for fast and accurate similarity-based search.
- **Answer Queries**: Interact with an LLM (via OpenAI API) to receive detailed answers and source references.

---

## How It Works

1. **Input**: Enter up to three news article URLs in the Streamlit sidebar.
2. **Data Loading**: Content is fetched from the URLs using `UnstructuredURLLoader`.
3. **Text Splitting**: Articles are split into manageable chunks using `RecursiveCharacterTextSplitter`.
4. **Embedding Creation**: Generate embeddings for text chunks using OpenAI embeddings.
5. **Indexing**: Store embeddings in a FAISS index for fast similarity search.
6. **Query Processing**: Input a question, and the system retrieves relevant chunks and generates an answer using an LLM.
7. **Output**: Display the answer and source links in the Streamlit interface.

---

## Installation

### Prerequisites
- Python 3.8 or later
- OpenAI API key (create an account on [OpenAI](https://openai.com) to get your API key)

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/rockybot.git
    ```
2. Navigate to the project directory:
    ```bash
    cd rockybot
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Set up your OpenAI API key:
    - Create a `.env` file in the root directory and add the following line:
      ```
      OPENAI_API_KEY=your_openai_api_key
      ```

---

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run main.py
    ```
2. The web app will open in your browser.
3. On the sidebar:
    - Input up to three URLs.
    - Click the **Process URLs** button.
4. Observe the system as it:
    - Loads and processes article content.
    - Splits text into chunks.
    - Builds and indexes embedding vectors.
5. Enter your question in the query box.
6. View the answer and source links.

---

## Example URLs

Here are some sample URLs for testing:
- [Tata Motors gains production-linked payouts](https://www.moneycontrol.com/news/business/tata-motors-mahindra-gain-certificates-for-production-linked-payouts-11281691.html)
- [Tata Motors launches Punch ICNG](https://www.moneycontrol.com/news/business/tata-motors-launches-punch-icng-price-starts-at-rs-7-1-lakh-11098751.html)
- [Buy Tata Motors - Target Price Rs 743](https://www.moneycontrol.com/news/business/stocks/buy-tata-motors-target-of-rs-743-kr-choksey-11080811.html)

---

## Project Structure

```plaintext
rockybot/
├── main.py               # Main Streamlit application script
├── requirements.txt      # List of required Python packages
├── faiss_store_openai.pkl # Saved FAISS index (generated after processing)
├── .env                  # Environment variables (API key)
└── README.md             # Project documentation
```

---

## How It Works (Under the Hood)

1. **LangChain Modules**:
   - `UnstructuredURLLoader`: Extracts text from article URLs.
   - `RecursiveCharacterTextSplitter`: Splits large articles into manageable chunks for analysis.
   - `OpenAIEmbeddings`: Converts text chunks into vector embeddings.
   - `FAISS`: Enables similarity search for fast retrieval.

2. **OpenAI API**:
   - Used for both embedding generation and query-answering tasks.

3. **Streamlit**:
   - Provides an intuitive web-based user interface for seamless interaction.

---

## Future Improvements

- Add support for more document formats (e.g., PDFs, Word files).
- Implement a local embedding model for cost efficiency.
- Enable conversational context for multi-turn queries.
- Enhance UI/UX for better user experience.

---

## Contributing

Contributions are welcome! Please fork the repository and create a pull request for any feature suggestions or bug fixes.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments

- [OpenAI](https://openai.com) for their powerful embedding and language models.
- [LangChain](https://www.langchain.com) for providing modular NLP tools.
- [FAISS](https://github.com/facebookresearch/faiss) for efficient similarity search.
- [Streamlit](https://streamlit.io) for the easy-to-use web interface.

---

## Screenshots

![RockyBot Interface](rockybot.jpg)
*Example of RockyBot fetching and answering queries based on news articles.*

---

Happy Researching! 🚀
