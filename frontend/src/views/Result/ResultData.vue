<template>
  <div class="results-data">
    <img src="../../assets/images/paintSpring.png" class="paintSpring" />
    <div class="results-main-screen">
      <h1 class="userName">&lt;{{ username }}님의 결과&gt;</h1>
      <div class="characterName">
        {{ character_name[character_id] }}
      </div>
      <div>
        <img
          class="characterImage"
          :src="getImageUrl(character_id)"
          alt="Character Image"
        />
      </div>

      <!-- <img class="paint-spring" src="../../assets/images/paintSpring.png" /> -->
      <button class="showDetailBtn" @click="showDetail">상세보기</button>
    </div>

    <transition name="fade" @after-enter="createChart">
      <div v-if="showResults" class="details" :class="{ open: showDetails }">
        <div>
          <canvas id="myChart" :width="14" :height="14"></canvas>
        </div>
        <div class="first-result">
          <div>
            <canvas id="myChart" :width="14" :height="14"></canvas>
          </div>
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
        <div style="padding-top: 10px">
          <iframe src="https://ads-partners.coupang.com/widgets.html?id=679296&template=carousel&trackingCode=AF0334851&subId=&width=680&height=140&tsource=" width="390" height="140" frameborder="0" scrolling="no" referrerpolicy="unsafe-url"></iframe>
        </div>
        <div class="second-result">
          <h1 class="first-result-title">{{ username }}님의 집 그림</h1>
          <img
            width="200"
            height="300"
            :src="newData.house_image"
            alt="image"
          />
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
    </transition>

    <!-- 광고 -->
    <div style="padding-top: 10px">
      <iframe src="https://ads-partners.coupang.com/widgets.html?id=679309&template=carousel&trackingCode=AF0334851&subId=&width=390&height=140&tsource=" width="390" height="140" frameborder="0" scrolling="no" referrerpolicy="unsafe-url"></iframe>
    </div>

    <!-- 광고 -->
    <div style="padding-top: 10px">
      <p>이곳에 광고가 표시됩니다.</p>
      <AdsenseComponent></AdsenseComponent>
    </div>



    <br />
    <footer class="footer">
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

        <!-- <button class="shareBtn" @click="urlCopy">링크복사</button> -->
      </div>
      <p class="result-contact">yoonyoung.lee1218@gmail.com</p>
      <p class="result-copyright">©2023 마음스케치 | All rights reserved.</p>
    </footer>
  </div>
</template>

