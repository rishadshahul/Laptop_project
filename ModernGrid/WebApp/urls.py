from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
from django.urls import path

from ModernGrid import settings
from WebApp import views

urlpatterns=[


    path('indexnew/',views.indexnew,name="indexnew"),
    path('ShopPage/<itemcatg>/', views.ShopPage, name="ShopPage"),
    path('Productpage/<int:dataid>/', views.Productpage, name="Productpage"),
    path('AboutPage/', views.AboutPage, name="AboutPage"),
    path('BlogPage/', views.BlogPage, name="BlogPage"),
    path('Loginpage/', views.Loginpage, name="Loginpage"),
    path('Cartpage/', views.Cartpage, name="Cartpage"),


    path('Login/', views.Login, name="Login"),
    path('Signup_page/', views.Signup_page, name="Signup_page"),
    path('CustomerLOgin/', views.CustomerLOgin, name="CustomerLOgin"),
    path('logout/', views.logout, name="logout"),


    path('ContactPage/', views.ContactPage, name="ContactPage"),
    path('Contactsave/', views.Contactsave, name="Contactsave"),
    path('Contactdisplay/', views.Contactdisplay, name="Contactdisplay"),
    path('ContactDlt/<int:dataid>/', views.ContactDlt, name="ContactDlt"),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)