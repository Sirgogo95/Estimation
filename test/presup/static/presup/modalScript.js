; (function () {
    const modal = document.getElementById('modal')

    htmx.on('htmx:afterSwap', (e) => {
        const modalToggle = document.getElementById('modal'); modalToggle.show(modal)
    })

    htmx.on('htmx:beforeSwap', (e) => {
        console.log('htmx:beforeSwap', e)
            if (e.detail.target.id === "modal_container" && !e.detail.xhr.response) 
                modal.hide()
    })
}
    )()