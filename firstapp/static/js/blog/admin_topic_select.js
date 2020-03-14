// django.jQuery(document).ready(function () {

  console.log('Это работает');

  // django.jQuery('#id_stadyfield').change(function() {
  //
  //     var stadyfield = $(this).val();
  //     console.log('Its works');
  //
  // })
  // const stady = document.querySelector("select[name=stadyfield]")
  // console.log(stady)
  // stady.addEventListener("change", function(e) {
  //
  //     var stadyfield = e.target.value//this.val();
  //     console.log('Its works');
  //
  // })
// });

(function($){
  $(document).ready(function ($) {
    $('#id_stadyfield').change(function() {

        var stadyfield = $(this).val();
        console.log('Its works');
      })
  })
})(jQuery);
