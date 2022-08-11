from django.urls import path,include
import pinmoney.views as views

app_name = 'pinmoney'

urlpatterns = [
    path('give/',views.give,name='give'),
    path('transaction/',views.transaction,name='transaction'),
    path('certification/',views.certification,name='certification'),
    path('success/',views.success,name='success'),
    path('regular/',views.regular,name="regular"),
    path('regular_list/',views.Regular_list,name="regular_list"),
]