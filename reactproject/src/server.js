import axios from 'axios';
import store from 'store';   //用于本地存储token
import settings from './ect/settings'

const Url = settings.url;

const registerServer = async (data) => {
  console.log(Url)
  let res = await axios.post (`${Url}/register/`, data);
  console.log(res);
  return res.data;
}

const loginServer = async (data) => {
  let res = await axios.post (`${Url}/login/`, data);
  if (res.status == 200) {
    let token = res.headers.auth;
    if (token) store.set('django_token', token);
    return res.data;
  }

}

const allUsersServer = async () => {
   //从本地缓存获取token添加到headers
  let token = store.get('django_token');
  let headers = {
    auth: token
  }
  let res = await axios.get(`${Url}/all_users/`, {headers});
  if (res.status === 200) {
    let token = res.headers.auth;
    if (token) store.set('django_token', token);    //刷新本地存储的token
    return res.data;
  }
}

export {
  registerServer,
  loginServer,
  allUsersServer
}