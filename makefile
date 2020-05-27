run:
	@printf "\033[0;32m>>> Running app\033[0m\n"
	pipenv run gunicorn -c "python:config.gunicorn" "todos.app:create_app()"

install:
	@printf "\033[0;32m>>> Installing dependencies\033[0m\n"
	pipenv install 
	make build

build:
	@printf "\033[0;32m>>> Compiling assets\033[0m\n"
	cd assets \
	&& yarn run build \
	&& cd .. \
	&& pipenv run flask digest compile

