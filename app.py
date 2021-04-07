from app import create_app

app = create_app('app.cfg')
app = app.run()
