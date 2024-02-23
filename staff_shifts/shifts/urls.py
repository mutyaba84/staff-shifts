from django.urls import path
from .views import (
    ShiftListView,
    ShiftCreateView,
    ShiftUpdateView,
    MakeOfferView,
    CancelShiftView,
    SetReminderView,
)

app_name = 'shifts'

urlpatterns = [
    path('', ShiftListView.as_view(), name='shift-list'),
    path('create/', ShiftCreateView.as_view(), name='shift-create'),
    path('<int:pk>/update/', ShiftUpdateView.as_view(), name='shift-update'),
    path('<int:pk>/make-offer/', MakeOfferView.as_view(), name='make-offer'),
    path('<int:pk>/cancel/', CancelShiftView.as_view(), name='cancel-shift'),
    path('<int:pk>/set-reminder/', SetReminderView.as_view(), name='set-reminder'),
    # Add more URL patterns as needed
]