<script>
import Chart from "chart.js/auto";
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
      username: null,
      tree: null,
      home: null,
      graph: [],
      character_id: null,
      showResults: false,
    };
  },
  methods: {
    createChart(){
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
        maintainAspectRatio: false,
        layout: {
          padding: {
            top: 10,
            bottom: 10,
            left: 10,
            right: 10,
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
    myChart
    },
    showDetail() {
      this.showResults = !this.showResults;
    },
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
    },
    urlCopy() {
      this.$copyText("http://ai-drawing-test.com/").then(() => {
        alert("클립보드에 성공적으로 복사되었습니다.");
      });
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
    const script = document.createElement("script");
    script.src = "//t1.daumcdn.net/kas/static/ba.min.js";
    script.async = true;
    document.head.appendChild(script);

    console.log("Component mounted.");
    // const ctx = document.getElementById("myChart");
    // const myChart = new Chart(ctx, {
    //   type: "radar",
    //   data: {
    //     labels: [
    //       "온화함 😚",
    //       "자신감 😏",
    //       "행복함 😆",
    //       "사회성 😎 ",
    //       "높은 자존감 😤",
    //     ],
    //     datasets: [
    //       {
    //         label: "수치",
    //         data: this.graph,
    //         backgroundColor: [
    //           // "rgba(255, 99, 132, 0.2)",
    //           // "rgba(54, 162, 235, 0.2)",
    //           // "rgba(255, 206, 86, 0.2)",
    //           // "rgba(75, 192, 192, 0.2)",
    //           // "rgba(153, 102, 255, 0.2)",
    //           "transparent",
    //         ],
    //         borderColor: [
    //           "rgba(255, 99, 132, 1)",
    //           // "rgba(54, 162, 235, 1)",
    //           // "rgba(255, 206, 86, 1)",
    //           // "rgba(75, 192, 192, 1)",
    //           // "rgba(153, 102, 255, 1)",
    //         ],
    //         borderWidth: 2,
    //       },
    //     ],
    //   },
    //   options: {
    //     maintainAspectRatio: false,
    //     layout: {
    //       padding: {
    //         top: 10,
    //         bottom: 10,
    //         left: 10,
    //         right: 10,
    //       },
    //     },
    //     plugins: {
    //       legend: {
    //         display: false, // Hide the legend
    //       },
    //     },
    //     scales: {
    //       r: {
    //         beginAtZero: true,
    //         max: 1,
    //         angleLines: {
    //           display: false,
    //         },
    //         gridLines: {
    //           display: false, // Hide the grid lines inside the pentagon
    //         },
    //         ticks: {
    //           display: false,
    //         },
    //         pointLabels: {
    //           fontSize: 18, // Set the font size for the labels
    //         },
    //       },
    //     },
    //   },
    // });
    // myChart;
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
    background-image: "../../assets/images/mainPage.png";
    background-size: cover;
    /* background-repeat: no-repeat; */
    background-position: center center;
    color: black;
    font-family: korFont1;
    width: 100%;
    height: auto !important;
  }
  .results-main-screen {
    background-size: cover;
    background-repeat: no-repeat;
    background-image: url("../../assets/images/mainPage.png");
    height: calc(var(--vh, 1vh) * 100);
  }
  .details {
    background: linear-gradient(180deg, #fbf0ee 0%, #ffffff 100%);
  }
  .paintSpring {
    position: absolute;
    top: 5px;
    width: 100%;
    left: 0;
    right: 0;
  }
  .userName {
    font-size: 25px;
    padding-top: 90px;
    font-family: korFont3;
    color: #424242;
  }
  .first-result {
    padding-top: 50px;
    border-bottom: 1px solid #ccc;
    margin-bottom: 20px;
  }

  .first-result-title {
    font-size: 20px;
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
    width: 200px;
    display: block;
    margin-left: auto;
    margin-right: auto;
    padding-top: 40px;
  }
  #myChart {
    width: 160px;
  }
  .showDetailBtn {
    background-color: #424242;
    padding: 10px 20px;
    color: #ffffff;
    border: none;
    cursor: pointer;
    border-radius: 25px;
    margin-top: 40px;
    font-family: korFont2;
    font-size: 16px;
  }
  .characterName {
    font-size: 19px;
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
  .footer {
    background-color: #424242;
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    color: #ffffff;
    text-align: left;
    align-items: left;
    padding: 10px;
    font-size: 14px;
    font-family: korFont2;
    box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;
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
}

/* Styles for iPads */
@media only screen and (min-width: 768px) and (max-width: 1023px) {
  .results-data {
    display: inline-block;
    font-family: korFont2;
    background-color: #ffffff;

    background-size: cover;
    /* background-repeat: no-repeat; */
    background-position: center center;
    color: black;
    font-family: korFont1;
    width: 100%;
    height: auto !important;
  }
  .userName {
    font-size: 40px;
    margin-top: 10%;
    font-family: korFont3;
    color: #0000008a;
  }
  .first-result {
    margin-top: 50px;
    border-bottom: 1px solid #ccc;
    margin-bottom: 20px;
  }

  .first-result-title {
    font-size: 30px;
    margin-bottom: 10px;
    font-family: korFont3;
  }
  .first-image {
    margin-top: 25px;
    width: 350px;
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
    margin-bottom: 20px;
  }
  .treeAttributes {
    font-weight: 1000;
    font-size: 30px;
    margin-bottom: 15px;
  }
  .treefeatures {
    font-size: 25px;
    margin-bottom: 8px;
  }
  .treevalues {
    font-size: 25px;
    margin-bottom: 15px;
    line-height: 1.2;
  }
  .share-btn {
    font-family: korFont2;
    margin-bottom: 10px;
    font-size: 20px;
    background-color: #fffaf8;
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
    margin-bottom: 15px;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    gap: 25px;
  }
  .kakaotalk-btn {
    height: 40px;
  }
  .copylink-btn {
    height: 70px;
  }
  .clipboard-copy {
    display: inline-block;
  }
  .clipboard-img {
    width: 70px;
  }
  .characterImage {
    width: 230px;
    display: block;
    margin-left: auto;
    margin-right: auto;
    margin-top: 30px;
  }
  #myChart {
    width: 320px;
  }
  .showDetailBtn {
    background-color: #424242;
    padding: 10px 20px;
    color: #ffffff;
    border: none;
    cursor: pointer;
    border-radius: 25px;
    margin-bottom: 35px;
    font-family: korFont2;
    font-size: 25px;
  }
  .characterName {
    font-size: 30px;
    font-family: korFont2;
    font-weight: 1000;
    margin-top: 50px;
    border-radius: 10px;
    display: inline-block;
    max-width: 800px;
    word-wrap: break-word;
  }
  .footer {
    background-color: #424242;
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    color: rgb(255, 255, 255);
    text-align: center;
    padding: 10px;
    font-size: 14px;
    font-family: korFont2;
  }
  .title-text-result {
    font-family: korFont1;
    font-size: 35px;
  }
  .result-contact {
    font-family: korFont2;
    font-size: 20px;
  }
  .result-copyright {
    font-family: korFont2;
    margin-top: 10px;
    font-size: 20px;
  }
  .second-result {
    margin-bottom: 120px;
  }
  .shareBtn {
    background-color: transparent;
    padding: 10px 17px;
    color: #424242;
    border: 1px solid #c7c7c7;
    cursor: pointer;
    border-radius: 20px;
    font-family: korFont2;
    font-size: 18px;
    font-weight: 1000;
  }
}
</style>
