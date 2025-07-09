package com.base.backend.servicios.Repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.base.backend.servicios.Entity.usuario;

public interface usuarioRepository extends JpaRepository<usuario, Integer>{

}
