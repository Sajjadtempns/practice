from unfold.sites import UnfoldAdminSite
from .forms import AdminLoginForm


class MyAdminSite(UnfoldAdminSite):
    login_form = AdminLoginForm


admin_site = MyAdminSite(name="admin")