from django.urls import path, include
import MyAPI.views as views

urlpatterns = [
    path('prisk/', views.Risk_Amount.as_view(), name='risk_amount'),
    path('sum/', views.sum, name='sum'),
    path('add_values/', views.Add_Values.as_view(), name='api_add_values')
]

