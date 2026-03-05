# 📚 Hub Inteligente de Recursos Educacionais
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/JVLFcc/educational-resources-hub)

This is a full-stack Single Page Application (SPA) for managing educational resources, featuring an integration with Google's Gemini AI to automatically generate pedagogical descriptions and relevant tags.

## 🚀 Overview

The **Educational Resources Hub** allows users to perform full CRUD (Create, Read, Update, Delete) operations on educational materials. Its standout feature is the "Smart Assist," which leverages a Large Language Model (LLM) to enrich resource entries with AI-generated content, streamlining the organization process for educators.

**Core Features:**
-   📌 **Resource Management:** Add, view, edit, and delete educational resources (links, videos, PDFs).
-   📋 **Paginated List:** View all resources in a clean, paginated list.
-   🤖 **AI-Powered Descriptions:** Automatically generate a pedagogical description and three specific tags for a resource based on its title and type using the Google Gemini API.
-   🔒 **Secure & Modular:** Built with a clean architecture, structured data validation, and secure API key management.
-   ✨ **User-Friendly:** Provides loading states and visual feedback for a smooth user experience.

## 🏗️ Architecture

The project is divided into a frontend and a backend, each with its own modern technology stack.

### Backend

-   **Framework:** **FastAPI** for high-performance REST APIs.
-   **Database:** **SQLAlchemy** ORM for database interaction (compatible with SQLite, PostgreSQL, etc.).
-   **Data Validation:** **Pydantic** for robust data validation and settings management.
-   **AI Integration:** Google's **Gemini 2.5 Flash** for generating content.
-   **Logging:** Custom logging to monitor AI service latency and token usage.

### Frontend

-   **Framework:** **React** (with Vite) for building a fast and interactive SPA.
-   **State Management:** React Hooks (`useState`, `useEffect`) for managing component state and side effects.
-   **API Consumption:** Standard `fetch` API for communicating with the backend REST endpoints.
-   **UI:** Minimalist and functional UI with clear feedback for asynchronous operations like API calls.

## 🧠 Smart Assist (AI) Feature

The Smart Assist feature simplifies the process of adding new educational materials.

1.  **User Input:** The user provides a **Title** and **Resource Type** in the frontend form and clicks "Gerar Descrição com IA" (Generate Description with AI).
2.  **Backend Request:** The frontend sends this information to the `/resources/smart-assist` endpoint.
3.  **AI Generation:** The backend constructs a highly-structured system prompt and sends a request to the `gemini-2.5-flash` model, forcing a strict JSON output.
4.  **Logging:** The backend logs the total token count and request latency for monitoring purposes.
5.  **Response:** The AI returns a JSON object containing a pedagogical `description` and a list of three relevant `tags`.
6.  **UI Update:** The frontend receives the data and automatically populates the "Description" and "Tags" fields, giving the user a ready-to-save resource entry.

## 📦 Getting Started

Follow these instructions to get the project running on your local machine.

### Prerequisites

-   Python 3.8+ and `pip`
-   Node.js and `npm`
-   A Google Gemini API Key

### Backend Setup

1.  **Navigate to the backend directory:**
    ```sh
    cd backend
    ```

2.  **Create and activate a virtual environment:**
    ```sh
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Configure environment variables:**
    -   Create a `.env` file by copying the example:
        ```sh
        cp .env.example .env
        ```
    -   Open the `.env` file and set the following variables. For local development, an SQLite database is recommended.
        ```env
        DATABASE_URL=sqlite:///./resources.db
        GEMINI_API_KEY=YOUR_GEMINI_API_KEY_HERE
        ```

5.  **Run the backend server:**
    ```sh
    uvicorn app.main:app --reload
    ```
    The API will be available at `http://localhost:8000`.

### Frontend Setup

1.  **Navigate to the frontend directory:**
    ```sh
    cd frontend
    ```

2.  **Install the dependencies:**
    ```sh
    npm install
    ```

3.  **Run the frontend development server:**
    ```sh
    npm run dev
    ```
    The application will be available at `http://localhost:5173` (or another port if 5173 is in use).

## 📡 API Endpoints

The backend provides the following RESTful API endpoints.

| Method | Endpoint                    | Description                                         |
| :----- | :-------------------------- | :-------------------------------------------------- |
| `GET`  | `/health`                   | Checks if the API is running.                       |
| `POST` | `/resources/`               | Creates a new educational resource.                 |
| `GET`  | `/resources/`               | Lists all resources with pagination (`page`, `limit`). |
| `PUT`  | `/resources/{resource_id}`  | Updates an existing resource by its ID.             |
| `DELETE`| `/resources/{resource_id}`  | Deletes a resource by its ID.                       |
| `POST` | `/resources/smart-assist`   | Generates a description and tags using AI.          |
