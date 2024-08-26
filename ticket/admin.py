from django.contrib import admin
from .models import Ticket
# Register your models here.



class TicketAdmin(admin.ModelAdmin):
    list_display = ("category", "description", "status",)

admin.site.register(Ticket, TicketAdmin)


# option 2
# admin.site.register(Ticket)

# option 3
# @admin.register(Ticket)
# class AuthorAdmin(admin.ModelAdmin):
#     pass


