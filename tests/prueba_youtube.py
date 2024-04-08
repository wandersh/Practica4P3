from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

# Función para tomar capturas de pantalla
def take_screenshot(nombre):
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    driver.save_screenshot(f"screenshots/{nombre}.png")

# Ruta al controlador IEDriverServer
ruta_controlador = "C:\\Users\\Capellan Rent Car\\Downloads\\Practica4p3\\Drivers\\IEDriverServer64.exe"

# Agregar la ruta del controlador al PATH
os.environ["PATH"] += os.pathsep + os.path.dirname(ruta_controlador)

# Configuración del WebDriver para Internet Explorer
driver = webdriver.Ie()  # Aquí se crea una instancia del controlador sin especificar la ruta

# Acceder a la página web de YouTube
driver.get("https://www.youtube.com")


# Historia de Usuario 1: Búsqueda de Videos
def test_busqueda_videos():
    """
    Como usuario, quiero poder realizar búsquedas de videos utilizando palabras clave para encontrar contenido relevante.
    """
    # Realizar una búsqueda de video
    campo_busqueda = driver.find_element_by_name("search_query")
    campo_busqueda.send_keys("prueba de Selenium en YouTube")
    campo_busqueda.send_keys(Keys.RETURN)

    
    time.sleep(5)  

    # Captura de pantalla
    take_screenshot("busqueda_videos")

# Historia de Usuario 2: Filtrado de Resultados de Búsqueda
def test_filtrado_resultados():
    """
    Como usuario, quiero poder filtrar los resultados de búsqueda por diferentes criterios para encontrar videos específicos más fácilmente.
    """
    # Realizar una búsqueda utilizando una palabra clave
    campo_busqueda = driver.find_element_by_name("search_query")
    campo_busqueda.send_keys("prueba de Selenium en YouTube")
    campo_busqueda.send_keys(Keys.RETURN)
    time.sleep(5)  # Espera 5 segundos
    
    # Utilizar los filtros proporcionados
    filtro_fecha_carga = driver.find_element_by_xpath("//yt-formatted-string[contains(text(),'Fecha de carga')]")
    filtro_fecha_carga.click()
    
    # Verificar que los resultados se reorganicen según el filtro seleccionado
    time.sleep(5)  # Espera 5 segundos
    
    # Captura de pantalla
    take_screenshot("filtrado_resultados")

# Historia de Usuario 3: Subida de Videos
def test_subida_videos():
    """
    Como creador de contenido, quiero poder subir videos a la plataforma para compartir mi contenido con otros usuarios.
    """
    # Iniciar sesión en la cuenta de creador
    # (Aquí se asume que ya se ha iniciado sesión)
    
    # Acceder a la opción de "Subir video"
    boton_subir_video = driver.find_element_by_xpath("//button[@aria-label='Subir video']")
    boton_subir_video.click()
    time.sleep(2)  # Espera 2 segundos
    
    # Seleccionar el video desde mi dispositivo local
    # (En este punto, la implementación puede variar dependiendo de cómo se maneje la subida de videos)
    
    # Agregar detalles como título, descripción y etiquetas
    # (En este punto, se pueden encontrar elementos HTML para ingresar estos detalles y completar el formulario de carga)
    
    # Confirmar y enviar el video para su carga
    # (Aquí se puede hacer clic en el botón de "Confirmar" o "Enviar" para iniciar la carga del video)
    
    # Resultado esperado: El video se carga correctamente en la plataforma
    # (Se debe verificar visualmente que el video se haya cargado correctamente y esté disponible para que otros usuarios lo vean)
    
    # Captura de pantalla
    take_screenshot("subida_videos")

# Historia de Usuario 4: Suscripción a Canales
def test_suscripcion_canales():
    """
    Como usuario registrado, quiero poder suscribirme a canales de creadores para recibir notificaciones sobre nuevos videos.
    """
    # Visitar el canal del creador
    # (Aquí se asume que ya estamos en la página del canal del creador)
    
    # Hacer clic en el botón de suscripción
    boton_suscripcion = driver.find_element_by_xpath("//paper-button[@aria-label='Suscribirse']")
    boton_suscripcion.click()
    time.sleep(2)  # Espera 2 segundos
    
    # Verificar que el botón cambie a "Suscrito"
    boton_suscrito = driver.find_element_by_xpath("//paper-button[@aria-label='Suscrito']")
    assert boton_suscrito is not None, "El botón de suscripción no cambió a 'Suscrito'"
    
    # Verificar que se activan las notificaciones para nuevos videos
    # (En este punto, se debe verificar que las notificaciones están habilitadas en la configuración de la cuenta)
    
    # Resultado esperado: Me he suscrito correctamente al canal y recibiré notificaciones sobre nuevos videos publicados por el creador
    # (Se debe verificar visualmente que el botón cambió a "Suscrito" y que las notificaciones están habilitadas)
    
    # Captura de pantalla
    take_screenshot("suscripcion_canales")

# Historia de Usuario 5: Reproducción de Videos
def test_reproduccion_videos():
    """
    Como usuario, quiero poder reproducir videos en la plataforma para ver su contenido.
    """
    # Navegar a un video específico (se asume que ya estamos en la página de un video)
    
    # Hacer clic en el botón de reproducción
    boton_reproduccion = driver.find_element_by_xpath("//button[@aria-label='Reproducir']")
    boton_reproduccion.click()
    time.sleep(5)  # Espera 5 segundos para la reproducción
    
    # Verificar que el video se esté reproduciendo correctamente
    estado_video = driver.find_element_by_xpath("//div[@class='html5-video-container']")
    assert estado_video is not None, "El video no se está reproduciendo correctamente"
    
    # Resultado esperado: El video se reproduce sin problemas y puedo ver su contenido
    # (Se debe verificar visualmente que el video se esté reproduciendo correctamente)
    
    # Captura de pantalla
    take_screenshot("reproduccion_videos")

# Historia de Usuario 6: Comentarios en Videos
def test_comentarios_videos():
    """
    Como usuario, quiero poder dejar comentarios en los videos para interactuar con otros usuarios y el creador del contenido.
    """
    # Navegar a un video específico (se asume que ya estamos en la página de un video)
    
    # Desplazarse hacia abajo hasta la sección de comentarios
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)  # Espera 2 segundos
    
    # Escribir un comentario en el cuadro de texto
    cuadro_comentarios = driver.find_element_by_xpath("//textarea[@id='contenteditable-textarea']")
    cuadro_comentarios.send_keys("¡Excelente video! Me encantó.")
    time.sleep(2)  # Espera 2 segundos
    
    # Publicar el comentario
    boton_publicar = driver.find_element_by_xpath("//yt-icon[@class='style-scope ytd-button-renderer']")
    boton_publicar.click()
    time.sleep(5)  # Espera 5 segundos para que se publique el comentario
    
    # Verificar que el comentario aparezca en la lista de comentarios
    comentarios = driver.find_elements_by_xpath("//ytd-comment-renderer[@class='style-scope ytd-comment-thread-renderer']")
    assert len(comentarios) > 0, "No se encontraron comentarios publicados"
    
    # Resultado esperado: El comentario se publica correctamente y es visible para otros usuarios que ven el video
    # (Se debe verificar visualmente que el comentario se publique y sea visible para otros usuarios)
    
    # Captura de pantalla
    take_screenshot("comentarios_videos")

# Ejecutar todas las pruebas
test_busqueda_videos()
test_filtrado_resultados()
test_subida_videos()
test_suscripcion_canales()
test_reproduccion_videos()
test_comentarios_videos()

# Cerrar el navegador
driver.quit()
