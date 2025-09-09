# conversational_chatbot_with_Gemini

# Conversational Chat Bot with Gemini

A conversational chatbot powered by Google Gemini, built with [LangGraph](https://github.com/langchain-ai/langgraph) for managing conversation flow and [SQLite](https://www.sqlite.org/) for persistent chat history. The project is designed to be deployed as a [Streamlit](https://streamlit.io/) web application.

---

## Features

- Conversational AI using Google Gemini (Generative AI)
- Persistent chat history using SQLite
- Modular and extensible codebase
- Easy deployment with Streamlit

---

## Installation

### Prerequisites

- Python 3.9 or higher
- Google API Key for Gemini

### Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your API key:**
    - Create a `.env` file in the project root directory.
    - Add your Google API key:
        ```
        GOOGLE_API_KEY="your-google-api-key-here"
        ```

---

## Usage

1. **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```
    *(Replace `app.py` with your actual Streamlit app filename if different.)*

2. **Interact with the chatbot** through the web interface.

---

## Configuration

- The chatbot requires a valid Google API key for Gemini, provided via the `.env` file.
- All chat history is stored in a local SQLite database (`chatbot.db`).

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for improvements or bug fixes.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [LangGraph](https://github.com/langchain-ai/langgraph)
- [Google Gemini](https://ai.google.dev/gemini-api/docs)
- [Streamlit](https://streamlit.io/)
