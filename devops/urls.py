"""devops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from rest_framework import routers

from books.views import PublishViewSet, AuthorViewSet, BookViewSet
from users.views import UsersViewSet, UserRegViewSet,UserInfoViewset
from groups.views import UserGroupViewSet,GroupViewSet,GroupMemberList,GroupMemberNoList
from permissions.views import PermissionViewSet,GroupPermissionViewSet
from rest_framework_jwt.views import obtain_jwt_token

from workorder.views import WorkOrderViewSet

router = routers.DefaultRouter()
router.register("userGroups", UserGroupViewSet, base_name='userGroups')
router.register("groups", GroupViewSet, base_name='groups')
router.register("groupUsers", GroupMemberList, base_name='groupUsers')
router.register("groupNoUsers", GroupMemberNoList, base_name='groupNoUsers')
router.register("users", UsersViewSet, base_name='users')
router.register("userReg", UserRegViewSet, base_name='userReg')
router.register("permission", PermissionViewSet, base_name='permission')
router.register("groupPermission", GroupPermissionViewSet, base_name='groupPermission')
router.register("publish", PublishViewSet, base_name='publish')
router.register("author", AuthorViewSet, base_name='author')
router.register("book", BookViewSet, base_name='book')
router.register("UserInfo", UserInfoViewset, basename="UserInfo")
router.register("workorder", WorkOrderViewSet, basename="workorder")


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='api文档')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token),

]

#from resources.apscheduler import scheduler


#scheduler.start()
