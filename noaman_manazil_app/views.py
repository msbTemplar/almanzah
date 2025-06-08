from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .forms import NewsletterForm, CustomUserCreationForm, TabForm, PropertyForm, PropertyImageForm, ContactMessageForm,TestimonialForm
from django.core.mail import send_mail
from datetime import datetime
from django.contrib.auth import logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from django.contrib.auth.views import LoginView
from django.views.decorators.cache import cache_page
import locale
from .models import PropertyImage, Property,Purpose, Country,ContactInfo,PropertyReservation,HeaderSlide, Testimonial,ClientsHeadersHome
from django.template.loader import render_to_string
from datetime import timedelta
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.



def create_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        images = request.FILES.getlist('property_images')  # Campo múltiple

        if form.is_valid():
            property = form.save(commit=False)
            property.property_created_by = request.user
            property.save()

            for img in images:
                PropertyImage.objects.create(
                    propertyImage_property=property,
                    propertyImage_image=img,
                    propertyImage_created_by=request.user
                )

            return redirect('property_detail', pk=property.pk)

    else:
        form = PropertyForm()
    
    return render(request, 'noaman_manazil_app/create_property.html', {'form': form})


def custom_logout_view(request):
    logout(request)
    return redirect('home') 

class CustomLoginView(LoginView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Actualizar el contexto
        context.update({
            
        })

        return context

def register(request):
    

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "¡Tu cuenta ha sido creada con éxito!")

            # Enviar correo electrónico de bienvenida
            email_content = f"""
            ¡Bienvenido {user.username}!

            Tu cuenta ha sido creada con éxito en nuestro sitio web.

            Gracias por unirte a nuestra comunidad.
            """

            send_mail(
                'Bienvenido a nuestro sitio web',  # Asunto
                email_content,  # Cuerpo del correo
                'noreply@tusitio.com',  # Correo electrónico del remitente
                [user.email,'msb.caixa@gmail.com','msb.tesla@gmail.com', 'msb.coin@gmail.com', 'msb.duck@gmail.com', 'msebti2@gmail.com', 'papioles@gmail.com', 'msb.motive@gmail.com', 'msb.acer@gmail.com'],  # Correo electrónico del usuario registrado
            )

            return redirect('login')  # Redirige a la página de login después de registrarse
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {
        'form': form,
        
    })

def privacy_policy(request):
    return render(request, 'noaman_manazil_app/privacy_policy.html')

def all_the_options_view(request):
    #la_lista_des_services_images = ServiceImage.objects.all()  # Recupera todos los servicios
    return render(request, 'noaman_manazil_app/all_the_options_view.html', {})

def set_cookie_consent(request):
    response = JsonResponse({'status': 'ok'})
    response.set_cookie('cookie_consent', 'true', max_age=365*24*60*60)  # 1 año
    return response



