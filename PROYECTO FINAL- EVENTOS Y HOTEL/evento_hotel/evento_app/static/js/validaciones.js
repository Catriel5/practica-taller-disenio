function validarFormulario() {
    
    resetearMensajesDeError();

    
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var confirm_password = document.getElementById("confirm_password").value;
    var nombre = document.getElementById("nombre").value;
    var apellido = document.getElementById("apellido").value;
    var correo = document.getElementById("correo").value;
    var fechaRegistro = document.getElementById("fechaRegistro").value;

    
    var errores = [];

    if (!username.trim()) {
        errores.push("El nombre de usuario es requerido.");
        mostrarError("username-error", "El nombre de usuario es requerido.");
    }

    if (!password.trim()) {
        errores.push("La contraseña es requerida.");
        mostrarError("password-error", "La contraseña es requerida.");
    } else if (password.length < 8) {
        errores.push("La contraseña debe tener al menos 8 caracteres.");
        mostrarError("password-error", "La contraseña debe tener al menos 8 caracteres.");
    } else if (!(/[A-Z]/.test(password))) {
        errores.push("La contraseña debe contener al menos una mayúscula.");
        mostrarError("password-error", "La contraseña debe contener al menos una mayúscula.");
    }

    if (password !== confirm_password) {
        errores.push("Las contraseñas no coinciden.");
        mostrarError("confirm_password-error", "Las contraseñas no coinciden.");
    }

    if (!nombre.trim()) {
        errores.push("El nombre es requerido.");
        mostrarError("nombre-error", "El nombre es requerido.");
    }

    if (!apellido.trim()) {
        errores.push("El apellido es requerido.");
        mostrarError("apellido-error", "El apellido es requerido.");
    }

    if (!correo.trim()) {
        errores.push("El correo electrónico es requerido.");
        mostrarError("correo-error", "El correo electrónico es requerido.");
    } else if (!/^.+@.+\..+$/.test(correo)) {
        errores.push("El correo electrónico no es válido.");
        mostrarError("correo-error", "El correo electrónico no es válido.");
    }

    if (!fechaRegistro.trim()) {
        errores.push("La fecha de registro es requerida.");
        mostrarError("fechaRegistro-error", "La fecha de registro es requerida.");
    }

    
    if (errores.length > 0) {
        return false;
    }

    
    return true;
}

function resetearMensajesDeError() {
    var mensajesDeError = document.getElementsByClassName("text-danger");

    for (var i = 0; i < mensajesDeError.length; i++) {
        mensajesDeError[i].innerText = "";
    }
}

function mostrarError(id, mensaje) {
    var elementoError = document.getElementById(id);
    if (elementoError) {
        elementoError.innerText = mensaje;
    }
}
