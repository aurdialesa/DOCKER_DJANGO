from django.contrib import admin
from django.urls import path, include

# ✅ Agregado para poder usar la vista home
from . import views   

urlpatterns = [
    path('admin/', admin.site.urls),          # 👈 esto estaba ya
    path('api/', include('api.urls')),        # 👈 esto estaba ya
    
    # ✅ Agregado para que la raíz "/" muestre la vista home
    path('', views.home, name='home'),        
]
