<h1 align="center">Descripción del proyecto</h1>
<p>Gestor de Países — aplicación de consola en Python para cargar, consultar, filtrar, ordenar y obtener estadísticas sobre un 
conjunto de países leído desde un CSV. El objetivo es demostrar buen diseño con listas y diccionarios, funciones moduladas,
validaciones robustas y manejo de archivos, cumpliendo los requerimientos del Trabajo Práctico Integrador de Programación 1.</p>

<h1 align="center">Datos de la Universidad y la cátedra</h1>
<h4 align="left">Universidad: UTN</h4>
<h4 align="left">Sede: Facultad Regional San Nicoláss</h4>
<h4 align="left">Carrera:  Tecnicatura Universitaria en Programación (a distancia)</h4>
<h4 align="left">Asignatura: Programación I</h4>
<h4 align="left">Año: 2025</h4>
<h4 align="left">Entrega: Trabajo Práctico Integrador (TPI) — Gestión de Datos de Países</h4>
<h4 align="left">Nivel (Año):1° </h4>
<h4 style="text-align:left;">Integrantes de la Cátedra:</h4>

<p><strong>Profesor Coordinador:</strong></p>
<p>Alberto Cortez</p>

<p><strong>Profesores a cargo comisión:</strong></p>
<ul style="margin-top:0; padding-left:1.25rem;">
  <li>Cinthia Rigoni</li>
  <li>Sebastián Bruselario</li>
  <li>Ariel Enferrel</li>
</ul>

<h1 align="left">Integrantes del grupo</h1>
<p><strong>alumnos por comisión:</strong></p>
<ul style="margin-top:0; padding-left:1.25rem;">
  <li>Juan Marco Raimundo (Comisión 11)- <em>juanmr.093@gmail.com</em> </li>
  <li>Lucas Bautista Garcia  (Comisión 5)- <em>bautigarcia264@gmail.com</em></li>
</ul>

<h1 align="left">Datos de profesores</h1>
<p><strong>Profesores por Comisión</strong></p>
<ul style="margin-top:0; padding-left:1.25rem;">
  <li>Luciano Chiroli (Comisión 11) </li>
  <li>Matias Santiago Torres  (Comisión 5) </li>
</ul>

<h1 align="left">Estructura</h1>
<p><strong>Directorio Principal</strong></p>
<ol style="margin-top:0; padding-left:1.25rem;">
  <li>TP-Integrador-Programación1 - Carpeta del trabajo Integrador de Programacion I (importante)</li>
    <ul style="margin-top:0; padding-left:1.25rem;">
      <li>Funciones(directorio) - directorio donde estan localizadas las funciones principales de main.py</li>
          <ul style="margin-top:0; padding-left:1.25rem;">
              <li>actualizarDatos.py - archivo py con la funciones necesarias para ejecutar la tarea de actualizar datos de los paises</li>
              <li>agregarPais.py - archivo py con la funciones necesarias para ejecutar la tarea de Agregar Paises</li>
              <li>buscarPais.py - archivo py con la funciones necesarias para ejecutar la tarea de Buscar Paises</li>
              <li>estadisticas.py - archivo py con la funciones necesarias para ejecutar la tarea de ver estadisticas de Paises</li>
              <li>filtrado.py - archivo py con la funciones necesarias para ejecutar la tarea de Filtrar paises segun ciertos datos como Continentes</li>
              <li>guardarArchivo.py - archivo py con la funciones necesarias para Guardar los datos ingresados en el csv</li>
              <li>leerArchivo.py - archivo py con la funciones necesarias para leer el archivo csv</li>
              <li>ordenamiento.py - archivo py con la funciones necesarias para Ordenar paises segun ciertos datos como por superficie o población</li>
           </ul><br>
      <li>Validaciones(directorio) directorio donde esta localizada una de las validaciones </li>
         <ul style="margin-top:0; padding-left:1.25rem;">
              <li>Validaciones py — Codigo donde se encuentran algunas validaciones como pedir_texto o pedir_numero</li>
         </ul><br>
      <li>dataBase(directorio) - directorio donde esta colocado el Dataset</li>
        <ul style="margin-top:0; padding-left:1.25rem;">
              <li>Paises.csv — Dataset base con formato: nombre,poblacion,superficie,continente</li>
           </ul><br>
      <li>gitignore</li>
      <li>main.py — Interfaz de menú y flujo principal de ejecución.</li>
    </ul><br>
  <li>TP-Mat1-Programación1 - Carpeta del trabajo Integrador de Matematicas</li>
  <li>README.md — Descripción del proyecto, instrucciones de uso, ejemplos y créditos.</li>
