from django import forms
from .models import Tab, TabPage, Newsletter,Property, Status, PropertyType, PropertyImage, ContactMessage, ContactInfo, Testimonial
import json
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Formulario simple para múltiples imágenes
class PropertyImageForm(forms.ModelForm):
    class Meta:
        model = PropertyImage
        fields = ['propertyImage_image', 'propertyImage_caption', 'propertyImage_is_featured']
        widgets = {
            'propertyImage_image': forms.ClearableFileInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
            }),
            'propertyImage_caption': forms.TextInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Título o descripción de la imagen',
            }),
            'propertyImage_is_featured': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            'property_title',
            'property_description',
            'property_price',
            'property_image',
            'property_status',
            'property_type',
            'property_location',
            'property_country',     # Cambiado: ahora es ForeignKey
            'property_purpose',     # Nuevo campo
            'property_area',
            'property_bedrooms',
            'property_bathrooms',
            'property_url_link',
            'property_date_start',
            'property_time_start',
            'property_day_start',
            'property_file',
            'property_is_active',
        ]
        widgets = {
            'property_title': forms.TextInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Título de la propiedad',
                'style': 'height: 55px;',
            }),
            'property_description': forms.Textarea(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Descripción de la propiedad',
                'rows': 4,
            }),
            'property_price': forms.NumberInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Precio de la propiedad',
                'style': 'height: 55px;',
            }),
            'property_image': forms.ClearableFileInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'style': 'height: 55px;',
            }),
            'property_status': forms.Select(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'style': 'height: 55px;',
            }),
            'property_type': forms.Select(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'style': 'height: 55px;',
            }),
            'property_location': forms.TextInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Ubicación de la propiedad',
                'style': 'height: 55px;',
            }),
            'property_country': forms.Select(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'style': 'height: 55px;',
            }),
            'property_purpose': forms.Select(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'style': 'height: 55px;',
            }),
            'property_area': forms.NumberInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Área en pies cuadrados',
                'style': 'height: 55px;',
            }),
            'property_bedrooms': forms.NumberInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Número de dormitorios',
                'style': 'height: 55px;',
            }),
            'property_bathrooms': forms.NumberInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Número de baños',
                'style': 'height: 55px;',
            }),
            'property_url_link': forms.URLInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'URL externa de la propiedad',
                'style': 'height: 55px;',
            }),
            'property_date_start': forms.DateInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'type': 'date',
                'placeholder': 'Fecha de publicación',
            }),
            'property_time_start': forms.TimeInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'type': 'time',
                'placeholder': 'Hora de publicación',
            }),
            'property_day_start': forms.Select(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'style': 'height: 55px;',
            }),
            'property_file': forms.ClearableFileInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'style': 'height: 55px;',
            }),
            'property_is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'style': 'margin-top: 10px;',
            }),
        }


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name', 'label', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Nombre interno del estado',
                'style': 'height: 55px;',
            }),
            'label': forms.TextInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Etiqueta visible del estado',
                'style': 'height: 55px;',
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'style': 'margin-top: 10px;',
            }),
        }


class PropertyTypeForm(forms.ModelForm):
    class Meta:
        model = PropertyType
        fields = ['name', 'label', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Nombre interno del tipo',
                'style': 'height: 55px;',
            }),
            'label': forms.TextInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Etiqueta visible del tipo',
                'style': 'height: 55px;',
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'style': 'margin-top: 10px;',
            }),
        }

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True, 
        help_text="Requerido. Introduce una dirección de correo válida.",
        widget=forms.EmailInput(attrs={
            'class': 'form-control border-1 bg-light px-4',
            'placeholder': 'Correo Electrónico',
            'style': 'height: 55px;'
        })
    )
    username = forms.CharField(
        required=True,
        help_text="El nombre de usuario debe tener entre 4 y 150 caracteres. No use caracteres especiales.",
        widget=forms.TextInput(attrs={
            'class': 'form-control border-1 bg-light px-4',
            'placeholder': 'Nombre de Usuario',
            'style': 'height: 55px;'
        })
    )
    password1 = forms.CharField(
        required=True,
        help_text="La contraseña debe tener al menos 8 caracteres y contener al menos un número, una mayúscula y un carácter especial.",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control border-1 bg-light px-4',
            'placeholder': 'Contraseña',
            'style': 'height: 55px;'
        })
    )
    password2 = forms.CharField(
        required=True,
        help_text="Introduzca nuevamente la contraseña para confirmarla.",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control border-1 bg-light px-4',
            'placeholder': 'Confirmar Contraseña',
            'style': 'height: 55px;'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe un usuario con este correo electrónico.")
        return email


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']  # Solo necesitamos el correo electrónico
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control border-white p-3',
                'placeholder': 'Your Email',
                'style': 'height: 55px;'
            }),
        }
        labels = {
            'email': ''
        }

