docker compose build
docker compose up --build

Run with:
curl -X POST http://localhost:8000/analyze \
-H "Content-Type: application/json" \
-d '{"company":"Walmart"}'
