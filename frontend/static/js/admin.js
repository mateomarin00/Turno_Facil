async function cargarDashboard(){

    const respuesta =
        await fetch(
            "/api/dashboard"
        );

    const datos =
        await respuesta.json();

    document.getElementById(
        "emitidos"
    ).innerText =
        datos.emitidos;

    document.getElementById(
        "espera"
    ).innerText =
        datos.espera;

    document.getElementById(
        "atencion"
    ).innerText =
        datos.atencion;

    document.getElementById(
        "cancelados"
    ).innerText =
        datos.cancelados;

    document.getElementById(
        "prioritarios"
    ).innerText =
        datos.prioritarios;

    document.getElementById(
        "regulares"
    ).innerText =
        datos.regulares;

    document.getElementById(
        "promedio"
    ).innerText =
        datos.promedio + " min";
}

cargarDashboard();

setInterval(
    cargarDashboard,
    3000
);
