from app import admin, get_data
from app.models import *
from flask import redirect
from flask_admin import BaseView, expose
from flask_admin.base import MenuLink
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user, logout_user


class AuthenticatedView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRole.ADMIN


class AuViewForBaseView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRole.ADMIN


class MyModelView(AuthenticatedView):
    column_display_pk = True
    can_create = True
    can_export = True
    can_delete = True


class BookModelView(AuthenticatedView):
    column_display_pk = True
    can_create = False
    can_export = True
    can_delete = True
    form_columns = ('name', 'content', 'description', 'image', 'price', 'quantity', 'categories', 'authors',)


class InventoryReportView(AuthenticatedView):
    column_display_pk = True
    can_create = True
    can_export = True
    can_delete = True
    form_columns = ('report_date',)


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


class TempBookView(AuViewForBaseView):
    @expose('/')
    def index(self):
        categories = get_data.get_category()
        authors = get_data.get_authors()

        return self.render('admin/temp_book.html', categories=categories, authors=authors)


admin.add_view(LogOutView(name="Đăng xuất"))
admin.add_view(ContactView(name='Liên hệ'))

admin.add_view(MyModelView(User, db.session, name="User"))
admin.add_view(MyModelView(Customer, db.session, name='Khách hàng'))
admin.add_view(MyModelView(Author, db.session, name='Tác giả'))
admin.add_view(MyModelView(Category, db.session, name='Thể loại'))
admin.add_view(BookModelView(Book, db.session, name='Sách'))

admin.add_view(TempBookView(name='Nhập Sách'))

admin.add_view(MyModelView(Invoice, db.session, name='Hóa đơn'))
admin.add_view(MyModelView(DetailInvoice, db.session, name='Chi tiết hóa đơn'))
admin.add_view(InventoryReportView(InventoryReport, db.session, name='Báo cáo tồn'))
admin.add_view(MyModelView(DetailInventoryReport, db.session, name='Chi tiết báo cáo tồn'))

admin.add_link(MenuLink(name='Thống kê', url='/report'))