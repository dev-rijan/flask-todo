run:
	@printf "\033[0;32m>>> Running app\033[0m\n"
	pipenv run gunicorn -c "python:config.gunicorn" "todos.app:create_app()"

install:
	@printf "\033[0;32m>>> Installing dependencies\033[0m\n"
	pip3 install -r requirements.txt

