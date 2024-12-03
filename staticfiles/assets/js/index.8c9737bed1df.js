let swiper = new Swiper(".slide-content", {
    slidesPerView: 3,
    spaceBetween: 25,
    loop: true,
    centerSlide: 'true',
    fade: 'true',
    grabCursor: 'true',
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
      dynamicBullets: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },

    breakpoints:{
        0: {
            slidesPerView: 1,
        },
        200: {
            slidesPerView: 2,
        },
        400: {
            slidesPerView: 3,
        },
    },
  });


    function showCourses() {
        // Hide all course options initially
        document.querySelectorAll('.course-options').forEach((div) => {
            div.style.display = 'none';
        });

        // Get the selected program value
        const selectedProgram = document.getElementById("program").value;

        // Show corresponding courses based on the selected program
        if (selectedProgram === "bootcamp") {
            document.getElementById("bootcampCourses").style.display = 'block';
        } else if (selectedProgram === "accelerator") {
            document.getElementById("acceleratorCourses").style.display = 'block';
        } else if (selectedProgram === "masterclass") {
            document.getElementById("masterclassCourses").style.display = 'block';
        }
    }