async function generarTurno() {

    try {

        const respuesta = await fetch(
            "/api/turno",
            {
                method: "POST"
            }
        );

        const datos = await respuesta.json();

        if (
            datos.mensaje ===
            "HORARIO_FINALIZADO"
        ) {

            window.location.href =
                "/horario-finalizado";

            return;
        }

        localStorage.setItem(
            "turnoActual",
            JSON.stringify(datos)
        );

        window.location.href =
            "/turno-emitido";

    } catch (error) {

        console.error(
            "Error al generar turno:",
            error
        );

    }

}


function mostrarPrioridades() {

    const panel =
        document.getElementById(
            "prioridades"
        );

    if (panel) {

        panel.style.display =
            "block";

    }

}


async function generarPrioritario(
    condicion
) {

    try {

        const respuesta = await fetch(
            "/api/turno-prioritario",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                    "application/json"
                },

                body: JSON.stringify({
                    condicion
                })
            }
        );

        const datos =
            await respuesta.json();

        if (
            datos.mensaje ===
            "HORARIO_FINALIZADO"
        ) {

            window.location.href =
                "/horario-finalizado";

            return;
        }

        localStorage.setItem(
            "turnoActual",
            JSON.stringify(datos)
        );

        window.location.href =
            "/turno-emitido";

    } catch (error) {

        console.error(
            "Error al generar turno prioritario:",
            error
        );

    }

}