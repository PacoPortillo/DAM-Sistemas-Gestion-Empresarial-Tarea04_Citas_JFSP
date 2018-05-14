# DAM - SISTEMAS DE GESTIÓN EMPRESARIAL - TAREA 04
## Creación de un módulo para Odoo:

- - -
<img src="./readme_imagenes/icono_40.png" align="right" width="90"/>

Título de la tarea: Desarrollo de componentes.
Unidad: 04
Ciclo formativo y módulo: DAM, Sistemas de Gestión Empresarial.
Curso académico: 2017/18
¿Qué contenidos o resultados de aprendizaje trabajaremos?
Desarrolla componentes para un sistema ERP-CRM analizando y utilizando el lenguaje de programación incorporado.


- - -
## Índice:

[TOC]

### Manual de usuario:
#### Instalación:
Una vez descargado el módulo de Odoo este tendrá un formato zip, debemos descomprimirle y una vez descomprimido:
![img01]

Lo debemos instalar en la ubicación donde se encuentran los addons de Odoo, por ejemplo en la versión Odoo10 y en Windows sería en:
`C:\Program Files(x86)\Odoo 10.0\server\odoo\addons\`

![img02]

Una vez ubicado el archivo en ese directorio, nos vamos e iniciamos una sesión, esto lo podemos hacer desde un cliente. Realizamos un login desde una cuenta que nos permita instalar complementos por ejemplo la de administrador.

Una vez dentro nos vamos a Configuración > Activar modo desarrollador:
![img05]

Una vez en modo desarrollador nos vamos a Aplicaciones > Actualizar lista de aplicaiones > Actualizar:
![img03]

Después quito del filtro de búsqueda ‘Aplicaciones’ y establezco como filtro ‘citas’:
![img04]

Me aparece el nuevo módulo que acabo de introducir en el directorio de addons si pincho sobre el cuerpo puedo acceder a su información:
![img06]

Puedo ver los requisitos necesarios que contiene el módulo en la pestaña de Datos técnicos aunque en este caso tan sólo necesita los módulos bases de Odoo.

En este punto se puede proceder a la instalación simplemente pulsando el botón de Instalar.
Y comienza la instalación.
Podemos comprobar al cabo de unos segundos como nos aparece un nuevo ítem en el menú de Odoo:
![img07]

La instalación ha resultado ser un éxito.

#### Forma de uso:
Este módulo es algo muy simple: crea citas asignadas a un usuario, con una fecha y una prioridad. El módulo establece un sistema de ordenación por fechas en orden descendente (la más actual arriba) y si las citas se encuentran en fechas idénticas se ordenan por prioridad siendo el número más alto la prioridad más alta.
Veamos un ejemplo:
##### Crear una cita:
Se pulsa sobre el botón Crear. Nos aparece el marco para crear la cita:
![img08]

Escribimos los campos que son todos obligatorios.
Escribimos la cita, en autor podemos elegir entre todos los usuarios del sistema e incluso podemos crear nuevos usuarios desde este mismo marco, lo normal y por defecto aparecerá nuestro usuario.
En fecha establecemos la fecha para ello se despliega un calendario.
Y en prioridad es importante establecer un número siendo 0 la prioridad más baja.
Una vez creada nuestra Cita pulsamos en el botón de Guardar.

Todas las citas pueden ser modificadas íntegramente a posteriori pulsando en el botón de Editar.

##### Ordenación de citas:
Estas citas se han creado en el siguiente orden:
Cita 01, Cita 02, Cita 03, Cita 04 y Cita 05, pero sin embargo el orden en el que aparecen vemos que atiende a una ordenación temporal y después por prioridad lo que resulta de utilidad a la hora de tener los datos de las citas más accesibles:
![img09]


- - -
#### Fuentes de información:
![ico01]
https://icons8.com/

https://youtu.be/9ojhJsXNWCI
https://youtu.be/yppT6GPZMyo
http://angelmoya.es/blog/openerp/como-empezar-a-desarrollar-modulos-en-openerp-22/
https://web.archive.org/web/20170912092435/docs.python.org.ar/tutorial/2/stdlib.html
https://web.archive.org/web/20170929135159/http://docs.python.org.ar/tutorial/3/errors.html
https://www.odoo.com/es_ES/
http://fundamentos-de-desarrollo-en-odoo.readthedocs.io/es/latest/capitulos.html
https://www.odoo.com/apps/modules/browse?search=Citas&order=Relevance
https://github.com/search?l=Python&p=1&q=Citas&type=Repositories


- - -
### Requisitos
- [Odoo] 10.0 o superior.
- Navegador Web [Firefox], [Chrome], [Opera], [Microsoft Edge], etc..

- - -
### Instalación:
El módulo ha sido desarrollado y testeado en la versión 10.0 del ERP [Odoo], por lo que no me hago responsable ni puedo garantizar su funcionamiento en versiones anteriores.
- - -
### Entorno de desarrollo
- Lenguajes [Python] y XML
- La aplicación ha sido desarrollada utilizando el IDE [Sublime Text].

- - -
### Licencia
Esta aplicación se ofrece bajo licencia [GPL versión 3].

- - -
### Fecha de creacción del proyecto:
martes, 3 de abril de 2018 19:35

- - -
### Fecha de la última actualización:
lunes, 14 de mayo de 2018 18:05

- - -

[ico01]: ./readme_imagenes/icono_40.png
[img01]: ./readme_imagenes/img01.jpg
[img02]: ./readme_imagenes/img02.jpg
[img03]: ./readme_imagenes/img03.jpg
[img04]: ./readme_imagenes/img04.jpg
[img05]: ./readme_imagenes/img05.jpg
[img06]: ./readme_imagenes/img06.jpg
[img07]: ./readme_imagenes/img07.jpg
[img08]: ./readme_imagenes/img08.jpg
[img09]: ./readme_imagenes/img09.jpg
[img10]: ./readme_imagenes/img10.jpg

[Odoo]: https://www.odoo.com/es_ES/
[Sublime Text]: https://www.sublimetext.com/3
[Python]: https://www.python.org/
[Chrome]: https://www.google.es/chrome/browser/desktop/index.html
[Firefox]: https://www.mozilla.org/es-ES/firefox/new/
[Opera]: http://www.opera.com/es
[Microsoft Edge]: https://www.microsoft.com/es-es/windows/microsoft-edge
[GPL versión 3]: https://www.gnu.org/licenses/gpl-3.0.en.html


