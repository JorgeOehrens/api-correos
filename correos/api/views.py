from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CorreoSerializacion
from base.models import Correo
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives

@api_view(['GET'])
def getData(request):
    correo = {'empresa': 'amagi', 'correo_admin': 'noreply@amagibitcoin.cl', 'correo_cliente': 'jorge.oehrens@gmail.com' , 'mensaje' : 'link recuperar contraseña' }

    correos=Correo.objects.all()
    serializer = CorreoSerializacion(correos, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def crearCorreo(request):
    serializer = CorreoSerializacion(data=request.data)
    if serializer.is_valid():
        serializer.save()
        empresa=serializer["empresa"].value
        correo_admin=serializer["correo_admin"].value
        correo_cliente=serializer["correo_cliente"].value
        mensaje=serializer["mensaje"].value
        asunto=serializer["asunto"].value



        asunto_conf = asunto
        correo_html = render_to_string('Correo/recuperacion.html', {
                    'empresa': empresa,
                    'correo_cliente': correo_cliente,
                    'mensaje': mensaje,

                })
        

        contenido= strip_tags(correo_html)

        correo_enviar = EmailMultiAlternatives(
            asunto,
            contenido,
        to=[correo_cliente])

        correo_enviar.fail_silenty=False
        correo_enviar.attach_alternative(correo_html,'text/html')
        correo_enviar.send()






    return Response(serializer.data)
