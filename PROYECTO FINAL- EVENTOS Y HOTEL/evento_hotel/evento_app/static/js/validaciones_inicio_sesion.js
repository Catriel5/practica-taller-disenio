


function resetearMensajesDeErrorInicioSesion() {
    var mensajeDeError = document.getElementById("mensaje-error");

    if (mensajeDeError) {
        mensajeDeError.innerText = "";
    }
}

resetearMensajesDeErrorInicioSesion();


function validarInicioSesion() {
    
    resetearMensajesDeErrorInicioSesion();

    
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    // Validaciones
    var errores = [];

    if (!username.trim() || !password.trim()) {
        errores.push("Usuario y contraseña son obligatorios.");
        mostrarErrorInicioSesion("mensaje-error", "Usuario y contraseña son obligatorios.");
    }

    
    if (errores.length > 0) {
        return false;
    }


    return true;
}


function mostrarErrorInicioSesion(id, mensaje) {
    var elementoError = document.getElementById(id);
    if (elementoError) {
        elementoError.innerText = mensaje;
    }
}
