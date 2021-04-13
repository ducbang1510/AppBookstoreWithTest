from app import admin, db
from app.models import *
from flask import redirect
from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user, logout_user


class AuthenticatedView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


class MyModelView(AuthenticatedView):
    column_display_pk = True
    can_create = True
    can_export = True
    can_delete = True


class ContactView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/contact.html')


class LogOutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')

    def is_accessible(self):
        return current_user.is_authenticated


admin.add_view(LogOutView(name="Đăng xuất"))
admin.add_view(ContactView(name='Liên hệ'))

admin.add_view(MyModelView(Customer, db.session, name='Khách hàng'))
admin.add_view(MyModelView(Author, db.session, name='Tác giả'))
admin.add_view(MyModelView(Category, db.session, name='Thể loại'))
admin.add_view(MyModelView(Book, db.session, name='Sách'))

admin.add_view(MyModelView(Invoice, db.session, name='Hóa đơn'))
admin.add_view(MyModelView(DetailInvoice, db.session, name='Chi tiết hóa đơn'))
admin.add_view(MyModelView(InventoryReport, db.session, name='Báo cáo tồn'))
admin.add_view(MyModelView(DetailInventoryReport, db.session, name='Chi tiết báo cáo tồn'))