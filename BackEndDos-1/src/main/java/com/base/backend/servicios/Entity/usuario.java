package com.base.backend.servicios.Entity;

import java.io.Serializable;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name="usuario")



public class usuario implements Serializable{

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	
	@Id
	@Column(name="Id_usuario")
	int Id_usuario;
	@Column(name="Nombre_usuario")
	String Nombre_usuario;
	@Column(name="Contrasena")
	String Contrasena;
	
	public int getId_usuario() {
		return Id_usuario;
	}
	public void setId_usuario(int id_usuario) {
		Id_usuario = id_usuario;
	}
	public String getNombre_usuario() {
		return Nombre_usuario;
	}
	public void setNombre_usuario(String nombre_usuario) {
		Nombre_usuario = nombre_usuario;
	}
	public String getContrasena() {
		return Contrasena;
	}
	public void setContrasena(String contrasena) {
		Contrasena = contrasena;
	}
	public static long getSerialversionuid() {
		return serialVersionUID;
	}
	@Override
	public String toString() {
		return "usuario [Id_usuario=" + Id_usuario + ", Nombre_usuario=" + Nombre_usuario + ", Contrasena=" + Contrasena
				+ "]";
	}
	
	
}
