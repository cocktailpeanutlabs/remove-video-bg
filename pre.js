module.exports = (config, kernel) => {
  const x = {
    "win32": {
      "nvidia": `pip install torch torchvision torchaudio ${config.xformers ? 'xformers' : ''} --index-url https://download.pytorch.org/whl/cu121`,
      "amd": "pip install torch-directml",
      "cpu": "pip install torch torchvision torchaudio"
    },
    "darwin": "pip install torch torchvision torchaudio",
    "linux": {
      "nvidia": `pip install torch torchvision torchaudio ${config.xformers ? 'xformers' : ''}`,
      "amd": "pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm5.7",
      "cpu": "pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu"
    }
  }
  if (config.torch) {
    if (kernel.platform === "darwin") {
      return x[kernel.platform]
    } else {
      return x[kernel.platform][kernel.gpu]
    }
  }
}
