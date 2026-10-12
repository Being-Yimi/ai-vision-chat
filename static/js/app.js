async function send() {
    const prompt = document.getElementById('prompt').value;
    const res = await fetch(`/api/chat?prompt=${encodeURIComponent(prompt)}`, {method: 'POST'});
    const data = await res.json();
    document.getElementById('result').innerText = data.reply;
}

async function analyzeImage() {
    const fileInput = document.getElementById('imageInput');
    if (fileInput.files.length === 0) return alert("请先选择一张图片！");

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    const res = await fetch("/api/analyze", { method: "POST", body: formData });
    const data = await res.json();

    const img = document.getElementById('resultImage');
    img.src = data.image_url;
    img.style.display = 'block';
    document.getElementById('imageDesc').innerText = "AI 描述：" + data.description;
}