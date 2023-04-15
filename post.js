const axios = require('axios');

const payload = {
  title: 'Harry Porter and the Sorcerers Stone',
  author: 'J.K.Rowling',
  year: 1998
};

axios.post('http://localhost:5000/books', payload)
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  });
