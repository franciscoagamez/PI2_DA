
![Image alt text](Assets\CABA-Presentacion.jpg)
# Proyecto de Análisis de Siniestros Viales en CABA

## Descripción General del Proyecto

Este proyecto se centra en el análisis de siniestros viales ocurridos en la Ciudad Autónoma de Buenos Aires (CABA) durante los años 2016 a 2022. El objetivo principal es proporcionar una comprensión detallada de los patrones y tendencias de los accidentes de tránsito, así como evaluar la efectividad de ciertas iniciativas de seguridad vial mediante la implementación de KPIs específicos.

## Contenido del Repositorio

- [`datasets/`](PI2_DA\DataSets): Contiene el archivo CSV `siniestros_viales.csv` con los datos de los siniestros viales.
- [`notebooks/`](PI2_DA\Notebooks): Incluye los Jupyter Notebooks utilizados para realizar el análisis de datos, incluyendo el ETL y EDA, ademas de algunas funciones usadas durante el proceso de ETL.
- [`Dashboard/`](PI2_DA\Dashboard): Contiene el informe completo del análisis y visualizaciones generadas.
- [`functions.py/`](PI2_DA\functions.py): Scripts de Python utilizados para procesar y analizar los datos.
- [`README.md`](PI2_DA\README.md): Este archivo, que proporciona una visión general del proyecto y detalles del análisis realizado.

## Reporte de Análisis

### Resumen Ejecutivo

El análisis de los siniestros viales en CABA ha revelado los siguientes hallazgos clave:

1. **Tendencia Temporal:**
   - Aumento en el número de siniestros desde 2016 hasta 2019, seguido de una disminución en 2020 y 2021.
   - No se observó una estacionalidad clara en la distribución mensual, trimestral o semestral de los siniestros.

2. **Distribución Geográfica:**
   - Algunas comunas presentan un mayor número de siniestros en comparación con otras, destacando la necesidad de focalizar esfuerzos de seguridad vial en estas áreas.

3. **Tipo de Calle y Vehículo:**
   - La mayoría de los siniestros ocurren en avenidas.
   - Las motos son el tipo de vehículo más común entre las víctimas, mientras que los autos son los más frecuentemente involucrados como acusados.

4. **Gravedad y Edad de las Víctimas:**
   - La mayoría de los siniestros son clasificados como leves.
   - Las víctimas de siniestros fatales tienden a ser más jóvenes en promedio.

### KPIs Sugeridos

1. **Reducir en un 10% la tasa de homicidios en siniestros viales en los últimos seis meses en comparación con el semestre anterior.**

   - **Fórmula:** `(Número de homicidios en siniestros viales / Población total) * 100,000`
   - **Objetivo:** Disminuir la tasa de homicidios de siniestros viales en un 10% en los próximos seis meses.
   - **Acciones Sugeridas:** Implementación de campañas de concientización, aumento de controles de tráfico y mejoras en la infraestructura vial.

2. **Reducir en un 7% la cantidad de accidentes mortales de motociclistas en el último año respecto al año anterior.**

   - **Fórmula:** `(Número de accidentes mortales con víctimas en moto en el año anterior - Número de accidentes mortales con víctimas en moto en el año actual) / Número de accidentes mortales con víctimas en moto en el año anterior) * 100`
   - **Objetivo:** Reducir los accidentes mortales de motociclistas en un 7% en el próximo año.
   - **Acciones Sugeridas:** Fomento del uso de equipos de protección personal, educación sobre conducción segura y creación de carriles exclusivos para motociclistas.

Este análisis y los KPIs propuestos servirán como base para la toma de decisiones informadas y la implementación de estrategias efectivas para mejorar la seguridad vial en CABA.

## Funcionalidad de los KPIs

Los KPIs propuestos permitirán evaluar el impacto de las políticas de seguridad vial en tiempo real y ajustar las estrategias según sea necesario para alcanzar los objetivos establecidos. Estos indicadores proporcionan una métrica clara y cuantificable para medir el éxito de las iniciativas de reducción de siniestros viales y mejorar la seguridad de todos los usuarios de la vía.

## Contacto

Para cualquier consulta o más información, por favor contactar a mi [LINKEDIN](https://www.linkedin.com/in/francisco-ag%C3%A1mez-bb132857/).

