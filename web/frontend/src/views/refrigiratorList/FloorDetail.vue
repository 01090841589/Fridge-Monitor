<template>
  <div class="detail">
    <!-- 식품 목록 컴포넌트 -->
    <Divider />
    <!-- 식품추가 버튼 -->
    <img
      v-b-modal.modal-prevent-closing
      src="@/image/add.png"
      width="50px"
      height="50px"
      style="display: block; margin: 150px auto 5px auto"
      @click="Register"
    />

    <!-- modal(컴포넌트화 하기) -->
    <b-modal
      id="modal-prevent-closing"
      ref="modal"
      title="식품 추가"
      @show="resetModal"
      @hidden="resetModal"
      @ok="handleOk"
    >
      <form ref="form" @submit.stop.prevent="handleSubmit">
        <b-form-group label="식품사진" label-for="name-input" invalid-feedback="Name is required">
          <div id="uploader">
            <div class="input-group">
              <input
                type="text"
                class="form-control"
                placeholder="식품 사진"
                v-model="filename"
                @dragover.prevent
                @dragenter.prevent
                @drop.prevent="onDrop"
                readonly
              />
              <div v-show="imageSrc" class="upload-image">
                <img id="addImg" :src="imageSrc" />
              </div>
              <div class="input-group-append">
                <span class="input-group-text" @click="onClickFile">
                  <i class="fa fa-paperclip">Select</i>
                </span>
                <!-- <span style="visibility:hidden">간격</span>
                <button class="btn btn-outline-info" @click="onClickUpload">Upload</button> -->
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
        </b-form-group>

        <b-form-group label="식품명" label-for="name-input" invalid-feedback="Name is required">
          <b-form-input id="name-input" required></b-form-input>
        </b-form-group>

        <b-form-group label="유통기한" label-for="name-input" invalid-feedback="Name is required">
          <b-calendar v-model="value" :min="min" :max="max" locale="en"></b-calendar>
        </b-form-group>
      </form>
    </b-modal>
  </div>
</template>
<script src="//unpkg.com/vue/dist/vue.js"></script>
<script src="//unpkg.com/element-ui@2.13.2/lib/index.js"></script>
<script>
import Divider from "@/components/Divider";

export default {
  name: "detail",
  components: { Divider },
  methods: {
    Register() {
      console.log("식품추가 이미지 클릭");
    },
    //이미지 삽입
    onDrop(event) {
      this.inputImageFile(event.dataTransfer.files);
      this.uploadImage = event.dataTransfer.files[0];
    },
    onClickFile(event) {
      console.log(event);
      this.$refs.fileInput.click();
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
    },
    onFileChange(event) {
      this.inputImageFile(event.target.files);
    },

    //modal
    checkFormValidity() {
      const valid = this.$refs.form.checkValidity();
      // this.nameState = valid;
      return valid;
    },
    resetModal() {
      // this.nameState = null;
    },
    handleOk(bvModalEvt) {
      // Prevent modal from closing
      bvModalEvt.preventDefault();
      // Trigger submit handler
      this.handleSubmit();
    },
    handleSubmit() {
      // Exit when the form isn't valid
      if (!this.checkFormValidity()) {
        return;
      }
      // Push the name to submitted names
      // this.submittedNames.push(this.name);
      // Hide the modal manually
      this.$nextTick(() => {
        this.$bvModal.hide("modal-prevent-closing");
      });
    }
  },
  data() {
    const now = new Date();
    const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
    // 15th two months prior
    const minDate = new Date(today);
    minDate.setMonth(minDate.getMonth());
    minDate.setDate(today.getDate());
    // 15th in two months
    const maxDate = new Date(today);
    maxDate.setMonth(maxDate.getMonth() + 36);
    maxDate.setDate(today.getDate());

    return {
      value: "",
      min: minDate,
      max: maxDate,
      uploadImage: "",
      filename: "",
      imageSrc: ""
    };
  }
};
</script>