1. Tener una url base del sitio
	https://listado.tucarro.com.co/camioneta
2. Listar las urls de todos los vehiculos que aparecen en el sitio actual, teniendo como patronde url: 
   articulo.tucarro.com.co/
   //h2[class=list-view-item-title]/a
3. Hacer una peticion con las urls para descargar la pagina de un sitios especifico
	3.1 Extraer los tags de interes:
	   Usar este selector:
	   	Datos tecnicos del carro
	     //li[class="specs-item"]/text()
	    Para obtener la ubicacion del vehiculo:
	    	Se asume que siembre esta la ubicacion en la misma parte:
	     //section[class=ui-view-more]p[class="card-description"].text()
	     //Obtener el precio
	     //span[class="price-tag-fraction"].text()
	3.2 Almacenar la informacion de cada uno
	Usando una libreria de base de datos como sqlite.
	3.2.1 import sqlite
	3.2.2 apuntador_db = crear_file_db("tucarro.db");
	3.2.3 Crear las tablas que se necesiten:
		 stmt = CREATE_TABLE("CAMIONETA(
		 	Color varchar,
		 	Modelo varchar,
		 	.....
		 	Precio INTEGER,
		 )")
	3.2.4 exec(stmt)
	3.2.5 for carro in lista_carro:
			stmt = 'INSERT INTO CAMIONETA(
			'+carro["Modelo"]....+carro[PRECIO])"
			exec(stmt)
4. Volver al paso 3 hasta que no queden mas vehiculos
5. Dar click en el boton siguiente e ir al paso 1:
		Sacar un selector del boton siguiente:
			Hacer una peticion para descargar esta pagina:'//li[@class=last-child]/a'

