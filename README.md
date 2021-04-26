# AENA

Para obtener todos los datos básicos de la sección estadísticas de AENA habría que ejecutar los siguientes dos scripts:

1) AENA_IATA_aeropuertos.ipynb : Este script contiene todos los aeropuertos y sus diferentes denominaciones a lo largo del tiempo.
2) AENA_scraping.ipynb : Este script obtiene tres dataframes (pasajeros, operaciones y mercancias) desde el 2004 hasta diciembre de 2020.

Posteriormente habría que ejecutar mensualmente los siguientes scripts:
1) AENA_update_IATA_aeropuertos.ipynb : Actualiza el listado de aeropuertos y sus denominaciones.
2) AENA_update_dataframes.ipynb : Actualiza los dataframes.

La información se almacena en un pickle de Dataframe de Pandas.

