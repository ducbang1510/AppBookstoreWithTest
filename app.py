from app import create_app
from app.admin_view import *

app = create_app('app.cfg')
app.app_context().push()
app = app.run()
