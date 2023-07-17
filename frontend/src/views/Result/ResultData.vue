<template>
  <div class="results-data">
    <div class="results-main-screen">
      <div class="results-top-container">
        <p class="logo-text">내가 그린 그림으로 확인해보는 나의 심리</p>
        <img class="mainLogo" src="../../assets/images/logo1.png" />
      </div>
      <div class="results-main-content">
        <h1 class="userName">&lt;{{ username }}님의 결과&gt;</h1>
        <div class="characterName">
          {{ character_name[character_id] }}
        </div>
        <img
          class="characterImage"
          :src="getImageUrl(character_id)"
          alt="Character Image"
        />
        <p class="character-desc">
          {{ character_desc[character_id] }}
        </p>

        <button class="showDetailBtn" @click="scrollIntoView">
          <img class="nextbtn" src="../../assets/images/next.png" />
        </button>
      </div>
      <div class="results-bottom-container">
        <div
          style="
            display: flex;
            flex-direction: row;
            align-items: center;
            justify-content: center;
            gap: 5px;
          "
        >
          <a target="_blank" href="https://www.instagram.com/ai.drawingtest/" id="instagram-link">
            <img
              class="socialmedia-icons"
              src="../../assets/images/instagram.png"
              alt="인스타그램 프로필 방문 버튼"
            />
          </a>
          <a id="kakaotalk-sharing-btn" href="javascript:;">
            <img
              class="socialmedia-icons"
              src="../../assets/images/kakaotalk.png"
              alt="카카오톡 공유 보내기 버튼"
              @click="kakaoLink"
            />
          </a>

          <img
            class="socialmedia-icons"
            src="../../assets/images/clipboard.png"
            alt="링크 공유 보내기 버튼"
            @click="urlCopy"
          />

          <img
            class="socialmedia-icons"
            src="../../assets/images/capture.png"
            alt="캡쳐 버튼"
            @click="captureScreen"
          />
        </div>
        <p class="copyright-text">©2023 마음스케치 | All rights reserved.</p>
      </div>
    </div>

    <div class="details" :class="{ open: showDetails }" ref="nextSpace">
      <div ref="adContainer1"></div>
      <p class="graph-text">나의 심리 그래프</p>
      <div class="chart-wrapper">
        <canvas id="myChart" :width="300" :height="270"></canvas>
      </div>
      <div class="first-result">
        <h1 class="first-result-title">{{ username }}님의 나무 그림</h1>
        <img width="200" height="300" :src="newData.tree_image" alt="image" />
        <div class="result-texts">
          <div v-for="(treeAttributes, key1) in tree" :key="key1">
            <br />
            <p class="treeAttributes">{{ key1 }}</p>
            <template v-for="(treeFeatures, key2) in treeAttributes">
              <div
                v-if="treeFeatures !== null && treeFeatures !== undefined"
                :key="key2"
              >
                <li class="treefeatures">
                  {{ key2 }}
                </li>
                <p class="treevalues">
                  {{ treeFeatures }}
                </p>
              </div>
            </template>
          </div>
        </div>
      </div>
      <!-- 광고 -->
      <div>
        <iframe
          src="https://ads-partners.coupang.com/widgets.html?id=679296&template=carousel&trackingCode=AF0334851&subId=&width=200&height=140&tsource="
          width="200"
          height="140"
          frameborder="0"
          scrolling="no"
          referrerpolicy="unsafe-url"
        >
        </iframe>
      </div>
      <div class="second-result">
        <h1 class="first-result-title">{{ username }}님의 집 그림</h1>
        <img width="200" height="300" :src="newData.house_image" alt="image" />
        <div class="result-texts">
          <div v-for="(homeAttributes, key1) in home" :key="key1">
            <br />
            <p class="treeAttributes">{{ key1 }}</p>
            <template
              v-for="(homeFeatures, key2) in homeAttributes"
              :key="key2"
            >
              <div
                v-if="homeFeatures !== null && homeFeatures !== undefined"
                :key="key2"
              >
                <li class="treefeatures">
                  {{ key2 }}
                </li>
                <p class="treevalues">
                  {{ homeFeatures }}
                </p>
              </div>
            </template>
          </div>
        </div>
      </div>
    </div>

    <!-- 광고 -->
    <p class="coupang-text">
      이 포스팅은 쿠팡 파트너스 활동의 일환으로, 이에 따른 일정액의 수수료를
      제공받습니다.
    </p>
    <div style="padding-top: 10px">
      <iframe
        src="https://ads-partners.coupang.com/widgets.html?id=679511&template=carousel&trackingCode=AF0334851&subId=&width=200&height=140&tsource="
        width="200"
        height="140"
        frameborder="0"
        scrolling="no"
        referrerpolicy="unsafe-url"
      >
      </iframe>
    </div>
    <!-- 카카오 배너 광고 2 -->
    <div ref="adContainer2"></div>
    <!-- 구글 광고 -->
    <div style="padding-top: 10px">
      <p>이곳에 광고가 표시됩니다.</p>
      <AdsenseComponent></AdsenseComponent>
    </div>



    <div class="footer">
      <img style="width: 60px" src="../../assets/images/icon5.png" />
      <p>광고 및 후원 문의</p>
      <p>yoonyoung.lee1218@gmail.com</p>
    </div>
    <br />
    <!-- <footer class="footer">
      <div class="share-btns">
        <p class="title-text-result">
          <span style="color: #eba090">마음</span>스케치
        </p>
        <div>
          <a id="kakaotalk-sharing-btn" href="javascript:;">
            <img
              src="https://developers.kakao.com/assets/img/about/logos/kakaotalksharing/kakaotalk_sharing_btn_medium.png"
              alt="카카오톡 공유 보내기 버튼"
              class="kakaotalk-btn"
              @click="kakaoLink"
            />
          </a>
          <div class="clipboard-copy">
            <img
              class="clipboard-img"
              @click="urlCopy"
              src="../../assets/images/sharelink.png"
            />
          </div>
        </div>
      </div>
      <p class="result-contact">yoonyoung.lee1218@gmail.com</p>
      <p class="result-copyright">©2023 마음스케치 | All rights reserved.</p>
    </footer> -->
  </div>
