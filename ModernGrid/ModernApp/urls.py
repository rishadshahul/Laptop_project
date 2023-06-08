from django.urls import path
from ModernApp import views

urlpatterns=[
    path('indexpage/', views.indexpage, name="indexpage"),

#-------------------------------------CATEGORY------------------------------------------------------------------#

    path('AddCategory/',views.AddCategory,name="AddCategory"),
    path('saveCategory/',views.saveCategory,name="saveCategory"),
    path('DisplayCategory/',views.DisplayCategory,name="DisplayCategory"),

#--------------------------------------CATEGORY-CRUD----------------------------------------------------------------------#


    path('EditCategory/<int:dataid>',views.EditCategory,name="EditCategory"),
    path('UpdateCategory/<int:dataid>',views.UpdateCategory,name="UpdateCategory"),
    path('deleteCategory/<int:dataid>', views.deleteCategory, name="deleteCategory"),

#--------------------------------------PRODUCT------------------------------------------------------------------#

    path('AddProduct/',views.AddProduct,name="AddProduct"),
    path('saveProduct/',views.saveProduct,name="saveProduct"),
    path('DisplayProduct/',views.DisplayProduct,name="DisplayProduct"),


#--------------------------------------PRODUCT-CRUD----------------------------------------------------------------------#
    path('EditProduct/<int:dataid>',views.EditProduct,name="EditProduct"),
    path('UpdateProduct/<int:dataid>', views.UpdateProduct, name="UpdateProduct"),
    path('DeleteProduct/<int:dataid>', views.DeleteProduct, name="DeleteProduct"),

#--------------------------------------LOGIN PAGE----------------------------------------------------------------#

    path('loginPAGE/',views.loginPAGE,name="loginPAGE"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('Userlogout/',views.Userlogout,name="Userlogout"),









]

