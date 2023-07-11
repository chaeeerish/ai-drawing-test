<template>
  <div class="prepage">
    <button v-if="isPlaying" @click="toggleSound" class="sound-btn">
      <img class="icon-sound" src="../../assets/images/volumeon.png" />
    </button>
    <button v-else @click="toggleSound" class="sound-btn1">
      <img class="icon-sound1" src="../../assets/images/volumeoff.png" />
    </button>

    <form method="post" class="name-form" @submit.prevent>
      <label class="name-label">시작하기 전, <br />이름을 입력해주세요:</label>
      <input class="name-input" type="text" required v-model="name" />
      <p class="prestart-text">
        이 테스트는 HTP 검사를 기반으로 하였으며 그림에 대한 해석은 전문 심리
        도서를 참고하였습니다. 따라서, 다양한 사람에 대한 포괄적인 해석이므로,
        모두에게 적용되지 않을 수 있습니다. 보다 정확한 해석을 위해서는 임상
        소견의 고려가 필요하므로, 전문적인 상담은 심리 전문가를 찾아주세요.
      </p>
      <div class="text1">
        <p>
          ※ 몰입감 있는 경험을 위해 소리를 높여주세요
          <font-awesome-icon icon="fa-solid fa-volume-high" />
        </p>
      </div>
    </form>
    <div class="prestart-img-box">
      <img class="prestart-image" src="../../assets/images/heart.png" />
    </div>
    <button type="submit" @click="onClickNext" class="next-btn">NEXT</button>
  </div>
</template>

<script>
export default {
  name: "PreStartPage",
  props: ["isPlaying"],
  methods: {
    onClickNext() {
      let name = this.name;
      if (name.length > 50) {
        alert("이름을 50자 이하로 입력해주세요");
      } else {
        if (name.length > 0) {
          if (this.isPlaying === true) {
            this.player.play();
            console.log(name);

            console.log(`환경변수 5000 : ${process.env.VUE_APP_FLASK_PORT}`);

            var file = JSON.stringify({ name: name });

            fetch(process.env.VUE_APP_IP_ADDRESS + process.env.VUE_APP_FLASK_PORT + "/main", {
              method: "POST",
              headers: {
                "Content-Type": "application/json",
              },
              body: file,
            })
              .then((response) => response.json())
              .then((data) => {
                console.log(data);
                this.$cookies.set("userid", data.id);
              });
            this.$emit("ToFirstScene");
          } else {
            console.log(name);
            this.$emit("ToFirstScene");
          }
        } else {
          alert("이름을 입력해주세요");
        }
      }
    },
    toggleSound() {
      this.$emit("toggleSound");
    }, //음소거
  },
  data() {
    return {
      name: "",
      current: {},
      index: 0,

      sounds: [
        {
          title: "MainSound",
          src: require("../../assets/audio/click.mp3"),
        },
      ],
      player: new Audio(),
    };
  },
  created() {
    this.current = this.sounds[this.index];
    this.player.src = this.current.src;
  },
};
</script>

<style>
/* mobile screen */
@media only screen and (max-width: 767px) {
  .prepage {
    background-color: #151515;
    height: calc(var(--vh, 1vh) * 100);
    overflow: hidden;
  }
  .text1 {
    text-align: left;
    display: inline-block;
    font-size: 16px;
    font-family: korFont3;
    margin-top: 30px;
    color: #ddd;
    line-height: 1.5;
  }
  .next-btn {
    font-family: korFont1;
    font-size: 25px;
    position: absolute;
    margin-left: auto;
    margin-right: auto;
    left: 0;
    right: 0;
    text-align: center;
    bottom: 8%;
    background: none;
    color: inherit;
    border: none;
    padding: 0;
    cursor: pointer;
    outline: inherit;
  }
  .sound-btn {
    color: #ffffff;
    border: none;
    padding: 0;
    display: inline-block;
    background: none;
    position: absolute;
    top: 3%;
    right: 5%;
  }
  .sound-btn1 {
    color: #ffffff;
    border: none;
    padding: 0;
    display: inline-block;
    background: none;
    position: absolute;
    top: 2.3%;
    right: 5%;
  }
  .icon-sound1 {
    height: 40px;
    color: #fff;
  }

  .icon-sound {
    height: 30px;
    color: #fff;
  }
  .name-form {
    width: 280px;
    margin: auto;
    background: transparent;
    text-align: left;
    border-radius: 10px;
    display: inline-block;
    margin-top: 50px;
  }
  .name-label {
    color: #fff;
    display: inline-block;
    margin: 25px 0 15px;
    font-size: 0.6em;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: bold;
    font-family: korFont3;
    font-size: 18px;
    line-height: 1.5;
  }
  .name-input {
    display: inline-block;
    padding: 6px 6px;
    width: 100%;
    box-sizing: border-box;
    border: none;
    border-bottom: 1px solid #ddd;
    color: #fafafa;
    font-family: korFont2;
    background: transparent;
    font-size: 20px;
  }
  .prestart-image {
    width: 45px;
    display: inline-block;
    margin-top: 30px;
  }
  .prestart-img-box {
    text-align: center;
    display: block;
  }
  .prestart-text {
    margin-top: 30px;
    font-size: 17px;
    line-height: 2;
    font-family: korFont3;
  }
}
/* for iPads and tabs */
@media only screen and (min-width: 768px) and (max-width: 1400px) {
  .prepage {
    background-color: #151515;
    height: calc(var(--vh, 1vh) * 100);
    overflow: hidden;
  }
  .text1 {
    text-align: left;
    display: inline-block;
    font-size: 25px;
    font-family: korFont3;
    margin-top: 30px;
    color: #ddd;
    line-height: 1.5;
  }
  .next-btn {
    font-family: korFont1;
    font-size: 35px;
    position: absolute;
    margin-left: auto;
    margin-right: auto;
    left: 0;
    right: 0;
    text-align: center;
    bottom: 8%;
    background: none;
    color: inherit;
    border: none;
    padding: 0;
    cursor: pointer;
    outline: inherit;
  }
  .sound-btn {
    color: #ffffff;
    border: none;
    padding: 0;
    display: inline-block;
    background: none;
    position: absolute;
    top: 3%;
    right: 5%;
  }
  .sound-btn1 {
    color: #ffffff;
    border: none;
    padding: 0;
    display: inline-block;
    background: none;
    position: absolute;
    top: 2.3%;
    right: 5%;
  }
  .icon-sound1 {
    height: 70px;
    color: #fff;
  }

  .icon-sound {
    height: 52px;
    color: #fff;
  }
  .name-form {
    width: 500px;
    margin: auto;
    background: transparent;
    text-align: left;
    border-radius: 10px;
    display: inline-block;
    margin-top: 50px;
  }
  .name-label {
    color: #fff;
    display: inline-block;
    margin: 25px 0 15px;
    font-size: 0.6em;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: bold;
    font-family: korFont3;
    font-size: 30px;
    line-height: 1.5;
  }
  .name-input {
    display: inline-block;
    padding: 6px 6px;
    width: 100%;
    box-sizing: border-box;
    border: none;
    border-bottom: 1px solid #ddd;
    color: #fafafa;
    font-family: korFont2;
    background: transparent;
    font-size: 35px;
  }
  .prestart-image {
    width: 75px;
    display: inline-block;
    margin-top: 30px;
  }
  .prestart-img-box {
    text-align: center;
    display: block;
  }
  .prestart-text {
    margin-top: 30px;
    font-size: 30px;
    line-height: 2;
    font-family: korFont3;
  }
}
</style>
