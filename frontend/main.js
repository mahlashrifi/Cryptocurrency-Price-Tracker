import './style.css';

const searchForm = document.querySelector('#search-form');
const subscriptionForm = document.querySelector('#subscription-form');

if (searchForm) {
  searchForm.addEventListener('submit', event => {
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
}

if (subscriptionForm) {
  document.querySelector('#subscription-form').addEventListener('submit', event => {
    event.preventDefault()
    const inputs = document.querySelectorAll('#subscription-form input');
    const data = {
      email: inputs[0].value,
      coin_name: inputs[1].value,
      diff: inputs[2].value,
    }
    inputs.forEach(input => input.value = '')
    fetch('http://127.0.0.1:8000/peyk/subscribe', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data),
    }).then(res => res.json())
      .then(data => {
        alert('Subscription successful')
      }
      ).catch(err => {
        console.log(err)
      })
  });
}