class TabPageForm(forms.ModelForm):
    class Meta:
        model = TabPage
        fields = [
            'tab_page_name',
            'tab_page_url_name',
            'tab_img_url',
            'tab_file',
            'tab_date_page',
            'tab_time_page',
            'tab_day_page',
            'is_active',
        ]
        widgets = {
            'tab_page_name': forms.TextInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Nombre de la Página del Tab',
                'style': 'height: 55px;',
            }),
            'tab_page_url_name': forms.TextInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'URL de la Página del Tab',
                'style': 'height: 55px;',
            }),
            'tab_img_url': forms.ClearableFileInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'style': 'height: 55px;',
            }),
            'tab_file': forms.ClearableFileInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'style': 'height: 55px;',
            }),
            'tab_date_page': forms.DateInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Fecha de la Página del Tab',
                'type': 'date',
            }),
            'tab_time_page': forms.TimeInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Hora de la Página del Tab',
                'type': 'time',
            }),
            'tab_day_page': forms.Select(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'style': 'height: 55px;',
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'style': 'margin-top: 10px;',
            }),
        }
        
class TabForm(forms.ModelForm):
    class Meta:
        model = Tab
        fields = [
            'tab_nombre',
            'tab_slug',
            'tab_description',
            'tab_url',
            'tab_img_url',
            'tab_file',
            'tab_date_page',
            'tab_time_page',
            'tab_day_page',
            'is_active'
        ]
        widgets = {
            'tab_nombre': forms.TextInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Ingrese el nombre',
                'style': 'height: 55px;',
            }),
            'tab_slug': forms.TextInput(attrs={  # Agregar input para el slug
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Slug automático basado en el nombre',
                'style': 'height: 55px;',
            }),
            'tab_description': forms.Textarea(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Ingrese la descripción',
                'style': 'height: 150px;',
            }),
            'tab_url': forms.URLInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Ingrese la URL',
                'style': 'height: 55px;',
            }),
            'tab_img_url': forms.ClearableFileInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'style': 'height: 55px;',
            }),
            'tab_file': forms.ClearableFileInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'style': 'height: 55px;',
            }),
            'tab_date_page': forms.DateInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Fecha de BestVideos',
                'type': 'date',
            }),
            'tab_time_page': forms.TimeInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Hora de BestVideos',
                'type': 'time',
            }),
            'tab_day_page': forms.Select(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'style': 'height: 55px;',
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'style': 'margin-top: 10px;',
            }),
        }
    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # Si el slug está vacío, lo genera automáticamente
        if not instance.tab_slug:
            instance.tab_slug = slugify(instance.tab_nombre)
        
        if commit:
            instance.save()
        return instance
    
    

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['contact_message_name', 'contact_message_email', 'contact_message_phone', 'contact_message_subject', 'contact_message_message']
        widgets = {
            'contact_message_name': forms.TextInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Your Name',
                'style': 'height: 55px;',
            }),
            'contact_message_email': forms.EmailInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Your Email',
                'style': 'height: 55px;',
            }),
            'contact_message_phone': forms.TextInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Your Phone',
                'style': 'height: 55px;',
            }),
            'contact_message_subject': forms.TextInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Subject',
                'style': 'height: 55px;',
            }),
            'contact_message_message': forms.Textarea(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Your Message',
                'style': 'height: 200px;',
            }),
            'contact_message_is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'style': 'margin-top: 10px;',
            }),
        }

class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = [
            'contact_info_name',
            'contact_info_phone_number',
            'contact_info_email',
            'contact_info_facebook_url',
            'contact_info_twitter_url',
            'contact_info_linkedin_url',
            'contact_info_instagram_url',
            'contact_info_date',
            'contact_info_time',
            'contact_info_day',
            'contact_info_img_url',
            'contact_info_file',
            'contact_info_is_active',
        ]
        widgets = {
            'contact_info_name': forms.TextInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Nombre Contacto',
                'style': 'height: 55px;',
            }),
            'contact_info_phone_number': forms.TextInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Phone Number',
                'style': 'height: 55px;',
            }),
            'contact_info_email': forms.EmailInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Email',
                'style': 'height: 55px;',
            }),
            'contact_info_facebook_url': forms.URLInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Facebook URL',
                'style': 'height: 55px;',
            }),
            'contact_info_twitter_url': forms.URLInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Twitter URL',
                'style': 'height: 55px;',
            }),
            'contact_info_linkedin_url': forms.URLInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'LinkedIn URL',
                'style': 'height: 55px;',
            }),
            'contact_info_instagram_url': forms.URLInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Instagram URL',
                'style': 'height: 55px;',
            }),
            'contact_info_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control border-1 bg-light px-4',
                'style': 'height: 55px;',
            }),
            'contact_info_time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control border-1 bg-light px-4',
                'style': 'height: 55px;',
            }),
            'contact_info_day': forms.Select(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'style': 'height: 55px;',
            }),
            'contact_info_img_url': forms.ClearableFileInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'style': 'height: 55px;',
            }),
            'contact_info_file': forms.ClearableFileInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'style': 'height: 55px;',
            }),
            'contact_info_is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'style': 'margin-top: 12px;',
            }),
        }

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'profession', 'message', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Tu nombre',
                'style': 'height: 55px;',
            }),
            'profession': forms.TextInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Profesión',
                'style': 'height: 55px;',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Escribe tu testimonio',
                'rows': 4,
                'style': 'height: auto;',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'style': 'height: 55px;',
            }),
        }