</template>

<script>
import Chart from "chart.js/auto";
import html2canvas from "html2canvas";
import AdsenseComponent from "@/AdsenseComponent.vue";
export default {
  name: "ResultData",
  props: ["newData"],
  components: {
    AdsenseComponent,
  },
  data() {
    return {
      character_name: [
        "공격적인 돼지바 프라푸치노",
        "노른자가 두 개 띄워진 쌍화탕",
        "샷 6번 추가한 공격적인 아메리카노",
        "자존감 높은 1리터 쌍화탕",
        "샷 6번 추가한 따뜻한 라떼",
        "혼자 있기 좋아하는 자몽 허니 블랙티",
        "따뜻한 아이스 아메리카노",
        "인정이 필요한 민트 초코 라떼",
        "미지근한 카모마일티",
        "자신감이 넘치는 유니콘 프라푸치노",
        "얼음이 녹아버린 아샷추",
        "톡 쏘는 블루레몬에이드",
        "휘핑 가득 따뜻한 민트초코라떼",
        "펄 추가 아이스아메리카노",
        "행복한 민트초코프라푸치노",
        "혼자가 된 제주 유기농 감귤 주스",
        "거품 뺀 카푸치노",
        "초코쉐이크가 되고싶은 밀크쉐이크",
        "따뜻한 숏라떼",
        "수줍은 복숭아 아이스티",
      ],
      character_desc: [
        "공격적인 돼지바 프라푸치노는 자신감이 넘치고, 어디서나 주목을 받는 타입이야. 누구보다 활기찬 에너지로 가득 차 있어서, 끊임없이 도전하는 모습이 인상적이지. 때로는 과감한 행동으로 주변을 놀라게 하기도 하지만, 웃음을 불러일으키기도 하지!",
        "노른자가 두 개 띄워진 쌍화탕은 예상을 깨는 독특한 매력을 가진 특별한 존재야! 네 보이는는 모습과는 달리, 내면에는 따뜻하고 안정적인 에너지가 넘쳐나. 네 모습은 예측할 수 없으면서도 흥미로워, 주변에 활력과 웃음을 전달하는 멋진 캐릭터야!",
        "샷 6번 추가한 공격적인 아메리카노는 사람들을 매료시키는 재주가 있어! 네 강인한 성향 뒤에는 사회적으로 능숙하게 어울리며 매력을 발휘하는 너의 모습이 있지. 어느 모임에 참여하더라도 주목받고, 즐거운 대화를 이끌어내는 네 모습 정말 멋지고 화려하단다!",
        "자존감 높은 1리터 쌍화탕은 타고난 파워와 자신감을 가진 흥겨운 존재야! 도전을 두려워하지 않고 어디든 뛰어들며 승부욕 넘치는 자세로 인생을 즐기는 너는 진정한 열정과 자신의 가치를 자랑스럽게 표현해. 그런 너의 모습은 주변에 희망과 도약의 불을 불러일으키지!",
        "샷 6번 추가한 따듯한 라떼는 사람들을 잘 배려하면서도 혼자 있는 시간을 소중히 여기는 사람이야. 너의 소중한 내면과 온화한 성격은 주변 사람들에게도 큰 영감을 주는 거 알지? 혼자 있는 시간과 사회적인 활동을 균형 있게 유지해 나가는 거 잊지 마! 항상 응원할게. 화이팅!",
        "혼자 있기를 좋아하는 자몽 허니 블랙티는 혼자만의 시간을 통해 힐링을 즐기는 상큼한 맛을 가지고 있어. 닫혀있는 뚜껑은 타인으로부터 자신을 보호하려고 하는 성격을 표현해. 가끔은 뚜껑을 열고 타인과 교류하며 너의 상큼함과 부드러움을 어필해 보자!",
        "따뜻함과 차가움을 모두 가진 아이스 아메리카노는 평온한 내면과 사회적인 능력도 모두 겸비한 멋진 캐릭터야. 자신만의 시간을 중요시하지만, 그와 더불어 타인을 배려하고 살필 줄 아는 진정한 사회인이지. 늘 잘 해내고 있지만 가끔은 너의 내면도 잊지 않고 살펴보는 게 필요하다는 걸 잊지 않았으면 좋겠어.",
        "안정이 필요한 민트 초코 라떼는 상큼하면서도 달콤한 맛을 가지고 있어서 두터운 매니아층을 형성하고 있어. 하지만 나는 혼자 있는 시간을 통해 힐링을 하고 힘을 얻어 세상을 살아가. 가끔은 편안하게 안정을 취해도 돼!",
        "미지근한 카모마일티는 너무 차갑지도 뜨겁지도 않은 차를 모티브로 하고 있어. 40'C의 먹기 좋은 온도가 마치 너의 온화함을 의미하지. 사람들은 너를 보며 마음이 편안해지고 안정감을 느껴. 네가 힘들 때도 다른 이들에게 희망과 위로를 전해줘서 고마워.",
        "유니콘 프라푸치노는 우울한 순간에도 자신감과 밝은 에너지를 전해주는 캐릭터야. 너의 넘치는 에너지는 화려한 색감의 프라푸치노를 모티브로 하여 그려졌어. 다채로운 색상의 음료가 마치 네가 자신감이 넘치는 사람이라는 것을 의미해!",
        "얼음이 녹아버린 아샷추는 마냥 부정적이지 않아. 어울리지 않을 것 같은 아이스티와 에스프레소의 만남은 네가 다른 사람들과 잘 지내는 성격임을 의미해. 얼음이 녹아버린 독특한 모습을 가지고 있지만, 너의 개성은 사람들에게 큰 인기를 끌고 있어!",
        "톡 쏘는 블루레몬에이드는 약간의 우울함이 있지만 자존감이 높은 캐릭터야. 파란색은 우울함을 의미하지만 에이드의 강한 탄산은 너의 높은 자존감을 의미해. 너의 긍정적인 마인드는 앞으로도 스스로를 사랑하고 받아들이도록 도와줄 거야!",
        "나는 휘핑 가득 올라간 민트 초코 라떼야. 머그잔에 담긴 나는 정말 달콤하고 시원한 맛이지. 사실 나는 많은 사람들과 섞이기는 조금 어려워. 그렇지만 내가 온화한 성격을 가지고 있어서, 나와 함께하면 편안하고 따뜻한 분위기를 느낄 수 있을 거야.",
        "펄 추가 아이스 아메리카노는 사람들이 다소 시도하지 않는 카페 메뉴일지라도, 자신감 넘치는 성격으로 상대방을 매료시킬 수 있어. 나와 함께하면 상대방은 특별함과 독보적인 매력을 가진 존재로 느껴질 거야. 함께 있는 동안, 상대방은 자신을 믿고 세상을 정복할 수 있을 거라고 확신해!",
        "행복한 민트 초코 프라푸치노는 밝은 웃음으로 상대방에게 다가가며, 함께 있는 동안 행복한 분위기를 만들 수 있어. 상대방은 나와 함께하는 시간에 행복을 느끼고, 나랑 어울릴 때 자유로움을 느낄 수 있을 거야. 나와 행복을 전달하면서 함께 특별한 경험을 만들어나가자!",
        "혼자가 된 제주 유기농 감귤 주스는 혼자일 때 편안함과 자유로움을 느끼는 편이지. 친구를 찾는 전단지를 들고 있지만, 외로움을 느끼는 건 아냐. 그건 내가 더 나은 나를 찾고 성장하고자 하는 욕망을 담은 거야. 나는 따뜻한 분위기를 만들어주면서, 상대방에게 높은 자존감을 전달해 줄 거야.",
        "거품 뺀 카푸치노는 자존감은 낮지만 온화하고 친근한 성격의 소유자야. 사람들은 카푸치노처럼 항상 따뜻하고 상냥한 미소를 짓는 너와 대화하며 안정감과 편안함을 느껴. 사람들에게 긍정적인 에너지를 주는 너를 항상 응원해! ",
        "초코 쉐이크가 되고 싶은 밀크 쉐이크는 자신의 부족한 면을 채우기 위해 초코 쉐이크로 변하고자 하는 너의 열망을 의미해. 너만의 독특함을 내세우고 자신의 대한 믿음을 키우면 언젠가 너만의 꿈을 이룰 수 있을 거야!",
        "따듯한 숏라떼는 자존감이 낮을 수 있지만 언제나 미소를 잃지 않는 캐릭터야 . 자존감이 낮다고 해서 행복을 느끼지 못하는 건 아니야. 작은 것들에도 행복을 느끼고 언제나 너 자신을 소중히 여기는 너는 어쩌면 이미 성공한 인생을 살고 있을지 몰라!",
        "수줍은 복숭아 아이스티는 자존감이 낮지만 주변 사람들에게 항상 따뜻한 관심과 도움을 주는 능력을 갖추고 있어. 초면에는 수줍음이 많아 보일 수 있지만 친해지고나면 누구보다 활발하고 즐거운 모습을 보여줄 거야!",
      ],
      username: null,
      tree: null,
      home: null,
      graph: [],
      character_id: null,
    };
  },
  methods: {
    trackInstagramLink() {this.$gtag.event('click', {event_category: 'Social Media', event_label: 'Instagram Link',
      });
    },
    trackKakaoLink() {this.$gtag.event('click', {event_category: 'Social Media', event_label: 'Kakao Link',
      });
    },
    trackCopyUrlButtonClick() {this.$gtag.event('click', {event_category: 'Social Media', event_label: 'Copy Button',
      });
    },
    trackDownloadButtonClick() {this.$gtag.event('click', {event_category: 'Social Media', event_label: 'Download Button',
      });
    },
    captureScreen() {
      const elements = document.getElementsByClassName("results-main-screen");
      const element = elements[0];

      html2canvas(element).then((canvas) => {
        const image = canvas.toDataURL("image/png");
        this.saveToPhotoAlbum(image);
      });
      // gtag 추적
      this.trackDownloadButtonClick();
    },
    saveToPhotoAlbum(imageData) {
      const link = document.createElement("a");
      link.href = imageData;
      link.download = "결과 화면.png";
      link.addEventListener("click", () => {
        alert("결과 화면을 저장합니다.");
      });
      link.click();
    },
    scrollIntoView() {
      this.$refs.nextSpace.scrollIntoView({ behavior: "smooth" });
    },
    // createChart() {
    //   const ctx = document.getElementById("myChart");
    //   const myChart = new Chart(ctx, {
    //     type: "radar",
    //     data: {
    //       labels: [
    //         "온화함 😚",
    //         "자신감 😏",
    //         "행복함 😆",
    //         "사회성 😎 ",
    //         "높은 자존감 😤",
    //       ],
    //       datasets: [
    //         {
    //           label: "수치",
    //           data: this.graph,
    //           backgroundColor: [
    //             // "rgba(255, 99, 132, 0.2)",
    //             // "rgba(54, 162, 235, 0.2)",
    //             // "rgba(255, 206, 86, 0.2)",
    //             // "rgba(75, 192, 192, 0.2)",
    //             // "rgba(153, 102, 255, 0.2)",
    //             "transparent",
    //           ],
    //           borderColor: [
    //             "rgba(255, 99, 132, 1)",
    //             // "rgba(54, 162, 235, 1)",
    //             // "rgba(255, 206, 86, 1)",
    //             // "rgba(75, 192, 192, 1)",
    //             // "rgba(153, 102, 255, 1)",
    //           ],
    //           borderWidth: 2,
    //         },
    //       ],
    //     },
    //     options: {
    //       maintainAspectRatio: false,
    //       layout: {
    //         padding: {
    //           top: 10,
    //           bottom: 10,
    //           left: 10,
    //           right: 10,
    //         },
    //       },
    //       plugins: {
    //         legend: {
    //           display: false, // Hide the legend
    //         },
    //       },
    //       scales: {
    //         r: {
    //           beginAtZero: true,
    //           max: 1,
    //           angleLines: {
    //             display: false,
    //           },
    //           gridLines: {
    //             display: false, // Hide the grid lines inside the pentagon
    //           },
    //           ticks: {
    //             display: false,
    //           },
    //           pointLabels: {
    //             fontSize: 18, // Set the font size for the labels
    //           },
    //         },
    //       },
    //     },
    //   });
    //   myChart;
    // },

    getImageUrl(value) {
      return require(`../../assets/images/${value}.png`);
    },
    kakaoLink() {
      window.Kakao.Share.createDefaultButton({
        container: "#kakaotalk-sharing-btn",
        objectType: "feed",
        content: {
          title: "마음스케치",
          description: "#AI심리검사 #그림심리검사",
          imageUrl: "https://ifh.cc/g/O8dgTT.jpg",
          link: {
            // [내 애플리케이션] > [플랫폼] 에서 등록한 사이트 도메인과 일치해야 함
            mobileWebUrl: "https://developers.kakao.com",
            webUrl: "https://developers.kakao.com",
          },
        },
        social: {
          likeCount: 178,
          commentCount: 45,
          sharedCount: 103,
        },
        buttons: [
          {
            title: "웹으로 보기",
            link: {
              mobileWebUrl: "https://developers.kakao.com",
              webUrl: "https://developers.kakao.com",
            },
          },
        ],
      });
      // gtag 추적
      this.trackKakaoLink();
    },
    urlCopy() {
      this.$copyText("http://ai-drawing-test.com/").then(() => {
        alert("클립보드에 성공적으로 복사되었습니다.");
      });
      // gtag 추적
      this.trackCopyUrlButtonClick();
    },
  },
  created() {
    this.username = this.newData.name;
    this.tree = this.newData.tree_result;
    this.home = this.newData.house_result;
    this.graph = this.newData.graph;
    this.character_id = this.newData.character;
  },
  mounted() {
    const adCode1 = `<ins class="kakao_ad_area" style="display:none;"
                    data-ad-unit="DAN-S0oPQzvHJoKMYkWA"
                    data-ad-width="320"
                    data-ad-height="50"></ins>`;

    const adElement1 = document.createElement('div');
    adElement1.innerHTML = adCode1;

    this.$refs.adContainer1.appendChild(adElement1);

    const adCode2 = `<ins class="kakao_ad_area" style="display:none;"
                    data-ad-unit = "DAN-QXgJxrirtoLIIXR1"
                    data-ad-width = "320"
                    data-ad-height = "100"></ins>`;

    const adElement2 = document.createElement('div');
    adElement2.innerHTML = adCode2;

    this.$refs.adContainer2.appendChild(adElement2);


    const script = document.createElement("script");
    script.src = "//t1.daumcdn.net/kas/static/ba.min.js";
    script.async = true;
    document.head.appendChild(script);
    // 카카오 광고

    // 인스타그램 링크 클릭 수 // gtag 추적
    const instagramLink = document.getElementById('instagram-link');
    if (instagramLink) {
      instagramLink.addEventListener('click', this.trackInstagramLink);
    }



    console.log("Component mounted.");
    const ctx = document.getElementById("myChart");
    const myChart = new Chart(ctx, {
      type: "radar",
      data: {
        labels: [
          "온화함 😚",
          "자신감 😏",
          "행복함 😆",
          "사회성 😎 ",
          "높은 자존감 😤",
        ],
        datasets: [
          {
            label: "수치",
            data: this.graph,
            backgroundColor: [
              // "rgba(255, 99, 132, 0.2)",
              // "rgba(54, 162, 235, 0.2)",
              // "rgba(255, 206, 86, 0.2)",
              // "rgba(75, 192, 192, 0.2)",
              // "rgba(153, 102, 255, 0.2)",
              "transparent",
            ],
            borderColor: [
              "rgba(255, 99, 132, 1)",
              // "rgba(54, 162, 235, 1)",
              // "rgba(255, 206, 86, 1)",
              // "rgba(75, 192, 192, 1)",
              // "rgba(153, 102, 255, 1)",
            ],
            borderWidth: 2,
          },
        ],
      },
      options: {
        responsive: false,
        maintainAspectRatio: false,
        aspectRatio: 1,
        layout: {
          padding: {
            top: 0,
            bottom: 0,
            left: 5,
            right: 12,
          },
        },
        plugins: {
          legend: {
            display: false, // Hide the legend
          },
        },
        scales: {
          r: {
            beginAtZero: true,
            max: 1,
            angleLines: {
              display: false,
            },
            gridLines: {
              display: false, // Hide the grid lines inside the pentagon
            },
            ticks: {
              display: false,
            },
            pointLabels: {
              fontSize: 18, // Set the font size for the labels
            },
          },
        },
      },
    });
    myChart;
  },
};
</script>

