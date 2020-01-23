import {user, checkAuth, getUserInfo, logout} from './util'
import {authorizeFacebook, loginWithFacebook} from './facebook'
import {authorizeGoogle, loginWithGoogle} from './google'
import {loginWithEmail, signUpWithEmail, activateAccount} from './email'




export default {
  user,
  loginWithEmail,
  signUpWithEmail,
  activateAccount,
  loginWithGoogle,
  authorizeGoogle,
  loginWithFacebook,
  authorizeFacebook,
  checkAuth,
  logout,
  getUserInfo
}