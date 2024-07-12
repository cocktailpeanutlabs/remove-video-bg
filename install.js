const config = require("./config.js")
const pre = require("./pre.js")
module.exports = async (kernel) => {
  let script = {
    run: [{
      method: "shell.run",
      params: {
        venv: "env",
        message: [
          "pip install opencv-python==4.9.0.80 timm tqdm kornia gdown transparent-background gradio"
        ],
      }
    }, {
      method: "fs.share",
      params: {
        venv: "env"
      }
    }, {
      method: "notify",
      params: {
        html: "Click the 'start' tab to get started!"
      }
    }]
  }
  let pre_command = pre(config, kernel)
  if (pre_command) {
    script.run[0].params.message = [pre_command].concat(script.run[0].params.message)
  }
  return script
}
