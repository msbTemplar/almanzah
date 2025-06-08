from django.contrib import admin
from .models import Newsletter, Tab, TabPage,Status, PropertyType, Property, PropertyImage, Purpose, Country, ContactInfo,ContactMessage,PropertyReservation, HeaderSlide,HeaderSlideImage,Testimonial, ClientsHeadersHome


# Register your models here.

admin.site.register(Tab)
admin.site.register(TabPage)
admin.site.register(Newsletter)
admin.site.register(Purpose)
admin.site.register(Country)
admin.site.register(PropertyReservation)
# admin.site.register(ContactInfo)
admin.site.register(ContactMessage)
# admin.site.register(Property)
@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('label', 'name', 'is_active', 'created_at', 'updated_at', 'created_by')
    list_filter = ('is_active',)
    search_fields = ('label', 'name')

@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ('label', 'name', 'is_active', 'created_at', 'updated_at', 'created_by')
    list_filter = ('is_active',)
    search_fields = ('label', 'name')
    
class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1  # Número de formularios vacíos por defecto

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImageInline]
    list_display = ('property_title', 'property_code', 'property_price', 'property_created_at', 'property_is_active')
    
    

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('contact_info_name', 'contact_info_email', 'contact_info_phone_number', 'contact_info_is_active')
    list_filter = ('contact_info_is_active', 'contact_info_created_at')
    search_fields = ('contact_info_name', 'contact_info_email', 'contact_info_phone_number')
    fields = (
        'contact_info_name', 'contact_info_phone_number', 'contact_info_email',
        'contact_info_facebook_url', 'contact_info_twitter_url', 'contact_info_linkedin_url', 'contact_info_instagram_url',
        'contact_info_date', 'contact_info_time', 'contact_info_day',
        'contact_info_img_url', 'contact_info_file',
        'contact_info_map_embed_url',  # nuevo campo aquí
        'contact_info_is_active'
    )

#admin.site.register(HeaderSlide)
class HeaderSlideImageInline(admin.TabularInline):
    model = HeaderSlideImage
    extra = 1

@admin.register(HeaderSlide)
class HeaderSlideAdmin(admin.ModelAdmin):
    inlines = [HeaderSlideImageInline]
    
    

admin.site.register(Testimonial)


@admin.register(ClientsHeadersHome)
class ClientsHeadersHomeAdmin(admin.ModelAdmin):
    list_display = [  # Campos que se verán en la lista de objetos (pantalla principal del admin)
        'clients_headers_home_title_1',
        'clients_headers_home_description_1',
        'clients_headers_home_title_2',
        'clients_headers_home_description_2',
        'clients_headers_home_title_3',
        'clients_headers_home_title_4',
        'clients_headers_home_title_5',
        'clients_headers_home_title_6',
        'clients_headers_home_title_contact',
        'clients_headers_home_description_contact',
        'clients_headers_home_is_active',
        'clients_headers_home_created_at',
        'clients_headers_home_updated_at',
    ]
    
    readonly_fields = ['clients_headers_home_created_at', 'clients_headers_home_updated_at']
    
    fields = [  # Campos que se verán al hacer clic (formulario de edición)
        'clients_headers_home_title_1',
        'clients_headers_home_description_1',
        'clients_headers_home_title_2',
        'clients_headers_home_description_2',
        'clients_headers_home_title_3',
        'clients_headers_home_title_4',
        'clients_headers_home_description_4',
        'clients_headers_home_title_5',
        'clients_headers_home_title_6',
        'clients_headers_home_title_contact',
        'clients_headers_home_description_contact',
        'clients_headers_home_is_active',
        'clients_headers_home_created_by',
        'clients_headers_home_created_at',
        'clients_headers_home_updated_at',
    ]