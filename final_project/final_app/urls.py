from django.urls import path
from . import views
from .views import engagement_ratio
from .views import retrain_model_view, predict_gpa, home, attendance_predict_view
from .views import recommend_courses
from django.contrib import admin

urlpatterns = [
    path('', home, name='home'),
    path("predict-career/", views.predict_career, name="predict_career"),
    path('admin/', admin.site.urls),
    path('retrain-model/<int:model_id>/', retrain_model_view, name='retrain-model'),
    path('engagement-ratio/', engagement_ratio, name='engagement_ratio'),
    # path('', home, name='home'),
    path('predict_gpa/', predict_gpa, name='predict_gpa'),
    path('recommend-courses/', recommend_courses, name='recommend_courses'),
]

# from django.urls import path, include
# from . import views
# from django.contrib import admin
# from .views import retrain_model_view, predict_gpa, home

# urlpatterns = [
#     path('admin/', include([
#         path('', admin.site.urls),
#         path('admin/retrain-model/', retrain_model_view, name='retrain-model'),
#     ])),
#     path('', home, name='home'),
#     path('predict_gpa/', predict_gpa, name='predict_gpa'),
# ]

