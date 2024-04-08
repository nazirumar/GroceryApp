  $(document).ready(function() {   
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  const csrftoken = getCookie('csrftoken');


  let $deleteButton = $('#delete-button');

  $('body').on('click', '.delete-modal', function () {
    $deleteButton.attr('href', $(this).attr('data-delete-url'))
  });

  $deleteButton.click(function (e) {
    e.preventDefault();
    let $this = $(this);
    $.ajax({
      url: $this.attr('href'),
      data: "",
      method: 'POST',
      headers: { 'X-CSRFToken': csrftoken },
      success: function () {
        $('#exampleModal').modal('hide')
        $('.delete-modal[data-delete-url="' + $this.attr('href') + '"]').parent().remove();
      }
    });
  });
})