"""
URL configuration for team app.
"""
from django.urls import path
from apps.team.views import TeamView, TeamMemberDetailView

app_name = 'team'

urlpatterns = [
    path('', TeamView.as_view(), name='list'),
    path('member/<str:reg_number>/', TeamMemberDetailView.as_view(), name='member_detail'),
]