</ol>

<h1 align="left">Instrucciones de ejecución</h1>
<p>primero el usuario ejecutara el archivo main.py del directorio TP-Integrador-Programación1, luego le saldran 7 opciones estas son</p>
<ol style="margin-top:0; padding-left:1.25rem;">
  <li> Agregar países - Agregar un país con todos los datos necesarios para almacenarse en el csv </li>
  <li> Actualizar un pais - Actualiza los datos de Población y Superfice de un Pais</li>
  <li> Buscar un país - Busca un país por nombre (coincidencia parcial o exacta).</li>
  <li> Filtrar países por: - Filtra países por continente, Rango de población y Rango de superficie </li>
  <li> Ordenar países por: - Ordena países por nombre ,Población o Superficie (ascendente o descendente) </li>
  <li> Mostrar estadísticas - Muestra estadisticas de Países con mayor y menor población, Promedio de población, Promedio de superficie o Cantidad de países por continente</li>
  <li>salir</li>
</ol>
<p>el usuario tendra que usar las teclas del 1 al 7 para poder seleccionar una opción, de otro modo marcara error<br> para salir del programa el usuario tendra apretar el boton 7 en el teclado, de otro modo el programa no se cerrara</p>

<h1 align="left">Links a video y repositorio GitHub</h1>
Enlace del video:
<a href="https://drive.google.com/file/d/1QgYtHKW6ZncEk3k_KlOSx5v8a6vGoIZK/view">

<h1 align="left">Ejemplo de entrada y salida</h1>
<h3>opcion 1:Agregar países</h3>
<p>Entrada:</p>
<img width="839" height="477" alt="image" src="https://github.com/user-attachments/assets/f2c23045-f3fd-4cae-af40-e4184028f3e7" />
<p>Salida:</p>
<img width="216" height="43" alt="image" src="https://github.com/user-attachments/assets/38272625-cd60-4296-891f-c0ecf395e4a1" /><br><br>


<h3>opcion 2:Actualizar Pais</h3>
<p>Entrada:</p>
<img width="844" height="108" alt="image" src="https://github.com/user-attachments/assets/62d72b4c-8eac-4a59-a113-d1150bd9f75e" />
<p>Salida:</p>
<img width="249" height="19" alt="image" src="https://github.com/user-attachments/assets/fd14dd80-55cb-4974-a31a-ac3d49654075" /><br><br>


<h3>opcion 3:Buscar Pais</h3>
<p>Entrada:</p>
<img width="291" height="142" alt="image" src="https://github.com/user-attachments/assets/7b079760-5355-4dda-9dee-eea8ba9193fd" />
<p>Salida:</p>
<img width="287" height="396" alt="image" src="https://github.com/user-attachments/assets/6633f050-27c1-4a0a-a96b-fcda617891fe" />


<h3>opcion 4:Filtrar países por:</h3>
<p>Entrada:</p>
<img width="541" height="155" alt="image" src="https://github.com/user-attachments/assets/d02d6485-4c35-4bec-b79d-9ca8721b82e3" />
<p>Salida:</p>
<img width="670" height="398" alt="image" src="https://github.com/user-attachments/assets/6078b209-b45f-465b-a0c2-6335689fc132" />

<h3>opcion 5:Ordenar países por:</h3>
<p>Entrada:</p>
<img width="331" height="180" alt="image" src="https://github.com/user-attachments/assets/f0cb4061-d766-4303-9dbb-2149068fe902" />
<p>Salida:</p>
<img width="670" height="405" alt="image" src="https://github.com/user-attachments/assets/b1d32049-6f41-49f1-92bc-01fbc5b8dc9a" />

<h3>opcion 6: Mostrar estadísticas </h3>
<p>Entrada:</p>
<img width="285" height="191" alt="image" src="https://github.com/user-attachments/assets/b763ae99-89e0-475f-82b0-cbc3a3755da5" />
<p>Salida:</p>
<img width="292" height="185" alt="image" src="https://github.com/user-attachments/assets/12edd02b-2f1d-4113-80db-e2ad32354da3" />

<h3>opcion 7: Salir </h3>
<p>Entrada:</p>
<img width="249" height="213" alt="image" src="https://github.com/user-attachments/assets/16b79ddc-925c-4c08-b0ec-c68fd5116768" />
<p>Salida:</p>
<img width="300" height="44" alt="image" src="https://github.com/user-attachments/assets/9449fcdc-8ce1-48d7-b51b-86d274c0d34d" />
