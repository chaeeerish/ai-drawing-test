<template>
  <transition name="first">
    <div v-if="secondNext1" class="second-scene">
      <button v-if="isPlaying" @click="$emit('toggleSound')" class="sound-btn">
        <img class="icon-sound" src="../../assets/images/volumeon.png" />
      </button>
      <button v-else @click="$emit('toggleSound')" class="sound-btn1">
        <img class="icon-sound1" src="../../assets/images/volumeoff.png" />
      </button>
      <div class="second-text">
        <transition name="fade">
          <p class="texts" v-if="timedTrigger1.Trigger5">
            길을 계속 걷다 보니 <br />어느새 길의 끝이 보입니다.
          </p>
        </transition>
        <transition name="fade">
          <p class="texts" v-if="timedTrigger1.Trigger6">
            길 끝에는 희미하게 집이 보입니다.
          </p>
        </transition>
        <transition name="fade">
          <p class="texts" v-if="timedTrigger1.Trigger7">
            상상 속 당신의 집을 그려주세요.
          </p>
        </transition>
      </div>

      <transition name="fade">
        <img
          v-if="timedTrigger1.Trigger8"
          @click="moveToSecondPaint"
          class="touch-screen"
          src="../../assets/images/next.png"
        />
      </transition>
    </div>
  </transition>

  <PaintingPageSecond
    v-if="secondPaint"
    v-bind:isPlaying="isPlaying"
    @toggleSound1="toggleSound"
    @turnOffSound="turnOffSound"
  ></PaintingPageSecond>
</template>

<script>
import { ref } from "vue";
import PaintingPageSecond from "./PaintingPageSecond.vue";
export default {
  name: "SecondSceneNext",
  components: { PaintingPageSecond },
  props: ["isPlaying"],
  methods: {
    moveToSecondPaint() {
      this.secondNext1 = false;
      this.secondPaint = true;
    },
    toggleSound() {
      this.$emit("toggleSound");
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
    return { secondNext1: true, secondPaint: false };
  },
};
</script>

<style></style>
