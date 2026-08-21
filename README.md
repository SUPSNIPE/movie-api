# Movie Recommender API

A backend REST API built with Python and FastAPI that interfaces directly with the [TMDB (The Movie Database) API](https://developer.themoviedb.org/docs) to fetch dynamic movie recommendations. 

The application processes user search parameters and dynamically fetches the top 5 recommended movies based on the query data, demonstrating RESTful API architecture and third-party data integration.

## Features
* **Dynamic Search:** Pass in search queries to receive tailored movie recommendations.
* **Top 5 Filtering:** Automatically sorts and returns the top 5 most relevant results.
* **Secure Credential Management:** Utilizes environment variables to keep API keys secure.
* **Automated Documentation:** Leverages FastAPI's built-in Swagger UI for easy endpoint testing.

## Tech Stack
* **Language:** Python
* **Framework:** FastAPI
* **Server:** Uvicorn
* **External API:** TMDB API

## Installation & Setup

If you want to run this project locally, follow these steps:

**1. Clone the repository**
```bash
git clone [https://github.com/SUPSNIPE/movie-api.git](https://github.com/SUPSNIPE/movie-api.git)
cd movie-api
```

**2. Create a virtual environment**
```bash
python -m venv venv
```

**3. Activate the virtual environment**
* On Windows:
  ```bash
  venv\Scripts\activate
  ```
* On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

**4. Install dependencies**
```bash
pip install -r requirements.txt
```

**5. Set up your Environment Variables**
Create a file named `.env` in the root directory of the project and add your TMDB API Key:
```text
TMDB_API_KEY=your_api_key_here
```

## Usage

Start the local development server using Uvicorn:
```bash
uvicorn main:app --reload
```

Once the server is running, navigate to `http://127.0.0.1:8000/docs` in your browser. This will open the interactive Swagger UI where you can easily test the search endpoints.

---
*Created by [Richard Huang](https://github.com/SUPSNIPE)*
