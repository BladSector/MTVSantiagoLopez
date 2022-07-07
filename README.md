# MTV Santiago Lopez

- Proyecto de CoderHouse mi primer MTV base funcional
- Proyecto no terminado aún (max 3 dias) y por ende no es para entregar
- Contiene:
- Entorno virtual activado
- .gitignore, README y requerimientos de programas
- App con una sola vewis.py y urls.py <home> con sus import adecuados para que  el Server funcione (Se van a agregar mas durante el desarrollo)
- Carpeta "templantes"
- Introduje: MVTSantiagoLopez> settings.py> 'DIRS': '[r'C:\P1\templates']'
- Archivo <index.html> [r'C:\P1\templates\index.html']
- Prueba de template funcional con lista_ejemplo. "path('template_ejemplo/', template_ejemplo)"
- Agregue [r'C:\P1\MVTSantiagoLopez\settings.py]> INSTALLED_APPS = 'app', makemigration en [r'app\migrations\0001_initial.py'] y migrate para que lo tome el db.sqlite3
- Carpeta  app> "static" y "app". Y pase las carpetas a [C:\P1\app\static\app\]>'assets', 'css' y 'js' de
Archivo <indexstartbootstrap.html>(template ya echo descargado) en  archivo 'templates'
Este index se lo pase al path('', home) en [C:\P1\app\urls.py]
- En [C:\P1\templates\indexstartbootstrap.html] introduje: '{% load static %}'.
En la misma direccion cambie: link href='{% static 'app/css/styles.css' %}'
