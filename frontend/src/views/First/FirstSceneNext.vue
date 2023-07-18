<template>
  <transition name="first">
    <div v-if="firstNext1" class="first-scene">
      <button v-if="isPlaying" @click="$emit('toggleSound')" class="sound-btn">
        <img class="icon-sound" src="../../assets/images/volumeon.png" />
      </button>
      <button v-else @click="$emit('toggleSound')" class="sound-btn1">
        <img class="icon-sound1" src="../../assets/images/volumeoff.png" />
      </button>
      <div class="first-text">
        <transition name="fade">
          <p class="texts" v-if="timedTrigger1.Trigger5">
            상상 속에서 당신은<br />
            길을 걷고 있습니다.
          </p>
        </transition>
        <transition name="fade">
          <p class="texts" v-if="timedTrigger1.Trigger6">
            길을 걷다가 저 멀리 <br />
            희미하게 나무가 보입니다.
          </p>
        </transition>
        <transition name="fade">
          <p class="texts" v-if="timedTrigger1.Trigger7">
            상상 속 당신의 <br />
            나무를 그려주세요.
          </p>
        </transition>
      </div>
      <transition name="fade">
        <img
          v-if="timedTrigger1.Trigger8"
          @click="moveToFirstPaint"
          class="touch-screen"
          src="../../assets/images/next.png"
        />
      </transition>
    </div>
  </transition>
  <PaintingPageFirst
    v-if="firstPaint"
    v-bind:isPlaying="isPlaying"
    @toggleSound1="toggleSound"
    @turnOffSound="turnOffSound"
    @ToSecondScene="ToSecondScene"
  ></PaintingPageFirst>
</template>

<script>
import { ref } from "vue";
import PaintingPageFirst from "./PaintingPageFirst.vue";

export default {
  name: "FirstSceneNext",
  components: { PaintingPageFirst },
  props: ["isPlaying"],
  methods: {
    ToSecondScene() {
      this.$emit("ToSecondScene");
    },
    toggleSound() {
      this.$emit("toggleSound");
    },
    moveToFirstPaint() {
      this.firstNext1 = false;
      this.firstPaint = true;
    },
    turnOffSound() {
      this.$emit("turnOffSound");
    },
  },
  setup() {
    const timedTrigger1 = ref({
      Trigger5: false,
      Trigger6: false,
      Trigger7: false,
      Trigger8: false,
    });
    setTimeout(() => {
      timedTrigger1.value.Trigger5 = true;
    }, 2000);
    setTimeout(() => {
      timedTrigger1.value.Trigger6 = true;
    }, 4000);
    setTimeout(() => {
      timedTrigger1.value.Trigger7 = true;
    }, 6000);
    setTimeout(() => {
      timedTrigger1.value.Trigger8 = true;
    }, 7000);
    return { timedTrigger1 };
  },
  data() {
    return { firstNext1: true, firstPaint: false };
  },
};
</script>

<style>
/*
.first-scene-next {

}
*/
.touch-screen-two {
  height: 100vh;
  background-color: white;
  margin-top: -305px;
  opacity: 30%;
}
</style>
