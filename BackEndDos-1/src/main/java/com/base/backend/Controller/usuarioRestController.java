package com.base.backend.Controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import com.base.backend.servicios.Entity.usuario;
import com.base.backend.servicios.Service.usuarioService;

@org.springframework.web.bind.annotation.RestController
@RequestMapping("/api")
@CrossOrigin

public class usuarioRestController {

	@Autowired
	private usuarioService usuarioSer;
	@GetMapping("/muestrausuario")
	
	public List<usuario> muestraUsu(){
		return usuarioSer.mostrar();
	}
	
}
