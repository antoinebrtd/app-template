import axios from 'axios'
import router from '@/modules/router'
import notifications from '@/modules/notifications'


let user = {
  authenticated: false,
  profile: undefined
};

function loginWithEmail(context) {
  return new Promise((resolve, reject) => {
    axios.post(process.env.VUE_APP_EMAIL_AUTH_URL + '/login', {email: context.email, password: context.password})
        .then((response) => {
          if (response.status === 200) {
            localStorage.setItem('access_token', response.data.access_token);
            checkAuth().then(() => {
              if (context.token) {
                axios.post(process.env.VUE_APP_EMAIL_AUTH_URL + `/confirm-email/${context.token}`).then(response => {
                  notifications.addNotification(response.data);
                  checkAuth().then(() => {
                    router.push('/home');
                    resolve();
                  })
                }).catch(error => {
                  notifications.addNotification(error.response.data.error);
                  router.push('/home');
                  resolve();
                })
              } else {
                router.push('/home');
                resolve();
              }
            });
          } else {
            reject();
          }
        })
        .catch(function (error) {
          if (error.response) {
            reject(new Error(error.response.data.error));
          } else {
            reject()
          }
        });
  })
}

function signUpWithEmail(context) {
  return new Promise((resolve, reject) => {
    axios.post(process.env.VUE_APP_EMAIL_AUTH_URL + '/sign-up', {email: context.email, password: context.password})
        .then((response) => {
          if (response.status === 200) {
            localStorage.setItem('access_token', response.data.access_token);
            checkAuth().then(() => {
              router.push('/home');
              notifications.addNotification(`An email to activate your account has been sent to ${user.profile.email}`);
              resolve()
            });
          } else {
            reject()
          }
        })
        .catch(function (error) {
          if (error.response) {
            reject(new Error(error.response.data.error));
          } else {
            reject()
          }
        });
  })
}

function loginWithGoogle(context) {
  axios.get(process.env.VUE_APP_GOOGLE_AUTH_URL + '/login')
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
  axios.get(process.env.VUE_APP_GOOGLE_AUTH_URL + '/authorize?code=' + code + '&state=' + state)
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
      context.errorMessage = 'An error occurred during the authentication.';
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
      axios.get(process.env.VUE_APP_API_URL + '/me')
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
    if (!user.authenticated && this.router.name !== '/') {
      router.replace('/');
    }
  });
}

export default {
  user,
  loginWithEmail,
  signUpWithEmail,
  loginWithGoogle,
  authorize,
  logout,
  checkAuth
}