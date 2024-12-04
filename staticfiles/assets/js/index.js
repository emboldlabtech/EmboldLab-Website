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
    autoplay: {
        delay: 3000,
        disableOnInteraction: false,
    },
    breakpoints:{
        0: {
            slidesPerView: 1,
        },
        520: {
            slidesPerView: 2,
        },
        950: {
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


    document.addEventListener('DOMContentLoaded', () => {
        animateCounter(document.getElementById('students'), 2);
        animateCounter(document.getElementById('projects'), 200);
        animateCounter(document.getElementById('partners'), 5);
    });

    function animateCounter(element, target) {
        let count = 0;
        const duration = 2000; // Animation duration in milliseconds
        const increment = target / (duration / 100); // Calculate the increment for each step

        const counter = setInterval(() => {
            count += increment;
            if (count >= target) {
                count = target;
                clearInterval(counter);
            }
            element.textContent = Math.floor(count); // Update the number in the element
        }, 100); // Interval of 100ms
    }