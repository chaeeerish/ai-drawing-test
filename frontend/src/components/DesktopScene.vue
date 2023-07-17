<template>
  <div class="desktop-scene">
    <img src="../assets/images/desktopbg.png" class="background-img" />
    <div class="desktop-text">
      <p class="title-text"><span style="color: #eba090">마음</span>스케치</p>
      <img class="icon1" src="../assets/images/icon5.png" />
      <p class="title-subtext">
        내가 그린 그림으로 <br />
        확인해보는 나의 심리
      </p>
      <div class="qrcode-div">
        <img class="qrcode" src="../assets/images/qrcode.png" />
        <p class="qrcode-text">
          시작하기 위해 QR코드를 <br />핸드폰으로 스캔해주세요
        </p>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "DesktopScene",
  components: {},
  data() {
    return {
      sampleData: "",
    };
  },
};
</script>
<style scoped>
.desktop-scene {
  height: 100%;
  background-repeat: repeat-y;
  background-attachment: fixed;
  background-size: cover;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  color: black;
}
.background-img {
  height: 100%;
  width: 100%;
}
.desktop-text {
  position: absolute;
  top: 20%;
  left: 0;
  right: 0;
}
.title-text {
  font-family: korFont1;
  font-size: 50px;
}
.title-subtext {
  font-family: korFont3;
  font-size: 25px;
  margin-top: 40px;
}
.icon1 {
  margin-top: 50px;
  width: 80px;
}
.qrcode-div {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  margin-top: 40px;
  gap: 10px;
}
.qrcode {
  width: 80px;
}
.qrcode-text {
  font-size: 15px;
  font-family: korFont2;
  line-height: 1.5;
}
</style>
