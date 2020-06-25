# todos

**Clone** project from: https://gitlab.com/flask-applications/todos

**Copy** .env.example and create .env file and change environment variables according to your environment setup.

**Run** `pipenv install` : If you encounter pg_config executable not found error in ubuntu then run `sudo apt-get install libpq-dev` .
Details https://tutorials.technology/solved_errors/9-Error-pg_config-executable-not-found.html

**Install dependencies**: If you have `make` available in your os then type make install from project root dir.
If you don’t have `make` installed then type the following command one by one.
 - `pipenv install`  (It installs dependencies and also create virtual env for us)
 - `cd assets`
 - `yarn install` (You should have yarn installed globally. It install dependencies for frontend)
 - `yarn run build` (It compiles, minifies and generate compiled js and css file to public dir)
 - `cd .. `(return to root dir)
 - `pipenv run flask digest compile` (Flask extension to help make your static files production ready by md5 tagging and gzipping them)

**Initialize database**: (Assume that you create a database same as defined in DATABASE_URI env variable) 

Run `pipenv run flask init-db init`
Run `pipenv run flask init-db seed`

**Run application**: If you have make available in your os then type `make run` from project root dir.
If you don’t have make installed then type the following command.

`pipenv run gunicorn -c "python:config.gunicorn" "todos.app:create_app()"`

Now your app is available at `http://localhost:8000`

**Seed users**: You can generate fake users using `pipenv run flask seed users`

**Login**: Now users are created. You can’t register an account for admin from UI. we already created using seeder,
  credentials for admin user is same as defined in `env vars(SEED_ADMIN_USER, SEED_ADMIN_PASSWORD)`

