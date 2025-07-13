from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

# Create your models here.


class PropertyType(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    label = models.CharField(max_length=500, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.label


class Status(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    label = models.CharField(max_length=500, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.label

class Purpose(models.Model):
        purpose_name = models.CharField(max_length=500, null=True, blank=True)
        purpose_icon = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="Nombre del archivo de icono (ejemplo: icon-apartment.png)"
        )
        purpose_created_at = models.DateTimeField(auto_now_add=True, help_text="Fecha cuando se creo el tab.") 
        purpose_updated_at = models.DateTimeField(auto_now=True, help_text="Última vez que se actualizó el tab.")
        purpose_is_active = models.BooleanField(default=True, help_text="Define si este tab está activo y visible.")
        purpose_created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    

        def __str__(self):
            return self.purpose_name

class Country(models.Model):
    country_name = models.CharField(max_length=500, null=True, blank=True)
    country_created_at = models.DateTimeField(auto_now_add=True, help_text="Fecha cuando se creo el tab.") 
    country_updated_at = models.DateTimeField(auto_now=True, help_text="Última vez que se actualizó el tab.")
    country_is_active = models.BooleanField(default=True, help_text="Define si este tab está activo y visible.")
    country_created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    

    def __str__(self):
        return self.country_name

class ClientsHeadersHome(models.Model):
    clients_headers_home_title_1 = models.CharField(max_length=500, blank=True, null=True)
    clients_headers_home_description_1 = models.TextField(blank=True, null=True)
    clients_headers_home_title_2 = models.CharField(max_length=500, blank=True, null=True)
    clients_headers_home_description_2 = models.TextField(blank=True, null=True)
    clients_headers_home_title_3 = models.CharField(max_length=500, blank=True, null=True)
    clients_headers_home_title_4 = models.CharField(max_length=500, blank=True, null=True)
    clients_headers_home_description_4 = models.TextField(blank=True, null=True)
    clients_headers_home_title_5 = models.CharField(max_length=500, blank=True, null=True)
    clients_headers_home_title_6 = models.CharField(max_length=500, blank=True, null=True)
    clients_headers_home_title_contact = models.CharField(max_length=500, blank=True, null=True)
    clients_headers_home_description_contact = models.TextField(blank=True, null=True)
    clients_headers_home_created_at = models.DateTimeField(auto_now_add=True, help_text="Fecha cuando se creo el tab.") 
    clients_headers_home_updated_at = models.DateTimeField(auto_now=True, help_text="Última vez que se actualizó el tab.")
    clients_headers_home_is_active = models.BooleanField(default=True, help_text="Define si este tab está activo y visible.")
    clients_headers_home_created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.clients_headers_home_title_1
    

class Property(models.Model):
    DAYS_OF_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    """ STATUS_CHOICES = [
        ('sell', 'For Sell'),
        ('rent', 'For Rent'),
    ]

    TYPE_CHOICES = [
        ('apartment', 'Appartment'),
        ('house', 'House'),
        # Agrega más tipos si es necesario
    ] """
    
    property_code = models.CharField(max_length=500, blank=True, null=True)
    property_title = models.CharField(max_length=255, blank=True, null=True)
    property_description = models.TextField(blank=True, null=True)
    property_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    property_image = models.ImageField(upload_to='properties/', max_length=5500, blank=True, null=True)
    # status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    # type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    property_status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    property_type = models.ForeignKey(PropertyType, on_delete=models.SET_NULL, null=True)
    property_location = models.CharField(max_length=2000, blank=True, null=True)
    property_purpose = models.ForeignKey(Purpose, on_delete=models.SET_NULL, null=True, blank=True)
    property_country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    property_area = models.PositiveIntegerField(help_text="Area in Sqft", blank=True, null=True)
    property_bedrooms = models.PositiveIntegerField(blank=True, null=True)
    property_bathrooms = models.PositiveIntegerField(blank=True, null=True)
    property_created_at = models.DateTimeField(auto_now_add=True, help_text="Fecha cuando se creo el tab.") 
    property_updated_at = models.DateTimeField(auto_now=True, help_text="Última vez que se actualizó el tab.")
    property_is_active = models.BooleanField(default=True, help_text="Define si este tab está activo y visible.")
    property_created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    property_url_link = models.URLField(max_length=4500, blank=True, null=True)
    property_date_start = models.DateField()
    property_time_start = models.TimeField()
    property_day_start = models.CharField(max_length=9, choices=DAYS_OF_WEEK)
    property_file = models.FileField(upload_to='property_files/', max_length=5500, blank=True, null=True)  # Para subir archivos
    
    @property
    def featured_image(self):
        # devuelve la imagen marcada como destacada, o la primera imagen si no hay destacada, o None
        featured = self.images.filter(propertyImage_is_featured=True).first()
        if featured:
            return featured
        return self.images.first()  # fallback a la primera imagen si no hay destacada
    
    def __str__(self):
        return f"{self.property_title} - {self.property_code}"

class PropertyImage(models.Model):
    propertyImage_property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    propertyImage_image = models.ImageField(upload_to='property_gallery/', max_length=5500, blank=True, null=True)
    propertyImage_caption = models.CharField(max_length=255, blank=True, null=True)
    propertyImage_is_featured = models.BooleanField(default=False)  # Si quieres marcar una imagen como destacada
    propertyImage_uploaded_at = models.DateTimeField(auto_now_add=True)
    propertyImage_created_at = models.DateTimeField(auto_now_add=True, help_text="Fecha cuando se creo el tab.") 
    propertyImage_updated_at = models.DateTimeField(auto_now=True, help_text="Última vez que se actualizó el tab.")
    propertyImage_is_active = models.BooleanField(default=True, help_text="Define si este tab está activo y visible.")
    propertyImage_created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"Image for {self.propertyImage_property.property_title}"
    

class PropertyReservation(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='reservas')
    start_date = models.DateField()
    end_date = models.DateField()
    
    def get_daterange(self):
        current = self.start_date
        while current <= self.end_date:
            yield current
            current += timedelta(days=1)
            
    def __str__(self):
        return f"{self.property.property_code} - {self.property.property_title} - {self.property.property_price} reservada del {self.start_date} al {self.end_date}"
    

class Newsletter(models.Model):
    email = models.EmailField(unique=True)  # Almacenará el correo electrónico
    date_subscribed = models.DateTimeField(auto_now_add=True)  # Fecha de suscripción
    is_active = models.BooleanField(default=True)  # Permitir activar o desactivar la suscripción
    
    def __str__(self):
        return self.email

class Tab(models.Model):
    DAYS_OF_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    tab_slug = models.SlugField(unique=True, help_text="Identificador único de la pestaña (ej: home, about, event)")
    tab_nombre = models.CharField(max_length=100)
    tab_description = models.TextField()
    tab_url = models.URLField(blank=True, null=True, verbose_name="tab URL")
    tab_img_url = models.ImageField(upload_to='tab_img_url_images/', max_length=5500, blank=True, null=True)
    tab_file = models.FileField(upload_to='tab_file_files/', max_length=5500, blank=True, null=True)  # Para subir
    tab_date_page = models.DateField(help_text="Fecha de tab", blank=True, null=True)
    tab_time_page = models.TimeField(help_text="Hora de tab", blank=True, null=True)
    tab_day_page = models.CharField(max_length=9, choices=DAYS_OF_WEEK)  # Día seleccionado del combo
    created_at = models.DateTimeField(auto_now_add=True, help_text="Fecha en la que se creó el tab.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Última vez que se actualizó el tab.")
    is_active = models.BooleanField(default=True, help_text="Define si este tab está activo y visible.")
    
    def __str__(self):
        return f'{self.tab_nombre} - {self.tab_description}'
    

class TabPage(models.Model):
    DAYS_OF_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    tab_page = models.ForeignKey(Tab, on_delete=models.CASCADE)
    tab_page_name = models.CharField(max_length=100, blank=True, null=True , verbose_name="tab page name")
    tab_page_url_name = models.CharField(max_length=100, blank=True, null=True , verbose_name="tab page URL name")
    tab_img_url = models.ImageField(upload_to='tab_page_img_url_images/', max_length=5500, blank=True, null=True)
    tab_file = models.FileField(upload_to='tab_page_file_files/', max_length=5500, blank=True, null=True)  # Para subir
    tab_date_page = models.DateField(help_text="Fecha de tab page", blank=True, null=True)
    tab_time_page = models.TimeField(help_text="Hora de tab page", blank=True, null=True)
    tab_day_page = models.CharField(max_length=9, choices=DAYS_OF_WEEK)  # Día seleccionado del combo
    created_at = models.DateTimeField(auto_now_add=True, help_text="Fecha en la que se creó el tab page.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Última vez que se actualizó el tab page.")
    is_active = models.BooleanField(default=True, help_text="Define si este tab page está activo y visible.")

    def __str__(self):
        return self.tab_page_name
    
    

class ContactMessage(models.Model):
    contact_message_name = models.CharField(max_length=500, blank=True, null=True)
    contact_message_email = models.EmailField(blank=True, null=True)
    contact_message_phone = models.CharField(max_length=500, blank=True, null=True)
    contact_message_subject = models.CharField(max_length=500, blank=True, null=True)
    contact_message_message = models.TextField( blank=True, null=True)
    contact_message_created_at = models.DateTimeField(auto_now_add=True)
    contact_message_updated_at = models.DateTimeField(auto_now=True, help_text="Última vez que se actualizó el tab page.")
    contact_message_is_active = models.BooleanField(default=True, help_text="Define si este tab page está activo y visible.")
    
    def __str__(self):
        return f'Message from {self.contact_message_name} - {self.contact_message_subject}'

class ContactInfo(models.Model):
    class Meta:
        ordering = ['-contact_info_created_at']
    
    DAYS_OF_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    contact_info_name = models.CharField(max_length=500, verbose_name="Nombre Contacto",blank=True, null=True)
    contact_info_phone_number = models.CharField(max_length=200, verbose_name="Phone Number", blank=True, null=True)
    contact_info_email = models.EmailField(verbose_name="Email", blank=True, null=True)
    contact_info_facebook_url = models.URLField(blank=True, null=True, verbose_name="Facebook URL")
    contact_info_twitter_url = models.URLField(blank=True, null=True, verbose_name="Twitter URL")
    contact_info_linkedin_url = models.URLField(blank=True, null=True, verbose_name="LinkedIn URL")
    contact_info_instagram_url = models.URLField(blank=True, null=True, verbose_name="Instagram URL")
    
    contact_info_date = models.DateField(help_text="Fecha de Contact Info", blank=True, null=True)
    contact_info_time = models.TimeField(help_text="Hora de Contact Info", blank=True, null=True)
    contact_info_day = models.CharField(max_length=9, choices=DAYS_OF_WEEK, blank=True, null=True)  # Día seleccionado del combo
    contact_info_img_url = models.ImageField(upload_to='contact_info_images/', max_length=5500, blank=True, null=True)
    contact_info_file = models.FileField(upload_to='contact_info_files/', max_length=5500, blank=True, null=True)  # Para subir archivos
    contact_info_created_at = models.DateTimeField(auto_now_add=True, help_text="Fecha en la que se creó el ContactInfo.")
    contact_info_updated_at = models.DateTimeField(auto_now=True, help_text="Última vez que se actualizó el ContactInfo.")
    contact_info_is_active = models.BooleanField(default=True, help_text="Define si este ContactInfo está activo y visible.")
    contact_info_map_embed_url = models.TextField(
    blank=True, null=True,
    verbose_name="URL de Google Maps embebido",
    help_text="Pega aquí la URL del iframe de Google Maps (la parte del 'src')."
)
    
    
    def __str__(self):
        return f"Contact Info ({self.contact_info_name or 'N/A'}, {self.contact_info_phone_number or 'N/A'}, {self.contact_info_email or 'N/A'})"


class HeaderSlide(models.Model):
    header_slide_title = models.CharField(max_length=900, blank=True, null=True)
    header_slide_perfect_home = models.CharField(max_length=900, blank=True, null=True)
    header_slide_to_live_with = models.CharField(max_length=900, blank=True, null=True)
    header_slide_description = models.TextField(blank=True, null=True)
    header_slide_button_text = models.CharField(max_length=500, blank=True, null=True)
    header_slide_button_link = models.URLField(blank=True, null=True)
    header_slide_image = models.ImageField(upload_to='header_slides/', blank=True, null=True)
    header_slide_is_active = models.BooleanField(default=True)
    header_slide_created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    header_slide_created_at = models.DateTimeField(auto_now_add=True)
    header_slide_updated_at = models.DateTimeField(auto_now=True, help_text="Última vez que se actualizó el HeaderSlide.")
    def __str__(self):
        return f"{self.header_slide_title} - {self.header_slide_perfect_home} - {self.header_slide_to_live_with}"
    

class HeaderSlideImage(models.Model):
    header_slide_image_header_slide = models.ForeignKey(HeaderSlide, on_delete=models.CASCADE, related_name='images')
    header_slide_image_image = models.ImageField(upload_to='header_slides_images/', blank=True, null=True)
    header_slide_image_is_active = models.BooleanField(default=True)
    header_slide_image_created_at = models.DateTimeField(auto_now_add=True)
    header_slide_image_created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    header_slide_image_updated_at = models.DateTimeField(auto_now=True, help_text="Última vez que se actualizó el HeaderSlide.")
    
    def __str__(self):
        return f"Image for: {self.header_slide_image_header_slide.header_slide_title}"




class Testimonial(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    profession = models.CharField(max_length=500, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='testimonials/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.name} - {self.profession}"
