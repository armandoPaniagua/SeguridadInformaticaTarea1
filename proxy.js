var express = require('express'); //Servidor que tiene las funcionalidades web
var request = require('request'); //Libreria que hace peticiones a node

//http://localhost/load/?url=***

var app =  express();
app.use('/load',
	function(req, res){
		var url = req.url.replace('/?url=', '');
		console.log('Se esta utilizando el proxy en la página '+(url));
		req.pipe(request(url)).pipe(res);//Peticion de la url y mandamos al pipe
	}
	);
app.listen(10401);
console.log('Proxy corriendo en el puerto 10401');

//Para usarlo desde el propio equipo se utiliza lo siguiente, despues de // va la dirección de la pagina Web.

//localhost:10401/load/?url=http://
