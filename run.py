from flaskblog import create_app,socketio
app=create_app()


if __name__=='__main__':
    # app.app_context().push()
    # socketio.run(app)
    app.run()