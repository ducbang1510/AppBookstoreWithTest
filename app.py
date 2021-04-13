from app import create_app
from app.admin_view import *


class MyView(BaseView):
    def __init__(self, *args, **kwargs):
        self._default_view = True
        super(MyView, self).__init__(*args, **kwargs)
        self.admin = admin


app = create_app('app.cfg')
app.app_context().push()
app = app.run()
