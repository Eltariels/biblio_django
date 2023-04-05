from django.contrib import admin

# Register your models here.
from .models import Bibliotheque, Abonne, Livre, Emprunt

admin.site.register(Bibliotheque)
admin.site.register(Abonne)
admin.site.register(Livre)
admin.site.register(Emprunt)