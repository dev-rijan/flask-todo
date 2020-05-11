run:
	@printf "\033[0;32m>>> Running app\033[0m\n"
	gunicorn -b 0.0.0.0:8000 "todos.app:create_app()"

install:
	@printf "\033[0;32m>>> Installing dependencies\033[0m\n"
	pip3 install -r requirements.txt

