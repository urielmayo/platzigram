from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

#models
from django.contrib.auth.models import User
from users.models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    #muestra las variables visibles en la tabla
    list_display = (
        'pk',
        'user',
        'phone_number',
        'website',
        'profile_picture'
    )
    
    #linkea a los usuarios a la edicion
    list_display_links = (
        'pk',
        'user',
    )

    #esta linea permite que se editen los valores sin redireccionar a edicion
    list_editable = (
        'phone_number',
        'website',
    )

    #permitimos la busqueda de usuarios segun los distintos campos
    search_fields = (
        'user__first_name',
        'user__last_name',
        'user__email',
    )

    list_filter = (
        'created',
        'modified',
        'user__is_active',
        'user__is_staff',
    )

    fieldsets = (
        ('Profile', {
            'fields': (('user', 'profile_picture'),),
            }
        ),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
            }
        ),
        ('Metadata', {
            'fields': (('created', 'modified'),),
            }
        )
    )

    readonly_fields = ('created', 'modified',)


class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users."""

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""

    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)