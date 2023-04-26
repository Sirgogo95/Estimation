; (function () {
    

    htmx.on('htmx:afterSwap', (e) => {
        const modal = new bootstrap.Modal(document.getElementById('modal')) 
        console.log('htmx:afterSwap', e)
        if(e.detail.target.id === "modal_container")
            modal.modal('show')
    })


}
    )()