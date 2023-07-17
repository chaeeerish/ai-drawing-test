import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import VueCookies from "vue-cookies";
import VueClipboard from "vue-clipboard2";
import VueGtag from 'vue-gtag'
import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import {
  faVolumeHigh,
  faMusic,
  faRotateRight,
  faLink,
} from "@fortawesome/free-solid-svg-icons";
library.add(faVolumeHigh, faMusic, faRotateRight, faLink);

// 여기가 맞나?
VueClipboard.config.autoSetContainer = true;

createApp(App)
  //쿠키를 사용한다.
  .use(VueCookies)
  .use(router)
  .use(VueClipboard)
  .component("font-awesome-icon", FontAwesomeIcon)
  .use(VueGtag, {
    config: {
        id: 'G-S219B0NVWC'  // Google Analytics의 Tracking ID
    }})
  .mount("#app");

//쿠키를 사용한다.
// App.use(VueCookies);
// //쿠키의 만료일은 7일이다. (글로벌 세팅)
// App.$cookies.config("7d");
