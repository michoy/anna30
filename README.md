# Flask Server

This project is a simple Flask server that demonstrates how to set up a basic web application using the Flask framework.

## Project Structure

```
flask-server
├── app
│   ├── __init__.py
│   └── routes.py
├── requirements.txt
├── run.py
└── README.md
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd flask-server
   ```

2. **Create a virtual environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```
   pip install -r requirements.txt
   ```

## Running the Server

To run the Flask server, execute the following command:

```
python run.py
```

The server will start and you can access it at `http://127.0.0.1:5000`.

## Usage

You can define your routes in the `app/routes.py` file. The application is initialized in `app/__init__.py`, and the server entry point is in `run.py`. 

Feel free to modify the code to suit your needs!