// Script to manage sliders and password generation

const defaultLength = 16,
    defaultNbUppers = 3,
    defaultNbDigits = 3,
    defaultNbSpecialChars = 3,
    inputLength = document.getElementById("input-length"),
    inputNbUppers = document.getElementById("input-nb-uppers"),
    inputNbDigits = document.getElementById("input-nb-digits"),
    inputNbSpecialChars = document.getElementById("input-nb-special-chars"),
    btnSubmit = document.querySelector("[type=submit]"),
    url = btnSubmit.getAttribute("data-url"),
    h2Password = document.getElementById("password"),
    rangeInputList = document.querySelectorAll(".range-input")

inputLength.value = defaultLength
inputNbDigits.value = defaultNbDigits
inputNbUppers.value = defaultNbUppers
inputNbSpecialChars.value = defaultNbSpecialChars

rangeInputList.forEach(elem => {
    let span = elem.nextElementSibling
    if (span && span.classList.contains("range-span")) {
        span.innerText = elem.value
        elem.addEventListener("input", () => {
            span.innerText = elem.value
            let total = Array.from(rangeInputList).reduce((sum, elem) => {
                return sum + parseInt(elem.value)
            }, 0)
            console.log(total)
            if (total > parseInt(inputLength.value)) {
                inputLength.value = total
            }
        })
    }
})

btnSubmit.addEventListener("click", async function (event) {
    event.preventDefault()
    let csrfTokenValue = document.querySelector("[name=csrfmiddlewaretoken]").value
    let form = new FormData()
    form.append("length", String(inputLength.value))
    form.append("nb-uppers", String(inputNbUppers.value))
    form.append("nb-digits", String(inputNbDigits.value))
    form.append("nb-special-chars", String(inputNbSpecialChars.value))

    let request = new Request(url, {
        method: "POST",
        body: form,
        headers: {"X-CSRFToken": csrfTokenValue}
    })

    let response = await fetch(request)
    let data = await response.json()
    console.log(`Mot de passe: ${data["password"]}`)
    h2Password.innerText = data["password"]
})