def home(request):
    fecha_actual = datetime.now().strftime('%A, %B %d, %Y')
    
    #slides = HeaderSlide.objects.filter(header_slide_is_active=True).order_by('-header_slide_created_at')
    header_slide = HeaderSlide.objects.filter(header_slide_is_active=True).order_by('-header_slide_created_at').first()
    
    clients_headers_home = ClientsHeadersHome.objects.filter(clients_headers_home_is_active=True).order_by('-clients_headers_home_created_at').first()
    
    contact_info = ContactInfo.objects.filter(contact_info_is_active=True).order_by('-contact_info_created_at').first()
    
    contact = ContactInfo.objects.filter(contact_info_is_active=True).order_by('-contact_info_created_at').first()
    message = "Hola, quiero hacer una consulta"
    
    # Preseleccionamos 6 propiedades activas
    properties = Property.objects.filter(property_is_active=True).order_by('-property_created_at')[:6]
    
    try:
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
        fecha_actual_es = datetime.now().strftime('%A, %d de %B de %Y') 
    except locale.Error:
        fecha_actual_es = datetime.now().strftime('%A, %d of %B of %Y')
    
    fecha_hora_actual = datetime.now().strftime('%A, %B %d, %Y %I:%M:%S %p')
    
    purposes = Purpose.objects.filter(purpose_is_active=True)
    countries = Country.objects.filter(country_is_active=True)
    
    combos = []
    for purpose in purposes:
        for country in countries:
            total_props = Property.objects.filter(
                property_purpose=purpose,
                property_country=country,
                property_is_active=True
            ).count()
            
            combos.append({
                'purpose': purpose,
                'country': country,
                'link': f"/{purpose.purpose_name.lower().replace(' ', '-')}/{country.country_name.lower().replace(' ', '-')}/",
                'icon': purpose.purpose_icon or 'default-icon.png',
                'count': total_props
            })
    
    featured_properties = Property.objects.filter(
        images__propertyImage_is_featured=True,
        property_is_active=True
    ).distinct()
    
    sell_properties = Property.objects.filter(
        property_purpose__purpose_name__iexact='sell',
        property_is_active=True
    )
    
    rent_properties = Property.objects.filter(
        property_purpose__purpose_name__iexact='rent',
        property_is_active=True
    )
    
    # Filtro según parámetro GET 'status'
    status = request.GET.get('status')
    if status == 'sell':
        properties = Property.objects.filter(property_status__name='sell', property_is_active=True)
    elif status == 'rent':
        properties = Property.objects.filter(property_status__name='rent', property_is_active=True)
    else:
        # Si quieres mostrar las propiedades con imagen destacada:
        properties = Property.objects.filter(images__propertyImage_is_featured=True, property_is_active=True).distinct()
    
    # Filtro por propósito y país
    purpose_id = request.GET.get('purpose')
    country_id = request.GET.get('country')

    if purpose_id:
        properties = properties.filter(property_purpose_id=purpose_id)
    if country_id:
        properties = properties.filter(property_country_id=country_id)
    
    
    # *** NUEVO: manejo del formulario ***
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # redirigir para limpiar el POST
    else:
        form = TestimonialForm()

    testimonials = Testimonial.objects.all().order_by('-created_at')
    
    
    context = {
        'fecha_actual': fecha_actual,
        'fecha_actual_es': fecha_actual_es,
        'fecha_hora_actual': fecha_hora_actual,
        'purposes': purposes,
        'countries': countries,
        'combos': combos,
        'contact': contact,
        'message': message,
        'properties': properties,
        'featured_properties': featured_properties,
        'sell_properties': sell_properties,
        'rent_properties': rent_properties,
        'header_slide': header_slide,
        'contact_info': contact_info,
        'clients_headers_home': clients_headers_home,
        
        # NUEVO para testimonios
        'form': form,
        'testimonials': testimonials,
    }
    
    return render(request, 'noaman_manazil_app/home.html', context)

def buscar_propiedades(request, purpose_id, country_id):
    purpose = get_object_or_404(Purpose, pk=purpose_id)
    country = get_object_or_404(Country, pk=country_id)
    
    contact_info = ContactInfo.objects.filter(contact_info_is_active=True).order_by('-contact_info_created_at').first()

    propiedades = Property.objects.filter(
        property_purpose=purpose,
        property_country=country,
        property_is_active=True
    )
    
    # *** NUEVO: manejo del formulario ***
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # redirigir para limpiar el POST
    else:
        form = TestimonialForm()

    testimonials = Testimonial.objects.all().order_by('-created_at')

    context = {
        'purpose_selected': purpose,
        'country_selected': country,
        'properties': propiedades,  # Este nombre debe coincidir con tu template
        'purposes': Purpose.objects.filter(purpose_is_active=True),
        'countries': Country.objects.filter(country_is_active=True),
        'contact_info': contact_info,
        
        
        # NUEVO para testimonios
        'form': form,
        'testimonials': testimonials,
    }
    
    return render(request, 'noaman_manazil_app/home.html', context)


def buscar_propiedades1(request, purpose_id, country_id):
    purpose = Purpose.objects.get(pk=purpose_id)
    country = Country.objects.get(pk=country_id)

    # Aquí puedes filtrar las propiedades reales si las tienes
    propiedades = Property.objects.filter(
        purpose_id=purpose_id,
        country_id=country_id,
        is_active=True
    )

    context = {
        'purpose': purpose,
        'country': country,
        'propiedades': propiedades,
    }
    return render(request, 'noaman_manazil_app/property_list.html', context)


