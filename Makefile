run-dev:
	@echo "Running dev environment..."
	@docker-compose up -d postgres
	@uvicorn webapp.main:app --reload --host 0.0.0.0 --port 8000
