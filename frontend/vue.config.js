const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    host: process.env.VUE_APP_IP_ADDRESS,
    port: process.env.VUE_APP_FLASK_PORT,
  },
})

module.exports = {
  devServer: {
    client: {
      overlay: false
    }
  }
}

module.exports = {
  devServer: {
    webSocketServer: false
  }
}
