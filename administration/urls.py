from django.urls import include, path, re_path
from django.conf import settings
from django.views.static import serve
from administration.views import dashboard as dashboard_views
from administration.views import experience as experience_views
from administration.views import skill as skill_views
from administration.views import user as user_views
from administration.views import authenticate as auth_views

app_name = "administration"

urlpatterns = [
    path('', dashboard_views.Dashboard.as_view(), name="dashboard"),
    #### USER ####
    path('utilisateurs/', user_views.Users.as_view(), name="users"),
    path('utilisateurs/ajout/', user_views.UserCreate.as_view(), name="user_create"),
    path('utilisateurs/<int:user_pk>/update/', user_views.UserUpdate.as_view(), name="user_update"),
    path('utilisateurs/<int:user_pk>/delete/', user_views.UserDelete.as_view(), name="user_delete"),
    #### CONTENT #####
    path('experience/', experience_views.Experience.as_view(), name="experience"),
    path('experience/ajout/', experience_views.ExperienceCreate.as_view(), name="experience_create"),
    path('experience/<int:experience_pk>/update/', experience_views.ExperienceUpdate.as_view(),
         name="experience_update"),
    path('experience/<int:experience_pk>/delete/', experience_views.ExperienceDelete.as_view(),
         name="experience_delete"),
    path('skill/', skill_views.Skill.as_view(), name="skill"),
    path('skill/ajout/', skill_views.SkillCreate.as_view(), name="skill_create"),
    path('skill/<int:skill_pk>/update/', skill_views.SkillUpdate.as_view(),
         name="skill_update"),
    path('skill/<int:skill_pk>/delete/', skill_views.SkillDelete.as_view(),
         name="skill_delete"),
    path('login/', auth_views.LoginUser.as_view(), name='login_user'),
    path('logout/', auth_views.LogoutUser.as_view(), name='logout_user'),
]
