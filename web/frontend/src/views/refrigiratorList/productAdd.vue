<template>
  <v-container>
    <div id="uploader">
      <div class="input-group">
        <input
          type="text"
          class="form-control"
          placeholder="추가할 식품 사진을 넣어주세요."
          v-model="filename"
          @dragover.prevent
          @dragenter.prevent
          @drop.prevent="onDrop"
          readonly
          style="text-align:center; width:100%; margin:0 10%"
        />
        <div v-show="imageSrc" class="upload-image" style="text-align:center">
          <img id="addImg" :src="imageSrc" />
        </div>
        <div class="input-group-append" v-if="!this.isLoading">
          <span class="input-group-text" @click="onClickFile">
            <i class="fa fa-paperclip">Select</i>
          </span>
          <span style="visibility:hidden">간격</span>
          <button class="btn btn-outline-info" @click="onClickUpload">Upload</button>
        </div>
        <input
          type="file"
          class="file-input"
          accept="image/*"
          ref="fileInput"
          @change="onFileChange"
          style="display:none"
        />
      </div>
    </div>
  </v-container>
</template>

<script>
import jwtDecode from 'jwt-decode'
import ProductApi from "../../apis/ProductApi";
import {mapActions, mapState} from "vuex"
import store from "../../vuex/store"
export default {
  name: "imageUpload",
  data() {
    return {
      uploadImage: "",
      filename: "",
      imageSrc: "",
      username: ""
    };
  },
  methods: {
    
    ...mapActions(['loading']),
  
    initialize () {
      this.username = jwtDecode(store.state.token).username
    },
    onDrop(event) {
      this.inputImageFile(event.dataTransfer.files);
      this.uploadImage = event.dataTransfer.files[0];
    },
    onClickFile(event) {
      console.log(event);
      this.$refs.fileInput.click();
    },
    onFileChange(event) {
      this.inputImageFile(event.target.files);
    },
    inputImageFile(files) {
      if (files.length) {
        let file = files[0];
        if (!/^image\//.test(file.type)) {
          alert("이미지 파일만 등록이 가능합니다");
          return false;
        }
        this.filename = file.name;
        this.uploadImage = file;
        this.preview(file);
      }
    },
    onClickUpload() {
      this.preview(this.filename);
      this.loading();
      console.log("이미지입니까?");
      const formData = new FormData();
      formData.append("file", this.uploadImage);
      formData.append("username", this.username);
      ProductApi.imgupload(
        formData,
        res => {
          console.log(res);
          const datas = res.data;
          console.log("이미지전송");
          this.$router.push({ name: "productAddInfo", params: { datas } });
          this.loading();
        },
        error => {
          console.log(error);
          console.log("이미지전송에러");
          this.loading();
        }
      );
    },
    preview(file) {
      if (typeof file === "string") {
        this.imageSrc = file;
      } else {
        let vm = this;
        let reader = new FileReader();
        reader.onload = () => {
          vm.imageSrc = reader.result;
        };
        reader.readAsDataURL(file);
      }
    }
  },
  computed: {
    ...mapState(["isLoading"])

  },
  created () {
    this.initialize()
  },
};
</script>

<style scoped>

img {
  width: 100%;
}
span {
  background: #f8d348;
  font-size: 16px;
  border-radius: 5px;
  padding: 10px 15px;
  margin-top: 15px;
}
button {
  background: #f8d348;
  font-size: 16px;
  border-radius: 5px;
  padding: 7.5px 15px;
  margin-top: 15px;
}

.input-group-text {
  cursor: pointer;
}

#addImg {
  width: 90%;
  height: auto;
  max-height: 400px;
  max-width: 400px;
  margin-top: 5px;
}
.upload-image{
  text-align: center;
  width: 100%;
  /* margin-left: 25vw */
}
.input-group{
  text-align: center;
  align-content: center;
}
.input-group-append{
  margin:0 30%;
  width:90%;
  display: flex;
  justify-content: center;
}
</style>