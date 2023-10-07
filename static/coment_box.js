const Help = document.querySelector('.comments_on_the_bottom');
const Messages = document.querySelector('.comment');
const Input = document.querySelector('.input');
const commentBox = document.getElementById('comment-box');

function scrollBottom() {
    Messages.scrollTop = Messages.scrollHeight;
}

function adjustMargin() {
    const inputHeight = Input.clientHeight;
    Messages.style.marginBottom = inputHeight + 'px';

}

function chatMargin() {
    const inputHeight = Input.clientHeight;
    Messages.style.marginBottom = inputHeight + 'px';
}
Input.addEventListener('focus', scrollBottom);

window.addEventListener('resize', chatMargin);

window.addEventListener('load', () => {
    scrollBottom();
    chatMargin();
});

window.addEventListener('load', scrollBottom);

commentBox.addEventListener('change', function () {
    this.style.height = 'auto';
    this.style.height = (this.scrollHeight) + 'px';
});

commentBox.addEventListener('focus', function () {
    this.style.height = 'auto';
    this.style.height = (this.scrollHeight) + 'px';
});


const inputField = document.querySelector('.input');

commentBox.addEventListener('input', function () {
    const maxHeight = 300;


    const contentHeight = Math.min(this.scrollHeight, maxHeight);


    inputField.style.height = contentHeight + 'px';
});
