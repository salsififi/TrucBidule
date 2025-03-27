const btnCalculer = document.getElementById("btn-calculer")
const url = btnCalculer.getAttribute("data-url")
btnCalculer.addEventListener("click", async function (event) {
    event.preventDefault()

    let nb1 = document.getElementById("input-nb1").value
    let nb2 = document.getElementById("input-nb2").value
    let form = new FormData()
    form.append("nb1", nb1)
    form.append("nb2", nb2)
    let csrfTokenValue = document.querySelector("[name=csrfmiddlewaretoken]").value
    let request = new Request(url, {
        method: "POST",
        body: form,
        headers: {"X-CSRFToken": csrfTokenValue}
    })

    let response = await fetch(request)
    let data = await response.json()
    let pResult = document.getElementById("p-result")
    pResult.innerText = `Total: ${data["operation_result"]}`
})

// btnCalculer.addEventListener("click", (event) => {
//     let nb1 = document.getElementById("input-nb1").value
//     let nb2 = document.getElementById("input-nb2").value
//
//     let form = new FormData()
//     form.append("nb1", nb1)
//     form.append("nb2", nb2)
//     let crsfTokenValue = document.querySelector("[name=csrfmiddlewaretoken]")
//
//     let request = new Request("{% url 'compute' %}", {
//         method: "POST",
//         body: form,
//         headers: {"X-CSRFToken": crsfTokenValue}
//     })
//
//     fetch(request)
//         .then(response => response.json())
//         .then(data => {
//             let pResult = document.getElementById("p-result")
//             pResult.innerText = `Somme: ${data["operation_result"]}`
//         })
//
// })