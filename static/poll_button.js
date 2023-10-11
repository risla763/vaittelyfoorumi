document.addEventListener("DOMContentLoaded", function() {
    const poll_id = document.getElementById("poll_id");
    const buttons = document.querySelectorAll('input[type="radio"]');
    const submit_button = pollForm.querySelector('input[type="submit"]');

    poll_id.addEventListener("change", function() {
        const selected = Array.from(buttons).some((radio) => radio.checked);
        submit_button.disabled = !selected;
    });
  });

