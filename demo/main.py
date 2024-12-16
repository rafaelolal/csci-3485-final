from easy_embed.easy_embed.src.main import App

if __name__ == "__main__":
    app = App()
    # to set a custom model
    # app.set_model(**kwargs)
    app.run(host="0.0.0.0", port=8000)