def contact(request):
    
    contact_info = ContactInfo.objects.filter(contact_info_is_active=True).first()  # O el que necesites
    
    fecha_actual = datetime.now().strftime('%A, %B %d, %Y')  # Ejemplo: Monday, January 01, 2045
    
    try:
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # Configura a español
        fecha_actual_es = datetime.now().strftime('%A, %d de %B de %Y') 
    except locale.Error:
        # Si no se puede establecer el locale, usa un formato alternativo
        fecha_actual_es = datetime.now().strftime('%A, %d of %B of %Y')
    
    fecha_hora_actual = datetime.now().strftime('%A, %B %d, %Y %I:%M:%S %p') 
    
    # Consulta de datos dinámicos
    purposes = Purpose.objects.filter(purpose_is_active=True)
    countries = Country.objects.filter(country_is_active=True)
    
    
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            # Guardar el registro en la base de datos
            form.save()
            
            # Obtener los datos del formulario
            contact_message_name = form.cleaned_data['contact_message_name']
            contact_message_email = form.cleaned_data['contact_message_email']
            contact_message_phone = form.cleaned_data['contact_message_phone']
            contact_message_subject = form.cleaned_data['contact_message_subject']
            contact_message_message = form.cleaned_data['contact_message_message']
            
            """
            # Enviar el correo electrónico
            send_mail(
                'Message from ' + message_name,  # Asunto
                message_message,  # Mensaje
                message_email,  # Correo electrónico del remitente
                ['msb.tesla@gmail.com', 'msb.coin@gmail.com', 'msb.duck@gmail.com', 'msebti2@gmail.com'],  # Correos de destino
            )
            """
            email_content = f"""
            You have received a new contact message from {contact_message_name}:

            Name: {contact_message_name}
            Email: {contact_message_email}
            Phone: {contact_message_phone}
            Subject: {contact_message_subject}
            Message: {contact_message_message}
            """
            
            # Enviar el correo electrónico
            send_mail(
                f'Message from {contact_message_name}',  # Asunto
                email_content,  # Cuerpo del correo con todos los detalles
                contact_message_email,  # Correo electrónico del remitente
                [contact_message_email,'msb.caixa@gmail.com','msb.tesla@gmail.com', 'msb.coin@gmail.com', 'msb.duck@gmail.com', 'msebti2@gmail.com', 'papioles@gmail.com', 'msb.motive@gmail.com', 'msb.acer@gmail.com'],  # Correos de destino
            )
            
            return render(request, 'noaman_manazil_app/contact.html', {'contact_message_name': contact_message_name,'contact_info':contact_info,'fecha_actual': fecha_actual,
        'fecha_actual_es': fecha_actual_es,
        'fecha_hora_actual': fecha_hora_actual,
        'purposes': purposes,
        'countries': countries,})
    else:
        form = ContactMessageForm()
    
    return render(request, 'noaman_manazil_app/contact.html', {'form': form,'contact_info':contact_info,'fecha_actual': fecha_actual,
        'fecha_actual_es': fecha_actual_es,
        'fecha_hora_actual': fecha_hora_actual,
        'purposes': purposes,
        'countries': countries,})


def generar_rango_fechas(start, end):
    dias = []
    while start <= end:
        dias.append(start)
        start += timedelta(days=1)
    return dias


def property_detail(request, pk):
    property_obj = get_object_or_404(Property, pk=pk)
    
    purposes = Purpose.objects.filter(purpose_is_active=True)
    countries = Country.objects.filter(country_is_active=True)

    # Suponiendo que tienes una relación con imágenes (ej: related_name='images')
    images = property_obj.images.all()  # Ajusta según tu modelo
    
    # Ejemplo: fechas ocupadas ficticias, reemplázalo con tus datos reales desde Booking, Reservas, etc.
    reservas = property_obj.reservas.all()  # Asumiendo que tienes esta relación
    fechas_ocupadas = []
    for r in reservas:
        fechas_ocupadas += [d.strftime("%Y-%m-%d") for d in r.get_daterange()]  # get_daterange devuelve lista de fechas
    

    context = {
        'property': property_obj,
        'images': images,
        'purposes': purposes,
        'countries': countries,
        'fechas_ocupadas': json.dumps(fechas_ocupadas, cls=DjangoJSONEncoder),  # Paso importante
    }
    return render(request, 'noaman_manazil_app/property_detail.html', context)



