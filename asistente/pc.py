import platform

operating_system = platform.system()
node_name = platform.node()
operating_system_version = platform.version()

processor_architecture = platform.machine()
processor_details = platform.processor()

print("Sistema Operativo: ", operating_system)
print("Nombre del Nodo: ", node_name)
print("Versión del sisteme operativo: ", operating_system_version)
print("Arquitectura del Procesador: ", processor_architecture)
print("Detalle del procesador: ", processor_details)