<template>
  <transition name="first">
    <div class="painting-page">
      <p class="sub-text-paint">※ 나무를 그려주세요!</p>
      <div class="painting-content">
        <div id="canvas_Wrapper">
          <canvas ref="jsCanvas" id="jsCanvas" class="canvas"></canvas>
        </div>
        <div class="controls">
          <div class="controls-container">
            <div class="controls__range">
              <input
                class="range-btn"
                type="range"
                id="jsRange"
                min="0.1"
                max="5"
                step="0.1"
                v-model="size"
              />
            </div>
            <div class="controls__btns">
              <img
                class="eraser"
                id="eraser"
                @click="handleEraserClick"
                src="../../assets/images/paintEraser.png"
                style="color: #fff"
              />
              <button
                type="button"
                class="reset-btn"
                id="jsReset"
                @click="resetCanvas"
              >
                <img class="reset-icon" src="../../assets/images/reset.png" />
              </button>
              <button
                v-if="isPlaying"
                @click="$emit('toggleSound1')"
                class="sound-btn1"
              >
                <img
                  class="icon-sound1"
                  src="../../assets/images/volumeon.png"
                />
              </button>
              <button v-else @click="$emit('toggleSound1')" class="sound-btn1">
                <img
                  class="icon-sound2"
                  src="../../assets/images/volumeoff.png"
                />
              </button>
            </div>
          </div>
          <div class="colors-container">
            <div class="controls__colors" id="jsColors" ref="jsColors">
              <img
                class="controls__color jsColor"
                @click="handleColorClick"
                src="../../assets/images/paintBlack.png"
                style="color: #3c3c3c"
              />

              <img
                class="controls__color jsColor"
                @click="handleColorClick"
                src="../../assets/images/paintRed.png"
                style="color: #ff3b30"
              />
              <img
                class="controls__color jsColor"
                @click="handleColorClick"
                src="../../assets/images/paintOrange.png"
                style="color: #ff9500"
              />
              <img
                class="controls__color jsColor"
                @click="handleColorClick"
                src="../../assets/images/paintYellow.png"
                style="color: #ffcc00"
              />
              <img
                class="controls__color jsColor"
                @click="handleColorClick"
                src="../../assets/images/paintGreen.png"
                style="color: #4cd963"
              />
              <img
                class="controls__color jsColor"
                @click="handleColorClick"
                src="../../assets/images/paintBlue2.png"
                style="color: #5ac8fa"
              />
              <img
                class="controls__color jsColor"
                @click="handleColorClick"
                src="../../assets/images/paintBlue.png"
                style="color: #0579ff"
              />
              <img
                class="controls__color jsColor"
                @click="handleColorClick"
                src="../../assets/images/paintPurple.png"
                style="color: #5856d6"
              />
              <img
                class="controls__color jsColor"
                @click="handleColorClick"
                src="../../assets/images/paintBrown.png"
                style="color: #884d1d"
              />
            </div>
          </div>
        </div>
      </div>
      <img
        src="../../assets/images/next.png"
        class="painting-next"
        @click="toggleModal"
      />
    </div>
  </transition>
  <transition name="zoom">
    <div v-show="showModal" class="overlay">
      <div v-show="showModal" class="modal-container">
        <div class="modal-content">
          <p>
            그림을 이대로 <br />
            제출하시겠습니까?
          </p>
        </div>
        <div class="modal-btn-grid">
          <button @click="toggleModal" class="modal-btn left">취소</button>
          <button @click="onClickSecond" class="modal-btn">확인</button>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: "PaintingPageFirst",
  components: {},
  props: ["isPlaying"],
  data() {
    return {
      ctx: null,
      painting: false,
      size: 2.5,
      color: "#2c2c2c",
      showModal: false,
      device: null,
      mode: null,
    };
  },
  methods: {
    toggleModal() {
      this.showModal = !this.showModal;
    }, //확인 모달 창
    onClickSecond() {
      this.$emit("turnOffSound");

      var canvasContents = this.$refs.jsCanvas.toDataURL();
      var cookie_userid = this.$cookies.get("userid");
      var file = JSON.stringify({
        image: canvasContents,
        id: cookie_userid,
      });
      fetch(process.env.VUE_APP_IP_ADDRESS + process.env.VUE_APP_FLASK_PORT + "/tree", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: file,
      })
        .then((response) => response.json())
        .then((data) => console.log(data));

      this.$emit("ToSecondScene");
    }, //클릭시 다음 페이지로 넘어가는 버튼
    onMouseMove(event) {
      const x = event.offsetX;
      const y = event.offsetY;

      if (!this.painting) {
        this.ctx.beginPath();
        this.ctx.moveTo(x, y);
      } else {
        this.ctx.lineTo(x, y); // lineTo는 path의 이전 위치에서 지금 위치까지 선을 만드는 것
        this.ctx.stroke();
      }
    },
    onMouseDown() {
      this.painting = true;
    },
    onMouseUp() {
      this.painting = false;
    },
    stopPainting() {
      this.painting = false;
    },
    checkMobile() {
      if (
        /iP(hone|od)|Android.*Mobile|BlackBerry|IEMobile|NetFront|Silk-Accelerated|(hpw|web)OS|Fennec|Minimo|Opera M(obi|ini)|Blazer|Dolfin|Dolphin|Skyfire|Zune|Lumia/g.test(
          navigator.userAgent
        )
      ) {
        this.device = "mobile";
      } else {
        this.device = "etc";
      }
    },
    resetCanvas() {
      this.ctx = this.$refs.jsCanvas.getContext("2d");
      this.ctx.clearRect(0, 0, 700, 700);
      this.ctx.fillStyle = "white";
      this.ctx.fillRect(0, 0, 700, 700);
    },
    getTouchPos(e) {
      return {
        x: e.targetTouches[0].clientX - e.target.offsetLeft,
        y:
          e.targetTouches[0].clientY -
          e.target.offsetTop +
          document.documentElement.scrollTop,
      };
    },
    touchStart(e) {
      e.preventDefault();
      this.painting = true;
      const { x, y } = this.getTouchPos(e);
      this.startX = x;
      this.startY = y;
    },
    touchMove(e) {
      if (!this.painting) return;
      if (this.mode === "eraser") {
        this.ctx.beginPath();
        const { x, y } = this.getTouchPos(e);
        this.startX = x;
        this.startY = y;
        this.ctx.arc(this.startX, this.startY, 40 / 2, 0, 2 * Math.PI);
        this.ctx.fillStyle = this.ctx.strokeStyle;
        this.ctx.fill();
        // 사각형으로 지우기
        // const { x, y } = this.getTouchPos(e);
        // this.ctx.lineTo(x, y);
        // this.ctx.stroke();
        // this.ctx.clearRect(x-10, y-10, 20, 20);
      } else {
        const { x, y } = this.getTouchPos(e);
        this.ctx.lineTo(x, y);
        this.ctx.stroke();
        this.startX = x;
        this.startY = y;
      }
    },
    touchEnd(e) {
      if (!this.painting) return;
      this.ctx.beginPath();
      const { x, y } = this.getTouchPos(e);
      this.startX = x;
      this.startY = y;
      this.ctx.arc(
        this.startX,
        this.startY,
        this.ctx.lineWidth / 2,
        0,
        2 * Math.PI
      );
      this.ctx.fillStyle = this.ctx.strokeStyle;
      this.ctx.fill();
      this.painting = false;
    },
    handleColorClick(e) {
      this.mode = "draw";
      this.color = e.target.style.color;
      this.ctx.strokeStyle = this.color;
    },
    handleEraserClick(e) {
      this.mode = "eraser";
      this.color = e.target.style.color;
      this.ctx.strokeStyle = this.color;
    },
  },

  mounted() {
    this.checkMobile();
    // this.ctx = this.$refs.jsCanvas.getContext("2d");
    // this.ctx.fillStyle = "white";
    // this.ctx.fillRect(0, 0, 700, 700);

    // this.ctx.strokeStyle = "#2c2c2c";
    // this.ctx.fillStyle = "#2c2c2c";
    // this.ctx.lineWidth = 2.5;

    // this.$refs.jsCanvas.addEventListener("mousemove", this.onMouseMove);
    // this.$refs.jsCanvas.addEventListener("mousedown", this.onMouseDown);
    // this.$refs.jsCanvas.addEventListener("mouseup", this.onMouseUp);

    if (this.device === "mobile") {
      // 모바일 버전
      this.$refs.jsCanvas.width = 310;
      this.$refs.jsCanvas.height = 465.3;

      this.ctx = this.$refs.jsCanvas.getContext("2d");
      this.ctx.fillStyle = "white";
      this.ctx.fillRect(0, 0, 700, 700);

      this.ctx.strokeStyle = "#2c2c2c";
      this.ctx.fillStyle = "#2c2c2c";
      this.ctx.lineWidth = 2.5;

      this.$refs.jsCanvas.addEventListener("touchmove", this.touchMove, false);
      this.$refs.jsCanvas.addEventListener(
        "touchstart",
        this.touchStart,
        false
      );
      this.$refs.jsCanvas.addEventListener("touchend", this.touchEnd, false);
    } else {
      this.$refs.jsCanvas.width = 700;
      this.$refs.jsCanvas.height = 700;

      this.ctx = this.$refs.jsCanvas.getContext("2d");
      this.ctx.fillStyle = "white";
      this.ctx.fillRect(0, 0, 700, 700);

      this.ctx.strokeStyle = "#2c2c2c";
      this.ctx.fillStyle = "#2c2c2c";
      this.ctx.lineWidth = 2.5;

      this.$refs.jsCanvas.addEventListener("mousemove", this.onMouseMove);
      this.$refs.jsCanvas.addEventListener("mousedown", this.onMouseDown);
      this.$refs.jsCanvas.addEventListener("mouseup", this.onMouseUp);

      //아이패드는 크기는 크지만 모바일취급이 되어서, PC로 분류 하게끔 그냥 바꿨습니다.
      this.$refs.jsCanvas.addEventListener("touchmove", this.touchMove, false);
      this.$refs.jsCanvas.addEventListener(
        "touchstart",
        this.touchStart,
        false
      );
      this.$refs.jsCanvas.addEventListener("touchend", this.touchEnd, false);
    }
  },

  // size 변경을 감지하면 양방향 데이터 바인딩을 통해 사이즈 변경 값으로 선 굵기 변경
  watch: {
    size() {
      this.ctx.lineWidth = this.size;
    },
    color() {
      this.ctx.strokeStyle = this.color;
    },
  },
};
</script>
<style scoped>
/* http://meyerweb.com/eric/tools/css/reset/
   v2.0 | 20110126
   License: none (public domain)
*/
/*
    브라우저마다 기존 값들이 달라서 내가 만든 화면과 다른 화면이 만들어질 수 있어서
    설정값들을 전부 초기화 하는 것 같음.
 */
