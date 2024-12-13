document.addEventListener('DOMContentLoaded', () => {
    const button = document.getElementById('learn-more');
    button.addEventListener('click', () => {
        alert('More features coming soon!');
    });
});

document.querySelector("#rotate").addEventListener('click', function() {
    document.querySelector("#sample").classList.add('rotating')
 });
 document.addEventListener("DOMContentLoaded", function () {
    const paras = document.querySelectorAll(".who-we-are-text");

    window.addEventListener("scroll", () => {
        const triggerHeight = window.innerHeight * 0.8;
        paras.forEach(para => {
            const paraTop = para.getBoundingClientRect().top;
            if (paraTop < triggerHeight) {
                para.classList.add("float-on-scroll");
            }
        });
    });
});
