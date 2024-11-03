import logging

# Configuración básica de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

# Crear un logger específico para la aplicación
logger = logging.getLogger("starwars_app")
