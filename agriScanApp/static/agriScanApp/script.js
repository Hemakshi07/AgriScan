document.addEventListener("DOMContentLoaded", function () {
    console.log("Script is running!");
  
    var button = document.getElementById("backToTopBtn");
  
    // Show/hide the button based on scroll position
    window.onscroll = function () {
      button.style.display = (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) ? "block" : "none";
    };
  
  });
  
  function scrollToTop() {
    var currentPosition = document.documentElement.scrollTop || document.body.scrollTop;
  
    function scrollStep() {
      if (currentPosition > 0) {
        window.requestAnimationFrame(function () {
          window.scrollTo(0, currentPosition);
          currentPosition -= 50; // You can adjust the step size for smoothness
          scrollStep();
        });
      }
    }
  
    scrollStep();
  }
  
  
  
  