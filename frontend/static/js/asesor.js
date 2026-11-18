async function llamarSiguiente() {

    try {

        const respuesta = await fetch(
            "/api/llamar",
            {
                method: "POST"
            }
        );

        const datos = await respuesta.json();

        const turnoActual =
            document.getElementById("turnoActual");

        const tipoActual =
            document.getElementById("tipoActual");

        const condicionActual =
            document.getElementById("condicionActual");

        const horaLlamado =
            document.getElementById("horaLlamado");

        if (turnoActual) {
            turnoActual.innerText =
                datos.numero || "---";
        }

        if (tipoActual) {
            tipoActual.innerText =
                datos.tipo || "Sin atención";
        }

        if (condicionActual) {
            condicionActual.innerText =
                datos.condicion || "";
        }

        if (horaLlamado) {

            const ahora = new Date();

            horaLlamado.innerText =
                "Llamado: " +
                ahora.toLocaleTimeString();
        }

        cargarFila();
        cargarEstadisticas();

    } catch (error) {

        console.error(
            "Error al llamar turno:",
            error
        );
    }
}


async function registrarInasistencia() {

    try {

        const respuesta = await fetch(
            "/api/inasistencia",
            {
                method: "POST"
            }
        );

        const datos = await respuesta.json();

        alert(
            datos.mensaje ||
            "Turno marcado como inasistencia"
        );

        cargarFila();
        cargarEstadisticas();

    } catch (error) {

        console.error(
            "Error al registrar inasistencia:",
            error
        );
    }
}


async function cargarFila() {

    try {

        const respuesta =
            await fetch("/api/fila");

        const datos =
            await respuesta.json();

        const tabla =
            document.getElementById(
                "tablaFila"
            );

        if (!tabla) return;

        tabla.innerHTML = "";

        datos.forEach(turno => {

            tabla.innerHTML += `
                <tr>

                    <td>${turno.numero}</td>

                    <td>
                        ${
                            turno.tipo === "PRIORITARIO"
                            ?
                            '<span class="badge-prioritario">Prioritario</span>'
                            :
                            '<span class="badge-regular">Regular</span>'
                        }
                    </td>

                    <td>
                        ${turno.estado}
                    </td>

                    <td>
                        ${turno.personas_delante}
                    </td>

                </tr>
            `;
        });

    } catch (error) {

        console.error(
            "Error cargando fila:",
            error
        );
    }
}


async function cargarEstadisticas() {

    try {

        const respuesta =
            await fetch(
                "/api/estadisticas"
            );

        const datos =
            await respuesta.json();

        const usuariosEspera =
            document.getElementById(
                "usuariosEspera"
            );

        const prioritarios =
            document.getElementById(
                "prioritarios"
            );

        const regulares =
            document.getElementById(
                "regulares"
            );

        const esperaTotal =
            document.getElementById(
                "esperaTotal"
            );

        if (usuariosEspera) {
            usuariosEspera.innerText =
                datos.espera;
        }

        if (prioritarios) {
            prioritarios.innerText =
                datos.prioritarios;
        }

        if (regulares) {
            regulares.innerText =
                datos.regulares;
        }

        if (esperaTotal) {
            esperaTotal.innerText =
                datos.tiempo_total + " min";
        }

    } catch (error) {

        console.error(
            "Error cargando estadísticas:",
            error
        );
    }
}


function iniciarPanel() {

    cargarFila();
    cargarEstadisticas();

    setInterval(() => {

        cargarFila();
        cargarEstadisticas();

    }, 2000);
}


document.addEventListener(
    "DOMContentLoaded",
    iniciarPanel
);