// import axios from "axios";
import http from "@/utils/http-require.js";
// const host = "http://127.0.0.1:8000";

const ProductApi = {
    imgupload: (data, callback, errorCallback) => imgupload(data, callback, errorCallback),
};

const imgupload = (formdata, callback, errorCallback) => {
    http({
      url: `userapi/test/`, //경로 설정.
      method: "post",
      data: formdata,
      headers: {
        "Content-Type": "multipart/form-data",
      },
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

export default ProductApi;