/*!
* Start Bootstrap - Landing Page v6.0.3 (https://startbootstrap.com/theme/landing-page)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-landing-page/blob/master/LICENSE)
*/

//  form validity js for travel story
(function () {
  'use strict';
  window.addEventListener('load', function () {
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.getElementsByClassName('needs-validation');
    // Loop over them and prevent submission
    var validation = Array.prototype.filter.call(forms, function (form) {
      form.addEventListener('submit', function (event) {
        if (form.checkValidity() === false) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add('was-validated');
      }, false);
    });
  }, false);
})();

//  Defensive js code for delete button in profile page
$(".confirm").click(function () {
  $('#deleteStory').modal('show');
});

$(".confirm").click(function () {
  $('#deleteComment').modal('show');
});

//  change password javascript for Profile page
$(document).ready(function () {
  $('.changepwd').parent().hide();
});

// toggle functionality for change password button
$(".btn-change").click(function () {
  $(this).parent().next().slideToggle('slow');
}); 

