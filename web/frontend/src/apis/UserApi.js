// import axios from "axios";
// const host = "http://127.0.0.1:8080";

import http from "@/utils/http-require.js";

const UserApi = {
  requestLogin: (data, callback, errorCallback) => requestLogin(data, callback, errorCallback),
  join: (data, callback, errorCallback) => join(data, callback, errorCallback),
  //   profileLoad: (data, callback, error) => profileLoad(data, callback, error),
};

const requestLogin = (data, callback, errorCallback) => {
  http
    .post(`back/login/`, {
      identify: data["identify"],
      password: data["password"],
    })
    .then((res) => {
      console.log(res);
      callback(res);
    })
    .catch((error) => {
      console.log(error);
      errorCallback(error);
    });
};

const join = (formdata, callback, errorCallback) => {
  http({
    url: `back/users/join/`,
    method: "post",
    data: formdata,
  })
    .then((res) => {
      console.log(res);
      callback(res);
    })
    .catch((error) => {
      console.log(error);
      errorCallback(error);
    });
};


export default UserApi;