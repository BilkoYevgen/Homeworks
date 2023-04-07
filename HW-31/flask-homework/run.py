from my_app import app


if __name__ == '__main__':
    app.run(port=app.config.get("PORT"),
            host=app.config.get("HOST"),
            debug=app.config.get("DEBUG"))