html,
body,
div,
span,
applet,
object,
iframe,
h1,
h2,
h3,
h4,
h5,
h6,
p,
blockquote,
pre,
a,
abbr,
acronym,
address,
big,
cite,
code,
del,
dfn,
em,
img,
ins,
kbd,
q,
s,
samp,
small,
strike,
strong,
sub,
sup,
tt,
var,
b,
u,
i,
center,
dl,
dt,
dd,
ol,
ul,
li,
fieldset,
form,
label,
legend,
table,
caption,
tbody,
tfoot,
thead,
tr,
th,
td,
article,
aside,
canvas,
details,
embed,
figure,
figcaption,
footer,
header,
hgroup,
menu,
nav,
output,
ruby,
section,
summary,
time,
mark,
audio,
video {
  margin: 0;
  padding: 0;
  border: 0;
  font-size: 100%;
  font: inherit;
  vertical-align: baseline;
}
/* HTML5 display-role reset for older browsers */
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
menu,
nav,
section {
  display: block;
}
body {
  line-height: 1;
}
ol,
ul {
  list-style: none;
}
blockquote,
q {
  quotes: none;
}
blockquote:before,
blockquote:after,
q:before,
q:after {
  content: "";
  content: none;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
body {
  background-color: #f6f9fc;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 50px 0px;
}
.painting-page {
  height: calc(var(--vh, 1vh) * 100);
  position: relative;
  background-image: url("../../assets/images/paintBackground.png");
  overflow: hidden;
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
}
.painting-content {
  padding-top: 30px;
}
.canvas {
  width: 700px;
  height: 700px;
  background-color: white;
  border-radius: 15px;
  box-shadow: 0 4px 6px rgba(50, 50, 93, 0.11), 0 1px 3px rgba(0, 0, 0, 0.08);
}

.controls {
  margin-top: 80px;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.controls-container {
  position: relative;
  width: 310px;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
}

.controls .controls__colors {
  display: flex;
}

.controls__colors .controls__color {
  width: 50px;
  height: 50px;
  border-radius: 25px;
  cursor: pointer;
}
.controls__btns {
  position: relative;
  margin-top: -10px;
  right: -40px;
}
.range-btn {
  position: relative;
  left: 0;
  margin-top: 15px;
}
.colors-container {
  position: relative;
}
.controls__colors {
  margin-top: 8px;
}
.controls__btns button {
  all: unset;
  cursor: pointer;
  text-align: center;
  padding-left: 10px;
}

.controls__btns button:active {
  transform: scale(0.98);
}

html {
  cursor: url("../../assets/images/cursor.png") 0 32, auto;
}
.sound-btn1 {
  color: #ffffff;
  border: none;
  padding: 0;
  display: inline-block;
  background: none;
  margin-top: -10px;
  padding-left: 5px;
}
.icon-sound1 {
  height: 40px;
  color: #fff;
  margin-top: 10px;
}
.icon-sound2 {
  height: 50px;
  color: #fff;
}
.painting-next {
  cursor: pointer;
  outline: inherit;
  height: 45px;
  margin-top: 10px;
}
.reset-btn {
  border: none;
  padding: 0;
  margin: 0;
  display: inline-block;
  background: transparent;
}
.reset-icon {
  color: #ffffff;
  height: 30px;
}
.overlay {
  position: fixed; /* Positioning and size */
  top: 0;
  left: 0;
  width: 100vw;
  height: 100%;
}
.modal-container {
  display: inline-block;
  position: fixed;
  width: 220px;
  background-color: #fff;
  border-radius: 10px;
  text-align: center;
  color: #000;
  font-family: korFont2;
  top: 40%;
  left: 0;
  right: 0;
  margin-left: auto;
  margin-right: auto;
  -webkit-box-shadow: 0 3px 7px rgba(0, 0, 0, 0.3);
  -moz-box-shadow: 0 3px 7px rgba(0, 0, 0, 0.3);
  box-shadow: 0 3px 7px rgba(0, 0, 0, 0.3);
  border-radius: 10px;
  border: 1px solid rgba(0, 0, 0, 0.3);
}
.modal-container p {
  margin: 20px;
}
.modal-content {
  border-bottom: 1px solid #d0d0d0;
  line-height: 1.5;
}
.modal-btn-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  overflow: hidden;
}
.modal-btn {
  border-radius: 0 0 10px 0;
  color: #333333;
  background-color: #fff;
  border: 0;
  font-size: 1rem;
  cursor: pointer;
  outline: none;
  min-height: 45px;
}
.modal-btn.left {
  border-radius: 0 0 0 10px;
  border-right: 1px solid #d0d0d0;
}

.results-data {
  height: calc(var(--vh, 1vh) * 100);
}

.zoom-enter-active,
.zoom-leave-active {
  animation-duration: 0.21s;
  animation-fill-mode: both;
  animation-name: zoom;
}
.zoom-leave-active {
  animation-direction: reverse;
}
@keyframes zoom {
  from {
    opacity: 0;
    transform: scale3d(1.1, 1.1, 1.1);
  }
  100% {
    opacity: 1;
    transform: scale3d(1, 1, 1);
  }
}
.sub-text-paint {
  color: rgba(100, 100, 100, 0.585);
  position: absolute;
  left: 9px;
  top: 4.5px;
  font-family: korFont1;
  font-size: 13px;
}
/* 핸드폰 사이즈*/
@media screen and (max-width: 767px) {
  body {
    align-items: center;
    background-color: #333333;
  }
  .canvas {
    width: 310px;
    height: 465.3px;
  }
  .controls {
    margin-top: 10px;
  }

  .controls__colors .controls__color {
    width: 36px;
    height: 40px;
    border-radius: 0px;
  }
}
</style>
