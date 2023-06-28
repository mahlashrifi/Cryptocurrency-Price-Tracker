import './style.css';

document.querySelector('#search-form').addEventListener('submit', event => {
  event.preventDefault()
  const input = document.querySelector('#search-form input')
  const query = input.value
  input.value = ''
  fetch(`http://127.0.0.1:8000/peyk/price?q=${query}`)
    .then(res => res.json())
    .then(data => {
      console.log(data)
      const ul = document.querySelector('#results')
      ul.innerHTML = ''
      data.forEach(item => {
        const li = document.createElement('li')
        li.textContent = item
        ul.appendChild(li)
      })
    }).catch(err => {
      console.log(err)
    })
});