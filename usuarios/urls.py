from django.urls import path
from . import views

#Rutas de la aplicación "Usuarios"
urlpatterns = [
    path('registroEstudiante/', views.mostrar_registro_estudiante, name='registroEstudiante'), #Vista RegistroEstudiante
    path('procesarRegistroEstudiante/', views.procesar_registro_estudiante, name='procesar_registro_estudiante'), #Ruta para el formulario
    path('login/',views.mostrar_login_usuario,name='loginUsuario'), # vista Login
    path('autenticarCredenciales/',views.autenticar_credenciales_usuario, name='autenticar_credenciales_usuario'), # Ruta para el formulario Login
    path('paginaPrincipalEstudiante/', views.mostrar_mainPage_estudiante, name='paginaPrincipal_estudiante'),
    path('login/recuperarContraseña/',views.mostrar_recuperar_contra, name='enviar_correo'), #Ruta para el formulario de recuperar contraseña
    path('cambiarContraseña/<str:correoUsuario>/<int:codigoCifrado>/', views.mostrar_ResetPasswordPage, name="cambiar_contrasena"),  # vista Reset Password
    path('cambiarContraseña/<str:correoUsuario2>/<int:codigoCifrado2>/procesarCambioContraseña/', views.procesar_cambio_contrasena, name="procesar_cambio_contrasena")
]