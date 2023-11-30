function confirmar(mensaje) {
    return confirm(mensaje);
}

function confirmarInscripcion() {
    // Limpiar mensajes de error anteriores
    resetMensajesError();

    
    var nombre = document.getElementById('id_nombre').value;
    var apellido = document.getElementById('id_apellido').value;
    var tel_part = document.getElementById('id_tel_part').value;
    var lugar_procedencia = document.getElementById('id_lugar_procedencia').value;
    var fecha_llegada = document.getElementById('id_fecha_llegada').value;

    if (nombre.trim() === '') {
        mostrarError('nombre', 'Por favor, completa el campo "Nombre".');
        return;
    }
    if (apellido.trim() === '') {
        mostrarError('apellido', 'Por favor, completa el campo "Apellido".');
        return;
    }

    if (tel_part.trim() === '') {
        mostrarError('tel_part', 'Por favor, completa el campo "Teléfono".');
        return;
    }

    if (lugar_procedencia.trim() === '') {
        mostrarError('lugar_procedencia', 'Por favor, completa el campo "Lugar de Procedencia".');
        return;
    }

    if (fecha_llegada.trim() === '') {
        mostrarError('fecha_llegada', 'Por favor, completa el campo "Fecha de Llegada".');
        return;
    }

    if (confirmar('¿Estás seguro de que quieres inscribirte?')) {
        
        enviarFormularioAsync();
    }
}

function mostrarError(campo, mensaje) {
    
    var errorElement = document.getElementById('error_' + campo);
    errorElement.innerText = mensaje;
    errorElement.style.display = 'block';
}

function resetMensajesError() {
    
    var mensajesError = document.querySelectorAll('[id^="error_"]');
    mensajesError.forEach(function (element) {
        element.innerText = '';
        element.style.display = 'none';
    });
}

function enviarFormularioAsync() {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', document.getElementById('inscripcionForm').action, true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

    xhr.onload = function () {
        if (xhr.status === 200) {
            
            var mensajeAviso = document.getElementById('mensajeAviso');
            mensajeAviso.style.display = 'block';

            
            mensajeAviso.addEventListener('click', function () {
                
                limpiarCamposFormulario();
                volverAtras();
            });
        }
    };

    
    var formData = new FormData(document.getElementById('inscripcionForm'));

    
    xhr.send(new URLSearchParams(formData));
}

function limpiarCamposFormulario() {
    
    var camposFormulario = document.querySelectorAll('#inscripcionForm input[type="text"], #inscripcionForm input[type="date"]');

    
    camposFormulario.forEach(function (campo) {
        campo.value = '';
    });
}

function volverAtras() {
    
    window.history.back();
}