<style>
/* Styles for phones */
@media only screen and (max-width: 767px) {
  .results-data {
    margin-top: 0px;
    display: inline-block;
    font-family: korFont2;
    background-color: #ffffff;
    background-position: center center;
    color: black;
    font-family: korFont1;
    width: 100%;
    height: auto !important;
  }
  .results-main-screen {
  }
  .mainLogo {
    width: 250px;
  }
  .results-top-container {
    background-image: url("../../assets/images/paintBackground.png");
    height: calc(var(--vh, 1vh) * 16);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 10px;
  }
  .results-main-content {
    background-color: #fff;
    height: calc(var(--vh, 1vh) * 68);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
  .results-bottom-container {
    background-image: url("../../assets/images/paintBackground.png");
    height: calc(var(--vh, 1vh) * 16);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 15px;
  }
  .nextbtn {
    width: 80px;
  }
  .logo-text {
    color: #fff;
    font-family: korFont3;
    font-size: 20px;
  }
  .socialmedia-icons {
    width: 50px;
  }
  .details {
    background-color: #fff;
  }
  .userName {
    font-size: 21px;
    font-family: korFont3;
    color: #424242;
    margin-top: 20px;
  }
  .character-desc {
    font-family: korFont2;
    font-size: 12.5px;
    width: 300px;
    text-align: left;
    margin-bottom: 20px;
    line-height: 1.5;
  }
  .first-result {
    padding-top: 50px;
    border-bottom: 1px solid #ccc;
  }
  .copyright-text {
    font-family: korFont2;
    font-size: 15px;
    color: #fff;
  }

  .first-result-title {
    font-size: 20px;
    margin-top: 20px;
    margin-bottom: 10px;
    font-family: korFont3;
    color: #0000008a;
  }
  .first-image {
    margin-top: 25px;
    width: 250px;
  }
  .first-result-text {
    width: 80%;
    margin: 50px auto;
  }
  .result-texts {
    text-align: left;
    font-family: korFont2;
    width: 80%;
    display: inline-block;
    padding-bottom: 20px;
  }
  .treeAttributes {
    font-weight: 1000;
    font-size: 22px;
    padding-bottom: 22px;
  }
  .treefeatures {
    font-size: 18px;
    padding-bottom: 13px;
  }
  .treevalues {
    font-size: 15px;
    padding-bottom: 15px;
    line-height: 1.8;
  }
  .share-btn {
    font-family: korFont2;
    padding-bottom: 10px;
    font-size: 20px;
    background-color: #fdd5cc;
    color: black;
    padding: 10px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 17px;
    font-weight: 1000;
    cursor: pointer;
    border-radius: 15px;
  }
  .share-btns {
    padding-bottom: 10px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    gap: 15px;
  }
  .kakaotalk-btn {
    height: 30px;
  }
  .copylink-btn {
    height: 30px;
  }
  .clipboard-copy {
    display: inline-block;
    padding-left: 5px;
  }
  .clipboard-img {
    width: 30px;
  }
  .characterImage {
    width: 140px;
    display: block;
    margin-left: auto;
    margin-right: auto;
    padding-top: 30px;
    padding-bottom: 30px;
  }
  #myChart {
    width: 160px;
    height: 160px;
    display: block;
    box-sizing: content-box;
  }
  .showDetailBtn {
    background-color: transparent;
    color: #ffffff;
    border: none;
    cursor: pointer;
    margin-bottom: 35px;
    font-family: korFont2;
    -webkit-tap-highlight-color: transparent !important;
  }
  .characterName {
    font-size: 17px;
    font-family: korFont2;
    font-weight: 1000;
    padding-top: 20px;
    padding-bottom: 0px;
    border-radius: 10px;
    display: inline-block;
    max-width: 340px;
    word-wrap: break-word;
    color: #2f2f2f;
  }
  .title-text-result {
    font-family: korFont1;
    font-size: 29px;
  }
  .result-contact {
    font-family: korFont2;
  }
  .result-copyright {
    font-family: korFont2;
    margin-top: 8px;
  }
  .second-result {
    margin-bottom: 100px;
  }
  .shareBtn {
    background-color: #e4e4e4;
    padding: 7px 14px;
    color: #4d4d4d;
    border: 1px solid #484848;
    cursor: pointer;
    border-radius: 20px;
    font-family: korFont2;
    font-size: 14px;
    font-weight: 1000;
  }
  .footer {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 13px;
    font-family: korFont2;
    font-size: 13px;
    color: #48484885;
  }
  iframe {
    width: 100%;
  }
  .coupang-text {
    font-size: 8px;
    text-align: center;
    color: gray;
    margin: 0;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .graph-text {
    padding-top: 30px;
    font-size: 20px;
    font-family: korFont2;
    font-weight: 600;
  }
  .chart-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .graph-text{
    padding-top: 30px;
    padding-bottom: 15px;
    font-family: korFont2;
    font-weight: 600;
  }
  .chart-wrapper{
    display: flex;
    justify-content: center;
    align-items: center;
  }
}

/* Styles for iPads */
@media only screen and (min-width: 768px) and (max-width: 1400px) {
  .results-data {
    margin-top: 0px;
    display: inline-block;
    font-family: korFont2;
    background-color: #ffffff;
    background-position: center center;
    color: black;
    font-family: korFont1;
    width: 100%;
    height: auto !important;
  }
  .results-main-screen {
  }
  .mainLogo {
    width: 400px;
  }
  .results-top-container {
    background-image: url("../../assets/images/paintBackground.png");
    height: calc(var(--vh, 1vh) * 16);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 10px;
  }
  .results-main-content {
    background-color: #fff;
    height: calc(var(--vh, 1vh) * 68);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
  .results-bottom-container {
    background-image: url("../../assets/images/paintBackground.png");
    height: calc(var(--vh, 1vh) * 16);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 20px;
  }
  .logo-text {
    color: #fff;
    font-family: korFont3;
    font-size: 28px;
  }
  .socialmedia-icons {
    width: 70px;
  }
  .details {
    background-color: #fff;
  }
  .userName {
    font-size: 30px;
    font-family: korFont3;
    color: #424242;
    margin-top: 20px;
  }
  .character-desc {
    font-family: korFont2;
    font-size: 23px;
    width: 550px;
    text-align: left;
    margin-bottom: 20px;
    line-height: 1.6;
  }
  .first-result {
    padding-top: 50px;
    border-bottom: 1px solid #ccc;
  }
  .copyright-text {
    font-family: korFont2;
    font-size: 22px;
    color: #fff;
  }
  .nextbtn {
    width: 120px;
  }

  .first-result-title {
    font-size: 20px;
    margin-top: 20px;
    margin-bottom: 10px;
    font-family: korFont3;
    color: #0000008a;
  }
  .first-image {
    margin-top: 25px;
    width: 250px;
  }
  .first-result-text {
    width: 80%;
    margin: 50px auto;
  }
  .result-texts {
    text-align: left;
    font-family: korFont2;
    width: 80%;
    display: inline-block;
    padding-bottom: 20px;
  }
  .treeAttributes {
    font-weight: 1000;
    font-size: 22px;
    padding-bottom: 22px;
  }
  .treefeatures {
    font-size: 18px;
    padding-bottom: 13px;
  }
  .treevalues {
    font-size: 15px;
    padding-bottom: 15px;
    line-height: 1.8;
  }
  .share-btn {
    font-family: korFont2;
    padding-bottom: 10px;
    font-size: 20px;
    background-color: #fdd5cc;
    color: black;
    padding: 10px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 17px;
    font-weight: 1000;
    cursor: pointer;
    border-radius: 15px;
  }
  .share-btns {
    padding-bottom: 10px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    gap: 15px;
  }
  .kakaotalk-btn {
    height: 30px;
  }
  .copylink-btn {
    height: 30px;
  }
  .clipboard-copy {
    display: inline-block;
    padding-left: 5px;
  }
  .clipboard-img {
    width: 30px;
  }
  .characterImage {
    width: 310px;
    display: block;
    margin-left: auto;
    margin-right: auto;
    padding-top: 20px;
    padding-bottom: 30px;
  }
  #myChart {
    width: 160px;
    height: 160px;
    display: block;
    box-sizing: content-box;
  }
  .showDetailBtn {
    background-color: transparent;
    color: #ffffff;
    border: none;
    cursor: pointer;
    margin-bottom: 35px;
    font-family: korFont2;
    -webkit-tap-highlight-color: transparent !important;
  }
  .characterName {
    font-size: 27px;
    font-family: korFont2;
    font-weight: 1000;
    padding-top: 30px;
    padding-bottom: 0px;
    border-radius: 10px;
    display: inline-block;
    max-width: 340px;
    word-wrap: break-word;
    color: #2f2f2f;
  }
  .title-text-result {
    font-family: korFont1;
    font-size: 29px;
  }
  .result-contact {
    font-family: korFont2;
  }
  .result-copyright {
    font-family: korFont2;
    margin-top: 8px;
  }
  .second-result {
    margin-bottom: 100px;
  }
  .shareBtn {
    background-color: #e4e4e4;
    padding: 7px 14px;
    color: #4d4d4d;
    border: 1px solid #484848;
    cursor: pointer;
    border-radius: 20px;
    font-family: korFont2;
    font-size: 14px;
    font-weight: 1000;
  }
  .footer {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 13px;
    font-family: korFont2;
    font-size: 13px;
    color: #48484885;
  }
  iframe {
    width: 100%;
  }
  .coupang-text {
    font-size: 8px;
    text-align: center;
    color: gray;
    margin: 0;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .graph-text {
    padding-top: 30px;
    font-size: 20px;
    font-family: korFont2;
    font-weight: 600;
  }
  .chart-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .graph-text{
    padding-top: 30px;
    padding-bottom: 15px;
    font-family: korFont2;
    font-weight: 600;
  }
}
</style>
