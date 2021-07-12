run: ## Run the backend server
	python manage.py runserver 0.0.0.0:8080

black:
	black --color --exclude '^.*\b(migrations)\b.*$$' .

black-diff:
	black --color --diff --exclude '^.*\b(migrations)\b.*$$' .

lint: ## Lint Python code
	flake8 .
	black --check --color --exclude '^.*\b(migrations)\b.*$$' .

migrations: ## Create or update database schema
	python manage.py makemigrations

migrate: ## Apply database schema
	python manage.py migrate

test:
	python manage.py test $(filter-out $@,$(MAKECMDGOALS))

fail:
	python manage.py test $(filter-out $@,$(MAKECMDGOALS)) --failfast

%:
	@:

build: ## Build the frontend assets (CSS, JS, images)
	npm run build

deploy: ## Build the frontend assets (CSS, JS, images)
	git pull
	venv
	npm install
	npm run build-production
	python manage.py collectstatic
	deactivate
	sudo supervisorctl restart pys

watch: ## Build the frontend assets when they are modified
	npm run watch

redis:
	docker container start redis

fixtures:
	python manage.py loaddata fixtures/init_etypes.json
