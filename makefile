run:
	@printf "\033[0;32m>>> Running app\033[0m\n"
	pipenv run gunicorn -c "python:config.gunicorn" "todos.app:create_app()"

install:
	@printf "\033[0;32m>>> Installing dependencies\033[0m\n"
	pipenv install && cd assets && yarn install && yarn run build && cd .. && pipenv run flask digest compile

