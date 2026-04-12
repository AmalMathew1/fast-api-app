# FastAPI Item Service

A learning project demonstrating a 3-layer FastAPI application.

## Setup

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt


Running the app
uvicorn app.main:app --reload

Endpoints
Method	Path	Description
GET	/	Root
GET	/health	Health check
GET	/items	Get all items
GET	/items/{id}	Get item by ID
Docs
Visit http://localhost:8000/docs for interactive API documentation.