def load_properties_ajax(request):
    tab = request.GET.get('tab')

    if tab == 'featured':
        properties = Property.objects.filter(images__propertyImage_is_featured=True, property_is_active=True).distinct()
    elif tab == 'sell':
        properties = Property.objects.filter(property_purpose__purpose_name__iexact='sell', property_is_active=True)
    elif tab == 'rent':
        properties = Property.objects.filter(property_purpose__purpose_name__iexact='rent', property_is_active=True)
    else:
        properties = Property.objects.none()

    # 💡 Agrega la imagen destacada a cada propiedad
    for prop in properties:
        featured_image = prop.images.filter(propertyImage_is_featured=True).first()
        prop.featured_image = featured_image

    html = render_to_string('partials/property_list.html', {'properties': properties}, request=request)
    return JsonResponse({'html': html})


def reservar_propiedad(request, property_id):
    
    if request.method == "POST":
        propiedad = get_object_or_404(Property, id=property_id)
        # Condición para fechas
        if propiedad.property_status.name.lower() == 'rent':
            fecha_desde = request.POST.get("fecha_desde")
            fecha_hasta = request.POST.get("fecha_hasta")
        else:
            # Poner fecha actual en formato adecuado (por ejemplo, 'YYYY-MM-DD')
            fecha_desde = datetime.now().strftime('%Y-%m-%d')
            fecha_hasta = datetime.now().strftime('%Y-%m-%d')
        
        #fecha_desde = request.POST.get("fecha_desde")
        #fecha_hasta = request.POST.get("fecha_hasta")
        name_hasta_desde = request.POST.get("name_hasta_desde")
        email_hasta_desde = request.POST.get("email_hasta_desde")

        # Validar que se hayan enviado fechas
        if not fecha_desde or not fecha_hasta:
            messages.error(request, "Por favor selecciona ambas fechas para reservar.")
            return redirect(request.META.get('HTTP_REFERER', '/'))

        # Aquí podrías validar que fechas estén disponibles, etc.

        # Construir mensaje email
        asunto = f"Reserva solicitada para la propiedad {propiedad.property_title}"
        mensaje = f"""
        Se ha recibido una solicitud de reserva para la propiedad:

        Título: {propiedad.property_title}
        Ubicación: {propiedad.property_location}, {propiedad.property_country.country_name}
        Fecha desde: {fecha_desde}
        Fecha hasta: {fecha_hasta}
        El nombre del solicitante: {name_hasta_desde}
        El email del solicitante: {email_hasta_desde}
        Descripcion: {propiedad.property_description}
        Precio: {propiedad.property_price}
        Estado: {propiedad.property_status}
        Tipo: {propiedad.property_type}
        
        Por favor, contacta con el usuario para confirmar la reserva.
        """
        

        # Enviar email
        # Enviar el correo electrónico
        send_mail(
                f'Message from {asunto}',  # Asunto
                mensaje,  # Cuerpo del correo con todos los detalles
                'msb.duck@gmail.com',  # Correo electrónico del remitente
                ['msb.caixa@gmail.com','msb.tesla@gmail.com', 'msb.coin@gmail.com', 'msb.duck@gmail.com', 'msebti2@gmail.com', 'papioles@gmail.com', 'msb.motive@gmail.com', 'msb.acer@gmail.com'],  # Correos de destino
            )
        
        messages.success(request, "Reserva solicitada correctamente. Te contactaremos pronto.")
        return redirect('home')  # o a donde quieras redirigir
    
    # Si no es POST, simplemente redirige o lanza error
    return redirect('home')