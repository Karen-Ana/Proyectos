package com.base.backend.servicios.Service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.base.backend.servicios.Entity.usuario;
import com.base.backend.servicios.Repository.usuarioRepository;

@Service


public class usuarioService {

	@Autowired
	private usuarioRepository usuarioRepo;
	
	@Transactional
	public List<usuario> mostrar(){
		return usuarioRepo.findAll();
	}
	
}
