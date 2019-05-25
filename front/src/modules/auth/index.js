import axios from 'axios'
import router from '../router/index'

let user = {
  authenticated: false,
  profile: undefined
};

function login(context) {
  axios.get(process.env.AUTH_URL + '/login')
    .then((response) => {
      if (response.status === 200) {
        window.location.replace(response.data.url);
      } else {
        context.error = true;
      }
    })
    .catch(function (error) {
      context.error = true;
      context.errorMessage = '';
      if (error.response) {
        context.errorMessage = error.response.data.error;
      } else {
        console.log(error);
      }
    });
}

function authorize(context, code, state) {
  axios.get(process.env.AUTH_URL + '/authorize?code=' + code + '&state=' + state)
    .then(function (response) {
      if (response.status === 200) {
        localStorage.setItem('access_token', response.data.access_token);
        checkAuth().then(() => {
          router.push('/home');
        });
      } else {
        context.error = true;
      }
    })
    .catch(function (error) {
      context.error = true;
      context.errorMessage = 'An error occured during the authentification.';
      if (error.response) {
        context.errorMessage = error.response.data.error;
      } else {
        console.log(error);
      }
    });
}

function logout() {
  localStorage.removeItem('access_token');
  localStorage.removeItem('profile');
  axios.defaults.headers.common['Authorization'] = '';
  user.authenticated = false;
  user.profile = null;
  router.replace('/');
}

function checkAuth() {
  return new Promise((resolve, reject) => {
    const jwt = localStorage.getItem('access_token');
    if (jwt !== null) {
      user.authenticated = true;
      axios.defaults.headers.common['Authorization'] = 'Bearer ' + jwt;
      axios.get(process.env.API_URL + '/me')
        .then(function (response) {
          user.authenticated = response.status === 200;
          if (!user.authenticated) {
            throw new Error(response);
          } else {
            user.profile = response.data;

            localStorage.setItem('profile', JSON.stringify(user.profile));
            resolve();
          }
        })
        .catch(function (error) {
          user.authenticated = false;
          reject();
          logout();
        });
    } else {
      user.authenticated = false;
      reject();
    }
    if (!user.authenticated) {
      router.replace('/');
    }
  });
}

export default {
  user,
  login,
  authorize,
  logout,
  checkAuth
}
